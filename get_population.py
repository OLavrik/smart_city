import argparse

import pandas


def get_args():
    parser = argparse.ArgumentParser("Convert UTF-8 TSV to CSV.")
    parser.add_argument("--input_file", help="TSV file to read", default="./population.csv", required=False)

    return parser.parse_args()


if __name__ == "__main__":
    args = get_args()

    with open(args.input_file, "rt", encoding="utf-8") as csv_file:
        data = pandas.read_csv(csv_file)
    data["Population"] = data["Population"].apply(lambda x: x.replace(" ", ""))
    data = data.astype({"Population": int})
    print(data)

    with open('./population_regions.csv', "rt", encoding="utf-8") as csv_file:
        data_r = pandas.read_csv(csv_file)
    data_r["Population"] = data_r["Population"].apply(lambda x: x.replace(" ", ""))
    data_r = data_r.astype({"Population": int})
    print(data_r.sort_values('Population'))
