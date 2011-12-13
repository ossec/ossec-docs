Log Samples from HP-UX
----------------------

File system full:
^^^^^^^^^^^^^^^^^

.. code-block:: console

  Sep  3 10:18:11 sys2 vmunix: msgcnt 1 vxfs: mesg 001: vx_nospace - /dev/vg00/lvol3 file system full (1 block extent)
  Sep  3 10:18:52 sys2 vmunix: msgcnt 3 vxfs: mesg 001: vx_nospace - /dev/vg00/lvol3 file system full (1 block extent)
  Sep  3 10:18:37 sys2 vmunix: msgcnt 5 vxfs: mesg 001: vx_nospace - /dev/vg00/lvol3 file system full (1 block extent)
  Sep  3 10:19:13 sys2 vmunix: msgcnt 7 vxfs: mesg 001: vx_nospace - /dev/vg00/lvol3 file system full (1 block extent)


EMS logs:
^^^^^^^^^

.. code-block:: console

  Jul 19 15:53:01 lime EMS [6259]: ------ EMS Event Notification ------ Value: "CRITICAL (5)" for Resource: "/system/events/ipmi_fpl/ipmi_fpl" (Threshold:  >= " 3")    Execute the following command to obtain event details:   /opt/resmon/bin/resdata -R 410189826 -r /system/events/ipmi_fpl/ipmi_fpl -n 410189825 -a

  Jul 19 15:58:03 lime EMS [6259]: ------ EMS Event Notification ------ Value: "MAJORWARNING (3)" for Resource: "/system/events/ipmi_fpl/ipmi_fpl" (Threshold:  >= " 3")    Execute the following command to obtain event details:   /opt/resmon/bin/resdata -R 410189826 -r /system/events/ipmi_fpl/ipmi_fpl -n 410189827 -a

  Aug 24 11:54:12 grape2 vmunix: SCSI: Resetting SCSI -- lbolt: 27505, bus: 18 path: 1/0/0/3/1
  Aug 24 11:54:12 grape2 vmunix: SCSI: Reset detected -- lbolt: 27505, bus: 18 path: 1/0/0/3/1
  Aug 24 11:54:12 grape2 vmunix: SCSI: Parity error -- lbolt: 27806, dev: cb121002
  Aug 24 11:54:12 grape2 vmunix:          lbolt_at_timeout: 0, lbolt_at_start: 0

