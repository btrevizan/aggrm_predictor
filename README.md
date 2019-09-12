# Aggregation Method Predictor
This application is a practical implementation of the 
discovered facts about aggregation methods on the 
"A comparative evaluation of aggregation methods for 
machine learning under vertically partitioned data" 
project.

It produces a ranking of the best aggregation methods 
based on the problems intrinsic characteristics.
So its input is the path for a dataset, preferably in 
CSV format.

The research's results can be found at 
[https://github.com/btrevizan/distributed_classifier](https://github.com/btrevizan/distributed_classifier).


## Command line usage
```
usage: main.py [-h] -d DATASET_PATH [-t TARGET_I] [-e HEADER] [-c INDEX_COL]

optional arguments:
  -h, --help            show this help message and exit
  -d DATASET_PATH, --dataset DATASET_PATH
                        Dataset's relative/absolute path.
  -t TARGET_I, --target TARGET_I
                        Target's column number.
  -e HEADER, --header HEADER
                        Header's index number.
  -c INDEX_COL, --col INDEX_COL
                        Index's column number.
```

## Example
The command
```
$ python3 main.py -d examples/credit_last.csv
```
outputs:
```
Extracting dataset credit_last.csv's characteristics... Done.
==================================================================
Number of Instances           690
Number of Features            589
Number of Targets             2
Silhouette coefficient        0.174
Imbalance coefficient         0.991
Number of binary features     585
Majority class size           383
Minority class size           307
==================================================================
Predicting ranking... Done.
============================ Ranking =============================
Position Aggregation Method               Mean F1-Score predicted
    1    Arbiter MDIC DTREE               0.792
    2    Combiner MLP                     0.725
    3    Combiner KNN                     0.724
    4    Combiner SVC                     0.709
    5    Social Choice Function Simpson   0.708
    6    Combiner GNB                     0.694
    7    Social Choice Functions          0.691
    8    Arbiter MD MLP                   0.677
    9    Arbiter MDIC MLP                 0.676
   10    Arbiter MDI                      0.672
   11    Arbiter MDIC                     0.672
   12    Arbiter MD GNB                   0.67
   13    Combiner DTREE                   0.67
   14    Arbiter MDIC KNN                 0.662
   15    Social Choice Function Borda     0.659
   16    Base classifiers                 0.657
   17    Plurality                        0.655
   18    Plurality                        0.655
   19    Social Choice Function Dowdall   0.646
   20    Arithmetic-based Median          0.645
   21    Base Classifier DTREE            0.633
   22    Combiners                        0.62
   23    Arbiter MD                       0.615
   24    Arithmetic-based                 0.613
   25    Arbiter MD SVC                   0.593
   26    Arbiter MDI KNN                  0.592
   27    Base Classifier GNB              0.578
   28    Base Classifier KNN              0.569
   29    Arithmetic-based Mean            0.547
   30    Base Classifier MLP              0.537
   31    Arbiter MD DTREE                 0.535
   32    Social Choice Function Copeland  0.529
   33    Base Classifier SVC              0.525
   34    Arbiter MDI GNB                  0.522
   35    Arbiter MDI DTREE                0.508
   36    Arbiter MD KNN                   0.506
   37    Arbiter MDI SVC                  0.501
   38    Arbiter MDIC SVC                 0.494
   39    Arbiter MDIC GNB                 0.464
   40    Arbiter MDI MLP                  0.437
```
The value between parenthesis is the predicted F1 
Score for the respective aggregation method.

## GUI Version
To run the GUI version, just:
```
$ python3 app.py
```

Or, you can generate an executable with `pyinstaller`:
```
$ pyinstaller --windowed --clean --onefile app.spec
```

The executable will be created at `dist/`.

### Troubleshooting
I've had some trouble using newer versions of `joblib` (a Python library).
I found out that the version which works the best with `pyinstaller` is `0.11.0`.