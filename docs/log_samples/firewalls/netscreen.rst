Log Samples from the Netscreen Firewall
---------------------------------------

Traffic denied:
^^^^^^^^^^^^^^^

.. code-block:: console

  Jun  2 14:55:46 fire00 fire00: NetScreen device_id=fire00  [Root]system-notification-00257(traffic): start_time="2006-06-02 14:55:45" duration=0 policy_id=119 service=udp/port:7001 proto=17 src zone=Trust dst zone=Untrust action=Deny sent=0 rcvd=0 src=192.168.2.1 dst=1.2.3.4 src_port=3036 dst_port=7001
  Jun  2 14:53:31 fire00 aka1: NetScreen device_id=aka1  [Root]system-notification-00257(traffic): start_time="2006-06-02 14:53:30" duration=0 policy_id=120 service=udp/port:20721 proto=17 src zone=Trust dst zone=DMZ action=Deny sent=0 rcvd=0 src=192.168.2.2 dst=1.2.3.4 src_port=53 dst_port=20721
  Jun  2 14:53:31 fire00 aka1: NetScreen device_id=aka1  [Root]system-notification-00257(traffic): start_time="2006-06-02 14:53:30" duration=0 policy_id=120 service=udp/port:17210 proto=17 src zone=Trust dst zone=DMZ action=Deny sent=0 rcvd=0 src=192.168.2.2 dst=1.2.3.4 src_port=53 dst_port=17210
  Mar 16 15:27:56 172.16.10.42 ns5gt: NetScreen device_id=ns5gt  [No Name]system-notification-00257(traffic): start_time=\"2005-03-16 16:33:22\" duration=0 policy_id=320001 service=tcp/port:120 proto=6 src zone=Null dst zone=self action=Deny sent=0 rcvd=60 src=192.168.2.1 dst=1.2.3.4 src_port=31048 dst_port=12



Alert messages:
^^^^^^^^^^^^^^^

.. code-block:: console

  Jun  1 22:01:35 [xx] ns5gt: NetScreen device_id=ns5gt  [Root]system-alert-00016: Port scan! From 1.2.3.4:54886 to 2.3.4.5:406, proto TCP (zone Untrust, int untrust). Occurred 1 times. (2004-06-01 22:09:03)
  Jun  1 22:01:57 [xx] ns5gt: NetScreen device_id=ns5gt  [Root]system-alert-00016: Port scan! From 1.2.3.4:55181 to 2.3.4.5:1358, proto TCP (zone Untrust, int untrust). Occurred 1 times. (2004-06-01 22:09:25)
  Jun  1 22:02:10 [xx] ns5gt: NetScreen device_id=ns5gt  [Root]system-alert-00016: Port scan! From 1.2.3.4:55339 to 2.3.4.5:1515, proto TCP (zone Untrust, int untrust). Occurred 1 times. (2004-06-01 22:09:38)


Critical messages:
^^^^^^^^^^^^^^^^^^

.. code-block:: console

  Jun  2 11:24:16 fire00 sav00: NetScreen device_id=sav00  [Root]system-critical-00436: Large ICMP packet! From 1.2.3.4 to 2.3.4.5, proto 1 (zone Untrust, int ethernet1/2). Occurred 1 times. (2006-06-02 11:24:16)
  [00001] 2007-04-01 15:32:00 [Root]system-critical-00031: arp req detected an IP conflict (IP 10.1.1.1, MAC 0027f2424c8c) on interface ethernet1
  [00001] 2007-03-12 12:47:36 [Root]system-critical-00001(second traffic alarm):  Policy ID=14 Rate=180 bytes/sec exceeds threshold
  [00008] 2006-06-30 13:10:09 [Root]system-critical-00041: VPN 'zzz-primary-vpn' from a.b.c.d is down.
  [00002] 2006-06-30 13:11:41 [Root]system-critical-00040: VPN 'zzz-primary-vpn' from a.b.c.d is up.
  [00001] 2005-05-16 12:55:10 [Root]system-critical-00042: Replay packet detected on IPSec tunnel on ethernet3 with tunnel ID 0x1c! From z.y.x.w to a.b.c.d/336, ESP, SPI 0xf63af637, SEQ 0xe337.
  [00001] 2006-05-25 13:34:33 [Root]system-alert-00008: IP spoofing! From 10.1.1.238:80 to a.b.c.d:49807, proto TCP (zone Untrust, int ethernet3). Occurred 1 times.

Admin login:
^^^^^^^^^^^^

.. code-block:: console

  Jun  1 22:02:12 [xx] ns5gt: NetScreen device_id=ns5gt  [Root]system-notification-00002: Admin user "baby" logged in for Web(http) management (port 8080) from 1.2.3.4:2150 (2004-06-01 22:09:40)

