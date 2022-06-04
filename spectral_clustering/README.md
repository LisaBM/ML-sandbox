# Spectral Clustering

## Development environment

In the Terminal, navigate to the `container` directory and run
```sh
./start_devcontainer.sh
```

This will open a local container for development.

## Running tests and type checks

To run the test suite, from the `/spectral_clustering` directory in the development container, run:
```sh
python -m pytest tests
```

To run the Python type checks, from the `/spectral_clustering` directory in the development container, run:
```sh
mypy *.py
```