Log Samples from S.M.A.R.T
--------------------------

smartd example:
^^^^^^^^^^^^^^^

.. code-block:: console

  Jun 16 18:34:31 Lab8 smartd[2842]: Device: /dev/sda [SAT], SMART Usage Attribute: 194 Temperature_Celsius changed from 106 to 105
  Jun 16 18:54:31 Lab8 -- MARK --
  Jun 16 19:04:31 Lab8 smartd[2842]: Device: /dev/sda [SAT], SMART Prefailure Attribute: 7 Seek_Error_Rate changed from 200 to 100
  Jun 16 12:32:40 Lab9 smartd[2881]: Configuration file /etc/smartd.conf was parsed, found DEVICESCAN, scanning devices
  Jun 16 12:32:40 Lab9 smartd[2881]: Device: /dev/sda, type changed from 'scsi' to 'sat'
  Jun 16 12:32:40 Lab9 smartd[2881]: Device: /dev/sda [SAT], opened
  Jun 16 12:32:40 Lab9 smartd[2881]: Device: /dev/sda [SAT], found in smartd database.
  Jun 16 12:32:40 Lab9 smartd[2881]: Device: /dev/sda [SAT], is SMART capable. Adding to "monitor" list.
  Jun 16 12:32:40 Lab9 smartd[2881]: Device: /dev/sda [SAT], state read from /var/lib/smartmontools/smartd.ST3500620AS-5QM2644Q.ata.state
  Jun 16 12:32:40 Lab9 smartd[2881]: Monitoring 1 ATA and 0 SCSI devices
  Jun 16 12:32:40 Lab9 smartd[2881]: Device: /dev/sda [SAT], 1 Currently unreadable (pending) sectors
  Jun 16 12:32:40 Lab9 smartd[2881]: Device: /dev/sda [SAT], 1 Offline uncorrectable sectors
  Jun 16 12:32:40 Lab9 smartd[2881]: Device: /dev/sda [SAT], SMART Prefailure Attribute: 1 Raw_Read_Error_Rate changed from 106 to 111
  Jun 16 12:32:40 Lab9 smartd[2881]: Device: /dev/sda [SAT], SMART Usage Attribute: 190 Airflow_Temperature_Cel changed from 72 to 69
  Jun 16 12:32:40 Lab9 smartd[2881]: Device: /dev/sda [SAT], SMART Usage Attribute: 194 Temperature_Celsius changed from 28 to 31
  Jun 16 12:32:40 Lab9 smartd[2881]: Device: /dev/sda [SAT], SMART Usage Attribute: 195 Hardware_ECC_Recovered changed from 45 to 42
  Jun 16 12:32:40 Lab9 smartd[2881]: Device: /dev/sda [SAT], state written to /var/lib/smartmontools/smartd.ST3500620AS-5QM2644Q.ata.state
  Jun 16 12:32:40 Lab9 smartd[2987]: smartd has fork()ed into background mode. New PID=2987.



