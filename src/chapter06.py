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
def story06(ma: Master):
    return ma.story("Race 6",
            ma.anri.be(ma.race2, ma.race2day, ma.race2stage),
            ma.anri.talk(ma.rondo, "口論"),
            ma.anri.have(ma.sagi_proposal),
            ma.rondo.talk(ma.anri, "あなたの事情は知らない", "自分は優勝したいだけ"),
            ma.rondo.talk(ma.anri, "優勝が使命"),
            ma.rondo.ask(ma.anri, "優勝したくないの？"),
            ma.anri.have(ma.race2, "優勝").want(),
            ma.anri.think(ma.race2, "勝利する").want(),
            ma.anri.reply(ma.rondo, "優勝したい"),
            ma.rondo.talk(ma.anri, "協力"),
            ma.anri.ask(ma.rondo, "自分を信じてくれるのか？"),
            ma.rondo.reply(ma.anri, "あなたの優勝したい気持ちを信じる"),
            ma.anri.have(ma.rondo, "協力"),
            ma.angelwing.be("破損"),
            ma.anri.go("失速"),
            ma.rondo.talk(ma.anri, "助ける"),
            ma.anri.reply(ma.rondo, "優勝したいなら助けるな"),
            ma.rondo.think("混乱"),
            ma.rondo.go("一人で行く"),
            ma.anri.go(ma.race2, ma.retire),
            )

def main(): # pragma: no cover
    from main import master
    return build_to_story(story06(master()))


if __name__ == '__main__':
    import sys
    sys.exit(main())

