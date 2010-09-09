

.. _install:

Installation 
============

The best installation tutorial is available in the `OSSEC book`_ and the installation 
chapter is available for FREE in PDF at: `OSSEC Book - Chapter 2.pdf`__ 

.. _OSSEC book: http://www.amazon.com/OSSEC-Host-Based-Intrusion-Detection-Guide/dp/159749240X
.. _OSSEC Book install: http://ossec.net/ossec-docs/OSSEC-book-Ch02_SA240.pdf

__ OSSEC Book install_


OSSEC HIDS Manager/Agent Installation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Installation of the OSSEC HIDS is very simple. Just follow these few steps to have 
it working.  Please make sure that you understand the type of installation you are choosing 
(manager, agent, local, etc) and are also aware of the order (always install the manager 
first). If you don’t know what I’m talking about, it’s a good idea to visit the `install types
page`.

.. warning::

    Remember that when following this installation the commands only start after the # Everything 
    before that is just the information about the prompt

.. note::
   
    If you have experience with Unix, just download the latest version, uncompress it and run the 
    "./install.sh" script.

.. note:: 

    If you want a step by step guide, you can use one of the many step by step install guides
    from `here`_

#. Download the latest version and verify it's checksum.

    .. note:: 

        On some systems, the command md5, sha1 or wget may not exist, so try md5sum, sha1sum 
        or lynx respectively instead.

    .. code-block:: console

        # wget http://www.ossec.net/files/ossec-hids-latest.tar.gz
        # wget http://www.ossec.net/files/ossec-hids-latest_sum.txt
        # cat ossec-hids-latest_sum.txt
        MD5 (ossec-hids-latest.tar.gz) = XXXXXXX
        SHA1 (ossec-hids-latest.tar.gz) = YYYYYYYY
        # md5 ossec-hids-latest.tar.gz
        MD5 (ossec-hids-latest.tar.gz) = XXXXXXX
        # sha1 ossec-hids-latest.tar.gz
        SHA1 (ossec-hids-latest.tar.gz) = YYYYYYYY


#. Extract the compressed package and run the “./install.sh” script (It will guide you 
   through the installation).

    .. code-block:: console 

        # tar -zxvf ossec-hids-*.tar.gz (or gunzip -d; tar -xvf)
        # cd ossec-hids-* 
        # ./install.sh

#. Remember to open the port 1514 (UDP) if there is a firewall between the server and 
   the agents (if you didn’t choose the local installation).

#. In case you are installing the server or the agent, remember to follow the `Managing 
   the agents section`.

#. Start OSSEC HIDS 

    .. code-block:: console 

        # /var/ossec/bin/ossec-control start  

OSSEC HIDS Windows agent Installation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Windows agent installation has its own page at: :ref:`manual-win-install`. 

OSSEC HIDS agentless Installation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Agentless installation has its own page at: :ref:`manual-agentless`.

OSSEC HIDS Binary installation 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 

On systems that do not have a C compiler or one is not allowed by policy 
installation can be done using :ref:`manual-install-binary`

OSSEC Updates
~~~~~~~~~~~~~

Updating OSSEC is as easy as it can get. Just download the latest package and follow 
the installation instructions as usual. It will detect that you already have it 
installed and ask:

.. code-block:: console
 
    - You already have OSSEC installed. Do you want to update it? (y/n): y
    - Do you want to update the rules? (y/n): y

Just say “yes” to these questions and it will update everything properly. Your local rules 
and configuration options will not be modified. The same applies to the Unix or Windows 
agent updates.

External installation documents
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


