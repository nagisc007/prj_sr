# -*- coding: utf-8 -*-
"""Story program.
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append('storybuilder')

from storybuilder.builder.master import Master
from storybuilder.builder.tools import build_to_story
from chapter01 import story01


# configs
CHARAS = (
        ("anri", "風霧アンリ", 18, "female", "レーサー", "me:私"),
        ("dad", "光峰祐一郎", 38, "male", "光舞グループ社長", "me:私"),
        ("mam", "風霧ユリ", 28, "female", "母親", "me:わたし", "亡くなっている"),
        )
STAGES = (
        ("factory", "工場", "アンリが働くネジ工場"),
        )
DAYS = (
        ("day1", "一日目"),
        )
ITEMS = (
        )
WORDS = (
        ("droid", "ドロイド", "人型の作業ロボット"),
        ("sr", "ストロングレース"),
        ("nr", "ノーマルレーサー", "一般のドロイドレーサー"),
        )


# chapters

# main
def master():
    ma = Master('SR project')
    ma.set_db(CHARAS, STAGES, DAYS, ITEMS, WORDS)
    return ma

def story(ma: Master):
    return ma.story("SR",
            ma.anri.be(ma.factory, ma.day1),
            ma.anri.look(ma.dad, "会う").want(),
            ma.anri.talk(ma.dad, ma.mam, "殺した"),
            ma.anri.talk(ma.sr, "優勝すれば会える"),
            ma.anri.do(ma.sr, "参加"),
            ma.anri.do("敗北"),
            ma.anri.look("会う", ma.dad),
            story01(ma),
            )

def main(): # pragma: no cover
    ma = master()
    return build_to_story(story(ma))


if __name__ == '__main__':
    import sys
    sys.exit(main())

