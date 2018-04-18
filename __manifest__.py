# -*- coding: utf-8 -*-

# Copyright (C) 2018 ABC_CODER designer.shaoyan@gmail.com

{
    'name': '中国省市县',
    'version': '0.1',
    'category': 'Base',
    'author': 'ABC_CODER',
    'maintainer': 'designer.shaoyan@gmail.com',
    'description': """

    添加中文市县数据

    添加partner三级联动

    """,
    'depends': ['base', 'l10n_cn'],
    'data': [
        'data/res_city_data.xml',
        'data/res_district_data.xml',
        'views/china_address_views.xml'
    ]
}