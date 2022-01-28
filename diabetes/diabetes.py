import pandas as pd
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


def run() -> None:
    dataset = load_diabetes(return_X_y=True, as_frame=True)
    data_train, data_test, target_train, target_test = train_test_split(
        *dataset, random_state=1993)
    lin_reg = LinearRegression(copy_X=True)
    lin_reg = lin_reg.fit(data_train, target_train)


if __name__ == "__main__":
    run()
