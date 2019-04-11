# -*- coding: utf-8 -*-
"""Define an action class.
"""
from .sbutils import assert_isclass, assert_isstr, assert_isbetween
from .description import Desc
from .enums import ActType, DescType, AuxVerb, GroupType, LangType, TagType
from .baseaction import _BaseAction
from .basesubject import _BaseSubject


class Action(_BaseAction):
    """A general action class.

    Attributes:
        act_type (:enum:`ActType`): an action category type.
        auxverb (:enum:`AuxVerb`): an auxiliary verb.
        deflags (:tuple:str): a story deflag to associate this action.
        descs (:obj:`_BaseDesc`): descriptions data object.
        flags (:tuple:str): a story flag to associate this action.
        is_negative (bool): if True is a negative mode.
        is_passive (bool): if True is a passive mode.
        objects (:tuple:obj:`_BaseSubject`): objects of this action.
        priority (int): a action priotiry.
        subject (:obj:`_BaseSubject`): a subject of this action.
        verb (str): a action verb.
    """
    DEFAULT_PRIORITY = 5
    MAX_PRIORITY = 10
    MIN_PRIORITY = 0

    def __init__(self, act_type: ActType, subject: _BaseSubject, verb: str, objects: tuple):
        """
        Args:
            act_type (:enum:`ActType`): an action type.
            subject (:obj:`_BaseSubject`): a subject.
            verb (str): an action verbs.
            objects (:tuple:obj:`_BaseSubject`): objects.
        """
        assert_isclass(act_type, ActType)
        assert_isclass(subject, _BaseSubject)
        assert_isstr(verb)

        super().__init__(act_type)
        self.auxverb = AuxVerb.NONE
        self.deflags = ()
        self.flags = ()
        self.is_negative = False
        self.is_passive = False
        self.priority = Action.DEFAULT_PRIORITY
        self.descs = Desc("")
        self.objects = objects
        self.subject = subject
        self.verb = verb

    def _flags_str_tuple_from(self, *args) -> tuple:
        return tuple(str(v) if isinstance(v, int) else v for v in args)

    def can(self):
        self.auxverb = AuxVerb.CAN
        return self

    def d(self, *args):
        return self.desc(*args)

    def desc(self, *args, is_dialogue: bool=False):
        self.descs = Desc(args, desc_type=DescType.DIALOGUE) if is_dialogue else Desc(args)
        return self

    def may(self):
        self.auxverb = AuxVerb.MAY
        return self

    def must(self):
        self.auxverb = AuxVerb.MUST
        return self

    def negative(self):
        self.is_negative = True
        return self

    def non(self): return self.negative()

    def omit(self):
        """Set minimum priority.
        """
        self.priority = Action.MIN_PRIORITY
        return self

    def passive(self):
        self.is_passive = True
        return self

    def ps(self): return self.passive()

    def set_deflags(self, *args):
        self.deflags = self._flags_str_tuple_from(*args)
        return self

    def set_flags(self, *args):
        self.flags = self._flags_str_tuple_from(*args)
        return self

    def set_priority(self, pri):
        assert_isbetween(pri, Action.MAX_PRIORITY, Action.MIN_PRIORITY)

        self.priority = pri
        return self

    def should(self):
        self.auxverb = AuxVerb.SHOULD
        return self

    def tell(self, *args):
        self.desc(*args, is_dialogue=True)
        return self

    def want(self):
        self.auxverb = AuxVerb.WANT
        return self

    def will(self):
        self.auxverb = AuxVerb.WILL
        return self


class ActionGroup(_BaseAction):
    """Action grouping class.

    Attributes:
        actions (:tuple:obj:`Action`): action lists.
        group_type (:enum:`GroupType`): a group type.
        lang (:enum:`LangType`): a language type.
    """
    CLS_NAME = "_actiongroup"

    def __init__(self, *args: Action, group_type: GroupType, lang: LangType=LangType.JPN):
        """
        Args:
            *args (:tuple:obj:`Action`): actions
            group_type (:enum:`GroupType`): a group type.
            lang (:enum:`LangType`, optional): a language type.
        """
        assert_isclass(group_type, GroupType)
        assert_isclass(lang, LangType)

        super().__init__(ActType.GROUP)
        self.actions = args
        self.group_type = group_type
        self.lang = lang


class TagAction(_BaseAction):
    """Action class for tag specialized.

    Attributes:
        tag (:enum:`TagType`): a tag type.
        tag_info (str): a tag information.
    """
    def __init__(self, tag: TagType, tag_info: str=""):
        super().__init__(ActType.TAG)
        assert_isclass(tag, TagType)
        assert_isstr(tag_info)
        
        self.tag = tag
        self.tag_info = tag_info

