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
            m.anri.be(m.race1, "参加", m.race1day, m.race1stage),
            m.anri.have(m.race1, "優勝").want(),
            m.anri.have(m.grandticket, "優勝できれば").can(),
            m.anri.be("出遅れた"),
            m.anri.talk(m.yabu).ps(),
            )

def ep_racers(m: Master):
    return m.story("レーサーたち",
            )

def ep_justbefore(m: Master):
    return m.story("レース直前",
            )

def ep_startcrash(m: Master):
    return m.story("開始直後の洗礼",
            m.yabu.talk("奪うだけがレースじゃない"),
            m.yabu.talk(m.anri, "協力しないか"),
            m.anri.reply(m.yabu, "協力する"),
            m.anri.have(m.yabu, "協力"),
            m.anri.do(m.yabu, "裏切り").ps(),
            )


# main
def story02(ma: Master):
    return ma.story("Race 2",
            ep_intro(ma),
            ep_racers(ma),
            ep_justbefore(ma),
            ep_startcrash(ma),
            )

def main(): # pragma: no cover
    from main import master
    return build_to_story(story02(master()))


if __name__ == '__main__':
    import sys
    sys.exit(main())

