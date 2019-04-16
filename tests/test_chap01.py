# -*- coding: utf-8 -*-
"""Test the story of main
"""
import unittest
import storybuilder.builder.testtools as testtools
from storybuilder.builder.sbutils import print_test_title
from src.main import master, story
from src.main import CHARAS, STAGES
from src.chapter01 import story01, ep_intro, ep_everyday, ep_raceticket, ep_firstrace


_FILENAME = 'chapter01.py'


class StoryTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print_test_title(_FILENAME, "chapter 01")

    def setUp(self):
        self.ma = master()
        self.story = story01(self.ma)
        self.ep1 = ep_intro(self.ma)
        self.ep2 = ep_everyday(self.ma)
        self.ep3 = ep_raceticket(self.ma)
        self.ep4 = ep_firstrace(self.ma)

    def test_exists_looking(self):
        pass

    def test_has_basic_infos(self):
        m = self.ma
        data = [
                ("chapter01", self.story, m.anri, m.dad),
                ("ep1", self.ep1, m.anri, m.dad),
                ("ep2", self.ep2, m.anri, m.dad),
                ("ep3", self.ep3, m.anri, m.dad),
                ("ep4", self.ep4, m.anri, m.dad),
                ]

        for title, story, hero, rival in data:
            with self.subTest(title=title, story=story, hero=hero, rival=rival):
                self.assertTrue(testtools.has_basic_infos(self, story, hero, rival))

    def test_has_outline_infos(self):
        m = self.ma
        data = [
                ("chapter01", self.story,
                    m.anri.do(m.sr, "参加").want(),
                    m.anri.look(m.dad, m.sr, "参加すると").can(),
                    m.anri.have(m.ticket1),
                    m.anri.go("参加", m.ticket1),
                    ),
                ("ep1", self.ep1,
                    m.anri.be(),
                    m.anri.be(),
                    m.anri.be(),
                    m.anri.be(),
                    ),
                ("ep2", self.ep2,
                    m.anri.be(),
                    m.anri.be(),
                    m.anri.be(),
                    m.anri.be(),
                    ),
                ("ep3", self.ep3,
                    m.anri.be(),
                    m.anri.be(),
                    m.anri.be(),
                    m.anri.be(),
                    ),
                ("ep4", self.ep4,
                    m.anri.be(),
                    m.anri.be(),
                    m.anri.be(),
                    m.anri.be(),
                    ),
                ]

        for title, story, what, why, how, result in data:
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
