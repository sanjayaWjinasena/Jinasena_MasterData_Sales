# -*- coding: utf-8 -*-
{
    'name': 'Jinasena : MasterData : Sales',
    'version': '17.0.0.0.2',
    'summary': 'Master-data extracted from CDB for Sales domain.',
    'description': 'Extracted from Clear-DB. Test-env master data. Edit the CSVs in data/ to add/remove rows before install.',
    'author': 'Jinasena Agricultural Machinery (Pvt) Ltd.',
    'category': 'Extra Tools',
    'license': 'LGPL-3',
    'depends': [
        'BugFix-Sales',
        'Jinasena_MasterData_Common',
        'Jinasena_MasterData_Accounting',
        'Jinasena_MasterData_Stock',
    ],
    'data': [
        'data/res_partner.csv',
        'data/crm_team.csv',
        'data/product_pricelist.csv',
        'data/product_pricelist_item.csv',
        'data/x_customer_group.csv',
        'data/x_minimum_sales_margin.csv',
        'data/x_sales_report_type.csv',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
