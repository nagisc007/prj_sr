# -*- coding: utf-8 -*-
"""Test suite for all tests
"""
import unittest

import test_action
import test_baseaction
import test_basesubject
import test_commons
import test_description
import test_enums
import test_master
import test_subject
import test_testtools
import test_tools
import test_utils


def suite():
    '''Packing all tests.
    '''
    suite = unittest.TestSuite()

    # action
    suite.addTest(unittest.makeSuite(test_action.ActionTest))
    suite.addTest(unittest.makeSuite(test_action.ActionGroupTest))
    suite.addTest(unittest.makeSuite(test_action.TagActionTest))

    # baseaction
    suite.addTest(unittest.makeSuite(test_baseaction.BaseActionTest))

    # basesubject
    suite.addTest(unittest.makeSuite(test_basesubject.BaseSubjectTest))

    # commons
    suite.addTest(unittest.makeSuite(test_commons.PublicMethodsTest))
    suite.addTest(unittest.makeSuite(test_commons.PrivateMethodsTest))

    # description
    suite.addTest(unittest.makeSuite(test_description.BaseDescTest))
    suite.addTest(unittest.makeSuite(test_description.DescTest))
    suite.addTest(unittest.makeSuite(test_description.DescGroupTest))

    # enums
    suite.addTest(unittest.makeSuite(test_enums.EnumsTest))

    # master
    suite.addTest(unittest.makeSuite(test_master.MasterTest))

    # subject
    suite.addTest(unittest.makeSuite(test_subject.SubjectTest))
    suite.addTest(unittest.makeSuite(test_subject.InfoTest))
    suite.addTest(unittest.makeSuite(test_subject.NothingTest))
    suite.addTest(unittest.makeSuite(test_subject.SomethingTest))
    suite.addTest(unittest.makeSuite(test_subject.PersonTest))
    suite.addTest(unittest.makeSuite(test_subject.DayTest))
    suite.addTest(unittest.makeSuite(test_subject.ItemTest))
    suite.addTest(unittest.makeSuite(test_subject.StageTest))
    suite.addTest(unittest.makeSuite(test_subject.WordTest))

    # testtools
    suite.addTest(unittest.makeSuite(test_testtools.PublicMethodsTest))
    suite.addTest(unittest.makeSuite(test_testtools.PrivateMethodsTest))

    # tools
    suite.addTest(unittest.makeSuite(test_tools.PublicMethodsTest))
    suite.addTest(unittest.makeSuite(test_tools.PrivateMethodsTest))

    # utils
    suite.addTest(unittest.makeSuite(test_utils.PublicMethodsTest))

    return suite

