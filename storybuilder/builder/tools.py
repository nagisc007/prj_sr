# -*- coding: utf-8 -*-
"""Utility tools for story building
"""
from __future__ import print_function
import os
import argparse
import re
from .sbutils import assert_isclass, assert_isbool, assert_isint, assert_isstr
from .action import Action, ActionGroup, TagAction
from .commons import descriptions_of, verb_with_np_of 
from .commons import double_comma_chopped, extraspace_chopped, extraend_chopped
from .commons import infos_of, object_names_of, subject_name_of
from .description import Desc
from .enums import ActType, DescType, GroupType, TagType, LangType
from .subject import Subject, Person


# functions
def build_to_story(story: ActionGroup):
    '''Build a story.

    Args:
        story (:obj:ActionGroup:): a story actions.
    Returns:
        True: if complete to success, otherwise False.
    '''
    assert_isclass(story, ActionGroup)

    FILE_NAME = "story"
    options = options_parsed()
    file_name = options.filename if options.filename else FILE_NAME
    return output_story(story, file_name, options.action, options.build,
            options.charcount, options.priority, options.debug)


def options_parsed():
    '''Get and setting a commandline option.

    Returns:
        :obj:`ArgumentParser`: contain commandline options.
    '''
    parser = argparse.ArgumentParser()

    parser.add_argument('-a', '--action', help="output as action data", action='store_true')
    parser.add_argument('-b', '--build', help="build and output as a file", action='store_true')
    parser.add_argument('-c', '--charcount', help="display characters count", action='store_true')
    parser.add_argument('-d', '--debug', help="with debug mode", action='store_true')
    parser.add_argument('-i', '--info', help="display with informations", action='store_true')
    parser.add_argument('-f', '--filename', help="advanced output file name")
    parser.add_argument('-p', '--priority', help="output an action filtered priorities", type=int, default=5)

    # get result
    args = parser.parse_args()

    return (args)


def output_info(story: ActionGroup):
    assert_isclass(story, ActionGroup)

    totals = _count_descriptions(story)
    print("Characters:\n    Total: {}".format(totals))


def output_story(story: ActionGroup, filename: str, is_action_data: bool=False,
        is_out_as_file: bool=False, is_out_chars: bool=False,
        pri_filter: int=Action.MIN_PRIORITY,
        is_debug: bool=False):
    '''Output a story.

    Args:
        story (:obj:`ActionGroup`): a story action group.
        filename (str): a filename.
        is_action_data (bool, optional): if True, output as an action data.
        is_out_as_file (bool, optional): if True, output to a markdown file.
        pri_filter (int, optional): the number has filtered to output an action.
        is_debug (bool, optional): if True, use a debug mode.
    Returns:
        True: if complete to success, otherwise False.
    '''
    assert_isclass(story, ActionGroup)
    assert_isstr(filename)
    assert_isbool(is_action_data)
    assert_isbool(is_out_as_file)
    assert_isbool(is_out_chars)
    assert_isint(pri_filter)
    assert_isbool(is_debug)

    if is_out_chars:
        output_info(story)

    if is_out_as_file:
        return _output_story_to_file(
                _story_data_converted(story, is_action_data, pri_filter, is_debug),
                filename, is_action_data, is_debug)
    else:
        return _output_story_to_console(
                _story_data_converted(story, is_action_data, pri_filter, is_debug),
                is_debug)


# private functions
def _action_of_by_tag(act: TagAction, group_type: GroupType, level: int) -> str:
    assert_isclass(act, TagAction)
    assert_isclass(group_type, GroupType)
    assert_isint(level)

    if act.tag is TagType.COMMENT:
        return _comment_of(act)
    elif act.tag is TagType.TITLE and group_type is GroupType.STORY:
        return _story_title_of(act, level)
    elif act.tag is TagType.TITLE and group_type is GroupType.SCENE:
        return _scene_title_of(act)
    elif act.tag is TagType.HR:
        return _hr_of()
    elif act.tag is TagType.SYMBOL:
        return _break_symbol_of(act)
    elif act.tag is TagType.BR:
        return "\n"
    else:
        return ""


