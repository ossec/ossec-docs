FROM sphinxdoc/sphinx
WORKDIR /docs
ADD requirements.txt /docs
ADD run.sh /run.sh

RUN \
	pip3 install -r requirements.txt


CMD ["/run.sh"]
