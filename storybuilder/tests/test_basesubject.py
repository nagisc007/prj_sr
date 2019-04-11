# -*- coding: utf-8 -*-
"""Test for basesubject.py
"""
import unittest
from builder.sbutils import print_test_title
from builder.basesubject import _BaseSubject


_FILENAME = "basesubject.py"


class BaseSubjectTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print_test_title(_FILENAME, "BaseSubject")

    def test_attributes(self):
        data = [
                ("Taro", "a man",
                    "Taro", "a man"),
                ("Hanako", "",
                    "Hanako", ""),
                ]

        for name, note, exp_name, exp_note in data:
            with self.subTest(name=name, note=note, exp_name=exp_name, exp_note=exp_note):
                tmp = _BaseSubject(name, note) if note else _BaseSubject(name)
                self.assertIsInstance(tmp, _BaseSubject)
                self.assertEqual(tmp.name, exp_name)
                self.assertEqual(tmp.note, exp_note)
               
