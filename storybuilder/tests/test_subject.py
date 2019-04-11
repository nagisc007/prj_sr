# -*- coding: utf-8 -*-
"""Test for subject.py
"""
import unittest
from builder.sbutils import print_test_title
from builder.subject import Subject,Person, Day, Item, Stage, Word
from builder.subject import Something, Info, Nothing
from builder.subject import Action
from builder.enums import ActType


_FILENAME = "subject.py"


class SubjectTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print_test_title(_FILENAME, "Subject")

    def setUp(self):
        self.taro = Subject("Taro")

    def test_attributes(self):
        data = [
                ("Taro", "test",
                    "Taro", "test"),
                ("Hanako", "",
                    "Hanako", ""),
                ]

        for name, note, exp_name, exp_note in data:
            with self.subTest(name=name, note=note, exp_name=exp_name, exp_note=exp_note):
                tmp = Subject(name, note) if note else Subject(name)
                self.assertIsInstance(tmp, Subject)
                self.assertEqual(tmp.name, exp_name)
                self.assertEqual(tmp.note, exp_note)

    def test_be_do_explain(self):
        sub = Subject("test")
        data = [
                ("be", (sub,), "",
                    ActType.BE, self.taro, "be", (sub,)),
                ("do", (sub,), "",
                    ActType.DO, self.taro, "do", (sub,)),
                ("explain", (sub,), "",
                    ActType.EXPLAIN, self.taro, "explain", (sub,)),
                ]

        for attr, obj, verb, exp_type, exp_sub, exp_verb, exp_obj in data:
            with self.subTest(attr=attr, obj=obj, verb=verb,
                    exp_type=exp_type, exp_sub=exp_sub, exp_verb=exp_verb, exp_obj=exp_obj):
                doing = getattr(self.taro, attr)
                tmp = doing(*obj, verb=verb) if verb else doing(*obj)
                self.assertIsInstance(tmp, Action)
                self.assertEqual(tmp.act_type, exp_type)
                self.assertEqual(tmp.subject, exp_sub)
                self.assertEqual(tmp.verb, exp_verb)
                self.assertEqual(tmp.objects, exp_obj)

    def test_objects_from(self):
        sub = Subject("Taro")
        data = [
                ((sub,),
                    (sub,)),
                (("test",),
                    (Info("test"),)),
                ]
        for v, expected in data:
            with self.subTest(v=v, expected=expected):
                test = Subject("test")
                tmp = test.objects_from(*v)
                for t, exp in zip(tmp, expected):
                    self.assertEqual(type(t), type(exp))


class InfoTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print_test_title(_FILENAME, "Info")

    def test_attributes(self):
        data = [
                ("test",
                    Info._NAME, "test"),
                ]

        for v, exp_name, exp_note in data:
            tmp = Info(v)
            self.assertIsInstance(tmp, Info)
            self.assertEqual(tmp.name, exp_name)
            self.assertEqual(tmp.note, exp_note)


class NothingTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print_test_title(_FILENAME, "Nothing")

    def test_attributes(self):
        data = [
                (Nothing._NAME, ""),
                ]
        for exp_name, exp_note in data:
            with self.subTest(exp_name=exp_name, exp_note=exp_note):
                tmp = Nothing()
                self.assertIsInstance(tmp, Nothing)
                self.assertEqual(tmp.name, exp_name)
                self.assertEqual(tmp.note, exp_note)

class SomethingTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print_test_title(_FILENAME, "Something")

    def test_attributes(self):
        data = [
                (Something._NAME, ""),
                ]

        for exp_name, exp_note in data:
            with self.subTest(exp_name=exp_name, exp_note=exp_note):
                tmp = Something()
                self.assertIsInstance(tmp, Something)
                self.assertEqual(tmp.name, exp_name)
                self.assertEqual(tmp.note, exp_note)


class PersonTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print_test_title(_FILENAME, "Person")

    def setUp(self):
        self.taro = Subject("Taro")
        self.hanako = Person("Hanako", 17, "female", "student")

    def test_attributes(self):
        data = [
                ("Taro", 17, "male", "student", "俺", "a man",
                    "Taro", 17, "male", "student", {"me":"俺"}, "a man"),
                ]
        for name, age, sex, job, calling, note, exp_name, exp_age, exp_sex, exp_job, exp_calling, exp_note in data:
            with self.subTest(name=name, age=age, sex=sex, job=job, calling=calling, note=note,
                    exp_name=exp_name, exp_age=exp_age, exp_sex=exp_sex, exp_job=exp_job,
                    exp_calling=exp_calling, exp_note=exp_note):
                tmp = Person(name, age, sex, job, calling, note)
                self.assertIsInstance(tmp, Person)
                self.assertEqual(tmp.name, exp_name)
                self.assertEqual(tmp.age, exp_age)
                self.assertEqual(tmp.sex, exp_sex)
                self.assertEqual(tmp.job, exp_job)
                self.assertEqual(tmp.calling, exp_calling)
                self.assertEqual(tmp.note, exp_note)

    def test_behaviors(self):
        data = [
                ("ask", (self.taro,), "",
                    ActType.TALK, self.hanako, "ask", (self.taro,)),
                ("behav", (self.taro,), "",
                    ActType.BEHAV, self.hanako, "behav", (self.taro,)),
                ("come", (self.taro,), "",
                    ActType.MOVE, self.hanako, "come", (self.taro,)),
                ("deal", (self.taro,), "",
                    ActType.DEAL, self.hanako, "deal", (self.taro,)),
                ("feel", (self.taro,), "",
                    ActType.FEEL, self.hanako, "feel", (self.taro,)),
                ("go", (self.taro,), "",
                    ActType.MOVE, self.hanako, "go", (self.taro,)),
                ("have", (self.taro,), "",
                    ActType.DEAL, self.hanako, "have", (self.taro,)),
                ("hear", (self.taro,), "",
                    ActType.TALK, self.hanako, "hear", (self.taro,)),
                ("know", (self.taro,), "",
                    ActType.THINK, self.hanako, "know", (self.taro,)),
                ("look", (self.taro,), "",
                    ActType.LOOK, self.hanako, "look", (self.taro,)),
                ("move", (self.taro,), "",
                    ActType.MOVE, self.hanako, "move", (self.taro,)),
                ("remember", (self.taro,), "",
                    ActType.THINK, self.hanako, "remember", (self.taro,)),
                ("reply", (self.taro,), "",
                    ActType.TALK, self.hanako, "reply", (self.taro,)),
                ("talk", (self.taro,), "",
                    ActType.TALK, self.hanako, "talk", (self.taro,)),
                ("think", (self.taro,), "",
                    ActType.THINK, self.hanako, "think", (self.taro,)),
                ]

        for attr, obj, verb, exp_type, exp_sub, exp_verb, exp_obj in data:
            with self.subTest(attr=attr, obj=obj, verb=verb,
                    exp_type=exp_type, exp_sub=exp_sub, exp_verb=exp_verb, exp_obj=exp_obj):
                doing = getattr(self.hanako, attr)
                tmp = doing(*obj, verb=verb) if verb else doing(*obj)
                self.assertIsInstance(tmp, Action)
                self.assertEqual(tmp.act_type, exp_type)
                self.assertEqual(tmp.subject, exp_sub)
                self.assertEqual(tmp.verb, exp_verb)
                self.assertEqual(tmp.objects, exp_obj)


class DayTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print_test_title(_FILENAME, "Day")

    def test_attributes(self):
        data = [
                ("test1", 1, 10, 2000, 12, 30, "a note",
                    "test1", 1, 10, 2000, 12, 30, "a note"),
                ("test2", 2, 11, 2001, 13, 31, "",
                    "test2", 2, 11, 2001, 13, 31, ""),
                ("test3", 3, 12, 2002, 14, 32, "",
                    "test3", 3, 12, 2002, 14, 32, ""),
                ("test4", 4, 13, 2003, 15, None, "",
                    "test4", 4, 13, 2003, 15, 0, ""),
                ("test5", 5, 14, 2004, None, None, "",
                    "test5", 5, 14, 2004, 0, 0, ""),
                ("test6", 6, 15, None, None, None, "",
                    "test6", 6, 15, 0, 0, 0, ""),
                ("test7", 7, None, None, None, None, "",
                    "test7", 7, 0, 0, 0, 0, ""),
                ("test8", None, None, None, None, None, "",
                    "test8", 0, 0, 0, 0, 0, ""),
                ]

        def creator(name, mon, day, year, hour, mi, note):
            if mon and day and year and hour and mi and note:
                return Day(name, mon, day, year, hour, mi, note)
            elif mon and day and year and hour and mi:
                return Day(name, mon, day, year, hour, mi)
            elif mon and day and year and hour:
                return Day(name, mon, day, year, hour)
            elif mon and day and year:
                return Day(name, mon, day, year)
            elif mon and day:
                return Day(name, mon, day)
            elif mon:
                return Day(name, mon)
            else:
                return Day(name)

        for name, mon, day, year, hour, mi, note, exp_name, exp_mon, exp_day, exp_year, exp_hour, exp_mi, exp_note in data:
            with self.subTest(name=name, mon=mon, day=day, year=year, hour=hour, mi=mi, note=note,
                exp_name=exp_name, exp_mon=exp_mon, exp_day=exp_day, exp_hour=exp_hour,
                exp_mi=exp_mi, exp_note=exp_note):
                tmp = creator(name, mon, day, year, hour, mi, note)
                self.assertIsInstance(tmp, Day)
                self.assertEqual(tmp.name, exp_name)
                self.assertEqual(tmp.mon, exp_mon)
                self.assertEqual(tmp.day, exp_day)
                self.assertEqual(tmp.year, exp_year)
                self.assertEqual(tmp.hour, exp_hour)
                self.assertEqual(tmp.min, exp_mi)
                self.assertEqual(tmp.note, exp_note)

    @unittest.skip("in preparation")
    def test_elapse(self):
        pass


class ItemTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print_test_title(_FILENAME, "Item")

    def setUp(self):
        self.taro = Person("Taro", 17, "male", "student")
        self.hanako = Person("Hanako", 17, "female", "student")

    def test_attributes(self):
        data = [
                ("test", "a note",
                    "test", "a note"),
                ("test", "",
                    "test", ""),
                ]
        for name, note, exp_name, exp_note in data:
            with self.subTest(name=name, note=note, exp_name=exp_name, exp_note=exp_note):
                tmp = Item(name, note) if note else Item(name)
                self.assertIsInstance(tmp, Item)
                self.assertEqual(tmp.name, exp_name)
                self.assertEqual(tmp.note, exp_note)

    def test_move(self):
        data = [
                ("move", (self.taro,), "",
                    ActType.MOVE, self.hanako, "move", (self.taro,)),
                ]

        for attr, obj, verb, exp_type, exp_sub, exp_verb, exp_obj in data:
            with self.subTest(attr=attr, obj=obj, verb=verb,
                    exp_type=exp_type, exp_sub=exp_sub, exp_verb=exp_verb, exp_obj=exp_obj):
                doing = getattr(self.hanako, attr)
                tmp = doing(*obj, verb=verb) if verb else doing(*obj)
                self.assertIsInstance(tmp, Action)
                self.assertEqual(tmp.act_type, exp_type)
                self.assertEqual(tmp.subject, exp_sub)
                self.assertEqual(tmp.verb, exp_verb)
                self.assertEqual(tmp.objects, exp_obj)


class StageTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print_test_title(_FILENAME, "Stage")

    def setUp(self):
        self.taro = Person("Taro", 17, "male", "student")
        self.hanako = Person("Hanako", 17, "female", "student")


    def test_attributes(self):
        data = [
                ("test", "a note",
                    "test", "a note"),
                ("test", "",
                    "test", ""),
                ]

        for name, note, exp_name, exp_note in data:
            with self.subTest(name=name, note=note, exp_name=exp_name, exp_note=exp_note):
                tmp = Stage(name, note) if note else Stage(name)
                self.assertIsInstance(tmp, Stage)
                self.assertEqual(tmp.name, exp_name)
                self.assertEqual(tmp.note, exp_note)

    def test_move(self):
        data = [
                ("move", (self.taro,), "",
                    ActType.MOVE, self.hanako, "move", (self.taro,)),
                ]

        for attr, obj, verb, exp_type, exp_sub, exp_verb, exp_obj in data:
            with self.subTest(attr=attr, obj=obj, verb=verb,
                    exp_type=exp_type, exp_sub=exp_sub, exp_verb=exp_verb, exp_obj=exp_obj):
                doing = getattr(self.hanako, attr)
                tmp = doing(*obj, verb=verb) if verb else doing(*obj)
                self.assertIsInstance(tmp, Action)
                self.assertEqual(tmp.act_type, exp_type)
                self.assertEqual(tmp.subject, exp_sub)
                self.assertEqual(tmp.verb, exp_verb)
                self.assertEqual(tmp.objects, exp_obj)



class WordTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print_test_title(_FILENAME, "Word")

    def test_attributes(self):
        data = [
                ("test", "a note",
                    "test", "a note"),
                ("test", "",
                    "test", "")
                ]

        for name, note, exp_name, exp_note in data:
            with self.subTest(name=name, note=note, exp_name=exp_name, exp_note=exp_note):
                tmp = Word(name, note) if note else Word(name)
                self.assertIsInstance(tmp, Word)
                self.assertEqual(tmp.name, exp_name)
                self.assertEqual(tmp.note, exp_note)

