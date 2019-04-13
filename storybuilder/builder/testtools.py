# -*- coding: utf-8 -*-
"""Useful tools for test with story builder
"""
import unittest
from enum import Enum, auto
from .sbutils import assert_isbool, assert_isclass, assert_islist, assert_istuple
from .action import Action, ActionGroup, TagAction
from .commons import infos_of, object_names_of, subject_name_of, verb_with_np_of
from .description import Desc, DescGroup
from .subject import Day, Flag, Info, Item, Person, Stage, Something, Subject, Word


class MatchLv(Enum):
    COMPLETE = auto()
    ALMOST = auto()
    NEAR = auto()


# public functions
def followed_all_flags(test_case: unittest.TestCase, story: ActionGroup) -> bool:
    '''Check if all flags and deflags.
    '''
    assert_isclass(story, ActionGroup)

    flags = set(_flags_str_converted(_flags_gathered_in_group(story)))
    deflags = set(_flags_str_converted(_flags_gathered_in_group(story, False)))
    result = flags & deflags
    if len(result) != len(flags):
        test_case.fail("Unsolved flags or deflags: {}".format((flags | deflags) - result))
        return False
    return True


def has_a_day(story: ActionGroup) -> bool:
    '''Check if a day time in the story.
    '''
    assert_isclass(story, ActionGroup)

    return _has_a_subject_in_group(story, Day)


def has_a_item(story: ActionGroup) -> bool:
    '''Check if a item in the story.
    '''
    assert_isclass(story, ActionGroup)

    return _has_a_subject_in_group(story, Item)


def has_a_person(story: ActionGroup) -> bool:
    '''Check if a person in the story.
    '''
    assert_isclass(story, ActionGroup)

    return _has_a_subject_in_group(story, Person)


def has_a_stage(story: ActionGroup) -> bool:
    '''Check if a stage in the story.
    '''
    assert_isclass(story, ActionGroup)

    return _has_a_subject_in_group(story, Stage)


def has_a_word(story: ActionGroup) -> bool:
    '''Check if a word in the story.
    '''
    assert_isclass(story, ActionGroup)

    return _has_a_subject_in_group(story, Word)


def has_basic_infos(test_case: unittest.TestCase, story: ActionGroup,
        hero: Person, rival: Person) -> bool:
    '''Check basic info.

    Basic informations are Who, Whom, When, Where
    '''
    assert_isclass(story, ActionGroup)
    assert_isclass(hero, Person)
    assert_isclass(rival, Person)

    ERR_MSG = "is not exists!"
    is_succeeded = True
    # who
    if not has_the_person(story, hero):
        test_case.fail("Hero {} {}".format(hero.name, ERR_MSG))
        is_succeeded = False
    # whom
    if not has_the_person(story, rival):
        test_case.fail("Rival {} {}".format(rival.name, ERR_MSG))
        is_succeeded = False
    # when
    if not has_a_day(story):
        test_case.fail("Day {}".format(ERR_MSG))
        is_succeeded = False
    # where
    if not has_a_stage(story):
        test_case.fail("Stage {}".format(ERR_MSG))
        is_succeeded = False

    return is_succeeded


def has_outline_infos(test_case: unittest.TestCase, story: ActionGroup,
        what: Action, why: Action, how: Action, result: Action,
        is_fuzzy: bool=False) -> bool:
    '''Check if the story has outline informations.
    '''
    assert_isclass(test_case, unittest.TestCase)
    assert_isclass(story, ActionGroup)
    assert_isclass(what, Action)
    assert_isclass(why, Action)
    assert_isclass(how, Action)
    assert_isclass(result, Action)

    matchlv = MatchLv.NEAR if is_fuzzy else MatchLv.COMPLETE
    is_succeed = True
    if not _has_the_action_in_group(story, what, matchlv): # what
        is_succeed = _fail_message_without_target(test_case, "Purpose", what)
    if not _has_the_action_in_group(story, why, matchlv): # why
        is_succeed = _fail_message_without_target(test_case, "Reason", why)
    if not _has_the_action_in_group(story, how, matchlv): # how
        is_succeed = _fail_message_without_target(test_case, "Process", how)
    if not _has_the_action_in_group(story, result, matchlv): # result
        is_succeed = _fail_message_without_target(test_case, "Result", result)
    return is_succeed


