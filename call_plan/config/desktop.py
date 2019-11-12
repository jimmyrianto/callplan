# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
        {
            "label": _("Call Plan"),
            "icon": "octicon octicon-briefcase",
            "items": [
                {
                    "type": "doctype",
                    "name": "Call Plan",
                    "label": _("Call Plan"),
                },
            ]
        }
    ]