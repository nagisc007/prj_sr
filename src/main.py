# -*- coding: utf-8 -*-
"""Story program.
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append('storybuilder')

from storybuilder.builder.master import Master
from storybuilder.builder.tools import build_to_story


# configs
CHARAS = (
        ("anri", "風霧アンリ", 18, "female", "レーサー", "me:私"),
        ("dad", "光峰祐一郎", 38, "male", "光舞グループ社長", "me:私"),
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
            )

def main(): # pragma: no cover
    return build_to_story(story())


if __name__ == '__main__':
    import sys
    sys.exit(main())

