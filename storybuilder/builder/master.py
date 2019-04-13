# -*- coding: utf-8 -*-
"""Story manager class.
"""
from .sbutils import assert_isint, assert_islist, assert_isstr
from .action import _BaseAction, ActionGroup, TagAction
from .enums import GroupType, LangType, TagType
from .subject import Subject, Day, Flag, Item, Person, Stage, Word, Something, Nothing, Info


# classes
class Master(dict):
    """Management a story and story's db.

    Attributes:
    """
    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__

    PREF_DAY = 'd'
    PREF_FLAG = 'f'
    PREF_ITEM = 'i'
    PREF_PERSON = 'p'
    PREF_STAGE = 's'
    PREF_WORD = 'w'

    def __init__(self, name: str, note: str=""):
        """
        Args:
            name (str): a master name.
            note (str, optional): a short description.
        """
        assert_isstr(name)
        assert_isstr(note)

        self.name = name
        self.note = note

    def _args_with_title_if(self, title: str, args: tuple) -> tuple:
        if isinstance(title, str):
            return (self.title(title),) + args
        else:
            return (title,) + args
    
    def _setattr_with_prefix_if(self, pref: str, key: str, data, is_absolute: bool=False):
        if is_absolute or key in self.keys():
            self.__setitem__(pref + '_' + key, data)
        else:
            self.__setitem__(key, data)

    def _append_one(self, key: str, val, prefix: str, subject: Subject, is_absolute_pref: bool=False):
        assert_isstr(key)

        data = val if isinstance(val, subject) else subject(*val)
        self._setattr_with_prefix_if(prefix, key, data, is_absolute_pref)
        return self

    def append_day(self, key: str, val):
        return self._append_one(key, val, Master.PREF_DAY, Day)

    def append_flag(self, key: str, val: str):
        return self._append_one(key, [val], Master.PREF_FLAG, Flag, True)

    def append_item(self, key: str, val):
        return self._append_one(key, val, Master.PREF_ITEM, Item)

    def append_person(self, key: str, val):
        return self._append_one(key, val, Master.PREF_PERSON, Person)

    def append_stage(self, key: str, val):
        return self._append_one(key, val, Master.PREF_STAGE, Stage)

    def append_word(self, key: str, val):
        return self._append_one(key, val, Master.PREF_WORD, Word)

    def br(self, lines: int=1) -> TagAction:
        assert_isint(lines)

        return TagAction(TagType.BR, str(lines))

    def break_symbol(self, char: str) -> TagAction:
        """
        Args:
            char (str): a symbol character.
        Returns:
            TagAction object.
        """
        assert_isstr(char)

        return TagAction(TagType.SYMBOL, char)

    def combine(self, *args: _BaseAction, lang: LangType=LangType.JPN):
        """
        Args:
            *args (:tuple:obj:`_BaseAction`): a combined actions.
            lang (:enum:`LangType`, optional): a language type.
        """
        return ActionGroup(lang=lang, group_type=GroupType.COMBI,  *args)

    def comment(self, comment_: str):
        """
        Args:
            comment_ (str): a comment.
        """
        return TagAction(TagType.COMMENT, comment_)

    def hr(self):
        """Horizontal line.
        """
        return TagAction(TagType.HR, "")

    def info(self, val) -> Info:
        return Info(val)

    def nothing(self) -> Nothing:
        return Nothing()

    def scene(self, title: str, *args: _BaseAction, lang: LangType=LangType.JPN, is_nobr: bool=False):
        """
        Args:
            title (str): a scene title.
            *args (:tuple:obj:`_BaseAction`): a scene actions.
            lang (:enum:`LangType`): a scene language type.
        """
        tmp = ()
        if not is_nobr:
            tmp = self._args_with_title_if(title, args + (self.br(1),))
        else:
            tmp = self._args_with_title_if(title, args)
        return ActionGroup(lang=lang, group_type=GroupType.SCENE, *tmp)

    def set_days(self, li: list):
        assert_islist(li)

        for v in li:
            self.append_day(v[0], v[1:])
        return self

    def set_db(self, persons: list=None, stages: list=None, days: list=None, items: list=None, words: list=None):
        self.set_persons(persons if persons else [])
        self.set_stages(stages if stages else [])
        self.set_days(days if days else [])
        self.set_items(items if items else [])
        self.set_words(words if words else [])
        return self

    def set_flags(self, li: list):
        assert_islist(li)

        for v in li:
            self.append_flag(v[0], v[1])
        return self

    def set_items(self, li: list):
        assert_islist(li)

        for v in li:
            self.append_item(v[0], v[1:])
        return self

    def set_persons(self, li: list):
        assert_islist(li)

        for v in li:
            self.append_person(v[0], v[1:])
        return self

    def set_stages(self, li: list):
        assert_islist(li)

        for v in li:
            self.append_stage(v[0], v[1:])
        return self

    def set_words(self, li: list):
        assert_islist(li)

        for v in li:
            self.append_word(v[0], v[1:])
        return self

    def some(self) -> Something:
        return Something()

    def story(self, title: str, *args: _BaseAction, lang: LangType=LangType.JPN):
        """
        Args:
            title (str): a story title.
            *args (:tuple:obj:`_BaseAction`): a story actions.
            lang (:enum:`LangType`): a story language type.
        """
        return ActionGroup(lang=lang, group_type=GroupType.STORY, *self._args_with_title_if(title, args))

    def title(self, title_: str):
        """
        Args:
            title_ (str): a story title inserted.
        """
        return TagAction(TagType.TITLE, title_)

