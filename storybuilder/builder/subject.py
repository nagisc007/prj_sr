# -*- coding: utf-8 -*-
"""Module to build a story.
"""
from .sbutils import assert_isstr, assert_isint
from .action import Action 
from .basesubject import _BaseSubject
from .enums import ActType


class Subject(_BaseSubject):
    """Base class for all subjects.

    Attributes:
        name (str): a name.
        note (str): a short description.
    """
    def __init__(self, name: str, note: str=""):
        super().__init__(name, note)

    def be(self, *args, verb: str="be"):
        return Action(ActType.BE, self, verb, self.objects_from(*args))

    def do(self, *args, verb: str="do"):
        return Action(ActType.DO, self, verb, self.objects_from(*args))

    def explain(self, *args, verb: str="explain"):
        return Action(ActType.EXPLAIN, self, verb, self.objects_from(*args))

    def objects_from(self, *args):
        return tuple(_info_or_subject_from(v) for v in args)


class Info(Subject):
    """Information class.
    """
    _NAME = "_information"
    def __init__(self, info: str):
        assert_isstr(info)

        super().__init__(Info._NAME, info)


class Nothing(Subject):
    """Nothing class.
    """
    _NAME = "_nothing"
    def __init__(self):
        super().__init__(Nothing._NAME, "")


class Something(Subject):
    """Something class.
    """
    _NAME = "_something"
    def __init__(self):
        super().__init__(Something._NAME, "")


class Person(Subject):
    """Person class.

    Attributes:
        age (int): an age.
        calling (dict): a calling dictionary.
        job (str): a job.
        name (str): a name.
        note (str): a short description.
        sex (str): a sex.
    """
    DEF_SELFCALL = "私"

    def __init__(self, name: str, age: int, sex: str, job: str, calling: [dict, str]=DEF_SELFCALL, note: str=""):
        """
        Args:
            name (str): a person name
            age (int): a person age
            sex (str): a person sex
            job (str): a person job
            calling ([dict, str]): a calling dictionary. 
            note (str, optional): a short description.
        """
        super().__init__(name, note)
        assert_isint(age)
        assert_isstr(job)
        assert_isstr(sex)

        self.age = age
        self.calling = self._calling_dict_from(calling)
        self.job = job
        self.sex = sex

    # private methods
    def _calling_dict_from(self, target: [str, dict]) -> dict:
        if isinstance(target, dict):
            return target
        elif isinstance(target, str):
            if ":" in target:
                tmp = target.split(":")
                ret = {}
                for k, v in zip(tmp[0::2], tmp[1::2]):
                    ret[k] = v
                if not "me" in ret.keys():
                    ret.update({"me":Person.DEF_SELFCALL})
                return ret
            else:
                return {"me": target}
        else:
            return {"me": target}

    def ask(self, *args, verb: str="ask"):
        return self.talk(*args, verb=verb)

    def behav(self, *args, verb: str="behav"):
        assert_isstr(verb)

        return Action(ActType.BEHAV, self, verb, self.objects_from(*args))

    def come(self, *args, verb: str="come"):
        return self.move(*args, verb=verb)

    def deal(self, *args, verb: str="deal"):
        assert_isstr(verb)

        return Action(ActType.DEAL, self, verb, self.objects_from(*args))

    def feel(self, *args, verb: str="feel"):
        assert_isstr(verb)

        return Action(ActType.FEEL, self, verb, self.objects_from(*args))

    def go(self, *args, verb: str="go"):
        return self.move(*args, verb=verb)

    def have(self, *args, verb: str="have"):
        return self.deal(*args, verb=verb)

    def hear(self, *args, verb: str="hear"):
        return self.talk(*args, verb=verb)

    def know(self, *args, verb: str="know"):
        return self.think(*args, verb=verb)

    def look(self, *args, verb: str="look"):
        assert_isstr(verb)

        return Action(ActType.LOOK, self, verb, self.objects_from(*args))

    def move(self, *args, verb: str="move"):
        assert_isstr(verb)

        return Action(ActType.MOVE, self, verb, self.objects_from(*args))

    def remember(self, *args, verb: str="remember"):
        return self.think(*args, verb=verb)

    def reply(self, *args, verb: str="reply"):
        assert_isstr(verb)

        return self.talk(*args, verb=verb)

    def talk(self, *args, verb: str="talk"):
        assert_isstr(verb)

        return Action(ActType.TALK, self, verb, self.objects_from(*args))

    def think(self, *args, verb: str="think"):
        assert_isstr(verb)

        return Action(ActType.THINK, self, verb, self.objects_from(*args))


class Day(Subject):
    """Day and Time management class.

    Attributes.
        day (int): a day number.
        hour (int): a hour number.
        min (int): a minute number.
        mon (int): a month number.
        name (str): a day name.
        note (str): a short description.
        year (int): a year number.
    """
    def __init__(self, name: str, mon: int=0, day: int=0, year: int=0,
            hour: int=0, min: int=0, note: str=""):
        """
        Args:
            name (str): a day name.
            mon (int): a month number.
            day (int): a day number.
            year (int): a year number.
            hour (int): a hour number.
            min (int): a minute number.
            note (str, optional): a short description.
        """
        super().__init__(name, note)
        assert_isint(day)
        assert_isint(hour)
        assert_isint(min)
        assert_isint(mon)
        assert_isint(year)

        self.day = day
        self.hour = hour
        self.min = min
        self.mon = mon
        self.year = year

    def elapse(self):
        # TODO: elapsed time count
        return Action(ActType.BE, self, "elapse", ())


class Item(Subject):
    """Item class.

    Attributes.
        name (str): a item name.
        note (str, optional): a short description.
    """
    def __init__(self, name: str, note: str=""):
        """
        Args:
            name (str): a item name.
            note (str, optional): a short description.
        """
        super().__init__(name, note)

    def move(self, *args, verb: str="move"):
        return Action(ActType.MOVE, self, verb, self.objects_from(*args))


class Stage(Subject):
    """Stage class.

    Attributes:
        name (str): a stage name.
        note (str): a short description.
    """
    def __init__(self, name: str, note: str=""):
        """
        Args:
            name (str): a stage name.
            note (str, optional): a short description.
        """
        super().__init__(name, note)

    def move(self, *args, verb: str="move"):
        return Action(ActType.MOVE, self, verb, self.objects_from(*args))


class Word(Subject):
    """Word class.

    Attributes.
        name (str): a word title.
        note (str): a short description.
    """
    def __init__(self, name: str, note: str=""):
        """
        Args:
            name (str): a word title.
            note (str, optional): a short description.
        """
        super().__init__(name, note)


# private functions
def _info_or_subject_from(target) -> [Info, Nothing, _BaseSubject]:
    if isinstance(target, _BaseSubject):
        return target
    elif isinstance(target, str):
        return Info(target)
    elif isinstance(target, int):
        return Info("number_" + str(target))
    else:
        return Nothing()
