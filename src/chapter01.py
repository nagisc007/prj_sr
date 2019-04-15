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

# main
def story01(ma: Master):
    return ma.story("title",
            ma.anri.do(ma.sr, "参加").want(),
            ma.anri.look(ma.dad, ma.sr, "参加すると").can(),
            ma.anri.do("働く", ma.factory, ma.day1),
            ma.anri.know(ma.ticket1, "当選通知"),
            ma.anri.go(ma.ticketcenter),
            ma.anri.have(ma.ticket1),
            ma.anri.go(ma.factory),
            ma.anri.do("襲う").ps(),
            ma.anri.do("奪う").ps(),
            ma.anri.go("取り返す", ma.ticket1),
            ma.anri.go(ma.race1, "参加", ma.ticket1),
            )

def main(): # pragma: no cover
    return build_to_story(story01(master()))


if __name__ == '__main__':
    import sys
    sys.exit(main())

