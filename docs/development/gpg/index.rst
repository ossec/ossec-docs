.. _gpg_keys:

OSSEC PGP/GPG keys
==================

Release tarballs for OSSEC HIDS are signed with a GPG key. Use these pages for
maintainer public keys and verification steps.

Verify a release tarball
------------------------

1. Download the tarball and detached ``.asc`` signature from
   `GitHub Releases <https://github.com/ossec/ossec-hids/releases>`_ or
   `ossec.net <https://www.ossec.net/download-ossec/>`_.

2. Import the signing key (prefer the file from ossec.net over keyservers):

   .. code-block:: console

      curl -O https://www.ossec.net/files/OSSEC-ARCHIVE-KEY.asc
      gpg --import OSSEC-ARCHIVE-KEY.asc

3. Verify (replace ``VERSION`` with the release tag, for example ``4.1.0``):

   .. code-block:: console

      gpg --verify ossec-hids-VERSION.tar.gz.asc ossec-hids-VERSION.tar.gz

   A good signature shows ``Good signature`` from ``Scott R. Shinn
   <scott@atomicorp.com>``. A warning that the key is not ultimately trusted
   is normal until you assign local trust with ``gpg --edit-key``.

Current release signing key fingerprint:

.. code-block:: console

   B50F B194 7A0A E311 45D0  5FAD EE1B 0E6B 2D83 87B7

Installation instructions with verification examples are in :ref:`install_source`.
See also :ref:`faq_gpg_verify` if ``gpg --recv-key`` fails.

Maintainer keys
---------------

.. toctree::
   :maxdepth: 1
   :glob:

   keys/*
