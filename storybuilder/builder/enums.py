# -*- coding: utf-8 -*-
"""Define enum types for storybuilder.
"""
from enum import Enum, auto


class ActType(Enum):
    """Act type enum.
    """
    BE = auto() # state type
    BEHAV = auto() # behavior type
    DEAL = auto() # deal type
    DO = auto() # general act type
    EXPLAIN = auto() # information type
    FEEL = auto() # feel type
    GROUP = auto() # for groups
    LOOK = auto() # look type
    MOVE = auto() # move type
    TAG = auto() # for tags
    TALK = auto() # talk type
    TEST = auto() # test type
    THINK = auto() # thinking type

    def __str__(self) -> str:
        return {
                self.BE.value: "BE",
                self.BEHAV.value: "BEHAV",
                self.DEAL.value: "DEAL",
                self.DO.value: "DO",
                self.EXPLAIN.value: "EXPLAIN",
                self.FEEL.value: "FEEL",
                self.GROUP.value: "GROUP",
                self.LOOK.value: "LOOK",
                self.MOVE.value: "MOVE",
                self.TAG.value: "TAG",
                self.TALK.value: "TALK",
                self.TEST.value: "TEST",
                self.THINK.value: "THINK",
                }[self.value]


class AuxVerb(Enum):
    """Auxiliary verb type enum.
    """
    CAN = auto()
    MAY = auto()
    MUST = auto()
    NONE = auto()
    SHOULD = auto()
    WANT = auto()
    WILL = auto()

    def __str__(self) -> str:
        return {
                self.CAN.value: "CAN",
                self.MAY.value: "MAY",
                self.MUST.value: "MUST",
                self.NONE.value: "NONE",
                self.SHOULD.value: "SHOULD",
                self.WANT.value: "WANT",
                self.WILL.value: "WILL",
                }[self.value]


class DescType(Enum):
    """Description type enum.
    """
    DESCRIPTION = auto()
    DIALOGUE = auto()
    NONE = auto()
    TAG = auto()

    def __str__(self) -> str:
        return {
                self.DESCRIPTION.value: "_DESCRIPTION",
                self.DIALOGUE.value: "_DIALOGUE",
                self.NONE.value: "_NONE",
                self.TAG.value: "_TAG",
                }[self.value]


class GroupType(Enum):
    """Action group type enum.
    """
    COMBI = auto()
    SCENE = auto()
    STORY = auto()

    def __str__(self) -> str:
        return {
                self.COMBI.value: "_COMBI",
                self.SCENE.value: "_SCENE",
                self.STORY.value: "_STORY",
                }[self.value]


class LangType(Enum):
    """Language type enum.
    """
    ENG = auto()
    JPN = auto()

    def __str__(self) -> str:
        return {
                self.ENG.value: "_ENG",
                self.JPN.value: "_JPN",
                }[self.value]


class TagType(Enum):
    """Tag type enum.
    """
    BR = auto()
    COMMENT = auto()
    HR = auto()
    NONE = auto()
    SYMBOL = auto()
    TITLE = auto()

    def __str__(self) -> str:
        return {
                self.BR.value: "_BR",
                self.COMMENT.value: "_COMMENT",
                self.HR.value: "_HR",
                self.NONE.value: "_NONE",
                self.TITLE.value: "_TITLE",
                self.SYMBOL.value: "_SYMBOL",
                }[self.value]

