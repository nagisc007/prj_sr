# -*- coding: utf-8 -*-
"""Test suite for all tests.
"""
import unittest
import test_main
import test_chap01
import test_chap02
import test_chap03
import test_chap04
import test_chap05


def suite():
    '''Packing all tests.

    Returns:
        obj:`TestSuite`: testing suite object contained test cases.
    '''
    suite = unittest.TestSuite()

    suite.addTest(unittest.makeSuite(test_main.StoryTest))

    suite.addTest(unittest.makeSuite(test_chap01.StoryTest))
    suite.addTest(unittest.makeSuite(test_chap02.StoryTest))
    suite.addTest(unittest.makeSuite(test_chap03.StoryTest))
    suite.addTest(unittest.makeSuite(test_chap04.StoryTest))
    suite.addTest(unittest.makeSuite(test_chap05.StoryTest))
    
    return suite
