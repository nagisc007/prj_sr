# -*- coding: utf-8 -*-
"""Test the story of main
"""
import unittest
import storybuilder.builder.testtools as testtools
from storybuilder.builder.sbutils import print_test_title
from src.main import master, story
from src.main import CHARAS, STAGES
from src.chapter05 import story05, ep_intro, ep_promise, ep_rondo, ep_obstacle


_FILENAME = 'chapter05.py'


class StoryTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print_test_title(_FILENAME, "chapter 05")

    def setUp(self):
        self.m = master()
        self.story = story05(self.m)
        self.ep1 = ep_intro(self.m)
        self.ep2 = ep_promise(self.m)
        self.ep3 = ep_rondo(self.m)
        self.ep4 = ep_obstacle(self.m)

    def test_exists_looking(self):
        pass

    def test_has_basic_infos(self):
        m = self.m
        data = [
                ("chapter05", self.story, m.anri, m.rondo),
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
                ("chapter05", self.story,
                    m.anri.have(m.grandticket).want(),
                    m.anri.do(m.sagi_proposal, "約束を守る", m.grandticket).can(),
                    m.anri.do(m.rondo, "優勝を邪魔する"),
                    m.anri.talk(m.rondo, "失望").ps(),
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
