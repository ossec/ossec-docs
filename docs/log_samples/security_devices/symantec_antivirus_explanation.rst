
symantec antivirus explanation
==============================

Explanation of Symantec Antivirus Corporate Edition Windows Event log entries

Symantec Antivirus Corporate Edition 8.x writes data to the Windows NT/2000 application event logs. These entries have Category and Event IDs.

The total number of categories is four. Each category corresponds to a different component of Symantec Antivirus and the category number indicates where the application event originated from. These are shown below:

.. code-block:: console

  Category number        Where the event is from

  1                From Quarantine/Q -Server
  2                NAV services
  3                Automatic Update/Virus Definitions
  4                Any change to a server's configuration

The 24 different event actions, along with their event numbers and severity levels, are shown below

.. code-block:: console

  Event number            Severity of event        What occurred
  1                       Warning                  An on-screen alert was sent.
  2                       Informational            A virus scan completed.
  3                       Informational            A virus scan was started.
  4                       Informational            Virus definitions have been updated.
  5                       Warning                  An infected file has been found.
  6                       Warning                  Error in opening a certain file.
  7                       Informational            Loading virus definitions.
  11                      Error                    Error in sending/receiving SNMP trap.
  12                      Informational            A configuration change has occurred.
  13                      Informational            Shut down of NAV services.
  14                      Informational            Start up of NAV services.
  16                      Informational            Downloading of definition update.
  18                      Informational            File sent to Q-Server.
  19                      Informational            Scan and Deliver.
  20                      Error                    Back up of sample.
  21                      Error                    Virus scan aborted.
  22                      Error                    Error in loading RTS service.
  23                      Informational            Services Loaded
  24                      Informational            Services Unloaded
  25                      Informational            Client Removed from Parent Server
  26                      Informational            Scan Delayed (pause/snooze occurred)
  27                      Informational            Scan Restarted
  28                      Informational            Client Roamed to new parent server
  29                      Informational            Client Roamed from parent server


Here are some examples to show how the above information can be put together to define the application event that has occurred.

.. code-block:: console

  Category number       Event number    What occurred
  4                     12              Configuration change
  2                     21              Scan canceled
  2                     6               Cannot open file to scan
  2                     3               Scan stopped
  2                     14              NAV service start up successful
  1                     5               An infected file has been found and quarantined
  3                     4               Virus definitions have been updated


Information taken from Symantec Support Document ID: 2002110112213648

