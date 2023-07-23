import numpy as np


class SVM:
    # Inisialisasi learningrate, paramterlambda dan iterasi
    def __init__(self, LearningRate=0.001, ParamLambda=0.01, Iteration=1000):
        self.lr = LearningRate
        self.ParamLambda = ParamLambda
        self.Iteration = Iteration
        self.w = None
        self.b = None

    # Rumus SVM
    def condition_check(self, condition_inp, x_inp, idx_inp):
        if condition_inp:
            self.w -= self.lr * (2 * self.ParamLambda * self.w)
        else:
            self.w -= self.lr * (
                2 * self.ParamLambda * self.w - np.dot(x_inp, self.cls_map[idx_inp])
            )
            self.b -= self.lr * self.cls_map[idx_inp]

    # Training SVM
    def fit(self, X, y):
        # Inisialisasi Bobot
        features = X.shape[1]
        self.w = np.zeros(features)
        self.b = 0

        # Inisialisasi Class -1 dan 1
        self.cls_map = np.where(y <= 0, -1, 1)

        for _ in range(self.Iteration):
            for idx, x in enumerate(X):
                condition = self.cls_map[idx] * (np.dot(x, self.w) - self.b) >= 1
                self.condition_check(condition, x, idx)

    # Prediksi
    def predict(self, X):
        approx = np.dot(X, self.w) - self.b
        return np.sign(approx)
