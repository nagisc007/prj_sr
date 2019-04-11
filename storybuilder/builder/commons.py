# -*- coding: utf-8 -*-
"""Common functions for storybuilder.
"""
import re
from .sbutils import assert_isclass, assert_isstr
from .action import Action
from .basesubject import _BaseSubject
from .description import Desc, DescGroup
from .enums import AuxVerb, DescType, LangType
from .subject import Info, Nothing, Something


# public functions
def descriptions_of(act: Action, lang: LangType) -> str:

    if isinstance(act.descs, DescGroup):
        return _desc_of_in_group(act.descs, lang)
    else:
        return _desc_of(act.descs, lang)


def double_comma_chopped(target: str, lang: LangType) -> str:
    assert_isstr(target)
    assert_isclass(lang, LangType)

    if lang is LangType.JPN:
        return re.sub(r'([、。]){2}', r'\1', target)
    else:
        return re.sub(r'([,\.]){2}', r'\1', target)


def extraend_chopped(target: str, lang: LangType) -> str:
    assert_isstr(target)
    assert_isclass(lang, LangType)

    if lang is LangType.JPN:
        return re.sub(r'([！？])。$', r'\1', target)
    else:
        return re.sub(r'([!?])\. $', r'\1', target)


def extraspace_chopped(target: str, lang: LangType) -> str:
    assert_isstr(target)
    assert_isclass(lang, LangType)

    if lang is LangType.JPN:
        return re.sub(r'([。」])[　、](.)', r'\1\2', target)
    else:
        return re.sub(r' +', r' ', target)


def infos_of(act: Action) -> str:
    '''Informations string from the action.

    Args:
        act (:obj:`Action`): an action.
    Returns:
        infromation string that the action has all Info.
    '''
    assert_isclass(act, Action)

    return "/".join(v.note for v in act.objects if isinstance(v, Info))


def infos_from(act: Action) -> set:
    assert_isclass(act, Action)

    return set(v.note for v in act.objects if isinstance(v, Info))


def object_names_of(act: Action) -> str:
    assert_isclass(act, Action)

    tmp = []
    for obj in act.objects:
        if isinstance(obj, Info) or isinstance(obj, Nothing):
            continue
        elif isinstance(obj, _BaseSubject):
            tmp.append(something_name_if(obj))
    return "/".join(tmp)


def object_names_of_without_something(act: Action) -> str:
    assert_isclass(act, Action)

    tmp = []
    for obj in act.objects:
        if isinstance(obj, Info) or isinstance(obj, Nothing) or isinstance(obj, Something):
            continue
        elif isinstance(obj, _BaseSubject):
            tmp.append(obj.name)
    return "/".join(tmp)


def something_name_if(obj: _BaseSubject) -> str:
    assert_isclass(obj, _BaseSubject)

    return "何か" if isinstance(obj, Something) else obj.name


def subject_name_of(act: Action) -> str:
    assert_isclass(act, Action)

    return something_name_if(act.subject) if act.subject else ""


def verb_with_np_of(act: Action) -> str:
    assert_isclass(act, Action)

    tmp_head = ""
    tmp_tail = ""
    if act.is_negative:
        tmp_head += "~~"
        tmp_tail += "~~"
    if act.is_passive:
        tmp_head += "_"
        tmp_tail += "_"
    return "{head}{verb}{tail}".format(
            head=tmp_head,
            verb=_verbs_of(act),
            tail=tmp_tail)


# private functions
def _comma_of(lang: LangType) -> str:
    assert_isclass(lang, LangType)

    return "、" if lang == LangType.JPN else ", "


def _desc_of(desc: Desc, lang: LangType) -> str:
    tmp = _space_replaced_if_with_symbol(_comma_of(lang).join(desc.data), lang)
    if desc.desc_type is DescType.DESCRIPTION:
        return _endpoint_replaced_if_invalid(tmp + _period_of(lang), lang)
    elif desc.desc_type is DescType.DIALOGUE:
        return _endpoint_replaced_if_invalid(_dialogue_converted(tmp, lang), lang)


def _desc_of_in_group(group: DescGroup, lang: LangType) -> str:
    assert_isclass(group, DescGroup)
    assert_isclass(lang, LangType)

    tmp = []
    for a in group.descriptions:
        if isinstance(a, DescGroup):
            val = _desc_of_in_group(a, lang)
            if val:
                tmp.extend(val)
        else:
            val = _desc_of(a, lang)
            if val:
                tmp.extend(val)
    return "".join(tmp)


def _dialogue_converted(target: str, lang: LangType) -> str:
    assert_isstr(target)
    assert_isclass(lang, LangType)

    return f'「{target}」' if lang is LangType.JPN else f' "{target}" '


def _endpoint_replaced_if_invalid(target: str, lang: LangType) -> str:
    assert_isstr(target)
    assert_isclass(lang, LangType)

    if lang is LangType.JPN:
        tmp = re.sub(r'[、]。', r'。', target)
        return re.sub(r'[、。]」', r'」', tmp)
    else:
        tmp = re.sub(r'[,]\.', r'.', target)
        return re.sub(r'[,\.]"', r'"', tmp)


def _period_of(lang: LangType) -> str:
    return "。" if lang is LangType.JPN else ". "


def _space_replaced_if_with_symbol(target: str, lang: LangType) -> str:
    assert_isstr(target)
    assert_isclass(lang, LangType)

    if lang is LangType.JPN:
        return re.sub(r'([！？])、', r'\1　', target)
    else:
        return re.sub(r'([!?])\,',  r'\1 ', target)



def _verbs_of(act: Action) -> str:
    assert_isclass(act, Action)

    return "{aux}{verb}".format(
            verb= act.verb,
            aux=str(act.auxverb).lower() if not act.auxverb is AuxVerb.NONE else "",
            )


