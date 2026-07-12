{
    'name': 'AssetFlow',
    'version': '1.0.0',
    'summary': 'Enterprise Asset & Resource Management System',
    'description': """
AssetFlow
=========
Enterprise Asset & Resource Management System
""",
    'author': 'Team AssetFlow',
    'category': 'Operations',
    'license': 'LGPL-3',

    'depends': [
        'base',
        'mail',
        'hr',
        'calendar',
    ],

    'data': [

        # Security
        'security/groups.xml',
        'security/ir.model.access.csv',
        'security/rules.xml',
        'data/ir_sequence_data.xml',

        # Views (must be before menus so actions exist)
        'views/department_views.xml',
        'views/category_views.xml',
        'views/employee_views.xml',
        'views/asset_views.xml',
        'views/allocation_views.xml',
        'views/booking_views.xml',
        'views/maintenance_views.xml',
        'views/audit_views.xml',
        'views/notification_views.xml',
        'views/dashboard_views.xml',

        # Auth / Frontend pages
        'views/login_views.xml',
        'views/signup.xml',
        'views/forgot_password_views.xml',
        'views/reset_password_views.xml',
        'views/email_templates.xml',

        # Menus (last — all actions must exist before this loads)
        'views/menus.xml',
    ],

    'installable': True,
    'application': True,
}