# coding=utf-8

from sklearn.model_selection import RandomizedSearchCV, KFold
from sklearn.metrics import make_scorer, accuracy_score
from scipy.stats import randint as sp_randint, uniform


# grid search method for decision tree
# too slow: presort = True, splitter = best
def best_estimator(clf, X_train, y_train):
    accuracy_scorer = make_scorer(accuracy_score)
    parameters = {'criterion': ['gini', 'entropy'], \
                  'splitter': ['random'], \
                  'class_weight': ['balanced', None], \
                  'presort': [False]}
    grid_obj = RandomizedSearchCV(estimator=clf, param_distributions=parameters, scoring=accuracy_scorer, cv=KFold(n_splits=2), n_jobs=1, n_iter=4)
    grid_obj = grid_obj.fit(X_train, y_train.tolist())
    clf = grid_obj.best_estimator_
    print(clf)
    return clf


# grid search method for kneighbors
# too slow: algorithm = brute
# error: metric = [wminkowski, seuclidean, mahalanobis]
def best_estimator_kn(clf, X_train, y_train):
    accuracy_scorer = make_scorer(accuracy_score)
    parameters = {'algorithm': ['ball_tree', 'kd_tree'], \
                  'metric': ['euclidean', 'manhattan', 'chebyshev', 'minkowski'], \
                  'weights': ['uniform', 'distance'], \
                  'leaf_size': [5, 10, 15], \
                  'p': [1, 2], \
                  'n_neighbors': [3, 4, 5]}
    grid_obj = RandomizedSearchCV(estimator=clf, param_distributions=parameters, scoring=accuracy_scorer, cv=KFold(n_splits=2), n_jobs=-1, n_iter=288)
    grid_obj = grid_obj.fit(X_train, y_train.tolist())
    clf = grid_obj.best_estimator_
    print(clf)
    return clf


# decode all features
def decode_features(X_all, X_encoder, NUMBER_OF_FEATURES):
    for col in range(0, NUMBER_OF_FEATURES):
        X_all.iloc[:, col] = X_encoder[col].inverse_transform(X_all.iloc[:, col])
    return X_all.iloc[:, :]


# decode all labels
def decode_labels(y_all, y_encoder):
    return y_encoder.inverse_transform(y_all)


# predict one product at a time
# useful to save memory and analyze the wrong predictions as well
def predict_loop(clf, X_test, y_test, X_encoder, y_encoder):
    # accuracy variables
    correct = 0
    wrong = 0

    # for each product in the testing data...
    for i in range(0, len(X_test)):

        # predict
        pred = clf.predict(X_test[i:i + 1])

        # increase accuracy variables
        if (pred == y_test[i]):
            correct += 1
        else:
            wrong += 1

            # decode features
            product = X_encoder[0].inverse_transform(X_test.iloc[i:i + 1, 0])

            # decode wrong and right labels
            # print decoded categories, product name and probability
            print(y_encoder.inverse_transform(pred)[0] + ';' + \
                  y_encoder.inverse_transform(y_test[i]) + ';' + \
                  product[0])

    # print accuracy value
    print('accuracy: {:.2f}%'.format(100. * correct / (correct + wrong)))
