import logging
import subprocess

logger = logging.getLogger('releaseme.sh')


def run(*command):
    logger.debug('Executting command: %s', command)
    p = subprocess.Popen(command,
                         stderr=subprocess.PIPE,
                         stdout=subprocess.PIPE)
    stdout, stderr = p.communicate()
    rc = p.wait()

    if rc:
        if stdout:
            logger.debug('STDOUT:\n %s', stdout)
        if stderr:
            logger.debug('STDERR:\n %s', stderr)
    return stdout, stderr, rc
