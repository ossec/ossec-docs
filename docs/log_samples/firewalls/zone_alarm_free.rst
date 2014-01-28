Zone Alarm (free version) Log samples
-------------------------------------

Details about Zone Alarm and it's logging features (including text log field descriptions) can be found in the [http://download.zonelabs.com/bin/media/pdf/zaclient65_user_manual.pdf ZoneAlarm manual]

The logfile can be tab, comma, or semi-colon delimited (user can make the choice).

Logfile located (on Windows XP) in C:\WINDOWS\Internet Logs

Filename = ZALog.txt:
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

  ZoneAlarm Logging Client v6.5.737.000
  Windows XP-5.1.2600-Service Pack 2-SMP
  type,date,time,source,destination,transport (Security)
  type,date,time,virus name,file name,mode,e-mail id (Anti-Virus)
  type,date,time,source,destination,action,service (IM Security)
  type,date,time,source,destination,program,action (Malicious Code Protection)
  type,date,time,action,product,file,event,subevent,class,data,data,... (OSFirewall)
  type,date,time,name,type,mode (Anti-Spyware)
  PE,2006/11/15,14:57:36 -5:00 GMT,tcsd_win32.exe,C:\Program Files\NTRU Cryptosystems\NTRU Hybrid TSS v2.0.7\bin\tcsd_win32.exe,0.0.0.0:10001,N/A
  PE,2006/11/15,14:57:36 -5:00 GMT,Systems Management Server,C:\WINDOWS\system32\CCM\clicomp\RemCtrl\Wuser32.exe,192.168.100.195:53,N/A
  ACCESS,2006/11/15,14:57:42 -5:00 GMT,Systems Management Server was temporarily blocked from connecting to the Internet (192.168.100.195:DNS).,N/A,N/A
  ACCESS,2006/11/15,14:57:58 -5:00 GMT,Generic Host Process for Win32 Services was blocked from accepting a connection from the Internet (10.69.0.138:Port 1900).,N/A,N/A
  PE,2006/11/15,14:58:30 -5:00 GMT,CCM Executive,C:\WINDOWS\system32\CCM\CcmExec.exe,192.168.100.18:80,N/A
  ACCESS,2006/11/15,14:58:36 -5:00 GMT,CCM Executive was temporarily blocked from connecting to the Internet (192.168.100.18:HTTP).,N/A,N/A
  ACCESS,2006/11/15,14:59:30 -5:00 GMT,Generic Host Process for Win32 Services was blocked from accepting a connection from the Internet (10.69.0.138:Port 2110).,N/A,N/A
  ACCESS,2006/11/15,14:59:30 -5:00 GMT,Generic Host Process for Win32 Services was blocked from accepting a connection from the Internet (10.69.0.138:Port 2111).,N/A,N/A
  ACCESS,2006/11/15,14:59:30 -5:00 GMT,Generic Host Process for Win32 Services was blocked from accepting a connection from the Internet (10.69.0.138:Port 2112).,N/A,N/A
  ACCESS,2006/11/15,14:59:30 -5:00 GMT,Generic Host Process for Win32 Services was blocked from accepting a connection from the Internet (10.69.0.138:Port 2113).,N/A,N/A
  ACCESS,2006/11/15,14:59:30 -5:00 GMT,Generic Host Process for Win32 Services was blocked from accepting a connection from the Internet (10.69.0.138:Port 2114).,N/A,N/A
  ACCESS,2006/11/15,14:59:30 -5:00 GMT,Generic Host Process for Win32 Services was blocked from accepting a connection from the Internet (10.69.0.138:Port 2115).,N/A,N/A
  ACCESS,2006/11/15,14:59:30 -5:00 GMT,Generic Host Process for Win32 Services was blocked from accepting a connection from the Internet (10.69.0.138:Port 2116).,N/A,N/A
  ACCESS,2006/11/15,14:59:30 -5:00 GMT,Generic Host Process for Win32 Services was blocked from accepting a connection from the Internet (10.69.0.138:Port 2117).,N/A,N/A
  ACCESS,2006/11/15,14:59:30 -5:00 GMT,Generic Host Process for Win32 Services was blocked from accepting a connection from the Internet (10.69.0.138:Port 2118).,N/A,N/A
  ACCESS,2006/11/15,14:59:30 -5:00 GMT,Generic Host Process for Win32 Services was blocked from accepting a connection from the Internet (10.69.0.138:Port 2119).,N/A,N/A
  ACCESS,2006/11/15,14:59:30 -5:00 GMT,Generic Host Process for Win32 Services was blocked from accepting a connection from the Internet (10.69.0.138:Port 2120).,N/A,N/A
  ACCESS,2006/11/15,14:59:30 -5:00 GMT,Generic Host Process for Win32 Services was blocked from accepting a connection from the Internet (10.69.0.138:Port 2121).,N/A,N/A
  ACCESS,2006/11/15,14:59:30 -5:00 GMT,Generic Host Process for Win32 Services was blocked from accepting a connection from the Internet (10.69.0.138:Port 2122).,N/A,N/A
  ACCESS,2006/11/15,14:59:30 -5:00 GMT,Generic Host Process for Win32 Services was blocked from accepting a connection from the Internet (10.69.0.138:Port 2123).,N/A,N/A
  ACCESS,2006/11/15,14:59:46 -5:00 GMT,CCM Executive was temporarily blocked from connecting to the Internet (192.168.100.18:HTTP).,N/A,N/A
  PE,2006/11/15,15:00:26 -5:00 GMT,CCM Executive,C:\WINDOWS\system32\CCM\CcmExec.exe,127.0.0.1:1125,N/A
  ACCESS,2006/11/15,15:00:26 -5:00 GMT,CCM Executive was temporarily blocked from connecting to the local zone (127.0.0.1:Port 1125).,N/A,N/A
  ACCESS,2006/11/15,15:00:26 -5:00 GMT,CCM Executive was temporarily blocked from connecting to the local zone (127.0.0.1:Port 1126).,N/A,N/A
  ACCESS,2006/11/15,15:00:28 -5:00 GMT,CCM Executive was temporarily blocked from connecting to the local zone (127.0.0.1:Port 1127).,N/A,N/A
  ACCESS,2006/11/15,15:00:28 -5:00 GMT,CCM Executive was temporarily blocked from connecting to the local zone (127.0.0.1:Port 1128).,N/A,N/A
  ACCESS,2006/11/15,15:00:28 -5:00 GMT,CCM Executive was temporarily blocked from connecting to the local zone (127.0.0.1:Port 1129).,N/A,N/A
  ACCESS,2006/11/15,15:00:28 -5:00 GMT,CCM Executive was temporarily blocked from connecting to the local zone (127.0.0.1:Port 1130).,N/A,N/A
  ACCESS,2006/11/15,15:00:28 -5:00 GMT,CCM Executive was temporarily blocked from connecting to the local zone (127.0.0.1:Port 1131).,N/A,N/A
  ACCESS,2006/11/15,15:00:28 -5:00 GMT,CCM Executive was temporarily blocked from connecting to the local zone (127.0.0.1:Port 1132).,N/A,N/A
  PE,2006/11/15,15:02:10 -5:00 GMT,Secure Update,C:\Program Files\Wave Systems Corp\Services Manager\Secure Update\AutoUpdate.exe,172.16.49.21:53,N/A
  ACCESS,2006/11/15,15:02:14 -5:00 GMT,Secure Update was temporarily blocked from connecting to the Internet (172.16.49.21:DNS).,N/A,N/A
  ACCESS,2006/11/15,15:02:14 -5:00 GMT,Secure Update was temporarily blocked from connecting to the Internet (10.69.0.138:DNS).,N/A,N/A
  ACCESS,2006/11/15,15:02:16 -5:00 GMT,Secure Update was temporarily blocked from sending data to the Internet (10.69.0.138:DNS).,N/A,N/A
  ACCESS,2006/11/15,15:02:16 -5:00 GMT,Secure Update was temporarily blocked from connecting to the Internet (192.168.100.195:DNS).,N/A,N/A
  ACCESS,2006/11/15,15:02:16 -5:00 GMT,Secure Update was temporarily blocked from connecting to the Internet (192.168.100.237:DNS).,N/A,N/A
  ACCESS,2006/11/15,15:02:40 -5:00 GMT,CCM Executive was temporarily blocked from connecting to the Internet (192.168.100.18:HTTP).,N/A,N/A
  PE,2006/11/15,15:03:58 -5:00 GMT,Nessus Plugin Update,C:\Program Files\Tenable\Nessus\update.exe,127.0.0.1:1159,N/A
  PE,2006/11/15,15:04:04 -5:00 GMT,Nessus Plugin Update,C:\Program Files\Tenable\Nessus\update.exe,172.16.49.21:53,N/A
  ACCESS,2006/11/15,15:04:08 -5:00 GMT,Generic Host Process for Win32 Services was blocked from accepting a connection from the Internet (10.69.0.138:DNS).,N/A,N/A
  ACCESS,2006/11/15,15:04:14 -5:00 GMT,Generic Host Process for Win32 Services was blocked from accepting a connection from the Internet (192.168.100.195:DNS).,N/A,N/A
  ACCESS,2006/11/15,15:04:18 -5:00 GMT,Generic Host Process for Win32 Services was blocked from accepting a connection from the Internet (192.168.100.237:DNS).,N/A,N/A
  ACCESS,2006/11/15,15:05:26 -5:00 GMT,CCM Executive was temporarily blocked from connecting to the local zone (127.0.0.1:Port 1181).,N/A,N/A
  ACCESS,2006/11/15,15:05:26 -5:00 GMT,CCM Executive was temporarily blocked from connecting to the local zone (127.0.0.1:Port 1182).,N/A,N/A
  ACCESS,2006/11/15,15:05:26 -5:00 GMT,CCM Executive was temporarily blocked from connecting to the local zone (127.0.0.1:Port 1183).,N/A,N/A
  ACCESS,2006/11/15,15:05:26 -5:00 GMT,CCM Executive was temporarily blocked from connecting to the local zone (127.0.0.1:Port 1184).,N/A,N/A
  ACCESS,2006/11/15,15:05:28 -5:00 GMT,CCM Executive was temporarily blocked from connecting to the local zone (127.0.0.1:Port 1185).,N/A,N/A
  ACCESS,2006/11/15,15:05:28 -5:00 GMT,CCM Executive was temporarily blocked from connecting to the local zone (127.0.0.1:Port 1186).,N/A,N/A
  ACCESS,2006/11/15,15:05:28 -5:00 GMT,CCM Executive was temporarily blocked from connecting to the local zone (127.0.0.1:Port 1187).,N/A,N/A
  ACCESS,2006/11/15,15:05:28 -5:00 GMT,CCM Executive was temporarily blocked from connecting to the local zone (127.0.0.1:Port 1188).,N/A,N/A
  ACCESS,2006/11/15,15:06:30 -5:00 GMT,CCM Executive was temporarily blocked from connecting to the Internet (192.168.100.18:HTTP).,N/A,N/A
  PE,2006/11/15,15:12:22 -5:00 GMT,Zone Labs Client,C:\Program Files\Zone Labs\ZoneAlarm\zlclient.exe,192.168.100.195:53,N/A
  ZLUpdate,2006/11/15,15:13:56 -5:00 GMT,,,Auto
  ZLUpdate,2006/11/15,15:14:22 -5:00 GMT,,,Auto


