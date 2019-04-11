# -*- coding: utf-8 -*-
"""Define basic action class.
"""
from .sbutils import assert_isclass
from .enums import ActType


class _BaseAction(object):
    """Base action class.

    Attributes:
        act_type (:enum:`ActType`): a type of action.
    """
    def __init__(self, act_type: ActType):
        """
        Args:
            act_type (:enum:`ActType`): a type of action.
        """
        assert_isclass(act_type, ActType)

        self.act_type = act_type

