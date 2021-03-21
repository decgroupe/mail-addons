# -*- coding: utf-8 -*-
{
    "name": "Sentbox",
    "summary": """Quick way to find sent messages""",
    "category": "Discuss",
    "images": ['images/menu.png'],
    "version": "1.0.4",

    "author": "IT-Projects LLC, Ivan Yelizariev, Pavel Romanchenko",
    "website": "https://twitter.com/OdooFree",
    "license": "LGPL-3",

    "depends": [
        "base",
        "mail",
        "mail_base"
    ],

    "data": [
        "views/templates.xml",
    ],
    "qweb": [
        "static/src/xml/menu.xml",
    ],
    'installable': True,
}
