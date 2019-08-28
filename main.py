from theobserver import Observer
from glob import glob
import argparse
import joblib


def human_readable_methods():
    ret = {
        "vote_plurality": "Plurality",
        "scf_simpson": "Social Choice Function Simpson",
        "scf_dowdall": "Social Choice Function Dowdall",
        "scf_copeland": "Social Choice Function Copeland",
        "scf_borda": "Social Choice Function Borda",
        "math_median": "Arithmetic-based Median",
        "math_mean": "Arithmetic-based Mean",
        "cmb_svc": "Combiner SVC",
        "cmb_mlp": "Combiner MLP",
        "cmb_knn": "Combiner KNN",
        "cmb_gnb": "Combiner GNB",
        "cmb_dtree": "Combiner DTREE",
        "classif_svc": "Base Classifier SVC",
        "classif_mlp": "Base Classifier MLP",
        "classif_knn": "Base Classifier KNN",
        "classif_gnb": "Base Classifier GNB",
        "classif_dtree": "Base Classifier DTREE",
        "arbmdic_svc": "Arbiter MDIC SVC",
        "arbmdic_mlp": "Arbiter MDIC MLP",
        "arbmdic_knn": "Arbiter MDIC KNN",
        "arbmdic_gnb": "Arbiter MDIC GNB",
        "arbmdic_dtree": "Arbiter MDIC DTREE",
        "arbmdi_svc": "Arbiter MDI SVC",
        "arbmdi_mlp": "Arbiter MDI MLP",
        "arbmdi_knn": "Arbiter MDI KNN",
        "arbmdi_gnb": "Arbiter MDI GNB",
        "arbmdi_dtree": "Arbiter MDI DTREE",
        "arbmd_svc": "Arbiter MD SVC",
        "arbmd_mlp": "Arbiter MD MLP",
        "arbmd_knn": "Arbiter MD KNN",
        "arbmd_gnb": "Arbiter MD GNB",
        "arbmd_dtree": "Arbiter MD DTREE",
        'arbmd': 'Arbiter MD',
        'arbmdi': 'Arbiter MDI',
        'arbmdic': 'Arbiter MDIC',
        'classif': 'Base classifiers',
        'cmb': 'Combiners',
        'math': 'Arithmetic-based',
        'scf': 'Social Choice Functions',
        'vote': 'Plurality'
    }

    ret['arb_md_dtree'] = ret['arbmd_dtree']
    ret['arb_md_gnb'] = ret['arbmd_gnb']
    ret['arb_md_knn'] = ret['arbmd_knn']
    ret['arb_md_mlp'] = ret['arbmd_mlp']
    ret['arb_md_svc'] = ret['arbmd_svc']

    ret['arb_mdi_dtree'] = ret['arbmdi_dtree']
    ret['arb_mdi_gnb'] = ret['arbmdi_gnb']
    ret['arb_mdi_knn'] = ret['arbmdi_knn']
    ret['arb_mdi_mlp'] = ret['arbmdi_mlp']
    ret['arb_mdi_svc'] = ret['arbmdi_svc']

    ret['arb_mdic_dtree'] = ret['arbmdic_dtree']
    ret['arb_mdic_gnb'] = ret['arbmdic_gnb']
    ret['arb_mdic_knn'] = ret['arbmdic_knn']
    ret['arb_mdic_mlp'] = ret['arbmdic_mlp']
    ret['arb_mdic_svc'] = ret['arbmdic_svc']

    ret['arb_md'] = ret['arbmd']
    ret['arb_mdi'] = ret['arbmdi']
    ret['arb_mdic'] = ret['arbmdic']

    ret['borda'] = ret['scf_borda']
    ret['copeland'] = ret['scf_copeland']
    ret['dowdall'] = ret['scf_dowdall']
    ret['simpson'] = ret['scf_simpson']
    ret['dtree'] = ret['classif_dtree']
    ret['gnb'] = ret['classif_gnb']
    ret['knn'] = ret['classif_knn']
    ret['mlp'] = ret['classif_mlp']
    ret['svc'] = ret['classif_svc']
    ret['mean'] = ret['math_mean']
    ret['median'] = ret['math_median']
    ret['plurality'] = ret['vote_plurality']

    return ret


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
