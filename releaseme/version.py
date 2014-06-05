import re
import logging


logger = logging.getLogger(__name__)


class Version(object):
    SPLIT = re.compile('[\.\-]')
    VERSION = re.compile(
        '(?:^|[^\d\.])(\d+(?:\.\d+){0,3}(?:\-\w+)?)(?:$|[^\d\.])'
    )

    def __init__(self, content):
        self._content = content
        self._version_pattern = None
        self._version = None

    @property
    def version(self):
        if not self._version:
            versions = self.VERSION.findall(self._content) or ['0']
            self._version_pattern = max(versions)
            self._version = self.split(self._version_pattern)
        return self._version

    @property
    def content(self):
        version = self._as_str()
        return self._content.replace(self._version_pattern, version)

    def split(self, version):
        return [int(x) if self._is_number(x) else x
                for x in self.SPLIT.split(version or '0')]

    def increment(self, increment=1):
        for i in range(len(self.version), 0, -1):
            if not self._is_number(self.version[i-1]):
                continue
            self.version[i-1] += increment
            break

        return self

    def _as_str(self):
        result = ''
        v = self.version or [0]

        for i in range(len(v)):
            n = v[i]
            result += str(n)

            if i + 1 == len(v):
                break

            result += '.' if self._is_number(v[i+1]) else '-'

        return result

    def _is_number(self, n):
        return all(x.isdigit() for x in str(n))

    def __str__(self):
        return self._as_str()

    def __gt__(self, value):
        if isinstance(value, Version):
            result = self.version > value.version
            logger.debug('Compare %s > %s = %s', self, value, result)
            return result
        logger.debug('Compare %s > %s = True', self, value)
        return True

    def __add__(self, value):
        return self.increment(value)
