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

OSSEC's DEB packages are made available by `Atomicorp <http://www.atomicorp.com>`_.

Run the Repo installer:

.. code-block:: console
    
    # wget -q -O - https://updates.atomicorp.com/installers/atomic | sudo bash

Update the repository:
 
.. code-block::console

    # apt-get update

Install OSSEC HIDS server/manager:

.. code-block:: console

    # apt-get install ossec-hids-server

Or install OSSEC HIDS agent:

.. code-block:: console

    # apt-get install ossec-hids-agent

pkg Installation
----------------

Some of the BSD operating systems offer OSSEC packages you can use. Here you have
FreeBSD and OpenBSD as example.

* **FreeBSD**

You are going to work together with ``pkg`` here. Just choose which type of setup you need
(agent, local monitoring, or server/manager) and install the respective OSSEC package.

Should you opt to install an OSSEC Server/Manager:

.. code-block:: console

   # pkg install ossec-hids-server

If you want to install an OSSEC Agent:

.. code-block:: console

   # pkg install ossec-hids-agent

.. note::

   These steps also work for **DragonFlyBSD**. It also uses ``pkg``, just like FreeBSD. You can
   read more about it `here <https://www.dragonflybsd.org/docs/howtos/HowToDPorts/>`_.

* **OpenBSD**

Here you must work with ``pkg_add`` instead of `pkg`, but no worries it's the same concept.

As it only offers one package, here is how to install OSSEC HIDS on OpenBSD:

.. code-block:: console

   # pkg_add ossec-hids

