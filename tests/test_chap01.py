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
                ("ep1", self.ep1, m.anri, m.golda),
                ("ep2", self.ep2, m.anri, m.chief),
                ("ep3", self.ep3, m.anri, m.golda),
                ("ep4", self.ep4, m.anri, m.golda),
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
                    m.anri.go(m.race1stage),
                    ),
                ("ep1", self.ep1,
                    m.anri.do("逮捕", m.partsrobber),
                    m.chief.deal("被害", m.partsrobber),
                    m.anri.look("見張る", m.wreckfactory),
                    m.anri.deal("通報", m.golda, m.partsrobber),
                    ),
                ("ep2", self.ep2,
                    m.anri.do(m.sr, "参加").want(),
                    m.anri.look(m.dad, m.sr, "参加すると").can(),
                    m.anri.deal("申し込み", m.ticket1),
                    m.anri.know("当選", m.ticket1),
                    ),
                ("ep3", self.ep3,
                    m.anri.have(m.ticket1).must(),
                    m.anri.go(m.race1).want(),
                    m.anri.go("取りに行く", m.ticketcenter),
                    m.anri.have("奪う", m.golda).ps(),
                    ),
                ("ep4", self.ep4,
                    m.anri.go(m.race1).must(),
                    m.anri.ask(m.dad, m.dad_reason).want(),
                    m.anri.have(m.ticket1),
                    m.anri.go(m.race1stage),
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
                m.sr,
                ]

        for v in data:
            with self.subTest(v=v):
                self.assertTrue(testtools.has_the_keyword(self.story, v))
