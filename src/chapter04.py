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
            m.anri.feel("失望", m.race1, "敗戦"),
            m.anri.be(m.factory, m.race1day.elapsed_day(mon=1)),
            m.anri.have(m.ticket2).want(),
            m.anri.have(m.grandticket).can(),
            )

def ep_boringday(m: Master):
    return m.story("怠惰な日々",
            )

def ep_stranger(m: Master):
    return m.story("奇妙な男",
            )

def ep_retry(m: Master):
    return m.story("もう一度のチャンス",
            m.sagisawa.come(m.factory),
            m.anri.hear(m.sagisawa, m.race2, m.sagi_proposal),
            m.anri.reply(m.sagisawa, m.sagi_proposal),
            m.anri.go(m.race2stage),
            m.anri.look(m.rondo),
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

