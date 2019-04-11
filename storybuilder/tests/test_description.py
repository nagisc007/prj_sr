# -*- coding: utf-8 -*-
"""Test for description.py
"""
import unittest
from builder.sbutils import print_test_title
from builder.description import _BaseDesc, Desc, DescGroup
from builder.enums import DescType


_FILENAME = "description.py"


class BaseDescTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print_test_title(_FILENAME, "_BaseDesc")

    def test_attributes(self):
        data = [
                (DescType.DESCRIPTION, DescType.DESCRIPTION, None),
                (DescType.DIALOGUE, DescType.DIALOGUE, None),
                ]

        for v, expected, exp_data in data:
            with self.subTest(v=v, expected=expected, exp_data=exp_data):
                tmp = _BaseDesc(v)
                self.assertIsInstance(tmp, _BaseDesc)
                self.assertEqual(tmp.desc_type, expected)
                self.assertEqual(tmp.data, exp_data)


class DescTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print_test_title(_FILENAME, "Desc")

    def test_attributes(self):
        data = [
                (("test",), DescType.DESCRIPTION,
                    ("test",), DescType.DESCRIPTION),
                (("test", "apple"), DescType.DESCRIPTION,
                    ("test", "apple"), DescType.DESCRIPTION),
                ("", DescType.DESCRIPTION,
                    (), DescType.DESCRIPTION),
                ]

        for v, dtype, expected, exp_type in data:
            with self.subTest(v=v, dtype=dtype, expected=expected, exp_type=exp_type):
                tmp = Desc(v, dtype)
                self.assertIsInstance(tmp, Desc)
                self.assertEqual(tmp.data, expected)
                self.assertEqual(tmp.desc_type, exp_type)


class DescGroupTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print_test_title(_FILENAME, "DescGroup")

    def test_attributes(self):
        dsc = _BaseDesc(DescType.DESCRIPTION)
        data = [
                ((dsc,), DescType.DESCRIPTION,
                    (dsc,), DescType.DESCRIPTION),
                ((dsc, dsc), DescType.DESCRIPTION,
                    (dsc, dsc), DescType.DESCRIPTION),
                ((dsc,), None,
                    (dsc,), DescType.DESCRIPTION),
                ]

        for v, dtype, expected, exp_type in data:
            with self.subTest(v=v, dtype=dtype, expected=expected, exp_type=exp_type):
                tmp = DescGroup(base_type=dtype, *v) if dtype else DescGroup(*v)
                self.assertIsInstance(tmp, DescGroup)
                self.assertEqual(tmp.desc_type, exp_type)
                self.assertEqual(tmp.descriptions, expected)

