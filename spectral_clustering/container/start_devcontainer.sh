set -e

DOCKER_TAG=spectral-clustering:latest
WORKING_DIR=/spectral_clustering
ENTRYPOINT="bash"

docker build \
    .. \
    -f Dockerfile \
    -t $DOCKER_TAG

docker run \
    -it \
    --rm \
    --entrypoint $ENTRYPOINT \
    -v $(pwd)/..:$WORKING_DIR \
    -w $WORKING_DIR \
    $DOCKER_TAG \
    container/on_start.sh
