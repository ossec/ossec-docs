
.. _manual_analysis::

Log monitoring/analysis 
======================= 

Log Analysis (or log inspection) is done inside OSSEC by the logcollector and 
analysisd processes. The first one collects the events and the second one 
analyzes (decodes, filters and classify) them.

It is done in real time, so as soon as an event is written, OSSEC will process 
them. OSSEC can read events from internal log files, from the Windows event 
log and also receive them directly via remote syslog.

What is log analysis?
---------------------

Inside OSSEC we call log analysis as LIDS (log-based intrusion detection). Our 
goal is to detect attacks, misuse or system errors using the logs.

LIDS - Log-based intrusion detection or security log analysis are the processes 
or techniques used to detect attacks on a specific network, system or application 
using logs as the primary source of information. It is also very useful to detect 
software misuse, policy violations and other forms of inappropriate activities.

Quick Facts
----------- 


- How often? 
  
  - In real time.

- Where are the events analyzed? 
  
  - In the manager.

- How long are they stored? 
  
  - For as long as your policy dictates (it is user configurable).
    
- Where it helps me with compliance? 
  
  - (PCI DSS, etc) It helps with the whole section 10 (log monitoring) of PCI.

- How much CPU it uses? 
  
  - On the agent, it uses very little CPU/memory since it just read the events. 
    On the manager, it depends on the number of EPS.

- How it deals with false positives? 
  
  - False positives can be eliminated using local rules.

Configuration Options 
---------------------

These options should be specified locally on each agent ossec.conf file. Inside 
the “localfile” element, you can have the following options. 

.. include:: ../syntax/ossec_config.localfile.rst 

Monitoring logs 
--------------- 

With in OSSEC their is two major methods for monitoring logs: file and process.  Each 
method has it's own page and examples. 

.. toctree::

    process-monitoring
    file-log-monitoring




