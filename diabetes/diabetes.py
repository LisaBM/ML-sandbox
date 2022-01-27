import pandas as pd
from sklearn.datasets import load_diabetes


def run() -> None:
    (data, target) = load_diabetes(return_X_y=True, as_frame=True)
    print(data.head())


if __name__ == "__main__":
    run()
