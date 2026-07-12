import uuid
import logging
from odoo import http
from odoo.http import request
from odoo.addons.web.controllers.home import Home

_logger = logging.getLogger(__name__)


class AssetFlowHome(Home):
    """Override Odoo's root controller so '/' always opens the signup page."""

    @http.route('/', type='http', auth='public')
    def index(self, **kw):
        # Always redirect root to the custom signup landing page
        return request.redirect('/assetflow/signup')

    @http.route('/web/login', type='http', auth='public')
    def web_login(self, redirect=None, **kw):
        """Keep Odoo's login page working normally, rendering our inherited login view."""
        return super().web_login(redirect=redirect, **kw)


class AssetFlowAuthController(http.Controller):

    # ── Sign-up page GET/POST ─────────────────────────────────────────────
    @http.route('/assetflow/signup', type='http', auth='public', methods=['GET', 'POST'])
    def signup(self, **kw):
        """Render signup page on GET, process user creation on POST."""
        if request.httprequest.method == 'POST':
            login = kw.get('login', '').strip()
            password = kw.get('password', '')
            confirm_password = kw.get('confirm_password', '')
            name = kw.get('name', '').strip()

            if not login or not password:
                return request.render('assetflow.signup', {
                    'error': 'Email and Password are required.',
                    'login': login,
                })

            if password != confirm_password:
                return request.render('assetflow.signup', {
                    'error': 'Passwords do not match.',
                    'login': login,
                })

            # Check if email is already registered
            existing_user = request.env['res.users'].sudo().search([('login', '=', login)], limit=1)
            if existing_user:
                return request.render('assetflow.signup', {
                    'error': 'An account with this email address already exists.',
                    'login': login,
                })

            try:
                # Create the User record
                user_vals = {
                    'login': login,
                    'name': name or login.split('@')[0],
                    'password': password,
                    'groups_id': [
                        (4, request.env.ref('base.group_user').id),
                        (4, request.env.ref('assetflow.group_assetflow_employee').id),
                    ]
                }
                new_user = request.env['res.users'].sudo().create(user_vals)

                # Create the corresponding HR Employee record
                request.env['hr.employee'].sudo().create({
                    'name': new_user.name,
                    'user_id': new_user.id,
                    'work_email': login,
                    'role': 'employee',
                })

                # Commit the transaction so the new user is visible to authenticate()
                request.env.cr.commit()

                # Log the user in and redirect to dashboard
                db_name = request.session.db or request.db or request.env.cr.dbname
                request.session.authenticate(db_name, login, password)
                return request.redirect('/web')

            except Exception as e:
                _logger.exception("Signup process failed")
                return request.render('assetflow.signup', {
                    'error': f'Signup failed: {str(e)}',
                    'login': login,
                })

        return request.render('assetflow.signup', {})

    # ── Forgot password page ──────────────────────────────────────────────
    @http.route('/assetflow/forgot-password', type='http', auth='public', methods=['GET'])
    def forgot_password(self, **kw):
        """Render the AssetFlow forgot-password page."""
        return request.render('assetflow.assetflow_forgot_password', {
            'message_sent': False,
        })

    # ── Forgot password form submission ──────────────────────────────────
    @http.route('/assetflow/forgot-password/submit', type='http', auth='public', methods=['POST'], csrf=True)
    def forgot_password_submit(self, **kw):
        """Generate reset token and dispatch standard email template."""
        login = kw.get('login', '').strip()
        user = request.env['res.users'].sudo().search([('login', '=', login)], limit=1)

        if user:
            # Generate a secure token and store it
            token = uuid.uuid4().hex
            user.write({'reset_password_token': token})

            # Send the email template
            template = request.env.ref('assetflow.email_template_assetflow_reset_password', raise_if_not_found=False)
            if template:
                template.sudo().send_mail(user.id, force_send=True)

        # Always return Success view status so we don't disclose registered emails
        return request.render('assetflow.assetflow_forgot_password', {
            'message_sent': True,
        })

    # ── Reset password page ───────────────────────────────────────────────
    @http.route('/assetflow/reset-password', type='http', auth='public', methods=['GET'])
    def reset_password(self, token=None, **kw):
        """Validate reset token and render reset password page."""
        if not token:
            return request.redirect('/assetflow/forgot-password')

        user = request.env['res.users'].sudo().search([('reset_password_token', '=', token)], limit=1)
        if not user:
            return request.redirect('/assetflow/forgot-password')

        return request.render('assetflow.assetflow_reset_password', {
            'token': token,
        })

    # ── Reset password confirmation submission ────────────────────────────
    @http.route('/assetflow/reset-password/confirm', type='http', auth='public', methods=['POST'], csrf=True)
    def reset_password_confirm(self, **kw):
        """Confirm token and change password in the DB."""
        token = kw.get('token', '')
        password = kw.get('password', '')
        confirm_password = kw.get('confirm_password', '')

        if not token:
            return request.redirect('/assetflow/forgot-password')

        user = request.env['res.users'].sudo().search([('reset_password_token', '=', token)], limit=1)
        if not user:
            return request.redirect('/assetflow/forgot-password')

        if password != confirm_password:
            return request.render('assetflow.assetflow_reset_password', {
                'token': token,
                'error': 'Passwords do not match.',
            })

        # Clear token and save new password
        user.write({
            'password': password,
            'reset_password_token': False,
        })

        return request.redirect('/assetflow/reset-password/success')

    # ── Reset password success page ───────────────────────────────────────
    @http.route('/assetflow/reset-password/success', type='http', auth='public', methods=['GET'])
    def reset_password_success(self, **kw):
        """Render the success page after resetting password."""
        return request.render('assetflow.assetflow_reset_password_success', {})