def has_the_action(story: ActionGroup, target: Action, matchlv: MatchLv=MatchLv.COMPLETE) -> bool:
    '''Check if the action in the story.
    '''
    assert_isclass(story, ActionGroup)
    assert_isclass(target, Action)
    assert_isclass(matchlv, MatchLv)

    return _has_the_action_in_group(story, target, matchlv)


def has_the_day(story: ActionGroup, target: Day) -> bool:
    '''Check if the daytime in the story.
    '''
    assert_isclass(story, ActionGroup)
    assert_isclass(target, Day)

    return _has_the_subject_in_group(story, Day, target)


def has_the_item(story: ActionGroup, target: Item) -> bool:
    '''Check if the item in the story.
    '''
    assert_isclass(story, ActionGroup)
    assert_isclass(target, Item)

    return _has_the_subject_in_group(story, Item, target)


def has_the_keyword(story: ActionGroup, target: [str, Subject]) -> bool:
    '''Check if the keyword in the story.
    '''
    assert_isclass(story, ActionGroup)

    return _has_the_keyword_in_group(story, target if isinstance(target, Subject) else Info(target))


def has_the_keyword_in_descriptions(story: ActionGroup, target: [str, Subject]) -> bool:
    '''Check if the keyword in the story descriptions.
    '''
    assert_isclass(story, ActionGroup)

    return _has_the_keyword_in_desc_in_group(story, target if isinstance(target, Subject) else Info(target))


def has_the_person(story: ActionGroup, target: Person) -> bool:
    '''Check if the person in the story.
    '''
    assert_isclass(story, ActionGroup)
    assert_isclass(target, Person)

    return _has_the_subject_in_group(story, Person, target)


def has_the_stage(story: ActionGroup, target: Stage) -> bool:
    '''Check if the stage in the story.
    '''
    assert_isclass(story, ActionGroup)
    assert_isclass(target, Stage)

    return _has_the_subject_in_group(story, Stage, target)


def has_the_word(story: ActionGroup, target: Word) -> bool:
    '''Check if the word in the story.
    '''
    assert_isclass(story, ActionGroup)
    assert_isclass(target, Word)

    return _has_the_subject_in_group(story, Word, target)


def is_all_actions(story: ActionGroup) -> bool:
    '''Check if the story is all of an action and an action group.
    '''
    assert_isclass(story, ActionGroup)

    return _is_actiongroup_all_actions(story)


# private functions
def _contains_the_info(info: Info, target: Info) -> bool:
    assert_isclass(info, Info)
    assert_isclass(target, Info)

    return target.note in info.note


def _count_subjects_in(objs: tuple, subcls: Subject) -> int:
    assert_isclass(objs, tuple)

    return len(tuple(v for v in objs if isinstance(v, subcls)))


def _fail_message_without_target(test_case: unittest.TestCase,
        title: str, act: Action) -> bool:
    assert_isclass(test_case, unittest.TestCase)
    assert_isclass(title, str)
    assert_isclass(act, Action)

    ERR_MSG = "is not exists!"

    test_case.fail("{} = {}({}):{} - {}".format(
        title,
        subject_name_of(act),
        verb_with_np_of(act),
        object_names_of(act),
        infos_of(act),
        ERR_MSG
        ))

    return False


def _flags_str_converted(flags: list) -> list:
    assert_islist(flags)

    return [v.note for v in flags if isinstance(v, Flag)]


def _flags_gathered_at_action(act: Action, is_flag: bool) -> list:
    assert_isclass(act, Action)
    assert_isbool(is_flag)
    
    if is_flag:
        return list(act.flags) + [v for v in act.objects if isinstance(v, Flag)]
    else:
        return list(act.deflags)


def _flags_gathered_in_group(group: ActionGroup, is_flag: bool=True) -> list:
    assert_isclass(group, ActionGroup)
    assert_isbool(is_flag)

    tmp = []
    for a in group.actions:
        if isinstance(a, ActionGroup):
            tmp.extend(_flags_gathered_in_group(a, is_flag))
        elif isinstance(a, TagAction):
            continue
        else:
            tmp.extend(_flags_gathered_at_action(a, is_flag))
    return tmp


