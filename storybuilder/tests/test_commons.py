# -*- coding: utf-8 -*-
"""Test for commons.py
"""
import unittest
from builder.sbutils import print_test_title
from builder.action import Action
from builder.description import Desc
from builder.enums import ActType, LangType
from builder.subject import Subject, Person, Something, Item
import builder.commons as commons


_FILENAME = "commons.py"


class PublicMethodsTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print_test_title(_FILENAME, "public methods")

    def setUp(self):
        self.taro = Person("Taro", 17, "male", "student")
        self.hanako = Person("Hanako", 17, "female", "student")
        self.item = Item("stick")

    def test_descriptions_of(self):
        pass

    def test_double_comma_chopped(self):
        data = [
                ("　これを。。ただしく。。", LangType.JPN,
                    "　これを。ただしく。"),
                (" This is a pen.. the pen. ", LangType.ENG,
                    " This is a pen. the pen. "),
                ]

        for v, lng, expected in data:
            with self.subTest(v=v, lng=lng, expected=expected):
                self.assertEqual(commons.double_comma_chopped(v, lng), expected)

    def test_extraend_chopped(self):
        data = [
                ("！。", LangType.JPN,
                    "！"),
                ("？。", LangType.JPN,
                    "？"),
                ("!. ", LangType.ENG,
                    "!"),
                ("?. ", LangType.ENG,
                    "?")
                ]

        for v, lng, expected in data:
            with self.subTest(v=v, lng=lng, expected=expected):
                self.assertEqual(commons.extraend_chopped(v, lng), expected)

    def test_extraspace_chopped(self):
        data = [
                ("　これを。　ただしくする。", LangType.JPN,
                    "　これを。ただしくする。"),
                (" This is a pen.  the pen. ", LangType.ENG,
                    " This is a pen. the pen. "),
                ("　これを。、ただしくして。", LangType.JPN,
                    "　これを。ただしくして。"),
                ("「これを」　正しくする。", LangType.JPN,
                    "「これを」正しくする。"),
                ]

        for v, lng, expected in data:
            with self.subTest(v=v, lng=lng, expected=expected):
                self.assertEqual(commons.extraspace_chopped(v, lng), expected)

    def test_infos_of(self):
        taro = Person("Taro", 17, "male", "student")
        data = [
                (("test",), "test"),
                (("test", "must"), "test/must"),
                ((taro,), ""),
                ((taro, "test"), "test"),
                ]

        for infos, expected in data:
            with self.subTest(infos=infos, expected=expected):
                tmp = taro.be(*infos)
                self.assertIsInstance(tmp, Action)
                self.assertEqual(commons.infos_of(tmp), expected)

    def test_infos_from(self):
        pass

    def test_object_names_of(self):
        data = [
                (self.taro.be(self.hanako),
                    "Hanako"),
                (self.taro.be(self.hanako, self.item),
                    "Hanako/stick"),
                (self.taro.be("test"),
                    ""),
                ]

        for act, expected in data:
            with self.subTest(act=act, expected=expected):
                self.assertEqual(commons.object_names_of(act), expected)

    def test_object_names_of_without_something(self):
        data = [
                (self.taro.be(),
                    ""),
                (self.taro.be(self.hanako),
                    "Hanako"),
                (self.taro.be(self.hanako, self.item),
                    "Hanako/stick"),
                (self.taro.be("test", self.hanako),
                    "Hanako"),
                (self.taro.be(Something()),
                    "")
                ]

        for act, expected in data:
            with self.subTest(act=act, expected=expected):
                self.assertEqual(commons.object_names_of_without_something(act),
                        expected)

    def test_something_name_if(self):
        data = [
                (Subject("test taro", ""), "test taro"),
                (Something(), "何か")
                ]
        for obj, expected in data:
            with self.subTest(obj=obj, expected=expected):
                self.assertEqual(commons.something_name_if(obj), expected)

    def test_subject_name_of(self):
        taro = Person("Taro", 17, "male", "student")
        some = Something()
        data = [
                (taro.be("test taro"), "Taro"),
                (Action(ActType.BE, some, "be", ()), "何か"),
                ]
        for act, expected in data:
            with self.subTest(act=act, expected=expected):
                self.assertEqual(commons.subject_name_of(act), expected)

    def test_verb_with_np_of(self):
        data = [
                (True, True,
                    "~~_do~~_"),
                (True, False,
                    "~~do~~"),
                (False, True,
                    "_do_"),
                (False, False,
                    "do")
                ]

        for ne, ps, expected in data:
            tmp = self.taro.do()
            if ne:
                tmp.negative()
            if ps:
                tmp.passive()
            self.assertEqual(commons.verb_with_np_of(tmp), expected)


class PrivateMethodsTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print_test_title(_FILENAME, "private methods")

    def setUp(self):
        self.taro = Person("Taro", 17, "male", "student")

    def test_comma_of(self):
        data = [
                (LangType.JPN, "、"),
                (LangType.ENG, ", ")
                ]

        for lng, expected in data:
            with self.subTest(lng=lng, expected=expected):
                self.assertEqual(commons._comma_of(lng), expected)

    def test_desc_of(self):
        data = [
                ("test", LangType.JPN,
                    "test。")
                ]

        for v, lng, expected in data:
            with self.subTest(v=v, lng=lng, expected=expected):
                tmp = self.taro.do()
                tmp.d(v)
                self.assertEqual(commons._desc_of(tmp.descs, lng), expected)

    def test_desc_of_in_group(self):
        pass

    def test_dialogue_converted(self):
        pass

    def test_endpoint_replaced_if_invalid(self):
        pass

    def test_period_of(self):
        data = [
                (LangType.JPN, "。"),
                (LangType.ENG, ". ")
                ]

        for lng, expected in data:
            with self.subTest(lng=lng, expected=expected):
                self.assertEqual(commons._period_of(lng), expected)

    def test_space_replaced_if_with_symbol(self):
        data = [
                ("!,", LangType.ENG, "! "),
                ("?,", LangType.ENG, "? "),
                ("!?,", LangType.ENG, "!? "),
                ("！、", LangType.JPN, "！　"),
                ("？、", LangType.JPN, "？　"),
                ("！？、", LangType.JPN, "！？　"),
                ]

        for origin, lng, expected in data:
            with self.subTest(origin=origin, lng=lng, expected=expected):
                self.assertEqual(commons._space_replaced_if_with_symbol(
                    origin, lng), expected)

    def test_verbs_of(self):
        pass