More log samples showing different kinds of entries:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

  PE,2006/09/09,22:15:42 -5:00 GMT,Cisco Systems VPN Client,C:\Program Files\Cisco Systems\VPN Client\cvpnd.exe,127.0.0.1:62516,N/A
  PE,2006/09/09,22:15:46 -5:00 GMT,tcsd_win32.exe,C:\Program Files\NTRU Cryptosystems\NTRU Hybrid TSS v2.0.7\bin\tcsd_win32.exe,0.0.0.0:10001,N/A
  PE,2006/09/09,22:15:58 -5:00 GMT,Symantec AntiVirus,C:\Program Files\Symantec_Client_Security\Symantec AntiVirus\Rtvscan.exe,172.16.100.237:2967,N/A
  PE,2006/09/09,22:20:32 -5:00 GMT,Secure Update,C:\Program Files\Wave Systems Corp\Services Manager\Secure Update\AutoUpdate.exe,172.16.100.85:8080,N/A
  ACCESS,2006/09/09,22:23:04 -5:00 GMT,Secure Update was temporarily blocked from connecting to the Internet (172.16.100.85:Port 8080).,N/A,N/A
  FWROUTE,2006/09/09,22:26:58 -5:00 GMT,172.16.70.135:1027,172.16.100.195:53,UDP
  FWROUTE,2006/09/09,22:26:58 -5:00 GMT,172.16.70.135:137,172.16.100.204:137,UDP
  FWROUTE,2006/09/09,22:26:58 -5:00 GMT,172.16.70.135:1107,172.16.100.237:53,UDP
  ACCESS,2006/09/09,22:27:08 -5:00 GMT,Generic Host Process for Win32 Services was blocked from accepting a connection from the Internet (172.16.100.195:DNS).,N/A,N/A
  FWOUT,2006/09/09,22:27:22 -5:00 GMT,172.16.70.135:1134,172.16.100.195:445,TCP (flags:S)
  FWOUT,2006/09/09,22:27:22 -5:00 GMT,10.57.0.1:1135,172.16.100.195:139,TCP (flags:S)
  FWOUT,2006/09/09,22:27:22 -5:00 GMT,172.16.70.135:1136,172.16.100.195:139,TCP (flags:S)
  FWOUT,2006/09/09,22:27:48 -5:00 GMT,172.16.70.135:1144,172.16.100.237:445,TCP (flags:S)
  FWOUT,2006/09/09,22:27:48 -5:00 GMT,10.57.0.1:1145,172.16.100.237:139,TCP (flags:S)
  FWOUT,2006/09/09,22:27:48 -5:00 GMT,172.16.70.135:1146,172.16.100.237:139,TCP (flags:S)
  FWOUT,2006/09/09,22:28:14 -5:00 GMT,172.16.70.135:1153,172.16.100.195:445,TCP (flags:S)
  FWOUT,2006/09/09,22:28:14 -5:00 GMT,10.57.0.1:1154,172.16.100.195:139,TCP (flags:S)
  FWOUT,2006/09/09,22:28:14 -5:00 GMT,172.16.70.135:1155,172.16.100.195:139,TCP (flags:S)


