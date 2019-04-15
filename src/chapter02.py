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
def story02(ma: Master):
    return ma.story("Race 2",
            ma.anri.be(ma.race1, "参加", ma.race1day, ma.race1stage),
            ma.anri.have(ma.race1, "優勝").want(),
            ma.anri.have(ma.grandticket, "優勝できれば").can(),
            ma.anri.be("出遅れた"),
            ma.anri.talk(ma.yabu).ps(),
            ma.yabu.talk("奪うだけがレースじゃない"),
            ma.yabu.talk(ma.anri, "協力しないか"),
            ma.anri.reply(ma.yabu, "協力する"),
            ma.anri.have(ma.yabu, "協力"),
            ma.anri.do(ma.yabu, "裏切り").ps(),
            )

def main(): # pragma: no cover
    from main import master
    return build_to_story(story02(master()))


if __name__ == '__main__':
    import sys
    sys.exit(main())

