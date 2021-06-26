# Feel free to add new properties and methods to the class.
class MinMaxStack:

    def __init__(self):
        self.stack = []
        self._min_max_stack = []

    # T.C all methods: O(1)
    # S.C all methods: O(1)
    # but make sure from interviewer if they OK for extra space of _min_max_stack
    def peek(self):
        return self.stack[-1]

    def pop(self):
        _ = self.stack.pop()
        self._min_max_stack.pop()
        return _

    def push(self, number):
        self.stack.append(number)
        _min, _max = number, number
        if self._min_max_stack != []:
            last_min_max = self._min_max_stack[-1]
            _min = min(last_min_max['min'], number)
            _max = max(last_min_max['max'], number)
        self._min_max_stack.append({'min': _min, 'max': _max})

    def getMin(self):
        return self._min_max_stack[-1]['min']

    def getMax(self):
        return self._min_max_stack[-1]['max']
