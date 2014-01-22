
.. _manual-syscheck:

Syscheck
========

**Syscheck** is the name of the integrity checking process inside OSSEC. 
It runs periodically to check if any configured file (or registry entry on Windows) has changed.

Why Integrity checking?
-----------------------

This is the explanation from the `OSSEC book`_:

.. _OSSEC book: http://www.amazon.com/OSSEC-Host-Based-Intrusion-Detection-Guide/dp/159749240X

    There are multiple types of attacks and many attack vectors, but there
    is one thing unique about all of them: they leave traces and always change
    the system in some way. From viruses that modify a few files, to kernel-level
    rootkits that alters the kernel, there is always some change in the
    integrity of the system.

    Integrity checking is an essential part of intrusion detection, that
    detects changes in the integrity of the system. OSSEC does that by
    looking for changes in the MD5/SHA1 checksums of the key files in the
    system and on the Windows registry.

    The way it works is that the agent scans the system every few hours
    (user defined) and send all the checksums to the server. The server
    stores the checksums and look for modifications on them. An alert
    is sent if anything changes.

Quick facts
-----------

* How often does it run? 
  
  - By default every 2 hours on agents and every 20 hours on servers, but the frequency or time/day are configurable.

* Where is the database stored? 
  
  - On the manager in ``/var/ossec/queue/syscheck``.

* How does it help with compliance? (PCI DSS, etc) 

  - It helps with sections 11.5 (install FIM software) and 10.5 (integrity checking of log files) of PCI.

* How much CPU does it use? 
  
  - The scans are performed slowly to avoid using too much CPU/memory.

* How are false positives handled? 
  
  - Files can be ignored manually in the configuration or using rules. By default when a file has changed 3 times further changes are automatically ignored.

Realtime options
----------------

``ossec-syscheckd`` is able to check file integrity in near realtime on Windows and modern Linux distros. 
Windows comes with support out of the box, but on Linux systems inotify packages may need to be installed. 
Check for inotify dev packages, and possibly an inotify-tools package.

Configuration options
---------------------

The configuration options can be specified in each agent's ossec.conf file, except 
for the ``auto_ignore`` and ``alert_new_file`` which only apply to manager and local installs. 
The ``ignore`` option applies to all agents if specified on the manager.


.. include:: ../../syntax/ossec_config.syscheck.trst 

Configuration Examples
----------------------

To configure syscheck, a list of files and directories must be provided. The check_all option checks md5, sha1, owner, and permissions of the file.

Example:

.. code-block:: xml

    <syscheck>
        <directories check_all="yes">/etc,/usr/bin,/usr/sbin</directories>
        <directories check_all="yes">/root/users.txt,/bsd,/root/db.html</directories>
    </syscheck>

Files and directories can be ignored using the ``ignore`` option (or ``registry_ignore`` for Windows registry entries):

.. code-block:: xml 

    <syscheck>
        <ignore>/etc/random-seed</ignore>
        <ignore>/root/dir</ignore>
        <ignore type="sregex">.log$|.tmp</ignore>
    </syscheck>

The ``type`` attribute can be set to sregex to specify a :ref:`regex` in the ignore option.

.. code-block:: xml

    <syscheck>
        <ignore type="sregex">^/opt/application/log</ignore>
    </syscheck>

A local rule can be used to modify the severity for changes to specific files or directories:

.. code-block:: xml 

    <rule id="100345" level="12">
        <if_matched_group>syscheck</if_matched_group>
        <match>/var/www/htdocs</match>
        <description>Changes to /var/www/htdocs - Critical file!</description>
    </rule>

In the above example, a rule was created to alert with high severity (12) for changes to the files in the htdocs directory.

Real time Monitoring
--------------------

OSSEC supports realtime (continuous) file integrity monitoring on Linux (support was added kernel version 2.6.13) and Windows systems.

The configuration is very simple. In the ``<directories>`` option where you specify what directories to monitor, adding ``realtime="yes"`` will enable it.
For example:

.. code-block:: xml 

    <syscheck>
        <directories realtime="yes" check_all="yes">/etc,/usr/bin,/usr/sbin</directories>
        <directories check_all="yes">/bin,/sbin</directories>
    </syscheck>

In this case, the directories /etc, /usr/bin and /usr/sbin will be monitored in real time. The same applies to Windows too.

.. warning:: 

    The real time monitoring will not start immediately. First ossec-syscheckd needs to scan the file system and add each sub-directory to the realtime queue.
    It can take a while for this to finish (wait for the log "ossec-syscheckd: INFO: Starting real time file monitoring" ).

.. note:: 

    Real time only works with directories, not individual files. So you can monitor the /etc 
    or C:\\program files directory, but not an individual file like /etc/file.txt.

.. note:: 

    Both rootcheck and syscheck runs on the same thread, so when rootcheck is running, the inotify events would get queued until it finishes.


Report Changes
--------------

OSSEC supports sending diffs when changes are made to text files on Linux and unix systems.

Configuring syscheck to show diffs is simple, add ``report_changes="yes"`` to the ``<directories`` option.

For example:

.. code-block:: xml

    <syscheck>
        <directories report_changes="yes" check_all="yes">/etc</directories>
        <directories check_all="yes">/bin,/sbin</directories>
    </syscheck>

.. notes::

    Report Changes will only work with text files, and the changes are stored on the agent 
    inside ``/var/ossec/queue/diff/local/dir/file``.

.. include:: ../../faq/syscheck.rst