def _action_of_by_type(act: Action, lang: LangType, group_type: GroupType, level: int,
        pri_filter: int, is_debug: bool) -> str:
    assert_isclass(act, Action)
    assert_isclass(lang, LangType)
    assert_isclass(group_type, GroupType)
    assert_isint(level)
    assert_isint(pri_filter)
    assert_isbool(is_debug)

    if pri_filter > act.priority:
        return ""
    if act.act_type is ActType.GROUP:
        return ""
    elif act.act_type is ActType.TAG:
        return _action_of_by_tag(act, group_type, level)
    elif act.act_type is ActType.TEST:
        if is_debug:
            if lang is LangType.JPN:
                return _action_info_as_jpn(act, group_type, True)
            else:
                return _action_info_as_eng(act, group_type, True)
        else:
            return ""
    else:
        if lang is LangType.JPN:
            return _action_info_as_jpn(act, group_type, False)
        else:
            return _action_info_as_eng(act, group_type, False)


def _action_info_as_eng(act: Action, group_type: GroupType, is_test: bool) -> str:
    assert_isclass(act, Action)
    assert_isclass(group_type, GroupType)
    assert_isbool(is_test)

    return "{test}{lihead}{subject:8}:{verb}{obj:8}/{info}{flag}".format(
            test=_test_head_if(is_test),
            lihead=_list_head_inserted(group_type),
            subject=subject_name_of(act),
            verb=verb_with_np_of(act),
            obj="({})".format(object_names_of(act)),
            info=infos_of(act),
            flag=_flag_info_if(act),
            )


def _action_info_as_jpn(act: Action, group_type: GroupType, is_test: bool) -> str:
    assert_isclass(act, Action)
    assert_isclass(group_type, GroupType)
    assert_isbool(is_test)

    return "{test}{lihead}{subject:\u3000<6s}:{verb}{obj:\u3000<6s}/{info}{flag}".format(
            test=_test_head_if(is_test),
            lihead=_list_head_inserted(group_type),
            subject=subject_name_of(act),
            verb=verb_with_np_of(act),
            obj="({})".format(object_names_of(act)),
            info=infos_of(act),
            flag=_flag_info_if(act),
            )


def _break_symbol_of(act: TagAction) -> str:
    assert_isclass(act, TagAction)

    return "\n\n{}\n\n".format(act.tag_info)


def _comment_of(act: TagAction) -> str:
    assert_isclass(act, TagAction)

    return "<!--{}-->".format(act.tag_info)


def _count_desc_at_action(act: Action) -> int:
    assert_isclass(act, Action)

    return sum([len(_desc_excepted_symbols(v)) for v in act.descs.data if not act.act_type in (ActType.TAG, ActType.TEST)])


def _count_desc_in_group(group: ActionGroup) -> int:
    assert_isclass(group, ActionGroup)

    tmp = []
    for a in group.actions:
        if isinstance(a, ActionGroup):
            tmp.append(_count_desc_in_group(a))
        elif isinstance(a, TagAction):
            continue
        else:
            tmp.append(_count_desc_at_action(a))
    return sum(tmp)


def _count_descriptions(story: ActionGroup) -> int:
    assert_isclass(story, ActionGroup)

    return _count_desc_in_group(story)


def _desc_head_of(desc: Desc, lang: LangType) -> str:
    if lang is LangType.JPN:
        return "　" if desc.desc_type is DescType.DESCRIPTION else ""
    else:
        return " " if desc.desc_type is DescType.DESCRIPTION else ""


def _desc_str_replaced_tag(descstr: str, subject: Subject) -> str:
    assert_isstr(descstr)
    assert_isclass(subject, Subject)

    if isinstance(subject, Person):
        tmp = descstr
        for k, v in subject.calling.items():
            tmp = re.sub(r'\${}'.format(k), v, tmp)
        return re.sub(r'\$S', subject.calling['me'], tmp)
    else:
        return descstr


