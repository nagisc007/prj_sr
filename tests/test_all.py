# -*- coding: utf-8 -*-
"""Test suite for all tests.
"""
import unittest
import test_main


def suite():
    '''Packing all tests.

    Returns:
        obj:`TestSuite`: testing suite object contained test cases.
    '''
    suite = unittest.TestSuite()

    suite.addTest(unittest.makeSuite(test_main.StoryTest))
    
    return suite
