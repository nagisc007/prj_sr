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

def ep_everyday(ma: Master):
    return ma.story("アンリの日常",
            )

def ep_raceticket(ma: Master):
    return ma.story("レースチケット",
            ma.anri.do(ma.sr, "参加").want(),
            ma.anri.look(ma.dad, ma.sr, "参加すると").can(),
            ma.anri.do("働く", ma.factory, ma.day1),
            ma.anri.know(ma.ticket1, "当選通知"),
            ma.anri.go(ma.ticketcenter),
            ma.anri.have(ma.ticket1),
            ma.anri.go(ma.factory),
            ma.anri.do("襲う").ps(),
            ma.anri.do("奪う").ps(),
            )

def ep_firstrace(ma: Master):
    return ma.story("いざ初レース",
            ma.anri.go("取り返す", ma.ticket1),
            ma.anri.go(ma.race1, "参加", ma.ticket1),
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

