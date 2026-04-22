from sklearn.neural_network import MLPRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from utils import build_features


def train_narx_nn(data):
    X, y = build_features(data.u, data.y)

    model = Pipeline([
        ("scaler", StandardScaler()),
        ("mlp", MLPRegressor(
            hidden_layer_sizes=(32, 32),
            activation="tanh",
            max_iter=500,
            learning_rate_init=0.001,
            random_state=0
        ))
    ])

    model.fit(X, y)
    return model