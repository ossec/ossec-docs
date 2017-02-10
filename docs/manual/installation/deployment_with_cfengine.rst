Intergration and Deployment with cfengine
-----------------------------------------

I recently required a larger deployment of OSSEC-HIDS without too much manual intervention.  Almost every OSSEC-HIDS tutorial I've across says this is possible, yet I was unable to find a tutorial demonstrating it.   So, in the spirit of open source, I'm contributing a brief overview.

Prerequisites:
^^^^^^^^^^^^^^

In order to facilitate the key request, I chose to generate a file with the relevant information and copy it back to my cfmaster server.  I developed the following tutorial to demonstrate a cfengine copy back scenario: `Copy Back with cfengine <http://divisionbyzero.net/blog/2007/05/03/copy-back-with-cfengine/>`_.

Configuring the cfengine clients:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

I added a group to my ``cfagent.conf`` for my ossec server named: ``hg_ossec_server`` (host group). I then created an ``ossec-hids.cf`` containing the following:

* control

My control sections sets up the variables I'll be using in the rest of the file.

.. code-block:: console

  control:
    any::
      ossec_key_dir = (/usr/local/cfkeys/ossec)
      ossec_req_dir = ( $(util_updir)/ossec )

* package

I'm using yum to automatically install OSSEC-HIDS from my local RPM Repository.

.. code-block:: console

  packages:
    !hg_ossec_server::
        ossec-hids                  action=install
        ossec-hids-client           action=install

* links

The Links section just links ossec-agent.conf to ossec.conf on the clients.

.. code-block:: console

  links:
    !hg_ossec_server::
      /var/ossec/etc/ossec.conf -> /var/ossec/etc/ossec-agent.conf

* copy

I manage the ``ossec-agent.conf`` in cfengine, because my cfengine configurations are all stored in a subversion repository.  The first stanza in copy just pushes the most recent copy of the ``ossec-agent.conf`` file to my network, setting the dynamic class ``dc_restart_ossec`` if the copy occurs.

.. code-block:: console

  copy:
    !hg_ossec_server::
        $(distribute)/ossec-agent.conf      dest=/var/ossec/etc/ossec-agent.conf
                                            server=$(policyhost)
                                            mode=640
                                            group=ossec
                                            type=sum
                                            define=dc_restart_ossec

This second stanza in the ``copy`` section copies a file from our ossec key directory to the client.keys file on the client.  This copy only happens if the two files are different.  It also sets ``dc_restart_ossec`` if the copy occurs.

.. code-block:: console

        $(ossec_key_dir)/$(host).ossec    dest=/var/ossec/etc/client.keys
                                          server=$(policyhost)
                                          mode=640
                                          group=ossec
                                          type=sum
                                          define=dc_restart_ossec
* processes

My processes block checks to ensure that OSSEC-HIDS is running the correct daemons.

.. code-block:: console

  processes:
    !hg_ossec_server::
        "ossec-agentd" elsedefine=dc_restart_ossec
    ``hg_ossec_server``::
        "ossec-remoted" elsedefine=dc_restart_ossec

* shellcommands

This section is where the certificate request occurs through some devious mechanisms I designed for no other reason than to amuse myself.  Hopefully, it amuses others as well.  The first thing it does is issue a command that echo's the client eth0 ipv4 address to a file named ''host.ossec'' in the ossec request directory I defined.   The ``hg_ossec_server`` class will use this to generate a cert to place in the aforementioned copy block.

.. code-block:: console

  shellcommands:
    !hg_ossec_server::
        "/usr/bin/ssh util@$(policyhost) -i $(util_privkey) 'echo $(global.ipv4[eth0]) > $(ossec_req_dir)/$(host).ossec'"

The last statement checks to see if anyone defined ``dc_restart_ossec``, and restart ossec-hids if it was defined.

.. code-block:: console

    dc_restart_ossec::
        "/sbin/service ossec-hids restart"

Ok, so who cares?
^^^^^^^^^^^^^^^^^

Well, now, our clients are setup to install, configure, and run OSSEC-HIDS as well as issuing a request for their certificate.  However, the certificate directory on the server is empty and so none of them will actually run.  This is a problem.

Configuring the OSSEC Server w/cfengine
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The cfengine part of this was a pain for me because of the order of the actions I had defined and the extent of work I had done incorrectly in the past.  I could have figured out an interesting way to handle this, but I didn't want to scrap my entire cfengine config and start from scratch.  So I created a perl script that allowed me to use the ``manage_agents`` script without interaction.  It does require the ``Expect.pm`` & ``Regexp::Common`` from CPAN, but is otherwise stock Perl 5.8.x.  I also wrote a shell script wrapper to handle running the perl script and culminating the results.  I saved these two scripts in ``/root/security``, so if you put them elsewhere, make sure to update the shell script wrapper.

The scripts for managing keys can be downloaded `here <http://db0.us/~brad/cfengine-ossec-scripts.tar.gz>`_

The cfengine bit was really simple, it just had to call my wrapper shell script and set the class.  I did this with a control block:

.. code-block:: console

  control:
   hg_ossec_server::
     AddClasses = ( ExecResult(/root/security/ossec-scan.sh) )

The combination of the two scripts and this one line in the cfengine configuration handle creating, removing, and exporting the keys, as well as configuring the ``dc_restart_ossec`` class if there have been changes.