def _description_of_by_tag(act: TagAction, lang: LangType, group_type: GroupType, level: int, is_debug: bool) -> str:
    assert_isclass(act, TagAction)
    assert_isclass(lang, LangType)
    assert_isclass(group_type, GroupType)
    assert_isint(level)
    assert_isbool(is_debug)

    if act.tag is TagType.COMMENT:
        return _comment_of(act) if is_debug else ""
    elif act.tag is TagType.TITLE and group_type is GroupType.STORY:
        return _story_title_of(act, level)
    elif act.tag is TagType.TITLE and group_type is GroupType.SCENE and is_debug:
        return _scene_title_of(act)
    elif act.tag is TagType.HR:
        return _hr_of()
    elif act.tag is TagType.SYMBOL:
        return _break_symbol_of(act)
    elif act.tag is TagType.BR:
        return "\n"
    else:
        return ""


def _description_of_by_type(act: Action, lang: LangType, group_type: GroupType, level: int,
        pri_filter: int, is_debug: bool) -> str:
    assert_isclass(act, Action)
    assert_isclass(lang, LangType)
    assert_isclass(group_type, GroupType)
    assert_isint(level)
    assert_isint(pri_filter)
    assert_isbool(is_debug)

    if act.priority < pri_filter:
        return ""
    elif act.act_type is ActType.TAG:
        return _description_of_by_tag(act, lang, group_type, level, is_debug)
    elif act.act_type is ActType.TEST and is_debug:
        return "> {}".format(descriptions_of(act, lang))
    elif not act.descs.data:
        return ""
    elif act.descs.desc_type in (DescType.DESCRIPTION, DescType.DIALOGUE):
        return _desc_head_of(act.descs, lang) + _desc_str_replaced_tag(descriptions_of(act, lang), act.subject)
    else:
        return ""


def _desc_excepted_symbols(target: str) -> str:
    assert_isstr(target)

    return re.sub(r'　|\s|\n|\r', '', target)


def _extra_chopped(target: str, lang: LangType) -> str:
    assert_isstr(target)
    assert_isclass(lang, LangType)

    return double_comma_chopped(
            extraend_chopped(
                extraspace_chopped(target, lang),
                lang),
            lang)


def _flag_info_if(act: Action) -> str:
    assert_isclass(act, Action)

    return _flag_info_of(act, True) + _flag_info_of(act, False)


def _flag_info_of(act: Action, is_flag: bool) -> str:
    _flags = act.flags if is_flag else act.deflags
    tmp = ""
    for flg in _flags:
        tmp += "[{de}{flag}]({flag})".format(flag=flg, de="" if is_flag else "D:")
    return tmp


def _hr_of(num: int=9) -> str:
    assert_isint(num)

    return "--------" * num


def _list_head_inserted(group_type: GroupType) -> str:
    assert_isclass(group_type, GroupType)

    if group_type is GroupType.COMBI:
        return "    " * 2 + "- "
    elif group_type is GroupType.SCENE:
        return "    " * 1 + "- "
    else:
        return "- "


def _output_story_to_console(story: list, is_debug: bool) -> bool:
    assert_isclass(story, list)
    assert_isbool(is_debug)

    idx = 0
    for s in story:
        print(_output_with_linenumber(s, idx, is_debug))
        idx += 1
    return True


def _output_story_to_file(story: list, filename: str, is_action_data: bool, is_debug: bool) -> bool:
    assert_isclass(story, list)
    assert_isstr(filename)
    assert_isbool(is_action_data)
    assert_isbool(is_debug)

    EXT_MARKDOWN = 'md'
    BUILD_DIR = 'build'
    if not os.path.isdir(BUILD_DIR):
        os.makedirs(BUILD_DIR)
    fullpath = os.path.join(BUILD_DIR, "{}.{}".format("{}_a".format(filename) if is_action_data else filename, EXT_MARKDOWN))
    with open(fullpath, 'w') as f:
        idx = 0
        for s in story:
            f.write("{}\n".format(_output_with_linenumber(s, idx, is_debug)))
            idx += 1

    return True


