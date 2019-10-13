import os
import string
from argparse import ArgumentParser
import random

parser = ArgumentParser()
parser.add_argument("-c", "--count", dest="line_count", help="count of auto generated lines ")
parser.add_argument("-f", "--file", dest="file_name", help="name of file (NOT REQUIRE)")

args = parser.parse_args()

if args.line_count is None:
    print("ERROR: argument count must be presented")
    exit(2)

line_count = None
try:
    line_count = int(args.line_count)
except ValueError:
    print("ERROR: count must be number")
    exit(4)

if line_count <= 0:
    print("ERROR: count must be positive")
    exit(3)

if args.file_name is None:
    filepath = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10)) + ".txt"
else:
    filepath = args.file_name

f = open(filepath, "w+")

for i in range(line_count):
    random_number = str(random.randint(1, 100000))
    f.write(random_number + '\n')

f.close()

print(os.path.abspath(filepath))
exit(0)
