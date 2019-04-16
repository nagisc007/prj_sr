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
def story10(ma: Master):
    return ma.story("Race 10",
            ma.anri.be(ma.grandrace, ma.grandracestage, ma.grandprixday),
            ma.anri.talk(ma.ren, ma.ren_secret),
            ma.ren.reply(ma.anri, ma.ren_secret),
            ma.ren.talk(ma.anri, ma.ren_secret, "自分が父だ"),
            ma.anri.know(ma.dad_reason).want(),
            ma.anri.know(ma.ren_secret),
            ma.anri.hear(ma.ren, ma.ren_secret),
            ma.anri.hear(ma.ren, ma.dad_reason),
            ma.anri.go().non(),
            ma.anri.do(ma.grandrace, "負ける"),
            ma.anri.be(ma.wreckfactory, ma.afterday),
            ma.anri.look(ma.rondo),
            ma.rondo.talk(ma.anri, "まだレースがしたいか？"),
            ma.anri.reply(ma.rondo),
            ma.rondo.deal(ma.anri, "自分を与える"),
            )

def main(): # pragma: no cover
    from main import master
    return build_to_story(story10(master()))


if __name__ == '__main__':
    import sys
    sys.exit(main())

