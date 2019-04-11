# -*- coding: utf-8 -*-
"""Story manager class.
"""
from .sbutils import assert_isint, assert_isstr
from .action import _BaseAction, ActionGroup, TagAction
from .enums import GroupType, LangType, TagType
from .subject import Subject, Day, Item, Person, Stage, Word


# classes
class Master(dict):
    """Management a story and story's db.

    Attributes:
    """
    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__

    PREF_DAY = 'd'
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
    
    def _setattr_with_prefix_if(self, pref: str, key: str, data):
        if key in self.keys():
            self.__setitem__(pref + '_' + key, data)
        else:
            self.__setitem__(key, data)

    def _append_one(self, key: str, val, prefix: str, subject: Subject):
        assert_isstr(key)

        data = val if isinstance(val, subject) else subject(*val)
        self._setattr_with_prefix_if(prefix, key, data)
        return self

    def append_day(self, key: str, val):
        return self._append_one(key, val, Master.PREF_DAY, Day)

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
        for v in li:
            self.append_day(v[0], v[1:])
        return self

    def set_db(self, persons: list, stages: list, days: list, items: list, words: list):
        self.set_persons(persons)
        self.set_stages(stages)
        self.set_days(days)
        self.set_items(items)
        self.set_words(words)
        return self

    def set_items(self, li: list):
        for v in li:
            self.append_item(v[0], v[1:])
        return self

    def set_persons(self, li: list):
        for v in li:
            self.append_person(v[0], v[1:])
        return self

    def set_stages(self, li: list):
        for v in li:
            self.append_stage(v[0], v[1:])
        return self

    def set_words(self, li: list):
        for v in li:
            self.append_word(v[0], v[1:])
        return self

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

