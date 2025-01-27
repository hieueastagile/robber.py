from robber import expect
from robber.matchers.base import Base


class CalledOnce(Base):
    """
    expect(mock).to.be.called_once()
    """

    def matches(self):
        try:
            return self.actual.call_count == 1
        except AttributeError:
            raise TypeError('{actual} is not a mock'.format(actual=self.actual))

    def failure_message(self):
        return 'Expected {actual}{negative_message} to be called once. Called {call_count} times'.format(
            actual=self.actual, negative_message=self.negative_message, call_count=self.actual.call_count
        )


expect.register('called_once', CalledOnce)
