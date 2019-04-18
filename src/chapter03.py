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
            m.anri.be("出遅れた", m.race1stage, m.race1day),
            m.anri.have(m.race1, "優勝").want(),
            m.anri.have(m.grandticket).can(),
            )

def ep_dashdash(m: Master):
    return m.story("追いつけ！",
            )

def ep_recoop(m: Master):
    return m.story("再協力",
            )

def ep_lostwin(m: Master):
    return m.story("逃げる優勝",
            m.taiga.do("皆殺し"),
            m.anri.have(m.yabu, "協力"),
            m.anri.do(m.taiga, "倒す", m.yabu, "協力して"),
            m.angelwing.be("壊れる"),
            m.anri.be("失速"),
            m.yabu.have(m.race1, "優勝"),
            m.anri.have("優勝を逃す"),
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

