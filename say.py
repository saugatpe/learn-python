import sys

from sayings import hello , goodby

if len(sys.argv) == 2:
    hello(sys.argv[1])

    goodby(sys.argv[1])


