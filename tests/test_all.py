# -*- coding: utf-8 -*-
"""Test suite for all tests.
"""
import unittest
import test_main
import test_chap01


def suite():
    '''Packing all tests.

    Returns:
        obj:`TestSuite`: testing suite object contained test cases.
    '''
    suite = unittest.TestSuite()

    suite.addTest(unittest.makeSuite(test_main.StoryTest))

    suite.addTest(unittest.makeSuite(test_chap01.StoryTest))
    
    return suite
