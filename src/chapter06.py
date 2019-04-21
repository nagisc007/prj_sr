# -*- coding: utf-8 -*-
"""Story program.
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append('storybuilder')
from storybuilder.builder.master import Master
from storybuilder.builder.tools import build_to_story


# episodes
def ep_intro(m: Master):
    return m.story("冒頭",
            m.anri.be(m.race2, m.race2day, m.race2stage),
            m.anri.talk(m.rondo, "口論"),
            m.anri.have(m.sagi_proposal),
            m.rondo.talk(m.anri, "あなたの事情は知らない", "自分は優勝したいだけ"),
            m.rondo.talk(m.anri, "優勝が使命"),
            )


def ep_racer(m: Master):
    return m.story("レーサーとは",
            m.rondo.ask(m.anri, "優勝したくないの？"),
            m.anri.have(m.race2, "優勝").want(),
            m.anri.think(m.race2, "勝利する").want(),
            m.anri.reply(m.rondo, "優勝したい"),
            m.rondo.talk(m.anri, "協力"),
            )


def ep_goalline(m: Master):
    return m.story("ゴールライン",
            m.anri.ask(m.rondo, "自分を信じてくれるのか？"),
            m.rondo.reply(m.anri, "あなたの優勝したい気持ちを信じる"),
            m.angelwing.be("破損"),
            m.anri.go("失速"),
            m.anri.know(m.race2, "本当のゴールは個人戦"),
            )


def ep_retire(m: Master):
    racetime = m.race2day.elapsed_day(hour=17)
    return m.story("リタイアの選択",
            m.anri.go(m.race2stage, racetime, "ゴールに向かう"),
            m.rondo.ask(m.anri, m.angelwing),
            m.anri.go(m.rondo, "ゴール", "一緒に").must(),
            m.race2.be("レース条件"),
            m.anri.think(m.rondo, m.sagi_proposal, "自分の気持"),
            m.anri.talk(m.rondo, "一人でいけ"),
            m.anri.deal(m.rondo, "協力"),
            m.anri.go(m.race2, m.retire),
            m.anri.have(m.race2, "優勝").non(),
            )


# main
def story06(m: Master):
    return m.story("Race 6",
            ep_intro(m),
            ep_racer(m),
            ep_goalline(m),
            ep_retire(m),
            )


def main(): # pragma: no cover
    from main import master
    return build_to_story(story06(master()))


if __name__ == '__main__':
    import sys
    sys.exit(main())

