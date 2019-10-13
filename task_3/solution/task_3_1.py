from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-c", "--count", dest="line_count", help="count line for read ")
parser.add_argument("-f", "--file", dest="file_path", help="input path to file")

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

try:
    with open(args.file_path) as f:
        data = f.readlines()
except IOError:
    print("ERROR: problem with reading file")
    exit(5)

lastline = data[-1]
tail = data[-line_count:]

for line in tail:
    print(line)

exit(0)
