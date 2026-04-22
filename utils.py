import numpy as np

def build_features(u, y, lag=2):
    X, Y = [], []
    for t in range(lag, len(y)):
        X.append([u[t], u[t-1], y[t-1], y[t-2]])
        Y.append(y[t])
    return np.array(X), np.array(Y)


def simulate(model, u, y_init):
    y_pred = list(y_init)

    for t in range(2, len(u)):
        x = np.array([
            u[t], u[t-1],
            y_pred[-1], y_pred[-2]
        ]).reshape(1, -1)

        y_next = model.predict(x)[0]
        y_next = np.clip(y_next, -2, 2)
        y_pred.append(y_next)

    return np.array(y_pred)