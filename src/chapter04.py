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
def story04(ma: Master):
    return ma.story("Race 4",
            ma.anri.feel("失望", ma.race1, "敗戦"),
            ma.anri.be(ma.factory, ma.race1day.elapsed_day(mon=1)),
            ma.anri.have(ma.ticket2).want(),
            ma.anri.have(ma.grandticket).can(),
            ma.sagisawa.come(ma.factory),
            ma.anri.hear(ma.sagisawa, ma.race2, ma.sagi_proposal),
            ma.anri.reply(ma.sagisawa, ma.sagi_proposal),
            ma.anri.go(ma.race2stage),
            ma.anri.look(ma.rondo),
            ma.anri.go(ma.rondo, ma.race2, "ペアで"),
            )

def main(): # pragma: no cover
    from main import master
    return build_to_story(story(master()))


if __name__ == '__main__':
    import sys
    sys.exit(main())

