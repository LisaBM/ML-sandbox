import logging
import pathlib
import pickle

import pandas as pd
from sklearn.linear_model import LinearRegression

DATA_DIR = "data"
MODEL_DIR = "model"


def run() -> None:
    data_dir = pathlib.Path(DATA_DIR)
    logging.info("Loading data from directory \"%s\"...", data_dir)
    data_train, target_train = load_data(data_dir)

    logging.info("Training linear regression...")
    lin_reg = LinearRegression(copy_X=True)
    lin_reg = lin_reg.fit(data_train, target_train)

    model_dir = pathlib.Path(MODEL_DIR)
    logging.info("Saving model to directory \"%s\"...", model_dir)
    save_model(lin_reg, model_dir)


def load_data(data_dir: pathlib.Path) -> tuple[pd.DataFrame, pd.DataFrame]:
    data_train = pd.read_csv(data_dir / "training_data.csv")
    target_train = pd.read_csv(data_dir / "training_target.csv")
    return data_train, target_train


def save_model(model: LinearRegression, model_dir: pathlib.Path) -> None:
    model_dir.mkdir(parents=True, exist_ok=True)
    with open(model_dir / "lin_reg.pkl", "wb") as f:
        pickle.dump(model, f)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    run()
