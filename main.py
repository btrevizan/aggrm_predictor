from src.utils import human_readable_methods
from theobserver import Observer
from glob import glob
import argparse
import joblib


def main(args):
    obs = Observer(args.dataset_path, args.target_i, args.header, args.index_col)

    dataset_name = args.dataset_path.split('/')[-1]

    print("Extracting dataset {}'s characteristics...".format(dataset_name), end=' ')
    print("Done.")

    line = "{:=^66}"
    print(line.format(''))

    chars = obs.extract()[:-2]
    chars_names = ['Number of Instances',
                   'Number of Features',
                   'Number of Targets',
                   'Silhouette coefficient',
                   'Imbalance coefficient',
                   'Number of binary features',
                   'Majority class size',
                   'Minority class size']

    for k, v in zip(chars_names, chars):
        print("{:30}{}".format(k, round(v, 3)))

    print(line.format(''))
    print('Predicting ranking...', end=' ')

    regressors_path = glob('regressors/*.joblib')
    predictions = []

    for regressor_path in regressors_path:
        regressor_name = regressor_path.split('/')[-1].split('.')[0]
        model = joblib.load(regressor_path)
        f1_score = model.predict([chars])[0]

        predictions.append((regressor_name, f1_score))

    predictions.sort(key=lambda x: x[1], reverse=True)

    print('Done.')

    readable = human_readable_methods()

    print(line.format(' Ranking '))
    print("{:<9}{:<33}{}".format('Position', 'Aggregation Method', 'Mean F1-Score predicted'))
    for i, prediction in enumerate(predictions):
        print("{:^9}{:<33}{}".format(i + 1, readable[prediction[0]], round(prediction[1], 3)))


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
