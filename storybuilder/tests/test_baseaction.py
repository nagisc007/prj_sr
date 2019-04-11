# -*- coding: utf-8 -*-
"""Test for basesubject.py
"""
import unittest
from builder.sbutils import print_test_title
from builder.baseaction import _BaseAction
from builder.enums import ActType


_FILENAME = "baseaction.py"


class BaseActionTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print_test_title(_FILENAME, "BaseAction")

    def test_attributes(self):
        data = [
                (ActType.BE, ActType.BE),
                ]

        for v, expected in data:
            tmp = _BaseAction(v)
            self.assertIsInstance(tmp, _BaseAction)
            self.assertEqual(tmp.act_type, expected)

