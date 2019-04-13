# -*- coding: utf-8 -*-
"""Test for testtools.py
"""
import unittest
from builder.sbutils import print_test_title
from builder.master import Master
from builder.subject import Person, Day, Info, Item, Stage, Something, Word, Flag
import builder.testtools as testtools
from builder.testtools import MatchLv


_FILENAME = "testtools.py"


class PublicMethodsTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print_test_title(_FILENAME, "public methods")

    def setUp(self):
        self.ma = Master("test")
        self.taro = Person("Taro", 17, "male", "student")
        self.hanako = Person("Hanako", 17, "female", "student")
        self.day = Day("Test day")
        self.stage = Stage("Test stage")
        self.item = Item("A test")
        self.word = Word("A test")

    @unittest.expectedFailure
    def test_followed_all_flags(self):
        data = [
                (self.ma.combine(
                    self.taro.talk().set_flags(1),
                    self.taro.talk().set_deflags(1),
                    ), True),
                (self.ma.combine(
                    self.taro.talk().set_flags(1),
                    self.taro.talk().set_deflags(2),
                    ), False),
                ]

        for story, expected in data:
            with self.subTest(story=story, expected=expected):
                self.assertEqual(testtools.followed_all_flags(self, story), expected)

    def test_has_a_day(self):
        data = [
                (self.ma.story("test", self.taro.be(self.day)),
                    True),
                (self.ma.story("fail", self.taro.be()),
                    False),
                ]

        for v, expected in data:
            with self.subTest(v=v, expected=expected):
                self.assertEqual(testtools.has_a_day(v), expected)

    def test_has_a_item(self):
        data = [
                (self.ma.story("test", self.taro.be(self.item)),
                    True),
                (self.ma.story("fail", self.taro.be()),
                    False),
                ]

        for v, expected in data:
            with self.subTest(v=v, expected=expected):
                self.assertEqual(testtools.has_a_item(v), expected)

    def test_has_a_person(self):
        data = [
                (self.ma.story("test", self.taro.be()),
                    True),
                (self.ma.story("fail", self.stage.be()),
                    False),
                ]

        for v, expected in data:
            with self.subTest(v=v, expected=expected):
                self.assertEqual(testtools.has_a_person(v), expected)

    def test_has_a_stage(self):
        data = [
                (self.ma.story("test", self.taro.be(self.stage)),
                    True),
                (self.ma.story("fail", self.taro.be()),
                    False),
                ]

        for v, expected in data:
            with self.subTest(v=v, expected=expected):
                self.assertEqual(testtools.has_a_stage(v), expected)

    def test_has_a_word(self):
        data = [
                (self.ma.story("test", self.taro.be(self.word)),
                    True),
                (self.ma.story("fail", self.taro.be()),
                    False),
                ]

        for v, expected in data:
            with self.subTest(v=v, expected=expected):
                self.assertEqual(testtools.has_a_word(v), expected)

    @unittest.expectedFailure
    def test_has_basic_infos(self):
        data = [
                (self.ma.story("test",
                    self.taro.be(self.day), self.taro.go(self.stage), self.taro.talk(self.hanako)),
                    self.taro, self.hanako, True),
                (self.ma.story("fail",
                    self.taro.be(), self.taro.go(),),
                    self.taro, self.hanako, False),
                ]

        for story, hero, rival, expected in data:
            with self.subTest(story=story, hero=hero, rival=rival, expected=expected):
                self.assertEqual(testtools.has_basic_infos(self, story, hero, rival),
                        expected)

    @unittest.expectedFailure
    def test_has_outline_infos(self):
        base_story = self.ma.story("test",
                self.taro.be(self.day), self.taro.go(self.stage),
                self.taro.have("apple"))

        data = [
                (self.taro.be(), self.taro.go(), self.taro.have(), self.taro.talk(),
                    False, True),
                (self.taro.go(), self.taro.be(), self.taro.be(), self.taro.be(),
                    False, False),
                ]

        for what, why, how, result, fuz, expected in data:
            with self.subTest(what=what, why=why, how=how, result=result, fuz=fuz,
                    expected=expected):
                self.assertEqual(testtools.has_outline_infos(self, base_story,
                    what, why, how, result, fuz), expected)

    def test_has_the_action(self):
        data = [
                (self.ma.story("test", self.taro.be()), self.taro.be(),
                    MatchLv.COMPLETE, True),
                (self.ma.story("test", self.taro.be()), self.taro.go(),
                    MatchLv.COMPLETE, False),
                ]

        for story, target, mlv, expected in data:
            with self.subTest(story=story, target=target, mlv=mlv, expected=expected):
                self.assertEqual(testtools.has_the_action(story, target, mlv), expected)

    def test_has_the_day(self):
        data = [
                (self.ma.story(self.taro.be(self.day)), self.day,
                    True),
                (self.ma.story(self.taro.be()), Day("test"),
                    False),
                ]

        for story, target, expected in data:
            with self.subTest(story=story, target=target, expected=expected):
                self.assertEqual(testtools.has_the_day(story, target), expected)

    def test_has_the_keyword(self):
        story = self.ma.story("Test",
                self.taro.be("test"), self.taro.talk("apple"),
                )
        data = [
                ("test", True),
                ("tes", True),
                ("orange", False),
                ]

        for v, expected in data:
            with self.subTest(v=v, expected=expected):
                self.assertEqual(testtools.has_the_keyword(story, v), expected)

    def test_has_the_keyword_in_descriptions(self):
        story = self.ma.story("Test",
                self.taro.be().d("this is an apple"),
                self.taro.be().tell("My favorite is her"),
                )
        data = [
                ("this", True),
                ("apple", True),
                ("her", True),
                ("orange", False),
                ("app", True),
                ]

        for v, expected in data:
            with self.subTest(v=v, expected=expected):
                self.assertEqual(testtools.has_the_keyword_in_descriptions(
                    story, v), expected)

    def test_has_the_item(self):
        data = [
                (self.ma.story(self.taro.be(self.item)), self.item,
                    True),
                (self.ma.story(self.taro.be()), Item("test"),
                    False),
                ]

        for story, target, expected in data:
            with self.subTest(story=story, target=target, expected=expected):
                self.assertEqual(testtools.has_the_item(story, target), expected)

    def test_has_the_person(self):
        data = [
                (self.ma.story(self.taro.be()), self.taro,
                    True),
                (self.ma.story(self.stage.be()), self.taro,
                    False),
                ]

        for story, target, expected in data:
            with self.subTest(story=story, target=target, expected=expected):
                self.assertEqual(testtools.has_the_person(story, target), expected)

    def test_has_the_stage(self):
        data = [
                (self.ma.story(self.taro.be(self.stage)), self.stage,
                    True),
                (self.ma.story(self.taro.be()), Stage("test"),
                    False),
                ]

        for story, target, expected in data:
            with self.subTest(story=story, target=target, expected=expected):
                self.assertEqual(testtools.has_the_stage(story, target), expected)

    def test_has_the_word(self):
        data = [
                (self.ma.story(self.taro.be(self.word)), self.word,
                    True),
                (self.ma.story(self.taro.be()), Word("test"),
                    False),
                ]

        for story, target, expected in data:
            with self.subTest(story=story, target=target, expected=expected):
                self.assertEqual(testtools.has_the_word(story, target), expected)

    def test_is_all_actions(self):
        data = [
                (self.ma.story("test", self.taro.be()),
                    True),
                (self.ma.story("test", Info("test")),
                    False),
                ]

        for v, expected in data:
            with self.subTest(v=v, expected=expected):
                self.assertEqual(testtools.is_all_actions(v), expected)


class PrivateMethodsTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print_test_title(_FILENAME, "private methods")

    def setUp(self):
        self.ma = Master("test")
        self.taro = Person("Taro", 17, "male", "student")
        self.day = Day("Test day")
        self.stage = Stage("Test stage")
        self.item = Item("A test")
        self.word = Word("A test")

    def test_contains_the_info(self):
        data = [
                (Info("test"), Info("tes"), True),
                (Info("test"), Info("apple"), False),
                ]

        for info, target, expected in data:
            self.assertEqual(testtools._contains_the_info(info, target), expected)

    def test_count_subjects_in(self):
        data = [
                ((Info("a"),),
                    Info, 1),
                ((Info("a"), Info("b")),
                    Info, 2),
                ((Info("a"), Something(), Info("c")),
                    Info, 2),
                ((),
                    Info, 0),
                ((Info("a"), Something()),
                    Something, 1)
                ]

        for v, sbcls, expected in data:
            with self.subTest(v=v, sbcls=sbcls, expected=expected):
                self.assertEqual(testtools._count_subjects_in(v, sbcls), expected)
        
    @unittest.expectedFailure
    def test_fail_message_with_target(self):
        self.assertFalse(testtools._fail_message_without_target(self, "test", self.taro.be()))

    def test_flags_gathered_at_action(self):
        flag1, flag2 = Flag("1"), Flag("2")
        data = [
                ((flag1,), None, True, [flag1]),
                (None, (flag1, flag2), False, [flag1, flag2])
                ]

        for flg, dflg, isflg, expected in data:
            with self.subTest(flg=flg, dflg=dflg, isflg=isflg, expected=expected):
                tmp = self.taro.be()
                if flg:
                    tmp.set_flags(*flg)
                if dflg:
                    tmp.set_deflags(*dflg)
                self.assertEqual(testtools._flags_gathered_at_action(tmp, isflg),
                        expected)

    def test_flags_gathered_in_group(self):
        flag1, flag2 = Flag(1), Flag(2)
        data = [
                (self.ma.story("test", self.taro.be().set_flags(flag1)),
                    True,
                    [flag1]),
                (self.ma.story("test", self.taro.be(flag1, flag2)),
                    True,
                    [flag1, flag2]),
                (self.ma.story("test", self.taro.be().set_deflags(flag1)),
                    False,
                    [flag1]),
                (self.ma.story("test", self.ma.scene("a", self.taro.be().set_flags(flag1))),
                    True,
                    [flag1]),
                ]

        for story, isflg, expected in data:
            with self.subTest(story=story, isflg=isflg, expected=expected):
                self.assertEqual(testtools._flags_gathered_in_group(story, isflg),
                        expected)

    def test_has_a_subject(self):
        data = [
                (self.taro.be(), Person, True),
                (self.taro.have(self.item), Item, True),
                (self.taro.go("school"), Info, True),
                (self.taro.come(), Word, False),
                ]

        for act, scls, expected in data:
            with self.subTest(act=act, scls=scls, expected=expected):
                self.assertEqual(testtools._has_a_subject(act, scls), expected)

    def test_has_a_subject_in(self):
        data = [
                ((self.taro,), Person, True),
                ((self.taro, self.item), Item, True),
                ((self.taro,), Info, False),
                ]

        for objs, scls, expected in data:
            with self.subTest(objs=objs, scls=scls, expected=expected):
                self.assertEqual(testtools._has_a_subject_in(objs, scls), expected)

    def test_has_a_subject_in_group(self):
        data = [
                (self.ma.story("test", self.taro.be()), Person,
                    True),
                (self.ma.story("test", self.taro.have(self.item)), Item,
                    True),
                (self.ma.story("test", self.taro.go("school")), Info,
                    True),
                (self.ma.story("test", self.taro.know("apple")), Word,
                    False),
                (self.ma.story("test", self.ma.scene("a", self.taro.be())),
                    Person, True),
                ]

        for story, scls, expected in data:
            with self.subTest(story=story, scls=scls, expected=expected):
                self.assertEqual(testtools._has_a_subject_in_group(story, scls),
                        expected)

    def test_has_the_action_in_group(self):
        data = [
                (self.ma.story("test", self.taro.be()), self.taro.be(),
                    MatchLv.COMPLETE, True),
                (self.ma.story("test", self.taro.have("apple")), self.taro.have("orrange"),
                    MatchLv.COMPLETE, False),
                (self.ma.story("test", self.taro.have("apple")), self.taro.have("app"),
                    MatchLv.NEAR, True),
                (self.ma.story("test", self.ma.scene("a", self.taro.be())),
                    self.taro.be(), MatchLv.COMPLETE, True),
                (self.ma.story("test", self.ma.scene("a", self.taro.have("apple"))),
                    self.taro.be(), MatchLv.COMPLETE, False),
                (self.ma.story("test", self.taro.have("apple", "orrange")),
                    self.taro.have(Something()), MatchLv.ALMOST, True),
                ]

        for story, target, mlv, expected in data:
            with self.subTest(story=story, target=target, mlv=mlv, expected=expected):
                self.assertEqual(testtools._has_the_action_in_group(story, target, mlv),
                        expected)

    def test_has_the_subject(self):
        data = [
                (self.taro.be(), Person, self.taro,
                    True),
                (self.taro.have(self.item), Item, self.item,
                    True),
                (self.taro.go(self.stage), Word, self.word,
                    False),
                (self.taro.know(Word("apple")), Word, Word("orrange"),
                    False),
                ]

        for act, scls, target, expected in data:
            with self.subTest(act=act, scls=scls, target=target, expected=expected):
                self.assertEqual(testtools._has_the_subject(act, scls, target),
                        expected)

    def test_has_the_subject_in_group(self):
        data = [
                (self.ma.story("test", self.taro.be()), Person, self.taro,
                    True),
                (self.ma.story("test", self.taro.have(self.item)), Item, self.item,
                    True),
                (self.ma.story("test", self.taro.go("test")), Word, self.word,
                    False),
                (self.ma.story("test", self.ma.scene("a", self.taro.be())),
                    Person, self.taro, True),
                ]

        for story, scls, target, expected in data:
            with self.subTest(story=story, scls=scls, target=target, expected=expected):
                self.assertEqual(testtools._has_the_subject_in_group(story, scls, target),
                        expected)

    def test_is_actiongroup_all_actions(self):
        data = [
                ((self.taro.talk(), self.taro.talk(),), True),
                ((self.taro.talk(), "test"), False),
                ((self.ma.scene("test", self.taro.be()),), True),
                ((self.ma.scene("test", Info("test")),), False),
                ]

        for vals, expected in data:
            with self.subTest(vals=vals, expected=expected):
                tmp = self.ma.combine(*vals)
                self.assertEqual(testtools._is_actiongroup_all_actions(tmp), expected)

    def test_is_the_action(self):
        data = [
                (self.taro.be(), self.taro.be(), True),
                (self.taro.go(), self.taro.come(), False),
                (self.taro.be("sad"), self.taro.be("sad"), True),
                ]

        for act, target, expected in data:
            with self.subTest(act=act, target=target, expected=expected):
                self.assertEqual(testtools._is_the_action(act, target), expected)

    def test_is_the_action_verb(self):
        data = [
                (self.taro.be(), self.taro.be(), True),
                (self.taro.be().can(), self.taro.be().can(), True),
                (self.taro.be().can(), self.taro.be().must(), False),
                (self.taro.be().non(), self.taro.be().non(), True),
                (self.taro.be().non(), self.taro.be(), False),
                (self.taro.be().ps(), self.taro.be().ps(), True),
                (self.taro.be(), self.taro.be().ps(), False),
                ]

        for act, target, expected in data:
            with self.subTest(act=act, target=target, expected=expected):
                self.assertEqual(testtools._is_the_action_verb(act, target), expected)

    def test_is_same_objects(self):
        data = [
                (self.taro.talk(self.item, self.word),
                    (self.item, self.word), True),
                (self.taro.talk(self.item, self.stage),
                    (self.item, self.word), False),
                ]

        for act, targets, expected in data:
            with self.subTest(act=act, targets=targets, expected=expected):
                self.assertEqual(testtools._is_same_objects(act.objects, targets), expected)

    def test_is_same_subjects(self):
        data = [
                (self.taro, self.item, False),
                (self.taro, self.taro, True),
                (self.taro, Person("Taro", 0, "ma", "job"), True),
                ]

        for sub, target, expected in data:
            with self.subTest(sub=sub, target=target, expected=expected):
                self.assertEqual(testtools._is_same_subjects(sub, target), expected)

    def test_near_eq_the_action(self):
        data = [
                (self.taro.be(), self.taro.be(), False, True),
                ]

        for act, target, isinfo, expected in data:
            with self.subTest(act=act, target=target, isinfo=isinfo, expected=expected):
                self.assertEqual(testtools._near_eq_the_action(act, target, isinfo),
                        expected)

    def test_near_eq_objects(self):
        data = [
                ((self.taro,), (self.taro,),
                    False, True),
                ((self.taro,), (self.item,),
                    False, False),
                ((self.taro, self.item,), (self.taro,),
                    False, True),
                ((self.taro, Info("test")), (self.taro, Info("test")),
                    False, True),
                ((self.taro, Info("test")), (self.taro, Info("tes")),
                    False, False),
                ((self.taro, Info("test"),), (self.taro, Info("tes"),),
                    True, True),
                ((self.taro, self.item), (self.taro, Something()),
                    False, True),
                ]

        for objs, targets, isinfo, expected in data:
            with self.subTest(objs=objs, targets=targets, isinfo=isinfo, expected=expected):
                self.assertEqual(testtools._near_eq_objects(objs, targets, isinfo),
                        expected)

    def test_near_eq_subjects(self):
        data = [
                (self.taro, self.item, False),
                (self.taro, self.taro, True),
                (self.taro, Something(), True),
                (Something(), self.item, True),
                ]

        for sub, target, expected in data:
            with self.subTest(sub=sub, target=target, expected=expected):
                self.assertEqual(testtools._near_eq_subjects(sub, target), expected)

