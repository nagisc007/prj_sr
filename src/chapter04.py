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
    return m.story("敗れ去って",
            m.anri.be(m.race1, "敗れる", m.race1stage, m.race1day),
            m.anri.be(m.factory, m.race1afterday),
            m.anri.feel("失望", m.race1, "敗戦"),
            m.anri.be(m.factory, m.race1day.elapsed_day(mon=1)),
            m.anri.have(m.ticket2).want(),
            m.anri.have(m.grandticket).can(),
            m.chief.come(m.factory),
            m.chief.talk(m.anri, "レースの感想"),
            m.anri.reply("悔しい"),
            m.chief.talk(m.anri, "助かっただけマシ"),
            m.anri.talk(m.chief, "次は絶対に勝つ"),
            m.anri.look(m.race2, "参加方法").must(),
            m.anri.have(m.dealer, m.race_ticket),
            m.chief.talk(m.anri, "諦めろ", m.race2),
            )


def ep_boringday(m: Master):
    beforeday = m.race1afterday.elapsed_day(day=10)
    return m.story("怠惰な日々",
            m.anri.be(m.factory, beforeday),
            m.anri.have(m.ticket2).must(),
            m.anri.go(m.race2, m.ticket2).can(),
            m.anri.look(m.some(), m.ticket2, "持っている"),
            m.chief.come(m.factory),
            m.sagisawa.come(m.factory),
            m.sagisawa.ask(m.chief, m.anri),
            m.anri.meet(m.sagisawa),
            )


def ep_stranger(m: Master):
    beforeday = m.race1afterday.elapsed_day(day=10)
    out_factory = m.factory.insided("工場裏")
    return m.story("奇妙な男",
            m.anri.go(m.sagisawa, out_factory, beforeday),
            m.sagisawa.talk(m.anri, "レースに関する話"),
            m.anri.hear(m.sagisawa, m.race2, m.sagi_proposal),
            m.anri.look("確かめる", m.sagi_proposal),
            m.sagisawa.talk(m.anri, m.sagi_proposal),
            m.sagi_proposal.explain(m.anri, m.rondo, "二人で出場する"),
            m.race2.explain("ペアレース"),
            )


def ep_retry(m: Master):
    beforeday = m.race1afterday.elapsed_day(day=10)
    out_factory = m.factory.insided("工場裏")
    return m.story("もう一度のチャンス",
            m.anri.talk(m.sagisawa, beforeday, out_factory),
            m.anri.deal("参加", m.race2).want(),
            m.anri.have(m.grandticket).must(),
            m.anri.reply(m.sagisawa, m.sagi_proposal),
            m.anri.deal("承諾", m.sagi_proposal),
            m.anri.go(m.race2stage).can(),
            m.anri.meet(m.rondo),
            m.anri.go(m.rondo, m.race2, "ペアで"),
            )


# main
def story04(m: Master):
    return m.story("Race 4",
            ep_intro(m),
            ep_boringday(m),
            ep_stranger(m),
            ep_retry(m),
            )

def main(): # pragma: no cover
    from main import master
    return build_to_story(story(master()))


if __name__ == '__main__':
    import sys
    sys.exit(main())

