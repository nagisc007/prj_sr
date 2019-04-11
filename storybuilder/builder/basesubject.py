# -*- coding: utf-8 -*-
"""Define a base subject class.
"""
from .sbutils import assert_isstr


class _BaseSubject(object):
    """Base subject class.

    Attributes:
        name (str): a name of this subject.
        note (str): a short description.
    """
    CLS_NAME = "_basesubject"
    def __init__(self, name: str, note: str=""):
        """
        Args:
            name (str): the name or title.
            note (str, optional): a short description.
        """
        assert_isstr(name)
        assert_isstr(note)

        self.name = name
        self.note = note

