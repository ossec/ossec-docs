#!/bin/sh

pushd /build
	make clean
	make html
popd
