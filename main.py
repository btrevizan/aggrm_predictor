from theobserver import Observer
from glob import glob
import joblib

from gui.app import Application
import tkinter as tk


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
    root = tk.Tk()

    app = Application(master=root, width=800, height=650)
    app.master.title("Aggregation Method Predictor")
    app.master.size()
    app.mainloop()
