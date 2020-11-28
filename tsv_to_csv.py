import argparse

import pandas


def get_args():
    parser = argparse.ArgumentParser("Convert UTF-8 TSV to CSV.")
    parser.add_argument("input_file", help="TSV file to read")

    return parser.parse_args()


if __name__ == "__main__":
    args = get_args()

    with open(args.input_file, "rt", encoding="utf-8") as csv_file:
        data = pandas.read_csv(csv_file, sep="\t")

    print(data)
    data.to_csv("converted_out.csv", index=False, encoding="utf-8")
