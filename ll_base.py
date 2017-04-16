import abc


class LinkedListBase:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def setData(self, data):
        return

    @abc.abstractmethod
    def setNext(self, data):
        return

    @abc.abstractmethod
    def getData(self):
        return

    @abc.abstractmethod
    def getNext(self):
        return

