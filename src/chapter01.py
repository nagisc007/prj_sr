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

# main
def story01(ma: Master):
    return ma.story("title",
            ma.anri.be(),
            ma.dad.be(),
            ma.day1.explain(),
            ma.factory.explain(),
            )

def main(): # pragma: no cover
    return build_to_story(story01(master()))


if __name__ == '__main__':
    import sys
    sys.exit(main())
