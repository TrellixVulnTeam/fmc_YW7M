# -*- coding: utf-8 -*-
"""
Definition of common template rendering process
"""
from __future__ import absolute_import, unicode_literals

import os
from jinja2 import Environment, FileSystemLoader


class Template(object):
    """
    Centralizes jinja rendering management
    """

    # pylint: disable=too-few-public-methods
    env = Environment(
        trim_blocks=True, lstrip_blocks=True, autoescape=False,
        extensions=['jinja2.ext.autoescape'],
        loader=FileSystemLoader(
            os.path.abspath(
                os.path.join(os.path.dirname(__file__), "templates")
            )
        )
    )

    def __init__(self, template):
        self.template = template

    def render_plain_text(self, context):
        """
        Centralizes template rendering file content
        """
        return self.env.get_template(self.template).render(context)
