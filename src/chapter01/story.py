# -*- coding: utf-8 -*-
"""Story program.
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder.master import Master
from storybuilder.builder.tools import build_to_story


# configs
CHARAS = (
        )

STAGES = (
        )

DAYS = (
        )

ITEMS = (
        )

WORDS = (
        )


# episodes


# main
def master():
    ma = Master("project")
    ma.set_db(CHARAS, STAGES, DAYS, ITEMS, WORDS)
    return ma

def story(ma: Master):
    return ma.story("title",
            )

def main(): # pragma: no cover
    return build_to_story(story())


if __name__ == '__main__':
    import sys
    sys.exit(main())

