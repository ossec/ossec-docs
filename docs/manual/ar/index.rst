
.. _manual-ar:

Active Responces
================

Overview
--------

Active response allows you to automatically execute “commands” or responses when
a specific event or a set of events are triggered. On the OSSEC HIDS, active
response is very scalable, allowing you to execute commands on the agent or on
the server side.

The benefits of active response are enormous, but there are also risks when
using this technology. By default, the OSSEC HIDS tries to minimize some of
these risks, but some problems may still arise. Read bellow for an explanation
about the risks/advantages of using the active response and also the risk
mitigation techniques.

**Benefits**:

- Fast (time-based) response on attacks. If an attack is detected,
  an action can be taken immediately.
- Extremely good deterrent against port scans, brute forces and some
  other types of “information gathering” attacks.

**Risks**:

- A false positive may block a legitimate user/host.
- An “attacker” may find out that you are using active response
  and try to cause some form of denial of service attack.

**Risk mitigation techniques used by the OSSEC HIDS**:

- Allows you to specify a white list of hosts that should never be blocked.
- Comes with granular options, allowing you to only block on rules with low
  false-positive rate.
- Allows the specification of timeouts. Even if someone is blocked by
  mistake, after a few minutes he or she will be able to access again.

Configuration options 
---------------------

.. include:: ../../syntax/ossec_config.active-responce.trst


Configure and running active Responce
-------------------------------------

.. toctree::
    :glob:
    
    ar-windows 
    ar-unix
    ar-custom

    





