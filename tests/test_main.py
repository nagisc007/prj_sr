# -*- coding: utf-8 -*-
"""Test the story of main
"""
import unittest
import storybuilder.builder.testtools as testtools
from storybuilder.builder.sbutils import print_test_title
from src.main import master, story
from src.main import CHARAS, STAGES


_FILENAME = 'main.py'


class StoryTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print_test_title(_FILENAME, "main story")

    def setUp(self):
        self.ma = master()
        self.story = story(self.ma)

    def test_is_all_actions(self):
        self.assertTrue(testtools.is_all_actions(self.story))

    @unittest.skip('in preparation')
    def test_exists_looking(self):
        for k in [v[0] for v in CHARAS] + [v[0] for v in STAGES]:
            with self.subTest(k=k):
                self.assertTrue(testtools.exists_looking_of_the_subject(self.story, self.ma[k]))

    def test_followed_flags(self):
        self.assertTrue(testtools.followed_all_flags(self, self.story))

    def test_has_basic_infos(self):
        m = self.ma
        data = [
                ("story", self.story, m.anri, m.dad),
                ]

        for title, story, hero, rival in data[0:1]:
            with self.subTest(title=title, story=story, hero=hero, rival=rival):
                self.assertTrue(testtools.has_basic_infos(self, story, hero, rival))

    def test_has_outline_infos(self):
        m = self.ma
        data = [
                ("story", self.story,
                    m.anri.look("会う", m.dad).want(),
                    m.anri.talk(m.dad, m.mam, "殺した"),
                    m.anri.talk(m.sr, "優勝すれば会える"),
                    m.anri.do("敗北")),
                ]

        for title, story, what, why, how, result in data[0:1]:
            with self.subTest(title=title, story=story, what=what, why=why, how=how, result=result):
                self.assertTrue(testtools.has_outline_infos(self, story, what, why, how, result))
