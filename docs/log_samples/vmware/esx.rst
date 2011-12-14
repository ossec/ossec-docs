Log Samples for VMware ESX
--------------------------

From /var/log/vmware/hostd.log:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console
  [2008-07-17 23:57:30.128 'FirewallSystem' 3076445088 error] Failed to update service ntpd: vim.fault.PlatformConfigFault
  [2008-07-26 10:09:56.601 'vm:/vmfs/volumes/485a72e0-dd49e4f1-796c-001517761286/Nostalgia/Nostalgia.vmx' 123898800 info] State Transition (VM_STATE_RECONFIGURING -> VM_STATE_OFF)
  [2008-07-26 10:09:59.506 'vm:/vmfs/volumes/485a72e0-dd49e4f1-796c-001517761286/Nostalgia/Nostalgia.vmx' 68991920 info] State Transition (VM_STATE_OFF -> VM_STATE_POWERING_ON)
  [2008-07-26 10:10:07.305 'vm:/vmfs/volumes/485a72e0-dd49e4f1-796c-001517761286/Nostalgia/Nostalgia.vmx' 102202288 info] State Transition (VM_STATE_POWERING_ON -> VM_STATE_ON)
  [2008-07-26 10:18:31.491 'vm:/vmfs/volumes/485a72e0-dd49e4f1-796c-001517761286/Nostalgia/Nostalgia.vmx' 21621680 info] State Transition (VM_STATE_RECONFIGURING -> VM_STATE_OFF)
  [2008-07-26 10:18:30.574 'vm:/vmfs/volumes/485a72e0-dd49e4f1-796c-001517761286/Nostalgia/Nostalgia.vmx' 21621680 info] State Transition (VM_STATE_OFF -> VM_STATE_RECONFIGURING)
  [2008-03-09 22:43:35.924 'ha-eventmgr' 84503472 info] Event 2053 : User root@127.0.0.1 logged in
  [2008-02-05 02:13:18.112 'ha-eventmgr' 95833272 info] Event xyz : User m@1.2.3.4 logged in
  [2008-08-26 11:06:16.359 'ha-eventmgr' 20532144 info] Event 285 : Failed login attempt for root@127.0.0.1




From /var/log/secure (user logins, etc):
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console
  Aug 25 06:01:10 hostname vmware-hostd[1863]: Accepted password for user root from 127.0.0.1
  Aug  7 11:05:34 localhost vmware-authd[9709]: login from 172.16.129.78 as 523b717c-4542-f5fc-c006-1644eb8f4330
  Aug 26 11:42:29 localhost vmware-hostd[1863]: Rejected password for user blablabla from 127.0.0.1