def _output_with_linenumber(val: str, num: int, is_debug: bool) -> str:
    assert_isstr(val)
    assert_isint(num)
    assert_isbool(is_debug)

    return "{}: {}".format(num, val) if is_debug else val


def _scene_title_of(act: TagAction) -> str:
    assert_isclass(act, TagAction)

    return "**{}**".format(act.tag_info)


def _story_converted_as_action(story: ActionGroup, pri_filter: int, is_debug: bool) -> list:
    '''
    Args:
        story (:obj:`ActionGroup`): a story action group.
        pri_filter (int): a number filtered an action.
        is_debug (bool): if True, with a debug mode.
    '''
    assert_isclass(story, ActionGroup)
    assert_isint(pri_filter)
    assert_isbool(is_debug)

    return _story_converted_as_action_in_group(story, story.group_type, 1, pri_filter, is_debug)


def _story_converted_as_action_in_group(group: ActionGroup, group_type: GroupType,
        level: int, pri_filter: int, is_debug: bool) -> list:
    assert_isclass(group, ActionGroup)
    assert_isclass(group_type, GroupType)
    assert_isint(level)
    assert_isint(pri_filter)
    assert_isbool(is_debug)

    tmp = []
    for a in group.actions:
        if isinstance(a, ActionGroup):
            tmp.extend(_story_converted_as_action_in_group(a, a.group_type, level + 1, pri_filter, is_debug))
        elif isinstance(a, TagAction):
            tmp.append(_action_of_by_tag(a, group.group_type, level))
        else:
            tmp.append(_action_of_by_type(a, group.lang, group.group_type, level, pri_filter, is_debug))
    return tmp


def _story_converted_as_description(story: ActionGroup, pri_filter: int, is_debug: bool):
    assert_isclass(story, ActionGroup)
    assert_isint(pri_filter)
    assert_isbool(is_debug)

    return _story_converted_as_description_in_group(story, story.group_type, 1, pri_filter, is_debug)


def _story_converted_as_description_in_group(group: ActionGroup, group_type: GroupType, level: int,
        pri_filter: int, is_debug: bool):
    assert_isclass(group, ActionGroup)
    assert_isclass(group_type, GroupType)
    assert_isint(level)
    assert_isint(pri_filter)
    assert_isbool(is_debug)

    tmp = []
    for a in group.actions:
        if isinstance(a, ActionGroup):
            tmp.extend(_story_converted_as_description_in_group(a, a.group_type, level + 1, pri_filter, is_debug))
        elif isinstance(a, TagAction):
            val = _description_of_by_tag(a, group.lang, group.group_type, level, is_debug)
            if val:
                tmp.append(_extra_chopped(val, group.lang))
        else:
            val = _description_of_by_type(a, group.lang, group.group_type, level, pri_filter, is_debug)
            if val:
                tmp.append(_extra_chopped(val, group.lang))
    if group_type is GroupType.COMBI:
        return [_extra_chopped("".join(tmp), group.lang),]
    else:
        return tmp


def _story_data_converted(story: ActionGroup, is_action_data: bool, pri_filter: int, is_debug: bool) -> list:
    '''Story data converter.
    
    Args:
        story (:obj:`ActionGroup`): a story action group.
        is_action_data (bool): if True, output as an action data.
        pri_filter (int): the number filtered an action.
        is_debug (bool): if True, use a debug mode.
    Returns:
        :list:str: strings list as a story.
    '''
    assert_isclass(story, ActionGroup)
    assert_isbool(is_action_data)
    assert_isint(pri_filter)
    assert_isbool(is_debug)

    return  _story_converted_as_action(story, pri_filter, is_debug) if is_action_data else _story_converted_as_description(story, pri_filter, is_debug)


def _story_title_of(act: TagAction, level: int) -> str:
    assert_isclass(act, TagAction)
    assert_isint(level)

    return "{}{} {}\n".format("\n" if level > 1 else "", "#" * level, act.tag_info)


def _test_head_if(is_test: bool) -> str:
    return "> " if is_test else ""
