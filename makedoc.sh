#!/bin/sh

pushd docker/el7
	docker build -t ossec-documentation .
popd

docker run --rm -v ${PWD}:/build ossec-documentation
