# -*- coding: utf-8 -*-
"""Test for action.py
"""
import unittest
from builder.sbutils import print_test_title
from builder.action import Action, ActionGroup, TagAction
from builder.basesubject import _BaseSubject
from builder.description import Desc
from builder.enums import ActType, AuxVerb, DescType, GroupType, LangType, TagType


_FILENAME = "action.py"


class ActionTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print_test_title(_FILENAME, "Action")

    def setUp(self):
        self.taro = _BaseSubject("Taro", "a man")
        self.act = Action(ActType.BE, self.taro, "be", ())

    def get_baseaction(self):
        return Action(ActType.BE, self.taro, "be", ())

    def test_attributes(self):
        data = [
                (ActType.BE, self.taro, "be", (),
                    ActType.BE, self.taro, "be", ()),
                (ActType.BE, self.taro, "been", (),
                    ActType.BE, self.taro, "been", ()),
                (ActType.BE, self.taro, "be", (self.taro,),
                    ActType.BE, self.taro, "be", (self.taro,)),
                ]
        for act, sub, verb, obj, exp_act, exp_sub, exp_verb, exp_obj in data:
            with self.subTest(act=act, sub=sub, verb=verb, obj=obj,
                    exp_act=exp_act, exp_sub=exp_sub, exp_verb=exp_verb, exp_obj=exp_obj):
                tmp = Action(act, sub, verb, obj)
                self.assertIsInstance(tmp, Action)
                self.assertEqual(tmp.act_type, exp_act)
                self.assertEqual(tmp.subject, exp_sub)
                self.assertEqual(tmp.verb, exp_verb)
                self.assertEqual(tmp.objects, exp_obj)
                self.assertIsInstance(tmp.descs, Desc)
                self.assertEqual(tmp.descs.data, ())
                self.assertEqual(tmp.auxverb, AuxVerb.NONE)
                self.assertEqual(tmp.flags, ())
                self.assertEqual(tmp.deflags, ())
                self.assertEqual(tmp.is_negative, False)
                self.assertEqual(tmp.is_passive, False)
                self.assertEqual(tmp.priority, Action.DEFAULT_PRIORITY)

    def test_auxverb_methods(self):
        data = [
                ("can", AuxVerb.CAN),
                ("may", AuxVerb.MAY),
                ("must", AuxVerb.MUST),
                ("should", AuxVerb.SHOULD),
                ("want", AuxVerb.WANT),
                ("will", AuxVerb.WILL),
                ]

        for v, expected in data:
            with self.subTest(v=v, expected=expected):
                tmp = self.get_baseaction()
                self.assertIsInstance(getattr(tmp, v)(), Action)
                self.assertEqual(tmp.auxverb, expected)

    def test_desc(self):
        data = [
                (("test",),
                    ("test",), DescType.DESCRIPTION),
                (("test", "apple"),
                    ("test", "apple"), DescType.DESCRIPTION),
                ("test",
                    ("test",), DescType.DESCRIPTION),
                ]

        for v, expected, exp_type in data:
            with self.subTest(v=v, expected=expected, exp_type=exp_type):
                tmp = self.get_baseaction()
                if isinstance(v, tuple):
                    tmp.desc(*v)
                else:
                    tmp.desc(v)
                self.assertIsInstance(tmp.descs, Desc)
                self.assertEqual(tmp.descs.desc_type, exp_type)
                self.assertEqual(tmp.descs.data, expected)

    def test_d(self):
        data = [
                (("test",),
                    ("test",)),
                ]

        for v, expected in data:
            with self.subTest(v=v, expected=expected):
                tmp = self.get_baseaction()
                tmp.d(*v)
                self.assertEqual(tmp.descs.data, expected)

    def test_negative(self):
        data = [
                (True, True),
                (None, False),
                ]

        for v, expected in data:
            with self.subTest(v=v, expected=expected):
                tmp = self.get_baseaction()
                if v:
                    tmp.negative()
                self.assertEqual(tmp.is_negative, expected)

    def test_omit(self):
        data = [
                (True, Action.MIN_PRIORITY),
                (None, Action.DEFAULT_PRIORITY),
                ]

        for v, expected in data:
            with self.subTest(v=v, expected=expected):
                tmp = self.get_baseaction()
                if v:
                    tmp.omit()
                self.assertEqual(tmp.priority, expected)

    def test_passive(self):
        data = [
                (True, True),
                (None, False),
                ]

        for v, expected in data:
            with self.subTest(v=v, expected=expected):
                tmp = self.get_baseaction()
                if v:
                    tmp.passive()
                self.assertEqual(tmp.is_passive, expected)

    def test_set_flags(self):
        data = [
                (("test",),
                    ("test",)),
                (("test", "apple"),
                    ("test", "apple")),
                ("test",
                    ("test",)),
                (1,
                    ("1",))
                ]
        for v, expected in data:
            with self.subTest(v=v, expected=expected):
                tmp = self.get_baseaction()
                if isinstance(v, tuple):
                    tmp.set_flags(*v)
                else:
                    tmp.set_flags(v)
                self.assertEqual(tmp.flags, expected)

    def test_set_deflag(self):
        data = [
                (("test",),
                    ("test",)),
                (("test", "apple"),
                    ("test", "apple")),
                ("test",
                    ("test",)),
                (1,
                    ("1",))
                ]
        for v, expected in data:
            with self.subTest(v=v, expected=expected):
                tmp = self.get_baseaction()
                if isinstance(v, tuple):
                    tmp.set_deflags(*v)
                else:
                    tmp.set_deflags(v)
                self.assertEqual(tmp.deflags, expected)

    def test_priority(self):
        data = [(x, x) for x in range(1, 10)]

        for v, expected in data:
            with self.subTest(v=v, expected=expected):
                tmp = self.get_baseaction()
                tmp.set_priority(v)
                self.assertEqual(tmp.priority, expected)

    def test_tell(self):
        data = [
                ("test", False,
                    ("test",), DescType.DESCRIPTION),
                ("test", True,
                    ("test",), DescType.DIALOGUE),
                ]

        for doc, dial, expected, exp_type in data:
            with self.subTest(doc=doc, dial=dial, expected=expected, exp_type=exp_type):
                tmp = self.get_baseaction()
                if dial:
                    tmp.tell(doc)
                else:
                    tmp.desc(doc)
                self.assertEqual(tmp.descs.desc_type, exp_type)
                self.assertEqual(tmp.descs.data, expected)


class ActionGroupTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print_test_title(_FILENAME, "ActionGroup")

    def setUp(self):
        self.taro = _BaseSubject("Taro", "a man")

    def get_baseaction(self):
        return Action(ActType.BE, self.taro, "be", ())

    def test_attributes(self):
        data = [
                (GroupType.STORY, LangType.JPN, (self.get_baseaction(),),
                    GroupType.STORY, LangType.JPN, 1),
                (GroupType.STORY, LangType.JPN, (self.get_baseaction(), self.get_baseaction()),
                    GroupType.STORY, LangType.JPN, 2),
                (GroupType.SCENE, None, (self.get_baseaction(),),
                    GroupType.SCENE, LangType.JPN, 1),
                ]

        for group, lng, acts, exp_group, exp_lng, exp_acts in data:
            with self.subTest(group=group, lng=lng, acts=acts,
                    exp_group=exp_group, exp_lng=exp_lng, exp_acts=exp_acts):
                tmp = ActionGroup(group_type=group, lang=lng, *acts) if lng else ActionGroup(group_type=group, *acts)
                self.assertIsInstance(tmp, ActionGroup)
                self.assertEqual(tmp.group_type, exp_group)
                self.assertEqual(tmp.lang, exp_lng)
                self.assertEqual(len(tmp.actions), exp_acts)


class TagActionTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print_test_title(_FILENAME, "TagAction")

    def test_attributes(self):
        data = [
                (TagType.COMMENT, "test",
                    TagType.COMMENT, "test"),
                (TagType.BR, "",
                    TagType.BR, ""),
                (TagType.HR, "hr",
                    TagType.HR, "hr"),
                (TagType.SYMBOL, "*",
                    TagType.SYMBOL, "*"),
                (TagType.TITLE, "test",
                    TagType.TITLE, "test"),
                ]

        for tag, info, exp_tag, exp_info in data:
            with self.subTest(tag=tag, info=info, exp_tag=exp_tag, exp_info=exp_info):
                tmp = TagAction(tag, info)
                self.assertIsInstance(tmp, TagAction)
                self.assertEqual(tmp.act_type, ActType.TAG)
                self.assertEqual(tmp.tag, exp_tag)
                self.assertEqual(tmp.tag_info, exp_info)

