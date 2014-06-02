import re
import logging


logger = logging.getLogger(__name__)


class Version(object):
    SPLIT = re.compile('[\.\-]')

    def __init__(self, number):
        self._number = number

    def split(self):
        return [int(x) if self._is_number(x) else x
                for x in self.SPLIT.split(self._number.strip() or '0')]

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

    def increment(self, increment=1):
        splitted = self.split()

        for i in range(len(splitted), 0, -1):
            if not self._is_number(splitted[i-1]):
                continue
            splitted[i-1] += increment
            break

        self._number = self._join(splitted)
        return self

    def _is_number(self, n):
        return all(x.isdigit() for x in str(n))

    def __str__(self):
        return (self._number or '0').strip()

    def __gt__(self, value):
        if isinstance(value, Version):
            result = self.split() > value.split()
            logger.debug('Compare %s > %s = %s', self, value, result)
            return result
        logger.debug('Compare %s > %s = True', self, value)
        return True

    def __add__(self, value):
        return self.increment(value)
