.. _communication:

Communication between agents and the OSSEC server
=================================================

Communication between agents and the OSSEC server generally
occurs on port 1514/udp in secure mode. If using the syslog
mode for `ossec-remoted`, then port 514 is the default (both
UDP and TCP are supported). These ports are configurable in
the `remote <../../syntax/head_ossec_config.remote.html>`_ 
section of the ossec.conf

The secure connection method is generally preferred over 
syslog. Also, an outside syslog daemon (like 
`rsyslog <http://www.rsyslog.com/>`_ or
`syslog-ng <https://syslog-ng.org/>`_) may be used instead 
of the syslog support in  `ossec-remoted`.

