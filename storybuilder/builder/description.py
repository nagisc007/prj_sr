# -*- coding: utf-8 -*-
"""Define descriptions.
"""
from .sbutils import assert_isclass, assert_istuple
from .enums import DescType


class _BaseDesc(object):
    """Base description class.

    Attributes:
        desc_type (:enum:`DescType`): a description type.
    """
    def __init__(self, desc_type: DescType):
        """
        Args:
            desc_type (:enum:`DescType`): a description type.
        """
        assert_isclass(desc_type, DescType)

        self.desc_type = desc_type
        self.data = None


class Desc(_BaseDesc):
    """Description class.

    Attributes:
        desc_type (:enum:`DescType`): a description type.
        data (:tuple:str): description data.
    """
    def __init__(self, descs, desc_type: DescType=DescType.DESCRIPTION):
        """
        Args:
            descs (:tuple:str): description strings.
            desc_type (:enum:`DescType`, optional): a description type.
        """
        assert_isclass(desc_type, DescType)

        super().__init__(desc_type)
        self.data = self._data_from(descs)

    def _data_from(self, descs) -> tuple:
        if descs:
            if isinstance(descs, str):
                return (descs,)
            else:
                assert_istuple(descs)
                return descs
        return ()


class DescGroup(_BaseDesc):
    """Description group class.

    Attributes:
        desc_type (:enum:`DescType`): a group type.
        descriptions (:tuple:`Desc`): descriptions.
    """
    def __init__(self, *args: _BaseDesc, base_type: DescType=DescType.DESCRIPTION):
        """
        Args:
            *args (_BaseDesc): descriptions in this container.
            base_type (:enum:`DescType`): a basic type for this container.
        """
        assert_isclass(base_type, DescType)

        super().__init__(base_type)
        self.descriptions = args

