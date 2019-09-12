from src.utils import chars_names
from theobserver import Observer
from glob import glob
import joblib


class Predictor:

    def __init__(self, filepath, target_i=-1, header=None, index_col=None):
        self.chars = []
        self.filepath = filepath
        self.obs = Observer(filepath, target_i, header, index_col)

    def extract(self):
        self.chars = self.obs.extract()[:-2]
        return dict(zip(chars_names(), self.chars))

    def predict(self):
        regressors_path = glob('regressors/*.joblib')
        predictions = []

        for regressor_path in regressors_path:
            regressor_name = regressor_path.split('/')[-1].split('.')[0]
            model = joblib.load(regressor_path)
            f1_score = model.predict([self.chars])[0]

            predictions.append((regressor_name, f1_score))

        predictions.sort(key=lambda x: x[1], reverse=True)
        return predictions
