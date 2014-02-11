OSSEC Updates
=============

Updating OSSEC is as easy as it can get. Just download the latest package and follow
the installation instructions as usual. It will detect that you already have it
installed and ask:

.. code-block:: console

    - You already have OSSEC installed. Do you want to update it? (y/n): y


Just answer ``yes`` to this question and the script will update the OSSEC binaries. 
``local_rules.xml`` and ``local_decoder.xml`` will not be modified during this upgrade.

The script will also prompt for an answer to the following question:

.. code-block:: console

   - Do you want to update the rules? (y/n): y

Answering ``yes`` to this question updates the ``<rules>`` section of the system's ossec.conf.
