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
def ep_intro(ma: Master):
    return ma.story("奪われる世界",
            ma.anri.do(ma.sr, "参加").want(),
            ma.anri.look(ma.dad, ma.sr, "参加すると").can(),
            ma.anri.do("働く", ma.factory, ma.day1),
            ma.anri.know(ma.ticket1, "当選通知"),
            ma.anri.go(ma.ticketcenter),
            ma.anri.have(ma.ticket1),
            ma.anri.go(ma.factory),
            ma.anri.do("襲う").ps(),
            ma.anri.do("奪う").ps(),
            )

def ep_everyday(ma: Master):
    return ma.story("アンリの日常",
            )

def ep_raceticket(ma: Master):
    return ma.story("レースチケット",
            )

def ep_firstrace(ma: Master):
    return ma.story("いざ初レース",
            ma.anri.go("取り返す", ma.ticket1),
            ma.anri.go(ma.race1, "参加", ma.ticket1),
            )


# main
def story01(ma: Master):
    return ma.story("title",
            ep_intro(ma),
            ep_everyday(ma),
            ep_raceticket(ma),
            ep_firstrace(ma),
            )

def main(): # pragma: no cover
    from main import master
    return build_to_story(story01(master()))


if __name__ == '__main__':
    import sys
    sys.exit(main())

