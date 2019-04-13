# -*- coding: utf-8 -*-
"""Test for storydb.py
"""
import unittest
from builder.sbutils import print_test_title
from builder.action import ActionGroup, TagAction
from builder.enums import ActType, LangType, TagType
from builder.master import Master
from builder.subject import Person, Stage, Day, Item, Word, Info, Flag, Nothing, Something

_FILENAME = "master.py"


class MasterTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print_test_title(_FILENAME, "Master")

    def setUp(self):
        self.ma = Master("test")
        self.taro = Person("Taro", 17, "male", "student")

    def test_attributes(self):
        data = [
                ("a test", "a note"),
                ("a test", ""),
                ]

        for name, note in data:
            with self.subTest(name=name, note=note):
                tmp = Master(name, note) if note else Master(name)
                self.assertIsInstance(tmp, Master)
                self.assertEqual(tmp.name, name)
                self.assertEqual(tmp.note, note)

    def test_append_flag(self):
        data = [
                ("test", "test",
                    "f_test", "test"),
                ]

        for v, info, key, expected in data:
            with self.subTest(v=v, info=info, key=key, expected=expected):
                self.ma.append_flag(v, info)
                self.assertEqual(self.ma[key].note, expected)

    def test_append_person(self):
        data = [
                ("taro", "Taro", 17, "male", "student", "me", "a man"),
                ("hanako", "Hanako", 17, "female", "student", "me", "a girl"),
                ("taro", "Kotaro", 40, "male", "lower", "me", "a parent"),
                ("takeshi", "Takeshi", 35, "male", "driver", {"taro":"Ta", "hanako":"Ha"}, ""),
                ]

        def calling_from(slf):
            if isinstance(slf, dict):
                return slf
            elif slf:
                return {"me":slf}
            else:
                return {"me":Person.DEF_SELFCALL}

        for k, name, age, sex, job, slf, note in data:
            with self.subTest(k=k, name=name, age=age, sex=sex, job=job, slf=slf, note=note):
                self.ma.append_person(k, (name, age, sex, job, slf, note))
                key = k if name != "Kotaro" else "p_taro"
                self.assertEqual(self.ma[key].name, name)
                self.assertEqual(self.ma[key].age, age)
                self.assertEqual(self.ma[key].sex, sex)
                self.assertEqual(self.ma[key].job, job)
                self.assertEqual(self.ma[key].calling, calling_from(slf))
                self.assertEqual(self.ma[key].note, note)

    def test_append_stage(self):
        data = [
                ("school", "school", "for a student",
                    "school", "school", "for a student"),
                ("room", "room", "a room",
                    "room", "room", "a room"),
                ("room", "taro room", "",
                    "s_room", "taro room", ""),
                ]

        for k, name, note, exp_key, exp_name, exp_note in data:
            with self.subTest(k=k, name=name,
                    exp_key=exp_key, exp_name=exp_name, exp_note=exp_note):
                self.ma.append_stage(k, (name, note))
                self.assertEqual(self.ma[exp_key].name, exp_name)
                self.assertEqual(self.ma[exp_key].note, exp_note)

    def test_append_day(self):
        data = [
                ("d1", "day1", 1, 10, 2000, 12, 30, "a day",
                    "d1", "day1", 1, 10, 2000, 12, 30, "a day"),
                ("d1", "day1", 1, 10, 2000, 12, 30, "a day",
                    "d_d1", "day1", 1, 10, 2000, 12, 30, "a day"),
                ("d2", "day2", 0, 00, 0, 0, 0, "",
                    "d2", "day2", 0, 0, 0, 0, 0, ""),
                ]

        for k, name, mon, day, year, hour, min, note, exp_key, exp_name, exp_mon, exp_day, exp_year, exp_hour, exp_min, exp_note in data:
            with self.subTest(k=k, name=name, mon=mon, day=day, year=year, hour=hour, min=min, note=note,
                    exp_key=exp_key, exp_name=exp_name, exp_mon=exp_mon, exp_day=exp_day, exp_year=exp_year, exp_hour=exp_hour, exp_min=exp_min, exp_note=exp_note):
                if isinstance(name, Day):
                    self.ma.append_day(k, name)
                elif note:
                    self.ma.append_day(k, (name, mon, day, year, hour, min, note))
                else:
                    self.ma.append_day(k, (name,))
                self.assertEqual(self.ma[exp_key].name, exp_name)
                self.assertEqual(self.ma[exp_key].mon, exp_mon)
                self.assertEqual(self.ma[exp_key].day, exp_day)
                self.assertEqual(self.ma[exp_key].year, exp_year)
                self.assertEqual(self.ma[exp_key].hour, exp_hour)
                self.assertEqual(self.ma[exp_key].min, exp_min)
                self.assertEqual(self.ma[exp_key].note, exp_note)

    def test_append_item(self):
        data = [
                ("pen", "pen", "a pen",
                    "pen", "pen", "a pen"),
                ("pen", "pencil", "a pencil",
                    "i_pen", "pencil", "a pencil"),
                ("test", Item("test"), "",
                    "test", "test", "")
                ]

        for k, name, note, exp_key, exp_name, exp_note in data:
            with self.subTest(k=k, name=name, note=note,
                    exp_key=exp_key, exp_name=exp_name, exp_note=exp_note):
                if isinstance(name, Item):
                    self.ma.append_item(k, name)
                elif note:
                    self.ma.append_item(k, (name, note))
                else:
                    self.ma.append_item(k, (name,))
                self.assertEqual(self.ma[exp_key].name, exp_name)
                self.assertEqual(self.ma[exp_key].note, exp_note)

    def test_append_word(self):
        data = [
                ("w", "word", "a word",
                    "w", "word", "a word"),
                ("t", "test", "a test",
                    "t", "test", "a test"),
                ("w", "word2", "a word2",
                    "w_w", "word2", "a word2"),
                ("lack", "test", "",
                    "lack", "test", ""),
                ("cls", Word("test"), "",
                    "cls", "test", "")
                ]

        for k, name, note, exp_key, exp_name, exp_note in data:
            with self.subTest(k=k, name=name, note=note,
                    exp_key=exp_key, exp_name=exp_name, exp_note=exp_note):
                if isinstance(name, Word):
                    self.ma.append_word(k, name)
                elif note:
                    self.ma.append_word(k, (name, note))
                else:
                    self.ma.append_word(k, (name,))
                self.assertEqual(self.ma[exp_key].name, exp_name)
                self.assertEqual(self.ma[exp_key].note, exp_note)

    def test_br(self):
        data = [
                (10, TagType.BR, "10"),
                (None, TagType.BR, "1")
                ]
        
        for v, exp_type, expected in data:
            with self.subTest(v=v, exp_type=exp_type, expected=expected):
                tmp = self.ma.br(v) if v else self.ma.br()
                self.assertIsInstance(tmp, TagAction)
                self.assertEqual(tmp.act_type, ActType.TAG)
                self.assertEqual(tmp.tag, exp_type)
                self.assertEqual(tmp.tag_info, expected)

    def test_break_symbol(self):
        data = [
                ("****", "****"),
                ]

        for v, expected in data:
            with self.subTest(v=v, expected=expected):
                tmp = self.ma.break_symbol(v)
                self.assertIsInstance(tmp, TagAction)
                self.assertEqual(tmp.act_type, ActType.TAG)
                self.assertEqual(tmp.tag, TagType.SYMBOL)
                self.assertEqual(tmp.tag_info, expected)

    def test_combine(self):
        data = [
                ((self.taro.be("a test"),), 1),
                ((self.taro.be("a test"), self.taro.be("a test")), 2),
                ]

        for args, expected in data:
            with self.subTest(args=args, expected=expected):
                tmp = self.ma.combine(*args)
                self.assertIsInstance(tmp, ActionGroup)
                self.assertEqual(len(tmp.actions), expected)
                self.assertEqual(tmp.actions, args)

    def test_comment(self):
        data = [
                ("a test"),
                ]

        for cmt in data:
            with self.subTest(cmt=cmt):
                tmp = self.ma.comment(cmt)
                self.assertIsInstance(tmp, TagAction)
                self.assertEqual(tmp.act_type, ActType.TAG)
                self.assertEqual(tmp.tag, TagType.COMMENT)
                self.assertEqual(tmp.tag_info, cmt)

    def test_hr(self):
        data = [
                (TagType.HR, ""),
                ]

        for tag, info in data:
            with self.subTest(tag=tag, info=info):
                tmp = self.ma.hr()
                self.assertIsInstance(tmp, TagAction)
                self.assertEqual(tmp.tag, tag)
                self.assertEqual(tmp.tag_info, info)

    def test_info(self):
        tmp = Master('test')
        self.assertIsInstance(tmp.info("test"), Info)

    def test_nothing(self):
        tmp = Master('test')
        self.assertIsInstance(tmp.nothing(), Nothing)

    def test_scene(self):
        data = [
                ("test1", (self.taro.do(),), LangType.JPN, None,
                    "test1", 3, LangType.JPN),
                ("test2", (self.taro.do(), self.taro.do()), LangType.JPN, True,
                    "test2", 3, LangType.JPN),
                ]

        for title, acts, lng, nobr, exp_title, exp_actlen, exp_lng in data:
            with self.subTest(title=title, acts=acts, lng=lng, nobr=nobr,
                    exp_title=exp_title, exp_actlen=exp_actlen, exp_lng=exp_lng):
                tmp = self.ma.scene(title, *acts, lang=lng, is_nobr=True) if nobr else self.ma.scene(title, *acts, lang=lng)
                self.assertIsInstance(tmp, ActionGroup)
                self.assertEqual(tmp.act_type, ActType.GROUP)
                self.assertEqual(len(tmp.actions), exp_actlen)
                self.assertEqual(tmp.actions[0].tag_info, exp_title)
                self.assertEqual(tmp.lang, exp_lng)

    def test_set_days(self):
        data = (
                ("t1", "test1", 1, 10, 2000, 12, 30, "note"),
                ("t2", "test2", 1, 10, 2000, 12, 30,),
                ("t3", "test3", 1, 10, 2000, 12,)
                )
        expected = (
                ("t1", "test1", 1, 10, 2000, 12, 30, "note"),
                ("t2", "test2", 1, 10, 2000, 12, 30, ""),
                ("t3", "test3", 1, 10, 2000, 12, 0, ""),
                )
       
        ma = Master("test")
        ma.set_days(data)
        for i in range(len(data)):
            exp = expected[i]
            k = exp[0]
            self.assertEqual(ma[k].name, exp[1])
            self.assertEqual(ma[k].mon, exp[2])
            self.assertEqual(ma[k].day, exp[3])
            self.assertEqual(ma[k].year, exp[4])
            self.assertEqual(ma[k].hour, exp[5])
            self.assertEqual(ma[k].min, exp[6])
            self.assertEqual(ma[k].note, exp[7])

    def test_set_db(self):
        data_p = (
                ("p1", "taro", 17, "male", "student"),
                )
        data_s = (
                ("s1", "stage1"),
                )
        data_d = (
                ("d1", "day1"),
                )
        data_i = (
                ("i1", "item1"),
                )
        data_w = (
                ("w1", "word1"),
                )
        expected = (
                ('p1', Person),
                ('s1', Stage),
                ('d1', Day),
                ('i1', Item),
                ('w1', Word),
                )
        ma = Master("test")
        ma.set_db(data_p, data_s, data_d, data_i, data_w)
        for k, exp in expected:
            self.assertIsInstance(ma[k], exp)

    def test_set_db_when_lacked(self):
        data_p = (("p1", "Taro", 17, "male", "student"),)
        data_s = (("s1", "stage1"),)
        data_d = (("d1", "day1"),)
        data_i = (("i1", "item1"),)
        data_w = (("w1", "word1"),)
        data = [
                (data_p, data_s, data_d, data_i, data_w),
                (data_p, data_s, data_d, data_i, None),
                (data_p, data_s, data_d, None, None),
                (data_p, data_s, None, None, None),
                (data_p, None, None, None, None),
                (None, None, None, None, None),
                ]

        for p, s, d, i, w in data:
            with self.subTest(p=p, s=s, d=d, i=i, w=w):
                ma = Master('test')
                self.assertIsInstance(ma.set_db(p, s, d, i, w), Master)

    def test_set_flags(self):
        data = (
                ("test1", "test"),
                ("test2", "apple"),
                ("test3", "orange"),
                )
        expected = (
                ("f_test1", "test"),
                ("f_test2", "apple"),
                ("f_test3", "orange")
                )
        ma = Master("test")
        ma.set_flags(data)

        for k, info in expected:
            self.assertIsInstance(ma[k], Flag)
            self.assertEqual(ma[k].note, info)

    def test_set_items(self):
        data = (
                ("t1", "item1"),
                ("t2", "item2"),
                )
        expected = (
                ("t1", "item1", ""),
                ("t2", "item2", ""),
                )
        ma = Master("test")
        ma.set_items(data)
        for k, name, note in expected:
            self.assertIsInstance(ma[k], Item)
            self.assertEqual(ma[k].name, name)
            self.assertEqual(ma[k].note, note)

    def test_set_persons(self):
        data = (
                ("p1", "Taro", 17, "male", "student"),
                ("p2", "Hana", 15, "female", "student"),
                )
        expected = (
                ("p1", "Taro", 17, "male", "student", {"me":"私"}, ""),
                ("p2", "Hana", 15, "female", "student", {"me":"私"}, ""),
                )
        ma = Master("test")
        ma.set_persons(data)
        for k, name, age, sex, job, calling, note in expected:
            self.assertIsInstance(ma[k], Person)
            self.assertEqual(ma[k].name, name)
            self.assertEqual(ma[k].age, age)
            self.assertEqual(ma[k].sex, sex)
            self.assertEqual(ma[k].job, job)
            self.assertEqual(ma[k].calling, calling)
            self.assertEqual(ma[k].note, note)

    def test_set_stages(self):
        data = (
                ("s1", "stage1",),
                ("s2", "stage2"),
                )
        expected = (
                ("s1", "stage1", ""),
                ("s2", "stage2", ""),
                )
        ma = Master("test")
        ma.set_stages(data)
        for k, name, note in expected:
            self.assertIsInstance(ma[k], Stage)
            self.assertEqual(ma[k].name, name)
            self.assertEqual(ma[k].note, note)

    def test_set_words(self):
        data = (
                ("w1", "word1"),
                ("w2", "word2"),
                )
        expected = (
                ("w1", "word1", ""),
                ("w2", "word2", ""),
                )
        ma = Master("test")
        ma.set_words(data)
        for k, name, note in expected:
            self.assertIsInstance(ma[k], Word)
            self.assertEqual(ma[k].name, name)
            self.assertEqual(ma[k].note, note)

    def test_something(self):
        tmp = Master('test')
        self.assertIsInstance(tmp.some(), Something)

    def test_story(self):
        data = [
                ("test1", (self.taro.do(),), LangType.JPN,
                    "test1", 2, LangType.JPN),
                ]
        for title, acts, lng, exp_title, exp_actlen, exp_lng in data:
            with self.subTest(title=title, acts=acts, lng=lng,
                    exp_title=exp_title, exp_actlen=exp_actlen, exp_lng=exp_lng):
                tmp = self.ma.story(title, *acts, lang=lng)
                self.assertIsInstance(tmp, ActionGroup)
                self.assertEqual(tmp.act_type, ActType.GROUP)
                self.assertEqual(len(tmp.actions), exp_actlen)
                self.assertEqual(tmp.actions[0].tag_info, exp_title)
                self.assertEqual(tmp.lang, exp_lng)

    def test_title(self):
        data = [
                ("test", "test"),
                ]

        for v, expected in data:
            tmp = self.ma.title(v)
            self.assertIsInstance(tmp, TagAction)
            self.assertEqual(tmp.tag, TagType.TITLE)
            self.assertEqual(tmp.tag_info, expected)

