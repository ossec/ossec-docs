
.. _manual_analysis:

Log monitoring/analysis 
======================= 

Log Analysis (or log inspection) is done inside OSSEC by the logcollector and 
analysisd processes. The first one collects the events and the second one 
analyzes (decodes, filters and classifies) them.

It is done in real time, so as soon as an event is written OSSEC will process 
them. OSSEC can read events from internal log files, from the Windows event 
log and also receive them directly via remote syslog.

What is log analysis?
---------------------

Inside OSSEC we call log analysis a LIDS, or log-based intrusion detection. The 
goal is to detect attacks, misuse or system errors using the logs.

LIDS - Log-based intrusion detection or security log analysis are the processes 
or techniques used to detect attacks on a specific network, system or application 
using logs as the primary source of information. It is also very useful to detect 
software misuse, policy violations and other forms of inappropriate activities.

Quick Facts
----------- 

- How often are logs monitored? 
  
  - In real time.

- Where are the events analyzed? 
  
  - In the manager.

- How long are they stored? 
  
  - For as long as your policy dictates (it is user configurable).
    
- Where does this help me with compliance? 
  
  - (PCI DSS, etc) It helps with the whole section 10 (log monitoring) of PCI.

- How much CPU does it use? 
  
  - On the agent, it uses very little CPU/memory since it just read the events and forwards them to the manager.

  - On the manager, it depends on the number of events per second (EPS).

- How does it deal with false positives? 
  
  - False positives can be eliminated using local rules.

Configuration Options 
---------------------

These options should be specified locally in each agent's ossec.conf file or the 
share agent.conf. Inside the ``<localfile>`` element, you can have the following 
options. 

.. include:: ../../syntax/ossec_config.localfile.trst 

Monitoring logs 
--------------- 

With in OSSEC there are two major methods for monitoring logs: file and process.  Each 
method has its own page and examples. 

.. toctree::

    process-monitoring
    file-log-monitoring




