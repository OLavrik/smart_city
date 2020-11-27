import argparse
import json

from smart_city_backend.ml import make_prediciton


def get_args():
    parser = argparse.ArgumentParser(
        "Read a JSON file and feed it to a predict function."
    )
    parser.add_argument("input_file", help="JSON file to read")
    return parser.parse_args()


def predict(data):
    """
    Do the actual prediction using some hustling ML&AI
    :param data: (dict) Dictionary with data passed by a user
    :return: (str) Prediction
    """
    df = convert_request_to_df(data)
    result = make_prediciton(df)
    return result


if __name__ == "__main__":
    args = get_args()
    with open(args.input_file) as f:
        data = json.load(f)

    predicted_str = predict(data)

    print(predicted_str)
