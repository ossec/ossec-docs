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


