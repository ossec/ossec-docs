.. _rootcheck_unix_policy_audit:


Understanding the Unix policy auditing on OSSEC
===============================================

OSSEC's policy monitor allows you to verify that all your systems conform to a set of policies regarding configuration settings and applications usage. 
They are configured centrally on the ossec server 
and pushed down to the agents. It also checks if a system in in compliance with the CIS Security Benchmarks
and VMware security hardening guidelines.

The following systems are tested for the CIS and VMware guidelines:

* `Debian and Ubuntu <audit/CIS_debian.html>`_

* `Red Hat and Fedora <audit/CIS_rhel.html>`_

* `Red Hat Enterprise Linux 5 <audit/CIS_rhel5.html>`_

* `VMWare ESX 3.0 and 3.5 <audit/vmware_hardening.html>`_


Receiving Audit and Application alerts via Email
------------------------------------------------

By default, both the policy auditing and application checks are logged as level ``3``, so you will not
receive any e-mail alerts with the original configuration.

If you wish to receive e-mail alerts for any (or both of the two) types of events, you need to create
local rules with a higher severity or with the ``alert_by_email`` option set.

.. More information on [[Know_How:Ignore_Rules|local rules here]].


Example1: Sending e-mail for every Audit event
----------------------------------------------

Add to your local_rules.xml the following:


.. code-block:: console

  <pre>
    <rule id="512" level="9" overwrite="yes">
      <if_sid>510</if_sid>
      <match>^System Audit</match>
      <description>System Audit event.</description>
      <group>rootcheck,</group>
    </rule>
  </pre>


Listing entries per agent
-------------------------

To control the policy database, use the '''rootcheck_control''' tool.




This page was originally authored by Daniel Cid for the OSSEC wiki.
