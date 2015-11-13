class Dqueue:

    def __init__(self):
        self.dq = []

    def addFront(self, val):
        return self.dq.insert(0, val)

    def addRear(self, val):
        return self.dq.append(val)

    def removeFront(self):
        if not self.isEmpty():
            return self.dq.pop(0)
        return False

    def removeRear(self):
        if not self.isEmpty():
            return self.dq.pop()
        return False

    def isEmpty(self):
        if self.dq:
            return True
        return False
