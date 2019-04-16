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
def story09(ma: Master):
    return ma.story("Race 9",
            ma.anri.be(ma.grandrace, ma.grandracestage, ma.grandprixday),
            ma.anri.have(ma.grandrace, "優勝").want(),
            ma.anri.ask(ma.dad, ma.dad_reason),
            ma.ren.talk(ma.anri, ma.dad),
            ma.anri.reply(ma.ren, "知っているの？"),
            ma.ren.talk(ma.anri, "勝ったら教えてあげる"),
            ma.ren.do(ma.angelwing, "壊す"),
            ma.ren.go("先に行ってしまう"),
            ma.anri.go().non(),
            ma.anri.think("優勝したい理由"),
            ma.anri.do(ma.ren, "勝利"),
            ma.anri.know(ma.ren, ma.ren_secret),
            )

def main(): # pragma: no cover
    from main import master
    return build_to_story(story09(master()))


if __name__ == '__main__':
    import sys
    sys.exit(main())

