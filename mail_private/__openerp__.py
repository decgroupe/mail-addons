# -*- coding: utf-8 -*-
{
    "name": """Internal Messaging""",
    "summary": """Send private messages to specified recipients, regardless of who are in followers list.""",
    "category": "Discuss",
    "images": ['images/mail_private_image.png'],
    "version": "1.0.1",
    "application": False,

    "author": "IT-Projects LLC, Pavel Romanchenko",
    "support": "apps@it-projects.info",
    "website": "https://twitter.com/OdooFree",
    "license": "GPL-3",

    "depends": [
        "mail",
    ],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
        'template.xml',
    ],
    "qweb": [
        'static/src/xml/mail_private.xml',
    ],
    "demo": [],

    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,

    "auto_install": False,
    "installable": True,
}
