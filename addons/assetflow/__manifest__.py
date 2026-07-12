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
        'data/ir_sequence_data.xml',

        # Menus
        'views/menus.xml',

        # Organization
        'views/department_views.xml',
        # 'views/category_views.xml',
        # 'views/employee_views.xml',

        # Assets
        'views/asset_views.xml',
        # 'views/allocation_views.xml',

        # Operations
        'views/booking_views.xml',
        # 'views/maintenance_views.xml',
        'views/audit_views.xml',
        'views/notification_views.xml',

        # Dashboard
        'views/dashboard_views.xml',
    ],

    'installable': True,
    'application': True,
}