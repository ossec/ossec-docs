.. _faq_ossec:

OSSEC: FAQ
-------------

.. contents:: 
    :local:


Can ossec logs be saved to a different directory?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  As a protection mechanism, OSSEC chroots most of its processes to the install directory (typically /var/ossec). 
  Due to this chroot, logs must be saved to a location under /var/ossec.
  OSSEC does rotate its logs, but will not be able to move them from /var/ossec.

  Be sure to allocate enough space to /var/ossec.


