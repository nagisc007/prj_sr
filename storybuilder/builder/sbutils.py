# -*- coding: utf-8 -*-
"""Test utility for story builder.
"""


_ASSERT_MSG = "{} Must be type {}!"

# public functions
def assert_are_int_str(ins) -> bool:
    assert isinstance(ins, int) or isinstance(ins, str), _ASSERT_MSG.format(_instance_name_if(ins), "int or str")


def assert_isbetween(ins, max_, min_) -> bool:
    assert ins <= max_ and ins >= min_, "Must be between {} to {}".format(max_, min_)

    return True


def assert_isbool(ins) -> bool:
    assert isinstance(ins, bool), _ASSERT_MSG.format(_instance_name_if(ins), "bool")

    return True


def assert_isclass(ins, cls) -> bool:
    assert isinstance(ins, cls), _ASSERT_MSG.format(_instance_name_if(ins), type(cls))

    return True


def assert_isdict(ins) -> bool:
    assert isinstance(ins, dict), _ASSERT_MSG.format(_instance_name_if(ins), "dict")

    return True


def assert_isint(ins) -> bool:
    assert isinstance(ins, int), _ASSERT_MSG.format(_instance_name_if(ins), "int")

    return True


def assert_islist(ins) -> bool:
    assert isinstance(ins, list) or isinstance(ins, tuple), _ASSERT_MSG.format(_instance_name_if(ins), "list or tuple")

    return True


def assert_islist_strict(ins) -> bool:
    assert isinstance(ins, list), _ASSERT_MSG.format(_instance_name_if(ins), "list")

    return True


def assert_isobject(ins) -> bool:
    assert isinstance(ins, object), _ASSERT_MSG.format(_instance_name_if(ins), "object")

    return True


def assert_isstr(ins) -> bool:
    assert isinstance(ins, str), _ASSERT_MSG.format(_instance_name_if(ins), "str")

    return True


def assert_istuple(ins) -> bool:
    assert isinstance(ins, tuple), _ASSERT_MSG.format(_instance_name_if(ins), "tuple")

    return True


def print_test_title(fname: str, title: str) -> bool:
    print("\n**** TEST: {} - {} ****".format(fname, title))
    return True


# private functions
def _instance_name_if(ins) -> str:
    return ins.__class__.name if hasattr(ins, "name") else "instance"