.. code-block:: console

  ACCESS,2006/09/26,13:14:36 -5:00 GMT,RogueScannerWin32 was unable to obtain permission for connecting to the Internet (169.254.207.118:Port 7000); access was denied.,N/A,N/A
  PE,2006/09/26,13:14:36 -5:00 GMT,RogueScannerWin32,C:\Program Files\Network Chemistry\RogueScanner GUI\RogueScannerGUI.exe,169.254.207.118:7001,N/A


.. code-block:: console

  FWOUT_OK,2006/09/26,21:05:06 -5:00 GMT,10.57.0.2:68,10.57.0.138:67,UDP
  FWIN_OK,2006/09/27,08:32:14 -5:00 GMT,0.0.0.0:68,255.255.255.255:67,UDP
  FWIN_OK,2006/09/27,09:05:58 -5:00 GMT,172.16.1.64:68,255.255.255.255:67,UDP
  FWIN_OK,2006/09/27,09:07:30 -5:00 GMT,172.16.1.22:68,255.255.255.255:67,UDP
  FWIN_OK,2006/09/27,09:13:16 -5:00 GMT,172.16.1.43:68,255.255.255.255:67,UDP
  FWIN_OK,2006/09/27,09:33:46 -5:00 GMT,0.0.0.0:68,255.255.255.255:67,UDP
  FWIN_OK,2006/09/27,09:36:44 -5:00 GMT,172.16.1.76:68,255.255.255.255:67,UDP
  FWIN,2006/09/27,09:43:48 -5:00 GMT,10.62.3.14:1043,172.16.1.60:38293,UDP
  FWIN_OK,2006/09/27,10:05:02 -5:00 GMT,172.16.1.69:68,255.255.255.255:67,UDP
  FWIN_OK,2006/09/27,10:05:56 -5:00 GMT,172.16.1.54:68,255.255.255.255:67,UDP
  FWIN_OK,2006/09/27,10:07:36 -5:00 GMT,172.16.1.34:68,255.255.255.255:67,UDP
  FWIN,2006/09/27,10:07:54 -5:00 GMT,10.62.3.54:1039,172.16.1.60:38293,UDP
  FWIN_OK,2006/09/27,10:16:48 -5:00 GMT,172.16.1.46:68,255.255.255.255:67,UDP


