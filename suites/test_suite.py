import unittest

import HtmlTestRunner

from test_cases.test_failed_login import TestFailedLogin
from test_cases.test_login_page_instance import TestLoginPage
from test_cases.test_place_order import Test_Place_Order
from test_cases.test_product_sort import TestSort
from test_cases.test_succes_login import TestPositiveLogin


class TestSuiteAll(unittest.TestCase):

    def test_suite(self):
        test_suite = unittest.TestSuite()
        test_suite.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(TestLoginPage),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestPositiveLogin),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestFailedLogin),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestSort),
            unittest.defaultTestLoader.loadTestsFromTestCase(Test_Place_Order)
        ])
        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_title="All Pages Test Report",
            report_name="All Pages Test Results"
        )
        runner.run(test_suite)
