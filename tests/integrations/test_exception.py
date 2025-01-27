from unittest import TestCase

from robber import expect
from tests import must_fail


class TestExceptionIntegrations(TestCase):
    def test_exception_success(self):
        expect(lambda: 1 / 0).to.throw(ZeroDivisionError)

    @must_fail
    def test_exception_failure(self):
        expect(lambda: None).to.throw(Exception)

    def test_not_exception_success(self):
        expect(lambda: None).not_to.throw(Exception)

    @must_fail
    def test_not_exception_failure(self):
        expect(lambda: 1 / 0).not_to.throw(ZeroDivisionError)
