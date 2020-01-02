.. _manual-ar-freebsd-firewall:

Understanding Active Response with FreeBSD
==========================================

There are currently 3 options for firewalls in `FreeBSD <http://www.freebsd.org/doc/en/books/handbook/firewalls.html>`_: IPF, IPFW, and PF. 
Each is configured differently on FreeBSD. OSSEC will attempt to check for IPFW and then PF, falling back to IPF if neither of these was found at the time of installation.

How does OSSEC know which firewall is being used?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The OSSEC install script will check `rc.conf` to determine which firewall is currently active. 
It first greps for `firewall_enable="YES"`, and enables IPFW if this is found. IPFW support is enabled by copying the ``ipfw.sh`` to ``/var/ossec/active-response/bin/firewall-drop.sh``.
The installation script will then look for ``pf_enable="YES"` in the rc.conf, and will enable PF instead if this is found. The script for pf is pf.sh.
If neither of these is found, the default firewall-drop.sh script will be installed. This script will use attempt to use IPF to block IPs.

How do I change which script is used by an agent?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Copy the appropriate script from the OSSEC source to ``/var/ossec/active-response/bin/firewall-drop.sh`` on the agent.


