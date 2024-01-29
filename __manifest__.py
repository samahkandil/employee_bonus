# -*- coding: utf-8 -*-

{
    'name': 'Employee Bonus Management',
    'version': '14',
    'license': 'LGPL-3',
    'category': 'Human Resources',
    'summary': 'This module allow you HR department to create employee bonuses and approvals.',
    'description': """
Employee Bonus Management
Bonus
This module allow you HR department to create employee bonuses and approvals
Employee Bonus
Bonus for Employee
bonus
bonus calculation
bonus employee
bonus gift
employee bonus management
This module allow you HR department to create employee bonuses and approvals.

Menus:

Bonus
Bonus/Bonus
Bonus/Bonus/Bonuses
Bonus/Bonus/Bonuses To Approve by Department
Bonus/Bonus/Bonuses To Approve by Officer
Bonus/Configuration
Bonus/Configuration/Bonus Reasons
Commission
sales commission
sales bonus
bonus to employee
commission sales
sale commission
            """,
    'support': 'samahqandeel22@gmail.com',
    'images': ['static/description/img1.jpg'],
    'author': 'Samah Kandil.',
    'website': 'https://www.linkedin.com/in/samah-kandil-odoo',
    'depends': [
                'hr_contract',
                 'hr',
                 'portal',
                 'hr_payroll'
                 ],
    #'live_test_url': 'https://youtu.be/tiIx0ZfqNPg',
    'live_test_url': 'https://youtu.be/l68xXCgShA0',
    'data': [
            # 'data/hr_payroll_data.xml',
             'security/security.xml',
             'security/ir.model.access.csv',
             'data/bonus_sequence.xml',
             'data/hr_payroll_data.xml',
             'views/employee_bonus_view.xml',
             'views/employee_bonus_reports.xml',
             'views/hr_view.xml',
             'views/contract.xml',
             ],
    'installable': True,
    'application': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
