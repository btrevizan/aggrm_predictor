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
1. (0.792) arb_mdic_dtree
2. (0.725) cmb_mlp
3. (0.724) cmb_knn
4. (0.709) cmb_svc
5. (0.708) simpson
6. (0.694) cmb_gnb
7. (0.691) scf
8. (0.677) arb_md_mlp
9. (0.676) arb_mdic_mlp
10. (0.672) arbmdi
11. (0.672) arbmdic
12. (0.67) arb_md_gnb
13. (0.67) cmb_dtree
14. (0.662) arb_mdic_knn
15. (0.659) borda
16. (0.657) classif
17. (0.655) plurality
18. (0.655) vote
19. (0.646) dowdall
20. (0.645) median
21. (0.633) dtree
22. (0.62) cmb
23. (0.615) arbmd
24. (0.613) math
25. (0.593) arb_md_svc
26. (0.592) arb_mdi_knn
27. (0.578) gnb
28. (0.569) knn
29. (0.547) mean
30. (0.537) mlp
31. (0.535) arb_md_dtree
32. (0.529) copeland
33. (0.525) svc
34. (0.522) arb_mdi_gnb
35. (0.508) arb_mdi_dtree
36. (0.506) arb_md_knn
37. (0.501) arb_mdi_svc
38. (0.494) arb_mdic_svc
39. (0.464) arb_mdic_gnb
40. (0.437) arb_mdi_mlp
```
The value between parenthesis is the predicted F1 
Score for the respective aggregation method.