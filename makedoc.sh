#!/bin/sh

pushd docker/sphinx
	podman build -t ossec-documentation .
popd

podman run --rm --userns=keep-id -v ${PWD}:/build ossec-documentation
