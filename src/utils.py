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


def chars_names():
    return ['Number of Instances',
            'Number of Features',
            'Number of Targets',
            'Silhouette coefficient',
            'Imbalance coefficient',
            'Number of binary features',
            'Majority class size',
            'Minority class size']
