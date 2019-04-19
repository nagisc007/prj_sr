# -*- coding: utf-8 -*-
"""Test the story of main
"""
import unittest
import storybuilder.builder.testtools as testtools
from storybuilder.builder.sbutils import print_test_title
from src.main import master, story
from src.main import CHARAS, STAGES
from src.chapter04 import story04, ep_intro, ep_boringday, ep_stranger, ep_retry


_FILENAME = 'chapter04.py'


class StoryTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print_test_title(_FILENAME, "chapter 04")

    def setUp(self):
        self.m = master()
        self.story = story04(self.m)
        self.ep1 = ep_intro(self.m)
        self.ep2 = ep_boringday(self.m)
        self.ep3 = ep_stranger(self.m)
        self.ep4 = ep_retry(self.m)

    def test_exists_looking(self):
        pass

    def test_has_basic_infos(self):
        m = self.m
        data = [
                ("chapter04", self.story, m.anri, m.sagisawa),
                ("ep1", self.ep1, m.anri, m.chief),
                ("ep2", self.ep2, m.anri, m.sagisawa),
                ("ep3", self.ep3, m.anri, m.sagisawa),
                ("ep4", self.ep4, m.anri, m.rondo),
                ]

        for title, story, hero, rival in data:
            with self.subTest(title=title, story=story, hero=hero, rival=rival):
                self.assertTrue(testtools.has_basic_infos(self, story, hero, rival))

    def test_has_outline_infos(self):
        m = self.m
        data = [
                ("chapter04", self.story,
                    m.anri.have(m.ticket2).want(),
                    m.anri.have(m.grandticket).can(),
                    m.anri.hear(m.sagisawa, m.race2, m.sagi_proposal),
                    m.anri.go(m.rondo, m.race2, "ペアで"),
                    ),
                ("ep1", self.ep1,
                    m.anri.look(m.race2, "参加方法").must(),
                    m.anri.be("負けた", m.race1),
                    m.anri.have(m.dealer, m.race_ticket),
                    m.anri.talk(m.chief, "諦めろ", m.race2),
                    ),
                ("ep2", self.ep2,
                    m.anri.have(m.ticket2).must(),
                    m.anri.go(m.race2, m.ticket2).can(),
                    m.anri.look(m.some(), m.ticket2, "持っている"),
                    m.anri.meet(m.sagisawa),
                    ),
                ("ep3", self.ep3,
                    m.anri.hear(m.sagisawa),
                    m.sagisawa.talk(m.anri, "レースに関する話"),
                    m.anri.look("確かめる", m.sagi_proposal),
                    m.sagisawa.talk(m.anri, m.sagi_proposal),
                    ),
                ("ep4", self.ep4,
                    m.anri.deal("参加", m.race2).want(),
                    m.anri.have(m.grandticket).must(),
                    m.anri.deal("承諾", m.sagi_proposal),
                    m.anri.go(m.rondo, m.race2, "ペアで"),
                    ),
                ]

        for title, story, what, why, how, result in data[0:1]:
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
