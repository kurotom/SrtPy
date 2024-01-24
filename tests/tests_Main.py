# -*- coding: utf-8 -*-
"""
Tests
"""


import unittest

from src.SrtPyMain import SrtPy


class PyConcatSRTTestCase(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(PyConcatSRTTestCase, self).__init__(*args, **kwargs)

    def setUp(self):
        self.single_file = 'tests/srts/sample1.srt'
        self.multi_files = 'tests/srts/multisrt/'

        self.getControl_attr = self.getControl()
        self.read_file_attr = self.read_file()
        self.read_multi_file_attr = self.read_dir()

    def getControl(self):
        return SrtPy()

    def read_file(self):
        control = self.getControl()
        data = control.read(path=self.single_file)
        return data

    def read_dir(self):
        control = self.getControl()
        data = control.read_directory(directory_path=self.multi_files)
        return data
