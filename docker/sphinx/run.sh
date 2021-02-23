#!/bin/bash

pushd /build
	make clean
	make html
popd
