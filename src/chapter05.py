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
    return m.story("ペアレース",
            m.anri.go(m.rondo, m.race2),
            m.anri.have(m.grandticket).want(),
            m.anri.do(m.sagi_proposal, "約束を守る", m.grandticket).can(),
            m.anri.go(m.race2stage, m.race2day),
            )


def ep_promise(m: Master):
    return m.story("暗黒の約束",
            m.rondo.talk(m.anri, "あなたのことは聞いている"),
            m.rondo.know(m.anri, m.dad),
            m.rondo.talk(m.anri, m.rondo_promise),
            m.anri.think("迷う", m.rondo_promise, m.sagi_proposal),
            )


def ep_rondo(m: Master):
    return m.story("レースの申し子ロンド",
            )


def ep_obstacle(m: Master):
    return m.story("邪魔者",
            m.anri.do(m.rondo, "優勝を邪魔する"),
            m.anri.talk(m.rondo, "失望").ps(),
            )


# main
def story05(m: Master):
    return m.story("Race 5",
            ep_intro(m),
            ep_promise(m),
            ep_rondo(m),
            ep_obstacle(m),
            )

def main(): # pragma: no cover
    from main import master
    return build_to_story(story05(master()))


if __name__ == '__main__':
    import sys
    sys.exit(main())

