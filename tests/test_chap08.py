# -*- coding: utf-8 -*-
"""Test the story of main
"""
import unittest
import storybuilder.builder.testtools as testtools
from storybuilder.builder.sbutils import print_test_title
from src.main import master, story
from src.main import CHARAS, STAGES
from src.chapter08 import story08


_FILENAME = 'chapter08.py'


class StoryTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print_test_title(_FILENAME, "chapter 08")

    def setUp(self):
        self.ma = master()
        self.story = story08(self.ma)

    def test_exists_looking(self):
        pass

    def test_has_basic_infos(self):
        m = self.ma
        data = [
                ("chapter08", self.story, m.anri, m.ren),
                ]

        for title, story, hero, rival in data[0:1]:
            with self.subTest(title=title, story=story, hero=hero, rival=rival):
                self.assertTrue(testtools.has_basic_infos(self, story, hero, rival))

    def test_has_outline_infos(self):
        m = self.ma
        data = [
                ("chapter08", self.story,
                    m.anri.have(m.grandrace, "優勝"),
                    m.anri.look(m.dad),
                    m.anri.have("奪う", "他人のパーツ"),
                    m.anri.have(m.bugparts)),
                ]

        for title, story, what, why, how, result in data[0:1]:
            with self.subTest(title=title, story=story, what=what, why=why, how=how, result=result):
                self.assertTrue(testtools.has_outline_infos(self, story, what, why, how, result, True))

    @unittest.skip("in preparation")
    def test_has_the_action(self):
        m = self.ma
        data = [
                m.droid.explain("作業ドロイド"),
                ]

        for v in data:
            with self.subTest(v=v):
                self.assertTrue(testtools.has_the_action(self.story, v, testtools.MatchLv.NEAR))

    @unittest.skip("in preparation")
    def test_has_the_keyword(self):
        m = self.ma
        data = [
                "ドロイド",
                ]

        for v in data:
            with self.subTest(v=v):
                self.assertTrue(testtools.has_the_keyword(self.story, v))
