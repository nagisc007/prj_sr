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
    racetime = m.race1day.elapsed_day(hour=11, min=10)
    return m.story("冒頭",
            m.comment("レース開始の振り返りと簡単な説明"),
            m.anri.be("出遅れた", m.race1stage, racetime),
            m.anri.be("スタートできていない"),
            m.anri.know("何が起きたか").must(),
            m.anri.remember("スタート"),
            m.anri.think(m.yabu, "嵌められた"),
            m.anri.go("急ぐ"),
            m.anri.look("自分は最後尾"),
            )

def ep_dashdash(m: Master):
    racetime = m.race1day.elapsed_day(hour=11, min=15)
    course = m.race1stage.insided("市街地コース")
    return m.story("追いつけ！",
            m.anri.go(course, racetime),
            course.explain("壊れたビルの残骸"),
            m.anri.deal("遅れを取り戻す").must(),
            m.anri.be("出遅れた"),
            m.anri.do(m.angelwing, "使う"),
            m.angelwing.explain("母の遺品", "全身が壊れそうなほどの速度"),
            m.anri.go(m.yabu, "追いつく"),
            )

def ep_recoop(m: Master):
    racetime = m.race1day.elapsed_day(hour=11, min=30)
    course = m.race1stage.insided("ビルの谷間")
    lastzone = m.race1stage.insided("ゴール前")
    return m.story("ゴール直前の壁",
            m.anri.go(m.race1, "ゴール"),
            m.anri.have(m.race1, "優勝").want(),
            m.anri.be(racetime, course),
            m.anri.ask(m.yabu, m.yabu_reason),
            m.yabu.reply(m.anri, m.yabu_reason),
            m.yabu.talk(m.anri, "どんな手を使っても勝つ", "これがSR"),
            m.anri.ask(m.yabu, "それでもずっと勝ててない"),
            m.yabu.talk(m.anri, m.taiga, "あいつがいる"),
            m.anri.go("先に進む"),
            m.anri.go(lastzone),
            m.taiga.do("皆殺し"),
            m.anri.be(m.taiga, "立ち塞がる"),
            )

def ep_lostwin(m: Master):
    racetime = m.race1day.elapsed_day(hour=11, min=45)
    lastzone = m.race1stage.insided("ゴール前")
    return m.story("逃げる優勝",
            m.anri.be(lastzone, racetime),
            m.anri.go("ゴール", m.taiga).non(),
            m.anri.have(m.race1, "優勝").want(),
            m.anri.have(m.grandticket).must(),
            m.anri.have(m.yabu, "協力"),
            m.anri.do(m.taiga, "倒す", m.yabu, "協力"),
            m.anri.be("壊れる"),
            m.yabu.be("壊れる"),
            m.anri.be("失速"),
            m.yabu.be("失速"),
            m.yabu.have(m.race1, "優勝"),
            m.anri.have(m.race1, "優勝").non(),
            )

# m.n
def story03(m: Master):
    return m.story("Race 3",
            ep_intro(m),
            ep_dashdash(m),
            ep_recoop(m),
            ep_lostwin(m),
            )

def main(): # pragm. no cover
    from main import master
    return build_to_story(story03(master()))


if __name__ == '__main__':
    import sys
    sys.exit(main())

