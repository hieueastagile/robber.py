import unittest
from robber import expect
from robber.matchers.respond_to import RespondTo


class TestRespondTo(unittest.TestCase):
    def test_matches(self):
        expect(RespondTo(expect, 'register').matches()).to.eq(True)
        expect(RespondTo(expect, 'invalid_method').matches()).to.eq(False)

    def test_failure_message(self):
        respond = RespondTo('object', 'method')
        expect(respond.failure_message()) == 'Expected "object" to respond to "method"'

    def test_negative_failure_message(self):
        respond = RespondTo('object', 'method', is_negative=True)
        expect(respond.failure_message()) == 'Expected "object" not to respond to "method"'

    def test_register(self):
        expect(expect.matcher('respond_to')) == RespondTo
