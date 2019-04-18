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
    return m.story("冒頭",
            m.comment("簡単な一話の振り返りと世界観振り返りを思想の中で"),
            m.anri.be(m.race_bus, m.race1day),
            m.anri.think(m.race1),
            m.anri.be(m.race1, "参加", m.race1day, m.race1stage),
            m.anri.have(m.race1, "優勝").want(),
            m.anri.have(m.grandticket, "優勝できれば").can(),
            m.anri.talk(m.dad, "静かな怒り"),
            m.anri.remember(m.chief, "迷わないように"),
            m.anri.go(m.race1stage, "迷わずに").must(),
            m.anri.go(m.race_bus, "下りる"),
            m.anri.look(m.buscenter),
            m.anri.think("ここどこ？"),
            m.anri.know(m.race1stage).non(),
            m.anri.hear(m.some()),
            m.yabu.explain("おじさんレーサー", "ぼろいスーツ"),
            m.anri.meet(m.yabu),
            m.anri.know(m.yabu, m.race1stage),
            )

def ep_racers(m: Master):
    beforetime = m.race1day.elapsed_day(hour=9)
    return m.story("レーサーたち",
            m.anri.go(m.race1stage, m.yabu, beforetime),
            m.race1stage.explain("市街地コース", "旧東京駅前から始まる"),
            m.race1stage.explain("立体観客席", m.skymonitor),
            m.skymonitor.be("映る", m.taiga, "優勝候補たち"),
            m.yabu.talk(m.anri, "他の選手"),
            m.yabu.talk("受付"),
            m.anri.deal("受付を済ませる").must(),
            m.anri.do(m.race1, "参加"),
            m.anri.go(m.race1front),
            m.anri.look("揉め事"),
            m.anri.be("巻き込まれる"),
            m.anri.deal(m.yabu, "助ける").ps(),
            )

def ep_justbefore(m: Master):
    justbefore = m.race1day.elapsed_day(hour=10)
    outside = m.race1waitroom.insided("控室の外")
    return m.story("レース直前",
            m.anri.be(outside, m.yabu, justbefore),
            m.yabu.talk("家族の話"),
            m.anri.talk(m.yabu, "自分の身の上"),
            m.anri.be(m.race1, "初レース"),
            m.anri.know(m.race1, "心得").want(),
            m.yabu.talk(m.anri, "心得"),
            m.anri.hear(m.yabu, "心得"),
            m.yabu.talk(m.anri, m.f_important_race),
            m.anri.know(m.f_important_race),
            m.yabu.talk("奪うだけがレースじゃない"),
            m.yabu.talk(m.anri, "協力しないか"),
            m.anri.reply(m.yabu, "協力する"),
            m.anri.have(m.yabu, "協力"),
            )

def ep_startcrash(m: Master):
    racetime = m.race1day.elapsed_day(hour=11)
    return m.story("開始直後の洗礼",
            racetime.explain("開始が迫る"),
            m.anri.be(m.race1stage.insided("スタート地点"), racetime),
            m.anri.do("スタート", "成功").must(),
            m.anri.hear(m.yabu, m.f_important_race),
            m.anri.be(m.yabu, "近くでスタート"),
            m.anri.do(m.yabu, "裏切り").ps().de(m.f_important_race),
            )


# main
def story02(ma: Master):
    return ma.story("Race 2",
            ep_intro(ma),
            ep_racers(ma),
            ep_justbefore(ma),
            ep_startcrash(ma),
            )

def main(): # pragma: no cover
    from main import master
    return build_to_story(story02(master()))


if __name__ == '__main__':
    import sys
    sys.exit(main())

