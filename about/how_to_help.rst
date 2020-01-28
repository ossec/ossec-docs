How to start helping with the project?
--------------------------------------

OSSEC is maintained by a small group of people from around the world. If you wish to
get involved, there are multiple ways to do so.


Testing OSSEC:
^^^^^^^^^^^^^^

The easiest way of getting involved with OSSEC is by helping testing it.


Translating OSSEC:
^^^^^^^^^^^^^^^^^^

.. warning:

   Translations have not been worked on for a long time.
   They are most likely out of date, and possibly incorrect at this point in time.

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

If you want to support a new language, just copy the English one to your country code and start translating:

.. code-block:: console

   $ cp -pr en br
   $ vim br/messages.txt

Documenting OSSEC:
^^^^^^^^^^^^^^^^^^

The OSSEC documentation is hosted in the `ossec-docs <https://github.com/ossec/ossec-docs>`_ github repository.
Issues and pull requests can be submitted on the site.
Emails containing details of issues can also be sent to the `ossec-list <https://groups.google.com/forum/#!forum/ossec-list>`_ google group.


Development of OSSEC:
^^^^^^^^^^^^^^^^^^^^^

The OSSEC code is hosted in the `ossec-hids <https://github.com/ossec/ossec-hids>`_ github repository.
Issues and pull requests can be submited on the site.

Contributing to the development of OSSEC's code base will most likely require knwoledge of **C**,
and will take time learning how the internals work.

