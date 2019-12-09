'''
    Created Dec 9, 2019

    @author: Brenton Holloway
    @version: 1.0.0
'''

class Model:
    def __init__(self):
        super().__init__()
        self.previous_value = ''
        self.value = ''
        self.operator = ''
        self.recent_value = ''

    def calculate(self, caption):
        if caption == 'C':
            self.previous_value = ''
            self.value = ''
            self.operator = ''
        elif isinstance(caption, int):
            self.value += str(caption)
            self.recent_value = self.value
        elif caption == '+/-':
            self.value = self.value[1:] if self.value[0] == '-' else '-' + self.value
        elif caption == '.':
            if not caption in self.value:
                self.value += caption
            elif caption == self.value[-1]:
                self.value = self.value[:-1]
        elif caption == '%':
            pass
        elif caption == '=':
            if self.previous_value:
                self.value = self._evaluate()
                self.previous_value = ''
            else:
                self.previous_value = self.recent_value
                self.value = self._evaluate()
                self.previous_value = ''
        else:
            self.operator = caption
            if self.value:
                if self.previous_value:
                    self.previous_value = self._evaluate()
                else:
                    self.previous_value = self.value

                self.value = ''

        return self.value

    def _evaluate(self):
        return str(eval(self.previous_value+self.operator+self.value))