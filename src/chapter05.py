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
    racetime = m.race2day.elapsed_day(hour=13)
    return m.story("ペアレース",
            m.anri.be(m.factory, m.rondo, m.race2day),
            m.rondo.talk(m.anri, "絶対に優勝").must(),
            m.anri.reply(m.rondo, "そのつもり"),
            m.anri.have(m.grandticket).want(),
            m.anri.do(m.sagi_proposal, "約束を守る", m.grandticket).can(),
            m.anri.go(m.race2stage, m.race2day, m.race_bus),
            m.anri.think(m.rondo),
            m.anri.deal("約束", m.sagi_proposal),
            m.anri.ask(m.rondo, "なぜレースを？"),
            m.rondo.reply(m.anri, m.rondo_reason),
            m.rondo.talk(m.anri, m.kobucorp),
            m.anri.know(m.rondo, m.kobucorp),
            m.kobucorp.explain(m.dad, "父が代表の大企業"),
            )


def ep_promise(m: Master):
    racetime = m.race2day.elapsed_day(hour=14)
    waitroom = m.race2stage.insided("控室")
    startpoint = m.race2stage.insided("スタート地点")
    return m.story("暗黒の約束",
            m.anri.go(m.rondo, m.race2stage, racetime),
            m.anri.deal(m.rondo, m.race2, "受付"),
            m.anri.deal(m.race2, "参加"),
            m.anri.go(m.rondo, waitroom),
            m.rondo.talk(m.anri, "あなたのことは聞いている"),
            m.rondo.know(m.anri, m.dad),
            m.rondo.talk(m.anri, m.rondo_promise),
            m.anri.think("迷う", m.rondo_promise, m.sagi_proposal),
            )


def ep_rondo(m: Master):
    racetime = m.race2day.elapsed_day(hour=15)
    startpoint = m.race2stage.insided("スタート地点")
    return m.story("レースの申し子ロンド",
            m.anri.be(m.rondo, startpoint, racetime),
            m.race2.explain("ペアレース"),
            m.anri.go(m.rondo, "二人の合計タイム"),
            m.anri.go(m.race2, m.rondo),
            m.rondo.talk(m.anri, "足を引っ張らないでね"),
            m.race2.do("開始"),
            m.anri.be("備える"),
            m.rondo.go("一人飛び出す"),
            m.anri.go(m.rondo, "ついていく"),
            m.rondo.be("圧倒的速度"),
            m.rondo.go(m.anri, "置き去り"),
            )


def ep_obstacle(m: Master):
    racetime = m.race2day.elapsed_day(hour=16)
    return m.story("邪魔者",
            m.anri.go(m.race2stage, racetime),
            m.anri.go(m.rondo).must(),
            m.anri.deal("約束を守る", m.sagi_proposal).must(),
            m.anri.have(m.grandticket, m.sagi_proposal).can(),
            m.anri.look(m.rondo),
            m.rondo.be("恐ろしく速い"),
            m.anri.deal("使う", m.angelwing),
            m.anri.go("追いつく", m.rondo),
            m.rondo.look(m.anri),
            m.rondo.ask(m.anri, "そんなのでよくレーサーやってるね"),
            m.anri.reply(m.rondo, m.anri_reason),
            m.rondo.talk(m.anri_reason, "嫌いじゃない"),
            m.anri.think(m.sagi_proposal, "悩む"),
            m.anri.do(m.rondo, "邪魔"),
            m.anri.talk(m.rondo, "失望").ps(),
            )


# main
def story05(m: Master):
    return m.story("Race 5",
            ep_intro(m),
            ep_promise(m),
            ep_rondo(m),
            ep_obstacle(m),
            )

def main(): # pragma: no cover
    from main import master
    return build_to_story(story05(master()))


if __name__ == '__main__':
    import sys
    sys.exit(main())

