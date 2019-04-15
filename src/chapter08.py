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
def story08(ma: Master):
    return ma.story("Race 8",
            ma.anri.have(ma.grandticket),
            ma.anri.be(ma.factory, ma.race_consday.elapsed_day(day=10)),
            ma.factory.be("廃業"),
            ma.anri.talk(ma.chief, "別れ"),
            ma.anri.go(ma.grandracestage, ma.grandprixday),
            ma.anri.be(ma.angelwing, "メンテ不足"),
            ma.anri.have(ma.grandrace, "優勝"),
            ma.anri.look(ma.dad),
            ma.anri.go(ma.grandrace, "開幕"),
            ma.anri.look(ma.ren),
            ma.anri.have("奪う", "他人のパーツ"),
            ma.anri.have(ma.bugparts),
            )

def main(): # pragma: no cover
    from main import master
    return build_to_story(story08(master()))


if __name__ == '__main__':
    import sys
    sys.exit(main())

