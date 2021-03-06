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
import test_chap06
import test_chap06
import test_chap07
import test_chap07
import test_chap08
import test_chap09
import test_chap10


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
    suite.addTest(unittest.makeSuite(test_chap06.StoryTest))
    suite.addTest(unittest.makeSuite(test_chap07.StoryTest))
    suite.addTest(unittest.makeSuite(test_chap08.StoryTest))
    suite.addTest(unittest.makeSuite(test_chap09.StoryTest))
    suite.addTest(unittest.makeSuite(test_chap10.StoryTest))
    
    return suite
