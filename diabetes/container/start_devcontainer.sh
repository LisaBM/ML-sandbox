set -e

DOCKER_TAG=diabetes:latest
WORKING_DIR=/diabetes
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
    diabetes:latest \
    container/on_start.sh
