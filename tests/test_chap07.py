# -*- coding: utf-8 -*-
"""Test the story of main
"""
import unittest
import storybuilder.builder.testtools as testtools
from storybuilder.builder.sbutils import print_test_title
from src.main import master, story
from src.main import CHARAS, STAGES
from src.chapter07 import story07, ep_intro, ep_grandprix, ep_re_sagisawa, ep_consolation


_FILENAME = 'chapter07.py'


class StoryTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print_test_title(_FILENAME, "chapter 07")

    def setUp(self):
        self.m = master()
        self.story = story07(self.m)
        self.ep1 = ep_intro(self.m)
        self.ep2 = ep_grandprix(self.m)
        self.ep3 = ep_re_sagisawa(self.m)
        self.ep4 = ep_consolation(self.m)

    def test_exists_looking(self):
        pass

    def test_has_basic_infos(self):
        m = self.m
        data = [
                ("chapter07", self.story, m.anri, m.sagisawa),
                ("ep1", self.ep1, m.anri, m.sagisawa),
                ("ep2", self.ep2, m.anri, m.sagisawa),
                ("ep3", self.ep3, m.anri, m.sagisawa),
                ("ep4", self.ep4, m.anri, m.sagisawa),
                ]

        for title, story, hero, rival in data:
            with self.subTest(title=title, story=story, hero=hero, rival=rival):
                self.assertTrue(testtools.has_basic_infos(self, story, hero, rival))

    def test_has_outline_infos(self):
        m = self.m
        data = [
                ("chapter07", self.story,
                    m.anri.have(m.grandticket).want(),
                    m.anri.think(m.dad_reason).want(),
                    m.anri.have(m.sagisawa, m.sagi_proposal2),
                    m.anri.go(m.race_cons, "参加"),
                    ),
                ("ep1", self.ep1,
                    m.anri.look(m.grandticket).must(),
                    m.anri.meet(m.dad).want(),
                    m.anri.look(m.sr, m.grandrace),
                    m.anri.meet(m.sagisawa),
                    ),
                ("ep2", self.ep2,
                    m.anri.be(),
                    m.anri.be(),
                    m.anri.be(),
                    m.anri.hear(m.sagisawa, m.sagi_proposal2),
                    ),
                ("ep3", self.ep3,
                    m.anri.have(m.grandticket).want(),
                    m.anri.be(m.anri_reason),
                    m.anri.hear(m.sagisawa, m.sagi_proposal2),
                    m.anri.think(m.sagi_proposal2),
                    ),
                ("ep4", self.ep4,
                    m.anri.have(m.grandticket).must(),
                    m.anri.know(m.dad_reason).want(),
                    m.anri.deal(m.sagi_proposal2),
                    m.anri.go(m.race_cons, "参加"),
                    ),
                ]

        for title, story, what, why, how, result in data:
            with self.subTest(title=title, story=story, what=what, why=why, how=how, result=result):
                self.assertTrue(testtools.has_outline_infos(self, story, what, why, how, result, True))

    @unittest.skip("in preparation")
    def test_has_the_action(self):
        m = self.m
        data = [
                m.droid.explain("作業ドロイド"),
                ]

        for v in data:
            with self.subTest(v=v):
                self.assertTrue(testtools.has_the_action(self.story, v, testtools.MatchLv.NEAR))

    @unittest.skip("in preparation")
    def test_has_the_keyword(self):
        m = self.m
        data = [
                "ドロイド",
                ]

        for v in data:
            with self.subTest(v=v):
                self.assertTrue(testtools.has_the_keyword(self.story, v))
