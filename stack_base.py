import abc


class StackBase:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def push(self, value):
        """Push value to stack"""
        return

    @abc.abstractmethod
    def pop(self):
        """Pop from top of stack"""
        return

