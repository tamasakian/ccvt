import argparse
import sys

from ccvt import cvt

def main():
    args = parse_args()
    function = functions[args.function]
    try:
        function(*args.args)
    except TypeError as e:
        print(e)
        sys.exit(1)

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("function", choices=functions)
    parser.add_argument("args", type=str, nargs='*')
    args = parser.parse_args()
    return args

functions = {
    "output_protein_id": cvt.output_protein_id
}

if __name__ == "__main__":
    main()