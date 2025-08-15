# Wine Quality Classification

## Dataset

**Source:** UCI Wine Quality Dataset (https://archive.ics.uci.edu/ml/datasets/wine+quality)

## Best Model

- **Model:** Logistic Regression
- **Reason:** More stable results across folds compared to Decision Tree.
- **Evaluation Metric:** F1-score (better balance between precision & recall).

## Metrics Table

| Model               | Mean F1-score | Std (±) |
| ------------------- | ------------: | ------: |
| Logistic Regression |         0.746 |   0.049 |
| Decision Tree       |         0.656 |   0.078 |

## Learnings

1. Binarizing the target variable simplifies multi-class problems when only two categories are needed.
2. Standardizing features improves convergence for models like Logistic Regression.
3. Cross-validation gives a more reliable performance estimate than a single train/test split.
4. Logistic Regression performed more consistently than Decision Tree for this dataset.
5. F1-score is more informative than accuracy for imbalanced datasets.
