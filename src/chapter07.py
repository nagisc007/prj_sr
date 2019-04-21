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
            m.anri.go(m.wreckfactory, m.race2day.elapsed_day(day=10)),
            m.anri.think(m.dad_reason).want(),
            m.anri.have(m.grandticket).want(),
            )


def ep_grandprix(m: Master):
    return m.story("遠いグランプリ",
            )


def ep_re_sagisawa(m: Master):
    return m.story("再びの鷺沢",
            m.sagisawa.talk(m.anri),
            m.sagisawa.ask(m.anri, m.sagi_proposal2),
            m.anri.reply(m.sagisawa, "断る"),
            m.sagisawa.talk(m.anri, "受ければ助かる", "欲しいものも手に入る"),
            m.anri.think(m.sagi_proposal2),
            m.anri.reply(m.sagisawa, "受ける"),
            m.anri.have(m.sagisawa, m.sagi_proposal2),
            )


def ep_consolation(m: Master):
    return m.story("敗者復活戦",
            m.anri.have(m.ticket_cons),
            m.anri.go(m.factory, m.race2day.elapsed_day(day=12)),
            m.anri.talk(m.chief, m.race_cons),
            m.anri.go(m.race_cons, "参加"),
            m.anri.go(m.race_consstage, m.race_consday),
            )


# main
def story07(m: Master):
    return m.story("Race 7",
            ep_intro(m),
            ep_grandprix(m),
            ep_re_sagisawa(m),
            ep_consolation(m),
            )

def main(): # pragma: no cover
    from main import master
    return build_to_story(story07(master()))


if __name__ == '__main__':
    import sys
    sys.exit(main())

