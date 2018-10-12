.. _cookbooks_recpies_elasticstack:

Using filebeat, logstash, and elasticsearch:
============================================

Enable json alert output in ossec.conf:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: xml

   <global>
     <jsonout_output>yes</jsonout_output>
   </global>

Configure filebeat to read alerts.json in filebeat.yml:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

   - input_type: log
   paths:
     - /var/ossec/logs/alerts/alerts.json

   json.keys_under_root: true
   fields: {log_type: osseclogs}

Configure logstash:
^^^^^^^^^^^^^^^^^^^

.. code-block:: console

   input {
     beats {
       id => "beats_test"
       port => 9001
       type => "ossec"
     }
   }

   filter {
     if([fields][log_type] == "osseclogs") {
       mutate {
         replace => {
           "[type]" => "osseclogs"
         }
       }
     }
   }

   output {

     if([type] == "osseclogs") {
       elasticsearch {
         index => "ossec-%{+YYYY.MM.dd}"
       }
     }
   }

