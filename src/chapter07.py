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
def story07(ma: Master):
    return ma.story("Race 7",
            ma.anri.go(ma.wreckfactory, ma.race2day.elapsed_day(day=10)),
            ma.anri.think(ma.dad_reason).want(),
            ma.anri.have(ma.grandticket).want(),
            ma.sagisawa.talk(ma.anri),
            ma.sagisawa.ask(ma.anri, ma.sagi_proposal2),
            ma.anri.reply(ma.sagisawa, "断る"),
            ma.sagisawa.talk(ma.anri, "受ければ助かる", "欲しいものも手に入る"),
            ma.anri.think(ma.sagi_proposal2),
            ma.anri.reply(ma.sagisawa, "受ける"),
            ma.anri.have(ma.sagisawa, ma.sagi_proposal2),
            ma.anri.have(ma.ticket_cons),
            ma.anri.go(ma.factory, ma.race2day.elapsed_day(day=12)),
            ma.anri.talk(ma.chief, ma.race_cons),
            ma.anri.go(ma.race_cons, "参加"),
            ma.anri.go(ma.race_consstage, ma.race_consday),
            )

def main(): # pragma: no cover
    from main import master
    return build_to_story(story07(master()))


if __name__ == '__main__':
    import sys
    sys.exit(main())

