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
def story05(ma: Master):
    return ma.story("Race 5",
            ma.anri.go(ma.rondo, ma.race2),
            ma.anri.have(ma.grandticket).want(),
            ma.anri.do(ma.sagi_proposal, "約束を守る", ma.grandticket).can(),
            ma.anri.go(ma.race2stage, ma.race2day),
            ma.rondo.talk(ma.anri, "あなたのことは聞いている"),
            ma.rondo.know(ma.anri, ma.dad),
            ma.rondo.talk(ma.anri, ma.rondo_promise),
            ma.anri.think("迷う", ma.rondo_promise, ma.sagi_proposal),
            ma.anri.do(ma.rondo, "優勝を邪魔する"),
            ma.anri.talk(ma.rondo, "失望").ps(),
            )

def main(): # pragma: no cover
    from main import master
    return build_to_story(story05(master()))


if __name__ == '__main__':
    import sys
    sys.exit(main())

