import argparse

parser = argparse.ArgumentParser(description='Manage project versions')
parser.add_argument('command', nargs='?', default='increment',
                    choices=['increment', 'get'],
                    help='Action to be performed')
parser.add_argument('--file',
                    help='File that manages the version')

args = parser.parse_args()

with file(args.file) as fd:
    version = fd.read()

version = '0.1.3'
with file(args.file, 'w') as fd:
    fd.write(version)
print version
