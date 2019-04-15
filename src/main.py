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
from chapter02 import story02
from chapter03 import story03
from chapter04 import story04
from chapter05 import story05
from chapter06 import story06
from chapter07 import story07
from chapter08 import story08
from chapter09 import story09
from chapter10 import story10


# configs
CHARAS = (
        ("anri", "風霧アンリ", 18, "female", "レーサー", "me:私"),
        ("dad", "光峰祐一郎", 38, "male", "光舞グループ社長", "me:私"),
        ("mam", "風霧ユリ", 28, "female", "母親", "me:わたし", "亡くなっている"),
        ("chief", "中村矢治男", 68, "male", "工場長", "me:俺", "アンリの勤める工場の管理者"),
        # chapter2
        ("yabu", "野武タクマ", 42, "male", "レーサー", "me:俺", "ベテランレーサー"),
        ("taiga", "台牙虎丸", 22, "male", "レーサー", "me:ワシ", "優勝候補"),
        # chapter4
        ("rondo", "光李ロンド", 20, "female", "レーサー", "me:アタシ", "光舞が開発した最新のレース専用ドロイド"),
        ("sagisawa", "鷺沢幽玄", 49, "male", "転売屋", "me:ワタクシ", "謎の多い転売屋"),
        )
STAGES = (
        ("factory", "　中村ネジ工場", "アンリが働くネジ工場"),
        ("ticketcenter", "チケットセンター"),
        ("race1stage", "最初のレース会場"),
        ("race2stage", "二番目のレース会場"),
        ("race_consstage", "敗者復活戦の会場"),
        ("grandracestage", "グランプリレース会場"),
        )
DAYS = (
        ("day1", "一日目"),
        ("race1day", "最初のレース日"),
        ("race2day", "二番目のレース日"),
        ("consolday", "敗者復活レースの日"),
        ("grandprixday", "グランプリレースの日"),
        )
ITEMS = (
        ("ticket1", "最初のレース参加権", "レースに参加する権利。これがないと参加不可能"),
        ("ticket2", "二番目のレース参加権"),
        ("ticket_cons", "敗者復活レース参加権"),
        ("grandticket", "グランプリ参加権"), 
        ("angelwing", "エンジェルウイング", "アンリの最大の武器にして母の遺品"),
        )
WORDS = (
        ("droid", "ドロイド", "人型の作業ロボット"),
        ("sr", "ストロングレース"),
        ("nr", "ノーマルレーサー", "一般のドロイドレーサー"),
        ("race1", "最初のレース"),
        ("race2", "二番目のレース"),
        ("race_cons", "敗者復活レース"),
        ("grandrace", "グランプリレース"),
        ("sagi_proposal", "鷺沢の提案"),
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
            story02(ma),
            story03(ma),
            story04(ma),
            story05(ma),
            story06(ma),
            story07(ma),
            story08(ma),
            story09(ma),
            story10(ma),
            )

def main(): # pragma: no cover
    ma = master()
    return build_to_story(story(ma))


if __name__ == '__main__':
    import sys
    sys.exit(main())

