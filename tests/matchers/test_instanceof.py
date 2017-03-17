from robber import expect
from robber.matchers.instanceof import Instanceof
from tests.fixtures import First, Second


class TestInstanceof:
    def test_matches(self):
        expect(Instanceof(First(), First).matches()) == True
        expect(Instanceof(First(), Second).matches()) == False

    def test_failure_message(self):
        first = First()
        instanceof = Instanceof(first, First)
        message = instanceof.failure_message()
        expect(message) == 'Expected "%s" to be an instance of "%s"' % (first, First)

    def test_register(self):
        expect(expect.matcher('instanceof')) == Instanceof
