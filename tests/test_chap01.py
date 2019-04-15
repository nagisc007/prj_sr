# -*- coding: utf-8 -*-
"""Test the story of main
"""
import unittest
import storybuilder.builder.testtools as testtools
from storybuilder.builder.sbutils import print_test_title
from src.main import master, story
from src.main import CHARAS, STAGES
from src.chapter01 import story01


_FILENAME = 'chapter01.py'


class StoryTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print_test_title(_FILENAME, "chapter 01")

    def setUp(self):
        self.ma = master()
        self.story = story01(self.ma)

    def test_exists_looking(self):
        pass

    def test_has_basic_infos(self):
        m = self.ma
        data = [
                ("chapter01", self.story, m.anri, m.dad),
                ]

        for title, story, hero, rival in data[0:1]:
            with self.subTest(title=title, story=story, hero=hero, rival=rival):
                self.assertTrue(testtools.has_basic_infos(self, story, hero, rival))

    def test_has_outline_infos(self):
        m = self.ma
        data = [
                ("chapter01", self.story,
                    m.anri.be(),
                    m.anri.be(),
                    m.anri.be(),
                    m.anri.be()),
                ]

        for title, story, what, why, how, result in data[0:1]:
            with self.subTest(title=title, story=story, what=what, why=why, how=how, result=result):
                self.assertTrue(testtools.has_outline_infos(self, story, what, why, how, result))

