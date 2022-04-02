import logging
import pathlib

import pandas as pd
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split

DATA_DIR = "data"


def run() -> None:
    logging.info("Loading data...")
    dataset = load_diabetes(return_X_y=True, as_frame=True)

    data_train, data_test, target_train, target_test = train_test_split(
        *dataset, random_state=1993)

    data_dir = pathlib.Path(DATA_DIR)
    data_dir.mkdir(parents=True, exist_ok=True)

    logging.info("Saving data to directory \"%s\"...", data_dir)
    data_train.to_csv(data_dir / "training_data.csv")
    data_test.to_csv(data_dir / "test_data.csv")
    target_train.to_csv(data_dir / "training_target.csv")
    target_test.to_csv(data_dir / "test_target.csv")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    run()
