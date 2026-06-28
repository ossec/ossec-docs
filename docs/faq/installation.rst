.. _faq_install:

Installation: FAQ
-----------------


.. contents::
    :local:


.. _AIX:

Chown errors during installation on AIX:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block: console

   chown: ossec is an unknown username.

AIX does not accept ``/bin/false`` as a valid shell by default. It must be added to 
the SHELLS line in ``/etc/security/login.cfg`` before running ``install.sh``.


.. _windows:


The Windows GUI is asking me for a key, where do I get it?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Windows version of OSSEC is agent only, it cannot work without a server. 
The key can be obtained from the server using `manage_agents`.


.. _faq_gpg_verify:

How do I verify the release tarball GPG signature?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Tarballs from `https://www.ossec.net/download-ossec/ <https://www.ossec.net/download-ossec/>`_
and `GitHub Releases <https://github.com/ossec/ossec-hids/releases>`_ ship with a detached
``.asc`` signature file. Import the public key published at
`https://www.ossec.net/files/OSSEC-ARCHIVE-KEY.asc <https://www.ossec.net/files/OSSEC-ARCHIVE-KEY.asc>`_,
then run ``gpg --verify`` on the tarball before installing.

Full step-by-step commands are in :ref:`install_source` under "Verify the tarball signature".