def _has_a_subject(act: Action, subcls: Subject) -> bool:
    assert_isclass(act, Action)

    return isinstance(act.subject, subcls) \
            or _has_a_subject_in(act.objects, subcls)


def _has_a_subject_in(objs: tuple, subcls: Subject) -> bool:
    assert_istuple(objs)

    return _count_subjects_in(objs, subcls) > 0


def _has_a_subject_in_group(group: ActionGroup, subcls: Subject) -> bool:
    assert_isclass(group, ActionGroup)

    for a in group.actions:
        if isinstance(a, ActionGroup):
            if _has_a_subject_in_group(a, subcls):
                return True
        elif isinstance(a, TagAction):
            continue
        else:
            if _has_a_subject(a, subcls):
                return True
    else:
        return False


def _has_the_action_in_group(group: ActionGroup, target: Action, matchlv: MatchLv) -> bool:
    assert_isclass(group, ActionGroup)
    assert_isclass(target, Action)
    assert_isclass(matchlv, MatchLv)
    # TODO: devided info and something check?

    for a in group.actions:
        if isinstance(a, ActionGroup):
            if _has_the_action_in_group(a, target, matchlv):
                return True
        elif isinstance(a, TagAction):
            continue
        else:
            if matchlv is MatchLv.COMPLETE:
                if _is_the_action(a, target):
                    return True
            elif matchlv is MatchLv.ALMOST:
                if _near_eq_the_action(a, target, False):
                    return True
            else:
                if _near_eq_the_action(a, target, True):
                    return True
    else:
        return False


def _has_the_keyword_at_action(act: Action, target: Subject) -> bool:
    assert_isclass(act, Action)
    assert_isclass(target, Subject)

    if isinstance(target, Info):
        return _has_the_keyword_at_action_as_info(act, target)
    else:
        return _has_the_keyword_at_action_as_subject(act, target)


def _has_the_keyword_at_action_as_info(act: Action, target: Info) -> bool:
    assert_isclass(act, Action)
    assert_isclass(target, Info)

    if target.note in act.subject.name \
            or target.note in act.subject.note:
        return True
    for o in act.objects:
        if target.note in o.name \
                or target.note in o.note:
            return True
    else:
        return False


def _has_the_keyword_at_action_as_subject(act: Action, target: Subject) -> bool:
    assert_isclass(act, Action)
    assert_isclass(target, Subject)

    if target.name in act.subject.name \
            or target.name in act.subject.note:
        return True
    for o in act.objects:
        if target.name in o.name \
                or target.name in o.note:
            return True
    else:
        return False


def _has_the_keyword_in_group(group: ActionGroup, target: Subject) -> bool:
    assert_isclass(group, ActionGroup)
    assert_isclass(target, Subject)

    for a in group.actions:
        if isinstance(a, ActionGroup):
            if _has_the_keyword_in_group(a, target):
                return True
        elif isinstance(a, TagAction):
            continue
        else:
            if _has_the_keyword_at_action(a, target):
                return True
    else:
        return False


def _has_the_keyword_in_desc(desc: Desc, target: Subject) -> bool:
    assert_isclass(desc, Desc)
    assert_isclass(target, Subject)

    if isinstance(target, Info):
        for d in desc.data:
            if target.note in d:
                return True
        else:
            return False
    else:
        for d in desc.data:
            if target.name in d or target.note in d:
                return True
        else:
            return False



def _has_the_keyword_in_desc_group(group: DescGroup, target: Subject) -> bool:
    assert_isclass(group, DescGroup)
    assert_isclass(target, Subject)

    for d in group.descriptions:
        if isinstance(d, DescGroup):
            if _has_the_keyword_in_desc_group(d, target):
                return True
        else:
            if _has_the_keyword_in_desc(d, target):
                return True
    else:
        return False


def _has_the_keyword_in_desc_at_action(act: Action, target: Subject) -> bool:
    assert_isclass(act, Action)
    assert_isclass(target, Subject)
    
    if isinstance(act.descs, DescGroup):
        if _has_the_keyword_in_desc_group(act.descs, target):
            return True
    else:
        return _has_the_keyword_in_desc(act.descs, target)


