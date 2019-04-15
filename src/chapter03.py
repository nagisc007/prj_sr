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
def story03(ma: Master):
    return ma.story("Race 3",
            ma.anri.be("出遅れた", ma.race1stage, ma.race1day),
            ma.anri.have(ma.race1, "優勝").want(),
            ma.anri.have(ma.grandticket).can(),
            ma.taiga.do("皆殺し"),
            ma.anri.have(ma.yabu, "協力"),
            ma.anri.do(ma.taiga, "倒す", ma.yabu, "協力して"),
            ma.angelwing.be("壊れる"),
            ma.anri.be("失速"),
            ma.yabu.have(ma.race1, "優勝"),
            ma.anri.have("優勝を逃す"),
            )

def main(): # pragma: no cover
    from main import master
    return build_to_story(story03(master()))


if __name__ == '__main__':
    import sys
    sys.exit(main())

