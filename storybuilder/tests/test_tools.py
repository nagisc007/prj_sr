# -*- coding: utf-8 -*-
"""Test for tools.py
"""

import unittest
import os
import sys
from io import StringIO
from builder.sbutils import print_test_title
from builder.action import Action, TagAction, GroupType
from builder.description import Desc
from builder.enums import DescType, LangType
from builder.master import Master
from builder.subject import Person, Item, Word, Flag
import builder.tools as tools


_FILENAME = "tools.py"


class PublicMethodsTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print_test_title(_FILENAME, "public methods")

    def setUp(self):
        self.ma = Master("test")
        self.sm = Master("test story")
        self.taro = Person("Taro", 17, "male", "student", "me")
        self.hanako = Person("Hanako", 17, "female", "student", "me")
        self.masao = Person("Masao", 17, "male", "student", "俺")
        self.story = self.sm.story(
                "Taro and Hanako",
                self.hanako.come("in room").desc("a cute girl come in"),
                self.taro.be("wow", self.hanako).desc("Nice to meet you"),
                self.hanako.be("like").negative().desc("I'm not fine"),
                lang=LangType.ENG,
                )
        self.story_j = self.sm.story(
                "太郎と花子",
                self.hanako.come("部屋").desc("可愛い少女"),
                self.taro.be("ああ").desc("よう"),
                self.hanako.be("好き", self.taro, self.masao).negative().desc("全然")
                )
        self.test_file = "test_file"

    @unittest.skip("almost same output_story")
    def test_build_to_story(self):
        pass

    @unittest.skip("must use stdout")
    def test_options_parsed(self):
        pass

    def test_output_info(self):
        _BASEMSG = "Characters:\n    Total: {}\n"
        data = [
                (self.ma.story("test", self.taro.be()),
                    _BASEMSG.format(0))
                ]

        for story, expected in data:
            with self.subTest(story=story, expected=expected):
                tmp_stdout, sys.stdout = sys.stdout, StringIO()
                tools.output_info(story)
                self.assertEqual(sys.stdout.getvalue(), expected)
                # fall back
                sys.stdout = tmp_stdout

    @unittest.skip("almost same _output_story_to_file and _output_story_to_console")
    def test_output_story(self):
        pass


class PrivateMethodsTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print_test_title(_FILENAME, "private methods")

    def setUp(self):
        self.ma = Master("test story")
        self.taro = Person("Taro", 17, "male", "student", "me")
        self.hanako = Person("Hanako", 17, "female", "student", "me")
        self.masao = Person("Masao", 17, "male", "student", "俺")
        self.misa = Person("Misa", 30, "female", "sheff", "taro:Taro:hanako:Hana")
        self.item = Item("stick")
        self.story = self.ma.story(
                "Taro and Hanako",
                self.hanako.come("in room").desc("a cute girl come in"),
                self.taro.be("wow", self.hanako).desc("Nice to meet you"),
                self.hanako.be("like").negative().desc("I'm not fine"),
                lang=LangType.ENG,
                )
        self.story_j = self.ma.story(
                "太郎と花子",
                self.hanako.come("部屋").desc("可愛い少女"),
                self.taro.be("ああ").desc("よう"),
                self.hanako.be("好き", self.taro, self.masao).negative().desc("全然")
                )
        self.test_file = "test_file"

    def test_action_of_by_tag(self):
        data = [
                (self.ma.comment("test"), GroupType.STORY, 1, "<!--test-->"),
                (self.ma.title("test"), GroupType.STORY, 1, "# test\n"),
                (self.ma.title("test"), GroupType.STORY, 2, "\n## test\n"),
                (self.ma.title("test"), GroupType.SCENE, 1, "**test**"),
                (self.ma.hr(), GroupType.STORY, 1, "--------" * 9),
                (self.ma.break_symbol("**"), GroupType.STORY, 1, "\n\n**\n\n"),
                (self.ma.br(), GroupType.STORY, 1, "\n"),
                ]
        
        for act, gtype, lv, expected in data:
            with self.subTest(act=act, gtype=gtype, lv=lv, expected=expected):
                self.assertEqual(tools._action_of_by_tag(act, gtype, lv), expected)

    def test_action_of_by_type(self):
        DEF_PRI = Action.DEFAULT_PRIORITY
        data = [
                (self.taro.talk(), LangType.JPN, GroupType.STORY, 1, DEF_PRI, False,
                    "- Taro　　:talk()　　　　/"),
                (self.taro.talk(self.hanako), LangType.JPN, GroupType.STORY, 1, DEF_PRI, False,
                    "- Taro　　:talk(Hanako)/"),
                (self.taro.be(), LangType.JPN, GroupType.STORY, 1, 10, False,
                    ""),
                ]

        for act, lng, gtype, lv, pri, dbg, expected in data:
            with self.subTest(act=act, lng=lng, gtype=gtype, lv=lv, pri=pri, dbg=dbg,
                    expected=expected):
                self.assertEqual(tools._action_of_by_type(act, lng, gtype, lv, pri, dbg),
                        expected)

    def test_action_info_as_eng(self):
        data = [
                (self.taro.talk(), GroupType.STORY, False,
                    "- Taro    :talk()      /"),
                (self.taro.talk(Flag(1)), GroupType.STORY, False,
                    "- Taro    :talk()      /[1](1)"),
                (self.taro.talk(Flag(1)).set_deflags(Flag(2)), GroupType.STORY, False,
                    "- Taro    :talk()      /[1](1)[D:2](2)"),
                ]

        for act, gtype, istest, expected in data:
            with self.subTest(act=act, gtype=gtype, istest=istest, expected=expected):
                self.assertEqual(tools._action_info_as_eng(
                    act, gtype, istest), expected)

    def test_action_info_as_jpn(self):
        data = [
                (self.taro.talk(), GroupType.STORY, False, 
                    "- Taro　　:talk()　　　　/"),
                ]

        for act, gtype, istest, expected in data:
            with self.subTest(act=act, gtype=gtype, istest=istest, expected=expected):
                self.assertEqual(tools._action_info_as_jpn(
                    act, gtype, istest), expected)

    def test_break_symbol_of(self):
        data = [
                ("****", "\n\n****\n\n"),
                ]

        for v, expected in data:
            with self.subTest(v=v, expected=expected):
                self.assertEqual(tools._break_symbol_of(self.ma.break_symbol(v)),
                        expected)

    def test_comment_of(self):
        data = [
                ("a test", "<!--a test-->"),
                ]
        for v, expected in data:
            with self.subTest(v=v, expected=expected):
                tmp = self.ma.comment(v)
                self.assertEqual(tools._comment_of(tmp), expected)

    def test_count_desc_at_action(self):
        data = [
                (self.taro.talk().d("test\n"), 4),
                (self.taro.talk().d("test", "apple"), 9),
                (self.taro.talk().d(""), 0),
                (self.taro.talk().d("おはよう"), 4),
                (self.taro.talk().d("　おはよう。"), 5),
                ]

        for v, expected in data:
            with self.subTest(v=v, expected=expected):
                self.assertEqual(tools._count_desc_at_action(v), expected)

    def test_count_desc_in_group(self):
        data = [
                (self.ma.scene("test", self.taro.talk().d("test")),
                    4),
                (self.ma.scene("test", self.taro.talk().d("test"), self.taro.talk().d("test")),
                    8),
                (self.ma.story("test", self.ma.scene("a", self.taro.talk().d("test"))),
                    4),
                ]

        for v, expected in data:
            with self.subTest(v=v, expected=expected):
                self.assertEqual(tools._count_desc_in_group(v), expected)

    def test_count_descriptions(self):
        data = [
                (self.ma.scene("test", self.taro.talk().d("test")),
                    4),
                (self.ma.scene("test", self.taro.talk().d("test"), self.taro.talk().d("test")),
                    8),
                ]

        for v, expected in data:
            with self.subTest(v=v, expected=expected):
                self.assertEqual(tools._count_descriptions(v), expected)

    def test_desc_head_of(self):
        data = [
                (Desc("test", desc_type=DescType.DESCRIPTION), LangType.JPN,
                    "　"),
                ]

        for dsc, lng, expected in data:
            with self.subTest(dsc=dsc, lng=lng, expected=expected):
                self.assertEqual(tools._desc_head_of(dsc, lng), expected)

    def test_desc_str_replaced_tag(self):
        data = [
                ("$Sだった", self.taro, "meだった"),
                ("$meMeme", self.hanako, "meMeme"),
                ("$Sだし", self.masao, "俺だし"),
                ("$hanakoはかわいい", self.misa, "Hanaはかわいい"),
                ("$Sはあんまりだが$hanakoは美人", self.misa, "私はあんまりだがHanaは美人"),
                ("$Sのテスト", Word("test"), "$Sのテスト"),
                ]

        for doc, sub, expected in data:
            with self.subTest(doc=doc, sub=sub, expected=expected):
                self.assertEqual(tools._desc_str_replaced_tag(doc, sub), expected)

    def test_description_of_by_tag(self):
        data = [
                (self.ma.comment("test"), LangType.JPN, GroupType.STORY, 1, False,
                    ""),
                (self.ma.title("test"), LangType.JPN, GroupType.STORY, 1, False,
                    "# test\n"),
                (self.ma.title("test"), LangType.JPN, GroupType.SCENE, 1, False,
                    ""),
                (self.ma.hr(), LangType.JPN, GroupType.STORY, 1, False,
                    "--------" * 9),
                (self.ma.break_symbol("**"), LangType.JPN, GroupType.STORY, 1, False,
                    "\n\n**\n\n"),
                (self.ma.title("test"), LangType.JPN, GroupType.SCENE, 1, True,
                    "**test**"),
                ]

        for act, lng, gtype, lv, dbg, expected in data:
            with self.subTest(act=act, lng=lng, gtype=gtype, lv=lv, dbg=dbg,
                    expected=expected):
                self.assertEqual(tools._description_of_by_tag(act, lng, gtype, lv, dbg),
                        expected)

    def test_description_of_by_type(self):
        DEF_PRI = Action.DEFAULT_PRIORITY
        data = [
                (self.taro.talk(), LangType.JPN, GroupType.STORY, 1, DEF_PRI, False,
                    ""),
                (self.taro.talk().desc("test"), LangType.JPN, GroupType.STORY, 1, DEF_PRI, False,
                    "　test。"),
                (self.taro.talk().desc("test", "is good"), LangType.JPN, GroupType.STORY, 1, DEF_PRI, False,
                    "　test、is good。"),
                (self.taro.talk().desc("test"), LangType.ENG, GroupType.STORY, 1, DEF_PRI, False,
                    " test. "),
                (self.taro.talk().desc("test").omit(), LangType.JPN, GroupType.STORY, 1, DEF_PRI, False,
                    ""),
                (self.taro.talk().tell("test"), LangType.JPN, GroupType.STORY, 1, DEF_PRI, False,
                    "「test」"),
                (self.taro.talk().tell("test", "apple"), LangType.ENG, GroupType.STORY, 1, DEF_PRI, False,
                    ' "test, apple" ')
                ]

        for act, lng, gtype, lv, pri, dbg, expected in data:
            with self.subTest(act=act, lng=lng, gtype=gtype, lv=lv, pri=pri, dbg=dbg,
                    expected=expected):
                self.assertEqual(tools._description_of_by_type(act, lng, gtype, lv, pri, dbg),
                        expected)

    def test_desc_excepted_symbols(self):
        pass

    def test_extra_chopped(self):
        pass

    def test_flags_if(self):
        data = [
                (Flag("flag"), Flag("deflag"), "[flag](flag)[D:deflag](deflag)"),
                (Flag("flag"), None, "[flag](flag)"),
                (None, Flag("deflag"), "[D:deflag](deflag)"),
                ]

        for flg, dflg, expected in data:
            with self.subTest(flg=flg, dflg=dflg, expected=expected):
                tmp = self.taro.talk()
                if flg and dflg:
                    tmp = self.taro.talk().set_flags(flg).set_deflags(dflg)
                elif flg:
                    tmp = self.taro.talk().set_flags(flg)
                elif dflg:
                    tmp = self.taro.talk().set_deflags(dflg)
                self.assertEqual(tools._flags_if(tmp), expected)

    def test_flag_info_of(self):
        data = [
                ("test", "", True, "[test](test)"),
                ]

        for flg, dflg, isflg, expected in data:
            with self.subTest(flg=flg, dflg=dflg, isflg=isflg, expected=expected):
                tmp = self.taro.be()
                if flg:
                    tmp.set_flags(flg)
                if dflg:
                    tmp.set_deflags(dflg)
                self.assertEqual(tools._flag_info_of(tmp, isflg), expected)


    def test_hr_of(self):
        data = [
                (0, ""),
                (1, "-" * 8),
                (5, "-" * (8 * 5)),
                (None, "-" * (8 * 9)),
                ]

        for v, expected in data:
            with self.subTest(v=v, expected=expected):
                tmp = tools._hr_of(v) if not v is None else tools._hr_of()
                self.assertEqual(tmp, expected)

    def test_list_head_inserted(self):
        data = [
                (GroupType.COMBI, "        - "),
                (GroupType.SCENE, "    - "),
                (GroupType.STORY, "- "),
                ]

        for v, expected in data:
            with self.subTest(v=v, expected=expected):
                self.assertEqual(tools._list_head_inserted(v), expected)

    def test_output_story_to_console(self):
        data = [
                (["# test story", "test"], False,
                    "# test story\ntest\n"),
                ]
        for story, isdbg, expected in data:
            with self.subTest(story=story, isdbg=isdbg, expected=expected):
                tmp_stdout, sys.stdout = sys.stdout, StringIO()
                self.assertTrue(tools._output_story_to_console(story, isdbg))
                self.assertEqual(sys.stdout.getvalue(),expected)
                # fall back
                sys.stdout = tmp_stdout

    def test_output_story_to_file(self):
        data = [
                (["# test story", "test"], "test_file", "_a", False,
                    "build/test_file_a.md"),
                (["# test story", "test"], "test_file", "", False,
                    "build/test_file.md"),
                ]

        for story, fname, suffix, isdbg, exp_path in data:
            with self.subTest(story=story, fname=fname, suffix=suffix, isdbg=isdbg, exp_path=exp_path):
                build_path = os.path.join(os.getcwd(), exp_path)
                self.assertTrue(tools._output_story_to_file(story, fname, suffix, isdbg))
                self.assertTrue(os.path.exists(build_path))

    def test_output_with_linenumber(self):
        data = [
                ("a test", 0, True, "0: a test"),
                ("a test", 1, True, "1: a test"),
                ("a test", 10, True, "10: a test"),
                ("a test", 5, False, "a test")
                ]

        for v, n, dbg, expected in data:
            with self.subTest(v=v, n=n, dgb=dbg, expected=expected):
                self.assertEqual(tools._output_with_linenumber(v, n, dbg), expected)

    def test_scene_title_of(self):
        data = [
                ("a test", "**a test**"),
                ]

        for title, expected in data:
            with self.subTest(title=title, expected=expected):
                tmp = self.ma.title(title)
                self.assertIsInstance(tmp, TagAction)
                self.assertEqual(tools._scene_title_of(tmp), expected)

    def test_story_converted_as_action(self):
        data = [
                (self.ma.story("Test", self.taro.be()),
                    0, False,
                    ["# Test\n", "- Taro　　:be()　　　　/"])
                ]

        for story, pri, isdbg, expected in data:
            with self.subTest(story=story, pri=pri, isdbg=isdbg, expected=expected):
                self.assertEqual(tools._story_converted_as_action(story, pri, isdbg),
                        expected)

    def test_story_converted_as_action_in_group(self):
        data = [
                (self.ma.story("Test", self.taro.be()),
                    GroupType.STORY, 1, 0, False,
                    ["# Test\n", "- Taro　　:be()　　　　/"]),
                (self.ma.story("Test", self.ma.scene("A", self.taro.be())),
                    GroupType.STORY, 1, 0, False,
                    ["# Test\n", "**A**","    - Taro　　:be()　　　　/", "\n"]),
                ]

        for story, gtype, lv, pri, isdbg, expected in data:
            with self.subTest(story=story, gtype=gtype, lv=lv, pri=pri, isdbg=isdbg, expected=expected):
                self.assertEqual(tools._story_converted_as_action_in_group(story, gtype, lv, pri, isdbg),
                        expected)

    def test_story_converted_as_description(self):
        data = [
                (self.ma.story("Test", self.taro.be().d("test")),
                    5, False,
                    ["# Test\n", "　test。"])
                ]

        for story, pri, isdbg, expected in data:
            with self.subTest(story=story, pri=pri, isdbg=isdbg, expected=expected):
                self.assertEqual(tools._story_converted_as_description(story, pri, isdbg),
                        expected)

    def test_story_converted_as_description_in_group(self):
        data = [
                (self.ma.story("Taro and Hanako", self.taro.talk().d("test"), self.hanako.talk().d("apple"), lang=LangType.ENG),
                    GroupType.STORY,
                    ["# Taro and Hanako\n", " test. ", " apple. "]),
                (self.ma.scene("Taro and Hanako", self.taro.talk().d("test"), self.hanako.talk().d("apple"), lang=LangType.ENG),
                    GroupType.SCENE,
                    [" test. ", " apple. ", "\n"]),
                (self.ma.story(self.taro.talk().d("test"), self.hanako.talk().d("apple")),
                    GroupType.COMBI,
                    ["　test。apple。"]),
                (self.ma.story(self.taro.talk().d("test"), self.hanako.talk().d("apple"), lang=LangType.ENG),
                    GroupType.COMBI,
                    [" test. apple. "]),
                (self.ma.story("test", self.ma.scene("a", self.taro.be().d("test"))),
                    GroupType.STORY,
                    ["# test\n", "　test。", "\n"])
                ]
        for v, gtype, expected in data:
            with self.subTest(v=v, gtype=gtype, expected=expected):
                self.assertEqual(tools._story_converted_as_description_in_group(
                    v, gtype, 1, 5, False), expected)

    def test_story_data_converted(self):
        data = [
                (self.ma.story("Test", self.taro.be()),
                    True, 5, False,
                    ["# Test\n", "- Taro　　:be()　　　　/"]),
                ]

        for story, isact, pri, isdbg, expected in data:
            with self.subTest(story=story, isact=isact, pri=pri, isdbg=isdbg, expected=expected):
                self.assertEqual(tools._story_data_converted(story, isact, pri, isdbg),
                        expected)

    def test_story_flags_info_converted(self):
        data = [
                (self.ma.story("test",
                    self.taro.be(Flag("taro"))),
                    ["[taro]:taro"]),
                ]

        for v, expected in data:
            with self.subTest(v=v, expected=expected):
                self.assertEqual(tools._story_flags_info_converted(v), expected)

    def test_story_info_data_converted(self):
        data = [
                (self.ma.story("test",
                    self.taro.be(Flag("apple"))),
                    False,
                    ["## Characters\n", "- Total: 0",
                        "## Actions\n", "- Total: 1",
                        "- be: 100.00%",
                        "- behav: 0.00%",
                        "- deal: 0.00%",
                        "- do: 0.00%",
                        "- explain: 0.00%",
                        "- feel: 0.00%",
                        "- look: 0.00%",
                        "- move: 0.00%",
                        "- talk: 0.00%",
                        "- think: 0.00%",
                        "## Flags\n", "[apple]:apple"]),
                (self.ma.story("test",
                    self.taro.be().d("test apple")),
                    False,
                    ["## Characters\n", "- Total: 9",
                        "## Actions\n", "- Total: 1",
                        "- be: 100.00%",
                        "- behav: 0.00%",
                        "- deal: 0.00%",
                        "- do: 0.00%",
                        "- explain: 0.00%",
                        "- feel: 0.00%",
                        "- look: 0.00%",
                        "- move: 0.00%",
                        "- talk: 0.00%",
                        "- think: 0.00%",
                        "## Flags\n"]),
                (self.ma.story("test",
                    self.taro.be().d("test"),
                    self.taro.talk().d("apple")),
                    False,
                    ["## Characters\n", "- Total: 9",
                        "## Actions\n", "- Total: 2",
                        "- be: 50.00%",
                        "- behav: 0.00%",
                        "- deal: 0.00%",
                        "- do: 0.00%",
                        "- explain: 0.00%",
                        "- feel: 0.00%",
                        "- look: 0.00%",
                        "- move: 0.00%",
                        "- talk: 50.00%",
                        "- think: 0.00%",
                        "## Flags\n"]),
                (self.ma.story("test",
                    self.ma.scene("A",
                    self.taro.be().d("test"),
                    self.taro.talk().d("apple"))),
                    False,
                    ["## Characters\n", "- Total: 9",
                        "## Actions\n", "- Total: 2",
                        "- be: 50.00%",
                        "- behav: 0.00%",
                        "- deal: 0.00%",
                        "- do: 0.00%",
                        "- explain: 0.00%",
                        "- feel: 0.00%",
                        "- look: 0.00%",
                        "- move: 0.00%",
                        "- talk: 50.00%",
                        "- think: 0.00%",
                        "## Flags\n"]),
                ]

        for v, isdbg, expected in data:
            with self.subTest(v=v, isdbg=isdbg, expected=expected):
                self.assertEqual(tools._story_info_data_converted(v, isdbg), expected)

    def test_story_title_of(self):
        ma = Master('test')

        data = [
                ("a test", 0, " a test\n"),
                ("a test", 1, "# a test\n"),
                ("a test", 2, "\n## a test\n"),
                ]

        for title, lv, expected in data:
            with self.subTest(title=title, lv=lv, expected=expected):
                tmp = ma.title(title)
                self.assertIsInstance(tmp, TagAction)
                self.assertEqual(tools._story_title_of(tmp, lv), expected)

    def test_test_head_if(self):
        data = [
                (True, "> "),
                (False, "")
                ]

        for v, expected in data:
            with self.subTest(v=v, expected=expected):
                self.assertEqual(tools._test_head_if(v), expected)
