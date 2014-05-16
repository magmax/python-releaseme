import re


class Version(object):
    SPLIT = re.compile('[\.\-]')

    def __init__(self, number):
        self._number = number

    def split(self):
        return [int(x) if self._is_number(x) else x
                for x in self.SPLIT.split(self._number)]

    def _join(self, v):
        result = ''

        last = v[-1]
        for i in range(len(v)):
            n = v[i]
            result += str(n)

            if last == n:
                break

            result += '.' if self._is_number(v[i+1]) else '-'

        return result

    def increment(self):
        splitted = self.split()

        for i in range(len(splitted)-1, 0, -1):
            if not self._is_number(splitted[i]):
                continue
            splitted[i] += 1
            break

        self._number = self._join(splitted)

    def _is_number(self, n):
        return all(x.isdigit() for x in str(n))

    def __str__(self):
        return self._number
