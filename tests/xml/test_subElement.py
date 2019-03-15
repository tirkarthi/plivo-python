from unittest import TestCase

from plivo import plivoxml


class SubElementTest(TestCase):
    def test_set_methods(self):
        expected_response = '<Response><Sub alias="World Wide Web Consortium"/></Response>'
        alias="World Wide Web Consortium"

        element = plivoxml.ResponseElement()
        response = element.add(
            plivoxml.SubElement().set_alias(alias)
        ).to_string()
        self.assertEqual(response, expected_response + '\n')
