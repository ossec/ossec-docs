FROM centos:7

ADD run.sh /run.sh

RUN \
	yum -y install epel-release && \
	yum -y install python-sphinx  make python2-sphinx-bootstrap-theme 


CMD ["/run.sh"]
