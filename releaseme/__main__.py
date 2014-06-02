import sys
from .runner import Runner


def main():
    runner = Runner()
    sys.exit(runner.run())

if __name__ == '__main__':
    main()
