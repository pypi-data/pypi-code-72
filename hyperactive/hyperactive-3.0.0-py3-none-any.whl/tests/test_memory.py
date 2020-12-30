import time
import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import GradientBoostingClassifier


from hyperactive import Hyperactive


def objective_function(opt):
    score = -opt["x1"] * opt["x1"]
    return score


search_space = {
    "x1": np.arange(0, 10, 1),
}


def test_memory_timeSave_0():
    data = load_breast_cancer()
    X, y = data.data, data.target

    def objective_function(opt):
        dtc = DecisionTreeClassifier(
            min_samples_split=opt["min_samples_split"]
        )
        scores = cross_val_score(dtc, X, y, cv=5)

        return scores.mean()

    search_space = {
        "min_samples_split": np.arange(2, 20),
    }

    c_time1 = time.time()
    hyper = Hyperactive()
    hyper.add_search(objective_function, search_space, n_iter=100)
    hyper.run()
    diff_time1 = time.time() - c_time1

    c_time2 = time.time()
    hyper = Hyperactive()
    hyper.add_search(
        objective_function, search_space, n_iter=100, memory=False
    )
    hyper.run()
    diff_time2 = time.time() - c_time2

    assert diff_time1 < diff_time2 * 0.8


def test_memory_timeSave_1():
    data = load_breast_cancer()
    X, y = data.data, data.target

    def objective_function(opt):
        dtc = DecisionTreeClassifier(max_depth=opt["max_depth"])
        scores = cross_val_score(dtc, X, y, cv=5)

        return scores.mean()

    search_space = {
        "max_depth": np.arange(1, 101),
    }

    results = pd.DataFrame(np.arange(1, 101), columns=["max_depth"])
    results["score"] = 0

    c_time1 = time.time()
    hyper = Hyperactive()
    hyper.add_search(
        objective_function, search_space, n_iter=300, memory_warm_start=results
    )
    hyper.run()
    diff_time1 = time.time() - c_time1

    assert diff_time1 < 1


def test_memory_warm_start():
    data = load_breast_cancer()
    X, y = data.data, data.target

    def objective_function(opt):
        dtc = DecisionTreeClassifier(
            max_depth=opt["max_depth"],
            min_samples_split=opt["min_samples_split"],
        )
        scores = cross_val_score(dtc, X, y, cv=5)

        return scores.mean()

    search_space = {
        "max_depth": np.arange(1, 10),
        "min_samples_split": np.arange(2, 20),
    }

    c_time1 = time.time()
    hyper0 = Hyperactive()
    hyper0.add_search(objective_function, search_space, n_iter=300)
    hyper0.run()
    diff_time1 = time.time() - c_time1

    c_time2 = time.time()

    results0 = hyper0.results(objective_function)

    hyper1 = Hyperactive()
    hyper1.add_search(
        objective_function,
        search_space,
        n_iter=300,
        memory_warm_start=results0,
    )
    hyper1.run()

    diff_time2 = time.time() - c_time2

    assert diff_time2 < diff_time1 * 0.5


def test_memory_warm_start_manual():
    data = load_breast_cancer()
    X, y = data.data, data.target

    def objective_function(opt):
        dtc = GradientBoostingClassifier(n_estimators=opt["n_estimators"],)
        scores = cross_val_score(dtc, X, y, cv=5)

        return scores.mean()

    search_space = {
        "n_estimators": np.arange(500, 502),
    }

    c_time_1 = time.time()
    hyper = Hyperactive()
    hyper.add_search(objective_function, search_space, n_iter=1)
    hyper.run()
    diff_time_1 = time.time() - c_time_1

    memory_warm_start = pd.DataFrame(
        [[500, 0.9], [501, 0.91]], columns=["n_estimators", "score"]
    )

    c_time = time.time()
    hyper0 = Hyperactive()
    hyper0.add_search(
        objective_function,
        search_space,
        n_iter=10,
        memory_warm_start=memory_warm_start,
    )
    hyper0.run()
    diff_time = time.time() - c_time

    assert diff_time_1 > diff_time * 0.3

