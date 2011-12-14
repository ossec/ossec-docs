How do I use or create my own compiled rules?
---------------------------------------------


*By `Daniel Cid <http://www.ossec.net/dcid/>`_*



Compiled rules are an extension to the *normal* (default) XML rules and should only be used when you
need additional functionality not present in there.


How do they work?
^^^^^^^^^^^^^^^^^

Inside the OSSEC package you will find the directory ``src/analysisd/compiled_rules/`` , with the
default compiled rules. To see a list of rules, run the command (inside that directory):


.. code-block:: console

   $ ``pwd``
   ../src/analysisd/compiled_rules
   $ ``./register_rule.sh list``
   *Available functions: 
   check_id_size
   comp_mswin_targetuser_calleruser_diff
   comp_srcuser_dstuser


To use any of them inside a rule, just add the <compiled_rule> tag with the function you want
to use. Ex:

.. code-block:: console

  <rule id="100155" level="10">
    <if_sid>18111</if_sid>
    ``<compiled_rule>comp_mswin_targetuser_calleruser_diff</compiled_rule>``
    <description>User changed someone else password.</description>
  </rule>

.. note:

  To know what each function does you have to look at the source code.


How to write my own rule:
^^^^^^^^^^^^^^^^^^^^^^^^^


To create your own rule, first open a new **.c** file (don't use the generic one, since it is modified during
upgrades).

.. code-block:: console

   $ touch myownrules.c

And create your function inside of it. In this example here we added a function to check if the url field
is longer than 1024:

.. code-block:: console

  void *myosrule_check_url_size1024(Eventinfo *lf)
  {
      if(!lf->url)
      {
          return(NULL);
      }

      if(strlen(lf->url) >= 1024)
      {
          return(lf);
      }
      return(NULL);
  }


.. note:

   You must return 'lf' (the eventinfo structure) if the function matches or NULL otherwise.

.. note:

   Give a good name to your function in a way to make sure it is not used anywhere else (eg: put your company name in it).


After that, register your function:

.. code-block:: console

   $ ./register_rule.sh add myosrule_check_url_size1024

You can also save it (if you have ossec installed) so that during the next upgrade it will reuse them:

.. code-block:: console

   $ ./register_rule.sh save
   *Save completed at /var/ossec/compiled_rules/



Available fields in the Event structure:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: consol

  typedef struct _Eventinfo
  {
      /* Extracted from the event */
      char *log;
      char *full_log;
      char *location;
      char *hostname;
      char *program_name;


      /* Extracted from the decoders */
      char *srcip;
      char *dstip;
      char *srcport;
      char *dstport;
      char *protocol;
      char *action;
      char *srcuser;
      char *dstuser;
      char *id;
      char *status;
      char *command;
      char *url;
      char *data;
      char *systemname;


      /* Pointer to the rule that generated it */
      RuleInfo *generated_rule;

      /* Pointer to the decoder that matched */
      OSDecoderInfo *decoder_info;
    
      ..
  }Eventinfo;




