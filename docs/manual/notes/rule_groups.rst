Rule Groups
-----------

We can specify groups for specific rules. It's used for active response reasons and for correlation.


We currently use the following groups:


Reconnaissance
^^^^^^^^^^^^^^

* Connection Attempt - connection_attempt
* Web scan - web_scan
* Generic scan - recon


Authentication Control
^^^^^^^^^^^^^^^^^^^^^^

* Success - authentication_success
* Failure - authentication_failed
* Invalid - invalid_login
* Login denied - login_denied
* Multiple failures - authentication_failures
* User account added/changed/removed - adduser|account_changed


Attack/Misuse
^^^^^^^^^^^^^

* Worm (Non targeted attack) - automatic_attack
* Exploit pattern - exploit_attempt
* Invalid access - invalid_access
* Spam - spam
* Multiple Spams - multiple_spam
* SQL Injection - sql_injection
* Generic Attack - attack
* Rootkit detection - rootcheck
* Virus detected - virus


Access Control
^^^^^^^^^^^^^^

* Access denied - access_denied
* Access allowed -access_allowed
* Access to Inexistent resource - unknown_resource
* Firewall Drop - firewall_drop
* Multiple firewall drops - multiple_drops
* Client mis-configuration - client_misconfig
* Client error - client_error


Network Control
^^^^^^^^^^^^^^^

* New host detected - new_host
* Possible ARP spoof - ip_spoof


System Monitor
^^^^^^^^^^^^^^

* Service start - service_start
* Service availability in Risk - service_availability
* System error - system_error
* Shutdown - system_shutdown
* Logs removed - logs_cleared
* Invalid request  - invalid_request
* Promiscuous mode detected - promisc
* Policy changed - policy_changed
* Configuration changed - config_changed
* Integrity Checking - syscheck
* Low disk space - low_diskspace
* Time changed - time_changed


Policy Violation
^^^^^^^^^^^^^^^^

* Login time - login_time
* Login day  - login_day


