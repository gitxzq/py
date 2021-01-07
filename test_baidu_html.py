# coding=utf-8

import unittest
from selenium import webdriver
from TestRunner import HTMLTestRunner
from time import sleep


class YouTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.base_url = 'http://www.baidu.com'

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test_success(self):
        self.driver.get(self.base_url)
        self.driver.find_element_by_id('kw').send_keys('HTMLTestRunner')
        self.driver.find_element_by_id('su').click()
        sleep(2)

    def test_err(self):
        self.driver.get(self.base_url)
        self.driver.find_element_by_id('kw').send_keys('python')
        self.driver.find_element_by_id('su22').click()
        sleep(2)

    def test_fail(self):
        self.driver.get(self.base_url)
        self.driver.find_element_by_id('kw').send_keys('unittest')
        self.driver.find_element_by_id('su').click()
        sleep(2)
        self.assertEqual(self.driver.title, "unittest")


if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTest(YouTest('test_success'))
    suit.addTest(YouTest('test_err'))
    suit.addTest(YouTest('test_fail'))

    report = "selenium_resulthaha.html"

    with(open(report, 'wb')) as fp:
        runner = HTMLTestRunner(stream=fp, title='自动化报告', description='windows')
        runner.run(suit)
