from src.utils import human_readable_methods, chars_names
from theobserver import Observer
from glob import glob
import joblib


class Predictor:

    def __init__(self, filepath, target_i=-1, header=None, index_col=None):
        self.chars = []
        self.filepath = filepath
        self.obs = Observer(filepath, target_i, header, index_col)

    def extract(self):
        dataset_name = self.filepath.split('/')[-1]

        result = "Dataset {}'s characteristics\n".format(dataset_name)
        self.chars = self.obs.extract()[:-2]

        line = "{:=^66}\n"
        result += line.format('')

        names = chars_names()

        for k, v in zip(names, self.chars):
            result += "{:30}{}\n".format(k, round(v, 3))

        return result

    def predict(self):
        line = "{:=^66}\n"
        result = line.format('')

        regressors_path = glob('regressors/*.joblib')
        predictions = []

        for regressor_path in regressors_path:
            regressor_name = regressor_path.split('/')[-1].split('.')[0]
            model = joblib.load(regressor_path)
            f1_score = model.predict([self.chars])[0]

            predictions.append((regressor_name, f1_score))

        predictions.sort(key=lambda x: x[1], reverse=True)

        readable = human_readable_methods()

        result += line.format(' Ranking ')
        result += "{:<9}{:<33}{}\n".format('Position', 'Aggregation Method', 'Mean F1-Score predicted')
        for i, prediction in enumerate(predictions):
            result += "{:^9}{:<33}{}\n".format(i + 1, readable[prediction[0]], round(prediction[1], 3))

        return result
