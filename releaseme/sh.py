import subprocess


def run(*command):
    p = subprocess.Popen(command,
                         stderr=subprocess.PIPE,
                         stdout=subprocess.PIPE)
    stdout, stderr = p.communicate()
    return stdout, stderr, p.wait()
