.. _manual-install-package:


Package Installation
====================

The OSSEC project has made RPM and deb packages available.
Links to the packages can be found on the OSSEC `download page <http://www.ossec.net/?page_id=19>`_

RPM Installation
----------------

OSSEC's RPMs are made available by `AtomiCorp <http://www.atomicorp.com>`_.

The RPMs can be installed by adding the AtomiCorp yum repository:

.. code-block:: console

   # wget -q -O - https://updates.atomicorp.com/installers/atomic | sh 

Next use ``yum`` to install the specific packages. For an OSSEC server run:

.. code-block:: console

   # yum install ossec-hids ossec-hids-server

And for an agent run:

.. code-block:: console

   # yum install ossec-hids ossec-hids-agent


Deb Installation
----------------

OSSEC's deb packages are available in the Wazuh repository.

Install the apt-get repository key:

.. code-block:: console
    
    # apt-key adv --fetch-keys http://ossec.wazuh.com/repos/apt/conf/ossec-key.gpg.key

Add the repository for Debian (available distributions are Sid, Jessie and Wheezy):

.. code-block:: console

    # echo 'deb http://ossec.wazuh.com/repos/apt/debian wheezy main' >> /etc/apt/sources.list

Or add the repository for Ubuntu (available distributions are Precise, Trusty and Utopic):

.. code-block:: console

    # echo 'deb http://ossec.wazuh.com/repos/apt/ubuntu precise main' >> /etc/apt/sources.list

Update the repository:
 
.. code-block::console

    # apt-get update

Install OSSEC HIDS server/manager:

.. code-block:: console

    # apt-get install ossec-hids

Or install OSSEC HIDS agent:

.. code-block:: console

    # apt-get install ossec-hids-agent

pkg Installation
----------------

Some of the BSD operating systems offer OSSEC packages you can use. Here you have FreeBSD as example.

* **FreeBSD**

You are going to work together with ``pkg`` here. Just choose which type of setup you need
(agent, local monitoring, or server/manager) and install the respective OSSEC package.

Should you opt to install an OSSEC Server/Manager:

.. code-block:: console

   # pkg install ossec-hids-server

