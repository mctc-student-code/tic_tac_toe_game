import unittest

import camel_case
from unittest import TestCase


class TestCamelCase(TestCase):

    def test_camelcase_sentence(self):

        self.assertEqual('helloWorld', camel_case.camelCase_convert('Hello World'))
        self.assertEqual('', camel_case.camelCase_convert(''))
        self.assertEqual('helloWorld', camel_case.camelCase_convert('    hello     world'))
        self.assertEqual('Hello world'.split(), ['Hello', 'world'])
        self.assertEqual('helloWorld', camel_case.camelCase_convert('HELLO WORLD'))
        self.assertEqual('Warning: There may be an issue in created variable name', camel_case.camelCase_convert('Hello World!'))


    # def test_regular_expression_attribute_error(self):
    #     with self.assertRaises(AttributeError):
    #         camel_case.camelCase_convert('helloWorld!', f'\nWarning: There may be an issue in created variable name "{camel_case.camelCase_convert.variable_name}"')




