import argparse

parser = argparse.ArgumentParser(description="meow like a cat")
parser.add_argument("-n",default=1, help="number of times to meow", type=int)
args = parser.parse_args()

for _ in range(int(args.n)):
    print("meow")