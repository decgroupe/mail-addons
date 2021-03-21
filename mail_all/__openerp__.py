# -*- coding: utf-8 -*-
{
    "name": "Show all messages",
    "summary": """Checkout all messages where you have access""",
    "category": "Discuss",
    "images": ['images/1.jpg'],
    "version": "1.0.0",

    "author": "IT-Projects LLC, Pavel Romanchenko",
    "website": "https://twitter.com/OdooFree",
    "license": "LGPL-3",

    "depends": [
        "mail_base"
    ],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
        "views/templates.xml",
    ],
    "qweb": [
        "static/src/xml/menu.xml",
    ],
    "demo": [],
    'installable': True,
    "auto_install": False,
}
