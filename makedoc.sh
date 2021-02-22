#!/bin/sh

pushd docker/sphinx
	docker build -t ossec-documentation .
popd

docker run --rm -v ${PWD}:/build ossec-documentation
