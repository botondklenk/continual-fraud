import numpy as np
from copy import deepcopy


class RollingRF:
    def __init__(self, ratio: float) -> None:
        self._ratio = ratio
        self._rf = None

    def merge(self, new_rf, X: np.ndarray=None) -> None:
        if self._rf is None:
            self._rf = deepcopy(new_rf)
        else:
            keep = int(self._ratio * len(self._rf.estimators_))
            add = min(len(new_rf.estimators_), len(self._rf.estimators_) - keep)
            self._rf.estimators_ = new_rf.estimators_[:add] + self._rf.estimators_[-keep:]

    def predict(self, X) -> np.ndarray:
        return self._rf.predict(X)

    def __repr__(self) -> str:
        return "RollingRF(%.2f)" % self._ratio


class SlowForgettingRF(RollingRF):
    def merge(self, new_rf, X: np.ndarray=None) -> None:
        if self._rf is None:
            self._rf = deepcopy(new_rf)
        else:
            keep = int(self._ratio * len(self._rf.estimators_))
            add = min(len(new_rf.estimators_), len(self._rf.estimators_) - keep)
            keep_i = np.random.choice(len(self._rf.estimators_), size=keep, replace=False)
            add_i = np.random.choice(len(new_rf.estimators_), size=add, replace=False)
            self._rf.estimators_ = [
                self._rf.estimators_[i] for i in keep_i
            ] + [
                new_rf.estimators_[i] for i in add_i
            ]
            

    def __repr__(self) -> str:
        return "SlowForgettingRF(%.2f)" % self._ratio
    
class BalancedForgettingRF(RollingRF):
    def __init__(self, max_ratio) -> None:
        self._max_ratio = max_ratio
        self._ratio = 1.0
        self._rf = None
        self._n_samples = 0
    
    def merge(self, new_rf, X: np.ndarray=None) -> None:
        new_n_samples = self._n_samples + X.shape[0]
        
        if self._rf is None:
            self._rf = deepcopy(new_rf)
        else:
            self._ratio = min((self._n_samples / new_n_samples), self._max_ratio)
            keep = int(self._ratio * len(self._rf.estimators_))
            add = min(len(new_rf.estimators_), len(self._rf.estimators_) - keep)
            keep_i = np.random.choice(len(self._rf.estimators_), size=keep, replace=False)
            counts = [estimator.predict(X).sum() for estimator in new_rf.estimators_]
            sorted_estimators = [est for _, est in sorted(zip(counts, new_rf.estimators_), key=lambda pair: pair[0])]
            self._rf.estimators_ = [
                self._rf.estimators_[i] for i in keep_i
            ] + sorted_estimators[-add:]
            
        self._n_samples = new_n_samples
            

    def __repr__(self) -> str:
        return "BalancedForgettingRF(%.2f)" % self._ratio
    

