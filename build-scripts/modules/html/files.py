# -*- coding: utf-8 -*-
"""
Gathers low level output generation functionality to avoid circular import
"""
from __future__ import absolute_import, unicode_literals

import logging
import os
import shutil
import tempfile
import six

from .template import Template

class ReleaseNote(object):
    """
    Centralizes file rendering management and provide a class method for tests
    """

    def __init__(self, path):
        self.path = path
        self.mode = 'w'

    @property
    def content(self):
        """
        Returns file content
        """
        try:
            with open(self.path) as fop:
                return fop.read()
        except IOError as err:
            logging.warning('Cannot display file content :%s', err)
            return ""

    def render(self, template, **kwargs):
        """
        Writes in file based on template rendering file content
        """
        self.write(Template(template).render_plain_text(kwargs))

    def write(self, content):
        """
        Writes parameter's content in the file with its mode

        mode can be 'p' to prepend onto previous file
        """
        if self.mode == 'p':
            try:
                with open(self.path) as previous:
                    previous_content = previous.read().decode('utf8')
            except IOError:
                previous_content = None

            write_mode = 'w'
        else:
            write_mode = self.mode

        with open(self.path, write_mode) as output:
            if six.PY2:
                content = content.encode('utf8')
            output.write(content)

            if self.mode == 'p' and previous_content is not None:
                output.write('\n{}'.format(previous_content).encode('utf8'))
