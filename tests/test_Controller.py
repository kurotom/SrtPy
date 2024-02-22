# -*- coding: utf-8 -*-
"""
Tests Controller
"""

import os

from tests_Main import PyConcatSRTTestCase

from src.DialogScript import Dialog


class ControllerTestCase(PyConcatSRTTestCase):

    def test_Controller_type_read_file(self):
        data = self.read_file_attr
        self.assertEqual(type(data), list)

    def test_Controller_type_read_dir(self):
        data = self.read_multi_file_attr
        self.assertEqual(type(data), list)

    def test_Controller_type_object_line(self):
        data = self.read_file_attr
        objs = [i for i in data if type(i) is not Dialog]
        self.assertEqual(len(objs), 0)

    def test_Controller_convertData(self):
        control = self.getControl_attr
        data = control.read(path=self.single_file)
        r = control.convertData(data)
        self.assertEqual(type(r), str)

    def test_Controller_convertData_empty(self):
        control = self.getControl_attr
        r = control.convertData('')
        self.assertEqual(r, '')

    def test_Controller_writeData(self):
        control = self.getControl_attr
        r = control.to_write(filename='tests/final', data='algo')
        os.remove('tests/final.srt')
        self.assertEqual(r, True)

    def test_Controller_writeData_empty(self):
        control = self.getControl_attr
        r = control.to_write(filename='final', data='')
        self.assertEqual(r, None)