def _has_the_keyword_in_desc_in_group(group: ActionGroup, target: Subject) -> bool:
    assert_isclass(group, ActionGroup)
    assert_isclass(target, Subject)

    for a in group.actions:
        if isinstance(a, ActionGroup):
            if _has_the_keyword_in_desc_in_group(a, target):
                return True
        elif isinstance(a, TagAction):
            continue
        else:
            if _has_the_keyword_in_desc_at_action(a, target):
                return True
    else:
        return False


def _has_the_subject(act: Action, subcls: Subject, target: Subject) -> bool:
    assert_isclass(act, Action)
    assert_isclass(target, Subject)

    if not _has_a_subject(act, subcls):
        return False

    if isinstance(act.subject, subcls) and _is_same_subjects(act.subject, target):
        return True

    for obj in act.objects:
        if isinstance(obj, subcls) and _is_same_subjects(obj, target):
            return True
    else:
        return False


def _has_the_subject_in_group(group: ActionGroup, subcls: Subject, target: Subject) -> bool:
    assert_isclass(group, ActionGroup)
    assert_isclass(target, Subject)

    for a in group.actions:
        if isinstance(a, ActionGroup):
            if _has_the_subject_in_group(a, subcls, target):
                return True
        elif isinstance(a, TagAction):
            continue
        else:
            if _has_the_subject(a, subcls, target):
                return True
    else:
        return False


def _is_actiongroup_all_actions(group: ActionGroup) -> bool:
    assert_isclass(group, ActionGroup)

    for a in group.actions:
        if isinstance(a, ActionGroup):
            if not _is_actiongroup_all_actions(a):
                return False
        elif isinstance(a, TagAction):
            continue
        else:
            if not isinstance(a, Action):
                return False
    else:
        return True


def _is_the_action(act: Action, target: Action) -> bool:
    assert_isclass(act, Action)
    assert_isclass(target, Action)

    return act.act_type is target.act_type \
            and _is_the_action_verb(act, target) \
            and _is_same_subjects(act.subject, target.subject) \
            and _is_same_objects(act.objects, target.objects)


def _is_the_action_verb(act: Action, target: Action) -> bool:
    assert_isclass(act, Action)
    assert_isclass(target, Action)

    return act.verb is target.verb \
            and act.auxverb is target.auxverb \
            and act.is_negative == target.is_negative \
            and act.is_passive == target.is_passive


def _is_same_objects(objs: tuple, targets: tuple) -> bool:
    assert_istuple(objs)
    assert_istuple(targets)

    for obj in objs:
        for target in targets:
            if _is_same_subjects(obj, target):
                break
        else:
            return False
    else:
        return True


def _is_same_subjects(subject: Subject, target: Subject) -> bool:
    assert_isclass(subject, Subject)
    assert_isclass(target, Subject)

    return type(subject) is type(target) \
            and subject.name == target.name \
            and subject.note == target.note


def _near_eq_the_action(act: Action, target: Action, is_neareq_info: bool=False) -> bool:
    assert_isclass(act, Action)
    assert_isclass(target, Action)

    return act.act_type is target.act_type \
            and _is_the_action_verb(act, target) \
            and _near_eq_subjects(act.subject, target.subject) \
            and _near_eq_objects(act.objects, target.objects, is_neareq_info)


def _near_eq_objects(objs: tuple, targets: tuple, is_neareq_info: bool=False) -> bool:
    assert_istuple(objs)
    assert_istuple(targets)
    assert_isbool(is_neareq_info)

    if _is_same_objects(objs, targets):
        return True

    nomatches = 0
    for target in targets:
        for obj in objs:
            if is_neareq_info and isinstance(target, Info):
                if isinstance(obj, Info) and _contains_the_info(obj, target):
                    break
            elif _is_same_subjects(obj, target):
                break
        else:
            nomatches += 1
    
    if nomatches == 0:
        return True
    else:
        if _has_a_subject_in(objs, Something) or _has_a_subject_in(targets, Something):
            obj_somes = _count_subjects_in(objs, Something)
            tar_somes = _count_subjects_in(targets, Something)
            delta = abs(obj_somes - tar_somes)
            return nomatches - delta <= 0
        else:
            return False


def _near_eq_subjects(subject: Subject, target: Subject) -> bool:
    assert_isclass(subject, Subject)
    assert_isclass(target, Subject)

    return isinstance(subject, Something) or isinstance(target, Something) \
            or _is_same_subjects(subject, target)

