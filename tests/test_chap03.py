# -*- coding: utf-8 -*-
"""Test the story of main
"""
import unittest
import storybuilder.builder.testtools as testtools
from storybuilder.builder.sbutils import print_test_title
from src.main import master, story
from src.main import CHARAS, STAGES
from src.chapter03 import story03, ep_intro, ep_dashdash, ep_recoop, ep_lostwin


_FILENAME = 'chapter03.py'


class StoryTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print_test_title(_FILENAME, "chapter 03")

    def setUp(self):
        self.ma = master()
        self.story = story03(self.ma)
        self.ep1 = ep_intro(self.ma)
        self.ep2 = ep_dashdash(self.ma)
        self.ep3 = ep_recoop(self.ma)
        self.ep4 = ep_lostwin(self.ma)

    def test_exists_looking(self):
        pass

    def test_has_basic_infos(self):
        m = self.ma
        data = [
                ("chapter03", self.story, m.anri, m.yabu),
                ("ep1", self.ep1, m.anri, m.yabu),
                ("ep2", self.ep2, m.anri, m.yabu),
                ("ep3", self.ep3, m.anri, m.yabu),
                ("ep4", self.ep4, m.anri, m.yabu),
                ]

        for title, story, hero, rival in data:
            with self.subTest(title=title, story=story, hero=hero, rival=rival):
                self.assertTrue(testtools.has_basic_infos(self, story, hero, rival))

    def test_has_outline_infos(self):
        m = self.ma
        data = [
                ("chapter03", self.story,
                    m.anri.have(m.race1, "優勝").want(),
                    m.anri.have(m.grandticket).can(),
                    m.anri.have(m.yabu, "協力"),
                    m.anri.have(m.race1, "優勝").non(),
                    ),
                ("ep1", self.ep1,
                    m.anri.know("何が起きたか").must(),
                    m.anri.be("スタートできていない"),
                    m.anri.remember("スタート"),
                    m.anri.think(m.yabu, "嵌められた"),
                    ),
                ("ep2", self.ep2,
                    m.anri.deal("遅れを取り戻す").must(),
                    m.anri.be("出遅れた"),
                    m.anri.do(m.angelwing, "使う"),
                    m.anri.go(m.yabu, "追いつく"),
                    ),
                ("ep3", self.ep3,
                    m.anri.go(m.race1, "ゴール"),
                    m.anri.have(m.race1, "優勝"),
                    m.anri.go("先に進む"),
                    m.anri.be(m.taiga, "立ち塞がる"),
                    ),
                ("ep4", self.ep4,
                    m.anri.have(m.race1, "優勝"),
                    m.anri.have(m.grandticket),
                    m.anri.have(m.yabu, "協力", m.taiga, "倒す"),
                    m.anri.have(m.race1, "優勝").non(),
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
