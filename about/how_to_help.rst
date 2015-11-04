How to start helping with the project?
--------------------------------------

OSSEC is maintained by a small group of people from around the world. If you wish to
get involved, there are multiple ways to do so. Check out our list of active contributors:
`ossec team <http://www.ossec.net/en/about.html#dev-team>`_.


Testing OSSEC:
^^^^^^^^^^^^^^

The easiest way of getting involved with OSSEC is by helping testing it. We always release 
beta versions and we need a good quality control on every supported version before publicly
releasing it.


Translating OSSEC:
^^^^^^^^^^^^^^^^^^

Translating OSSEC is easy. We already support many languages, but new ones are more than welcome and fixes
for the ones we have already too.

After you download OSSEC and untar/ungzip it, you will find the messages to be translated inside the etc/templates 
directory:

.. code-block:: console

    $ ls -la etc/templates/
    br
    cn
    en
    ..
    tr


Inside each directory you will find a messages.txt and language.txt file and a messages/ and errors/ directory. If you are fixing one of the languages we already have, just modify them and send the changes to us.

If you want to support a new language, just copy the English one to your contry code and start translating:

.. code-block:: console

   $ cp -pr en br
   $ vim br/messages.txt

Documenting OSSEC:
^^^^^^^^^^^^^^^^^^

Development of the OSSEC web ui:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Requires HTML/PHP knowledge.


Development of OSSEC:
^^^^^^^^^^^^^^^^^^^^^

The last way to get involved is by actually helping with the development of ossec. You must
know **C** and be willing to take some time (actually quite some time) to understand how 
the internals work.

