# -*- coding: utf-8 -*-
"""Test the story of main
"""
import unittest
import storybuilder.builder.testtools as testtools
from storybuilder.builder.sbutils import print_test_title
from src.main import master, story
from src.main import CHARAS, STAGES
from src.chapter06 import story06, ep_intro, ep_racer, ep_goalline, ep_retire


_FILENAME = 'chapter06.py'


class StoryTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print_test_title(_FILENAME, "chapter 06")

    def setUp(self):
        self.m = master()
        self.story = story06(self.m)
        self.ep1 = ep_intro(self.m)
        self.ep2 = ep_racer(self.m)
        self.ep3 = ep_goalline(self.m)
        self.ep4 = ep_retire(self.m)

    def test_exists_looking(self):
        pass

    def test_has_basic_infos(self):
        m = self.m
        data = [
                ("chapter06", self.story, m.anri, m.rondo),
                ("ep1", self.ep1, m.anri, m.rondo),
                ("ep2", self.ep2, m.anri, m.rondo),
                ("ep3", self.ep3, m.anri, m.rondo),
                ("ep4", self.ep4, m.anri, m.rondo),
                ]

        for title, story, hero, rival in data:
            with self.subTest(title=title, story=story, hero=hero, rival=rival):
                self.assertTrue(testtools.has_basic_infos(self, story, hero, rival))

    def test_has_outline_infos(self):
        m = self.m
        data = [
                ("chapter06", self.story,
                    m.anri.have(m.race2, "優勝").want(),
                    m.anri.think(m.race2, "勝利する").want(),
                    m.anri.have(m.rondo, "協力"),
                    m.anri.go(m.race2, m.retire),
                    ),
                ("ep1", self.ep1,
                    m.anri.do(m.rondo, "邪魔").must(),
                    m.anri.have(m.grandticket, m.sagi_proposal).can(),
                    m.anri.do(m.rondo, "戦う"),
                    m.anri.talk(m.rondo, "告白", m.sagi_proposal),
                    ),
                ("ep2", self.ep2,
                    m.anri.have(m.grandticket).must(),
                    m.anri.have(m.anri_reason),
                    m.anri.talk(m.rondo, "話し合う"),
                    m.anri.reply(m.rondo, "協力"),
                    ),
                ("ep3", self.ep3,
                    m.anri.go(m.rondo, m.race2, "ペアでゴール").must(),
                    m.race2.be("ルール"),
                    m.anri.deal(m.angelwing),
                    m.angelwing.be("破損"),
                    ),
                ("ep4", self.ep4,
                    m.anri.go(m.rondo, "ゴール", "一緒に").must(),
                    m.race2.be("レース条件"),
                    m.anri.deal(m.rondo, "協力"),
                    m.anri.have(m.race2, "優勝").non(),
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
