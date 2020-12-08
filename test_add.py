#coding=utf-8

import unittest
from TestRunner import HTMLTestRunner


class TestDemo(unittest.TestCase):
    """测试用例说明"""

    def test_success(self):
        """执行成功"""
        self.assertEqual(2 + 3, 5)

if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTest(TestDemo("test_success"))


    with open('test.html', 'wb') as fp:
        runner = HTMLTestRunner(
            stream=fp,
            title='<project name>test report',
            description='describe: ... ')
        runner.run(suit)
