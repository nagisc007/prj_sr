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
def ep_intro(m: Master):
    return m.story("奪われる世界",
            m.comment("三人称。基本はアンリ視点"),
            m.anri.be(m.wreckfactory, m.day1),
            m.wreckfactory.explain("山と積まれたパーツ"),
            m.golda.come(m.wreckfactory),
            m.taizo.be(m.golda, "仲間"),
            m.sanpe.be(m.golda, "仲間"),
            m.golda.explain("大柄で継ぎ接ぎのパーツ"),
            m.taizo.explain("ごつい眼鏡", "機械に詳しい"),
            m.sanpe.explain("大きな腕", "知能は足りてない"),
            m.anri.look(m.wreckfactory, "見張る"),
            m.anri.look(m.partsrobber),
            m.anri.talk(m.golda, "何してる？"),
            m.golda.ask(m.anri, m.robhunter),
            m.anri.reply(m.golda, "ただおっさんが困ってるだけ"),
            m.chief.deal("被害", m.partsrobber),
            m.anri.do("逮捕", m.partsrobber),
            m.golda.talk(m.taizo, m.sanpe, "やっちまえ"),
            m.golda.do("襲う", m.anri),
            m.anri.go("逃げる", m.angelwing),
            m.golda.move("追いつく").non(),
            m.anri.deal("通報", m.golda, m.partsrobber),
            m.wreckfactory.do("警報"),
            m.guardman.come(m.wreckfactory),
            m.guardman.deal(m.golda, "捕まえる"),
            m.anri.go("闇の中に帰っていく"),
            m.pubcar.do("宣伝", m.sr),
            m.sr.explain("ドロイドレース最高峰", "優勝者はドロイドから人間へ"),
            )

def ep_everyday(m: Master):
    day2 = m.day1.elapsed_day(day=3)
    return m.story("アンリの日常",
            m.comment("ドロイドの説明を中心に、世界観も説明"),
            m.anri.deal("ネジ製造", m.factory, day2),
            m.chief.come(m.factory),
            m.chief.talk(m.anri, "朝早いね"),
            m.chief.explain("工場長", "頭が禿げ上がる", "人間"),
            m.anri.reply("自分たちは作業ドロイドだから疲れない"),
            m.droid.explain("かつて人間がしていた肉体労働を行うロボット"),
            m.chief.ask(m.anri, "朝食", "食べる？"),
            m.anri.reply(m.chief, "食事は必要ない"),
            m.droid.explain("エネルギィは補給キューブを食べる"),
            m.chief.ask(m.anri, m.race1),
            m.combine(
                m.anri.reply(m.chief),
                m.anri.deal("申し込み", m.ticket1),
                ),
            m.chief.ask(m.anri, m.anri_reason),
            m.anri.do(m.sr, "参加").want(),
            m.combine(
                m.anri.think(),
                m.anri.look(m.dad, m.sr, "参加すると").can(),
                ),
            m.marca.come(m.factory, "配達"),
            m.anri.have("当選通知", m.ticket1),
            m.anri.know("当選", m.ticket1),
            )

def ep_raceticket(m: Master):
    day3 = m.day1.elapsed_day(day=5)
    return m.story("レースチケット",
            m.anri.go("取りに行く", m.ticketcenter, day3),
            m.anri.have(m.ticket1).must(),
            m.anri.go(m.race1).want(),
            m.ticketcenter.explain("役所の中にある", "専用窓口がある"),
            m.amano.ask(m.anri, m.ticket1notice),
            m.anri.look(m.amano, m.ticket1notice),
            m.anri.have(m.ticket1),
            m.anri.go(m.factory, "帰る"),
            m.anri.go(m.ohtacity, "路地"),
            m.anri.do("襲う", m.golda).ps(),
            m.anri.have("奪う", m.golda).ps(),
            )

def ep_firstrace(m: Master):
    day3 = m.day1.elapsed_day(day=5)
    return m.story("いざ初レース",
            m.anri.go(m.ohtacity, day3),
            m.anri.go(m.race1).must(),
            m.anri.ask(m.dad, m.dad_reason).want(),
            m.dad_reason.explain(m.dad, "自分の母を放置して見殺しにした"),
            m.anri.go(m.golda, "追いつく", m.angelwing),
            m.anri.ask(m.golda, m.ticket1, "どうするつもり？"),
            m.golda.reply(m.anri, "これを使って人間になる"),
            m.anri.ask(m.golda, "レーサーにはなれない"),
            m.golda.reply(m.anri, "お前こそレーサーは無理"),
            m.anri.deal(m.golda, m.streetstage, "野良レース"),
            m.golda.reply(m.anri, "承諾"),
            m.anri.go(m.uof_race),
            m.golda.go(m.uof_race),
            m.anri.deal(m.golda, "勝利"),
            m.anri.have("取り戻す", m.ticket1),
            m.anri.go(m.race1, "参加", m.ticket1),
            m.anri.go(m.race1stage),
            )


# main
def story01(ma: Master):
    return ma.story("title",
            ep_intro(ma),
            ep_everyday(ma),
            ep_raceticket(ma),
            ep_firstrace(ma),
            )

def main(): # pragma: no cover
    from main import master
    return build_to_story(story01(master()))


if __name__ == '__main__':
    import sys
    sys.exit(main())

