.. _checkpoint_config::

Configuring Checkpoint
----------------------


Run this command:
^^^^^^^^^^^^^^^^^

.. code-block:: console

  # fw log -ftnp fw.log | logger -t Checkpoint


Explanation:
^^^^^^^^^^^^

.. code-block:: console

  - fw log :
    -f select current log file
    -t tail file
    -n use ip instead of name
    -p use port number instead of name


Do not use the following options in fw log:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

  -
  -l add date before timestamp
  -  Use of -l changes log format slightly
  -
  -g without : and ; delimiters
  -  Use of -g significantly changes log format
  -  this decoder is incompatible with -g


