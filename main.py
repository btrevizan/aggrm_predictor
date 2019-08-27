from theobserver import Observer
from glob import glob
import argparse
import joblib


def main(args):
    obs = Observer(args.dataset_path, args.target_i, args.header, args.index_col)
    chars = obs.extract()[:-2]

    regressors_path = glob('regressors/*.joblib')
    predictions = []

    for regressor_path in regressors_path:
        regressor_name = regressor_path.split('/')[-1].split('.')[0]
        model = joblib.load(regressor_path)
        f1_score = model.predict([chars])[0]

        predictions.append((regressor_name, f1_score))

    predictions.sort(key=lambda x: x[1], reverse=True)

    for i, prediction in enumerate(predictions):
        print("{}. ({}) {}".format(i + 1, round(prediction[1], 3), prediction[0]))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("-d", "--dataset",
                        dest="dataset_path",
                        required=True,
                        help="Dataset's relative/absolute path.")

    parser.add_argument("-t", "--target",
                        dest="target_i",
                        default=-1,
                        help="Target's column number.")

    parser.add_argument("-e", "--header",
                        dest="header",
                        default=None,
                        help="Header's index number.")

    parser.add_argument("-c", "--col",
                        dest="index_col",
                        default=None,
                        help="Index's column number.")

    arguments = parser.parse_args()
    main(arguments)
