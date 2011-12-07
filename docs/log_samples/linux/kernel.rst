Log Samples from the Linux kernel
---------------------------------

NFS incompability between Linux and Solaris (not security related):
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

  Feb 28 07:46:15 bs11 kernel: svc: unknown program 100227 (me 100003)



System shutdown:
^^^^^^^^^^^^^^^^

.. code-block:: console

  Jun  1 22:20:05 secserv kernel: Kernel logging (proc) stopped.
  Jun  1 22:20:05 secserv kernel: Kernel log daemon terminating.
  Jun  1 22:20:06 secserv exiting on signal 15
  Nov 27 08:05:57 galileo kernel: Kernel logging (proc) stopped.
  Nov 27 08:05:57 galileo kernel: Kernel log daemon terminating.
  Nov 27 08:05:57 galileo exiting on signal 15


ADSL monitor:
^^^^^^^^^^^^^

.. code-block:: console

  Nov 22 02:35:36 thecla2 kernel: ATM dev 0: ADSL line is up (2752 kb/s down | 448 kb/s up)


description:
^^^^^^^^^^^^

.. code-block:: console

  May 21 20:22:28 slacker2 kernel: tcp_parse_options: Illegal window scaling value 200 >14 received.



Kernel level hardware SCSI error (not security related):
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

  Aug 30 10:06:11 newfish kernel: >>>>>>>>>>>>>>>>>> Dump Card State Begins <<<<<<<<<<<<<<<<<
  Aug 30 10:06:11 newfish kernel: scsi1: Dumping Card State in Message-out phase, at SEQADDR 0x16b
  Aug 30 10:06:11 newfish kernel: Card was paused
  Aug 30 10:06:11 newfish kernel: ACCUM = 0xa0, SINDEX = 0x61, DINDEX = 0xe4, ARG_2 = 0x1
  Aug 30 10:06:11 newfish kernel: HCNT = 0x0 SCBPTR = 0x1
  Aug 30 10:06:11 newfish kernel: SCSIPHASE[0x0] SCSISIGI[0xa4] ERROR[0x0] SCSIBUSL[0xd] 
  Aug 30 10:06:11 newfish kernel: LASTPHASE[0xa0] SCSISEQ[0x12] SBLKCTL[0xa] SCSIRATE[0xc2] 
  Aug 30 10:06:11 newfish kernel: SEQCTL[0x10] SEQ_FLAGS[0x40] SSTAT0[0x0] SSTAT1[0x0] 
  Aug 30 10:06:11 newfish kernel: SSTAT2[0x0] SSTAT3[0x0] SIMODE0[0x8] SIMODE1[0xac] 
  Aug 30 10:06:11 newfish kernel: SXFRCTL0[0x88] DFCNTRL[0x0] DFSTATUS[0x89] 
  Aug 30 10:06:11 newfish kernel: STACK: 0xe1 0xe1 0x163 0x178
  Aug 30 10:06:11 newfish kernel: SCB count = 12
  Aug 30 10:06:11 newfish kernel: Kernel NEXTQSCB = 11
  Aug 30 10:06:11 newfish kernel: Card NEXTQSCB = 4
  Aug 30 10:06:12 newfish kernel: QINFIFO entries: 4 
  Aug 30 10:06:12 newfish kernel: Waiting Queue entries: 
  Aug 30 10:06:12 newfish kernel: Disconnected Queue entries: 2:7 
  Aug 30 10:06:12 newfish kernel: QOUTFIFO entries: 
  Aug 30 10:06:12 newfish kernel: Sequencer Free SCB List: 0 6 7 5 4 3 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 
  Aug 30 10:06:12 newfish kernel: Sequencer SCB Info: 
  Aug 30 10:06:12 newfish kernel:   0 SCB_CONTROL[0x0] SCB_SCSIID[0x17] SCB_LUN[0x0] SCB_TAG[0xff] 
  Aug 30 10:06:12 newfish kernel:   1 SCB_CONTROL[0x64] SCB_SCSIID[0x17] SCB_LUN[0x0] SCB_TAG[0x5] 
  Aug 30 10:06:12 newfish kernel:   2 SCB_CONTROL[0x64] SCB_SCSIID[0x17] SCB_LUN[0x0] SCB_TAG[0x7] 
  Aug 30 10:06:12 newfish kernel:   3 SCB_CONTROL[0xe0] SCB_SCSIID[0x7] SCB_LUN[0x0] SCB_TAG[0xff] 
  Aug 30 10:06:12 newfish kernel:   4 SCB_CONTROL[0xe0] SCB_SCSIID[0x7] SCB_LUN[0x0] SCB_TAG[0xff] 
  Aug 30 10:06:12 newfish kernel:   5 SCB_CONTROL[0xe0] SCB_SCSIID[0x17] SCB_LUN[0x0] SCB_TAG[0xff] 
  Aug 30 10:06:12 newfish kernel:   6 SCB_CONTROL[0x0] SCB_SCSIID[0x17] SCB_LUN[0x0] SCB_TAG[0xff] 
  Aug 30 10:06:12 newfish kernel:   7 SCB_CONTROL[0xe0] SCB_SCSIID[0x17] SCB_LUN[0x0] SCB_TAG[0xff] 
  Aug 30 10:06:12 newfish kernel:   8 SCB_CONTROL[0x0] SCB_SCSIID[0xff] SCB_LUN[0xff] SCB_TAG[0xff] 
  Aug 30 10:06:12 newfish kernel:   9 SCB_CONTROL[0x0] SCB_SCSIID[0xff] SCB_LUN[0xff] SCB_TAG[0xff] 
  Aug 30 10:06:12 newfish kernel:  10 SCB_CONTROL[0x0] SCB_SCSIID[0xff] SCB_LUN[0xff] SCB_TAG[0xff] 
  Aug 30 10:06:12 newfish kernel:  11 SCB_CONTROL[0x0] SCB_SCSIID[0xff] SCB_LUN[0xff] SCB_TAG[0xff] 
  Aug 30 10:06:12 newfish kernel:  12 SCB_CONTROL[0x0] SCB_SCSIID[0xff] SCB_LUN[0xff] SCB_TAG[0xff] 
  Aug 30 10:06:12 newfish kernel:  13 SCB_CONTROL[0x0] SCB_SCSIID[0xff] SCB_LUN[0xff] SCB_TAG[0xff] 
  Aug 30 10:06:12 newfish kernel:  14 SCB_CONTROL[0x0] SCB_SCSIID[0xff] SCB_LUN[0xff] SCB_TAG[0xff] 
  Aug 30 10:06:12 newfish kernel:  15 SCB_CONTROL[0x0] SCB_SCSIID[0xff] SCB_LUN[0xff] SCB_TAG[0xff] 
  Aug 30 10:06:12 newfish kernel:  16 SCB_CONTROL[0x0] SCB_SCSIID[0xff] SCB_LUN[0xff] SCB_TAG[0xff] 
  Aug 30 10:06:12 newfish kernel:  17 SCB_CONTROL[0x0] SCB_SCSIID[0xff] SCB_LUN[0xff] SCB_TAG[0xff] 
  Aug 30 10:06:12 newfish kernel:  18 SCB_CONTROL[0x0] SCB_SCSIID[0xff] SCB_LUN[0xff] SCB_TAG[0xff] 
  Aug 30 10:06:13 newfish kernel:  19 SCB_CONTROL[0x0] SCB_SCSIID[0xff] SCB_LUN[0xff] SCB_TAG[0xff] 
  Aug 30 10:06:13 newfish kernel:  20 SCB_CONTROL[0x0] SCB_SCSIID[0xff] SCB_LUN[0xff] SCB_TAG[0xff] 
  Aug 30 10:06:13 newfish kernel:  21 SCB_CONTROL[0x0] SCB_SCSIID[0xff] SCB_LUN[0xff] SCB_TAG[0xff] 
  Aug 30 10:06:13 newfish kernel:  22 SCB_CONTROL[0x0] SCB_SCSIID[0xff] SCB_LUN[0xff] SCB_TAG[0xff] 
  Aug 30 10:06:13 newfish kernel:  23 SCB_CONTROL[0x0] SCB_SCSIID[0xff] SCB_LUN[0xff] SCB_TAG[0xff] 
  Aug 30 10:06:13 newfish kernel:  24 SCB_CONTROL[0x0] SCB_SCSIID[0xff] SCB_LUN[0xff] SCB_TAG[0xff] 
  Aug 30 10:06:13 newfish kernel:  25 SCB_CONTROL[0x0] SCB_SCSIID[0xff] SCB_LUN[0xff] SCB_TAG[0xff] 
  Aug 30 10:06:13 newfish kernel:  26 SCB_CONTROL[0x0] SCB_SCSIID[0xff] SCB_LUN[0xff] SCB_TAG[0xff] 
  Aug 30 10:06:13 newfish kernel:  27 SCB_CONTROL[0x0] SCB_SCSIID[0xff] SCB_LUN[0xff] SCB_TAG[0xff] 
  Aug 30 10:06:13 newfish kernel:  28 SCB_CONTROL[0x0] SCB_SCSIID[0xff] SCB_LUN[0xff] SCB_TAG[0xff] 
  Aug 30 10:06:13 newfish kernel:  29 SCB_CONTROL[0x0] SCB_SCSIID[0xff] SCB_LUN[0xff] SCB_TAG[0xff] 
  Aug 30 10:06:13 newfish kernel:  30 SCB_CONTROL[0x0] SCB_SCSIID[0xff] SCB_LUN[0xff] SCB_TAG[0xff] 
  Aug 30 10:06:13 newfish kernel:  31 SCB_CONTROL[0x0] SCB_SCSIID[0xff] SCB_LUN[0xff] SCB_TAG[0xff] 
  Aug 30 10:06:13 newfish kernel: Pending list: 
  Aug 30 10:06:13 newfish kernel:   7 SCB_CONTROL[0x60] SCB_SCSIID[0x17] SCB_LUN[0x0] 
  Aug 30 10:06:13 newfish kernel:   4 SCB_CONTROL[0x74] SCB_SCSIID[0x17] SCB_LUN[0x0] 
  Aug 30 10:06:13 newfish kernel:   5 SCB_CONTROL[0x64] SCB_SCSIID[0x17] SCB_LUN[0x0] 
  Aug 30 10:06:13 newfish kernel: Kernel Free SCB list: 1 0 2 3 6 10 9 8 
  Aug 30 10:06:13 newfish kernel: DevQ(0:0:0): 0 waiting
  Aug 30 10:06:13 newfish kernel: DevQ(0:1:0): 0 waiting
  Aug 30 10:06:13 newfish kernel: DevQ(0:6:0): 0 waiting
  Aug 30 10:06:13 newfish kernel: 
  Aug 30 10:06:13 newfish kernel: <<<<<<<<<<<<<<<<< Dump Card State Ends >>>>>>>>>>>>>>>>>>
  Aug 30 10:06:13 newfish kernel: Recovery SCB completes
  Aug 30 10:06:13 newfish kernel: (scsi1:A:1:0): Device is disconnected, re-queuing SCB
  Aug 30 10:06:13 newfish kernel: Recovery code sleeping
  Aug 30 10:06:13 newfish kernel: Recovery code awake
  Aug 30 10:06:13 newfish kernel: Timer Expired
  Aug 30 10:06:13 newfish kernel: aic7xxx_abort returns 0x2003
  Aug 30 10:06:13 newfish kernel: scsi1:0:1:0: Attempting to queue a TARGET RESET message
  Aug 30 10:06:13 newfish kernel: CDB: 0x28 0x0 0x4 0x7a 0x65 0xcf 0x0 0x0 0x10 0x0
  Aug 30 10:06:13 newfish kernel: aic7xxx_dev_reset returns 0x2003
  Aug 30 10:06:13 newfish kernel: Recovery SCB completes



Linux BUG and call trace example:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

  BUG: unable to handle kernel NULL pointer dereference at (null)
  IP: [<ffffffff8141c423>] 0xffffffff8141c423
  PGD 0
  Oops: 0002 [#1] PREEMPT SMP
  last sysfs file: /sys/devices/pci0000:00/0000:00:1f.2/host0/target0:0:0/0:0:0:0/scsi_level
  CPU 0
  Modules linked in: zr364xx videodev v4l1_compat v4l2_compat_ioctl32 videobuf_vmalloc videobuf_core usb_storage r8187 
  ieee80211_rtl ieee80211_crypt_ccmp_rtl ieee80211_crypt_tkip_rtl ieee80211_crypt_wep_rtl ieee80211_crypt_rtl coretemp 
  snd_seq_dummy sdhci_pci sdhci snd_seq_oss snd_hda_codec_realtek snd_seq_midi_event snd_seq snd_seq_device 
  mmc_core iTCO_wdt iTCO_vendor_support nvidia(P) snd_hda_intel snd_hda_codec snd_hwdep snd_pcm_oss snd_pcm 
  snd_timer snd_page_alloc snd_mixer_oss snd soundcore r8169 mii pata_acpi [last unloaded: ieee80211_crypt_rtl]
  Pid: 226, comm: khubd Tainted: P           2.6.30.5 #1 GX700
  RIP: 0010:[<ffffffff8141c423>]  [<ffffffff8141c423>] 0xffffffff8141c423
  RSP: 0018:ffff8800bfa2fc08  EFLAGS: 00010246
  RAX: 0000000000000000 RBX: ffff8800b0953d14 RCX: 0000000000000000
  RDX: 0000000000000000 RSI: 0000000000000083 RDI: ffff8800b0953d14
  RBP: ffff8800b0953d10 R08: 0000000000000000 R09: 00000000000000ae
  R10: ffff880001744540 R11: 0000000000000008 R12: ffffffffffffffff
  R13: ffff8800b0953d18 R14: 0000000000000000 R15: ffff8800bf8671c0
  FS:  0000000000000000(0000) GS:ffff88000165f000(0000) knlGS:0000000000000000
  CS:  0010 DS: 0018 ES: 0018 CR0: 000000008005003b
  CR2: 0000000000000000 CR3: 0000000001001000 CR4: 00000000000006e0
  DR0: 0000000000000000 DR1: 0000000000000000 DR2: 0000000000000000
  DR3: 0000000000000000 DR6: 00000000ffff0ff0 DR7: 0000000000000400
  Process khubd (pid: 226, threadinfo ffff8800bfa2e000, task ffff8800bf8671c0)
  Stack:
   ffff8800b0953d18 ffff8800a9049c30 ffff8800bfa2fc60 ffff8800bfa2fcb0
   ffffffff8110aaaa ffff8800b0953d10 ffff8800b08a5c00 ffffffffa09ea788
   ffff8800bb05f800 000000000000001f 0000000000000000 ffffffff8141c06a
  Call Trace:
   [<ffffffff8110aaaa>] ? 0xffffffff8110aaaa
   [<ffffffff8141c06a>] ? 0xffffffff8141c06a
   [<ffffffffa09cd5e6>] ? 0xffffffffa09cd5e6
   [<ffffffffa09e711a>] ? 0xffffffffa09e711a
   [<ffffffff812a8878>] ? 0xffffffff812a8878
   [<ffffffff81246932>] ? 0xffffffff81246932
   [<ffffffff81246a55>] ? 0xffffffff81246a55
   [<ffffffff81245bf1>] ? 0xffffffff81245bf1
   [<ffffffff81244208>] ? 0xffffffff81244208
   [<ffffffff812a609a>] ? 0xffffffff812a609a
   [<ffffffff812a12b9>] ? 0xffffffff812a12b9
   [<ffffffff812a214f>] ? 0xffffffff812a214f
   [<ffffffff810098cc>] ? 0xffffffff810098cc
   [<ffffffff81033551>] ? 0xffffffff81033551
   [<ffffffff8141dc39>] ? 0xffffffff8141dc39
   [<ffffffff81053f10>] ? 0xffffffff81053f10
   [<ffffffff812a1cf0>] ? 0xffffffff812a1cf0
   [<ffffffff81053b24>] ? 0xffffffff81053b24
   [<ffffffff8100c57a>] ? 0xffffffff8100c57a
   [<ffffffff81053ad0>] ? 0xffffffff81053ad0
   [<ffffffff8100c570>] ? 0xffffffff8100c570
  Code: 7f b6 66 0f 1f 44 00 00 48 8d 5d 04 4c 8d 6d 08 48 89 df 49 c7 c4 ff ff ff ff e8 c9 14 00 00 48 8b 45 10 4c 89 2c 24 48 89 65 10 <48> 89 20 48 89 44 24 08 4c 89 7c 24 10 4c 89 e0 87 45 00 83 f8
  RIP  [<ffffffff8141c423>] 0xffffffff8141c423
   RSP <ffff8800bfa2fc08>
  CR2: 0000000000000000
  ---[ end trace 05e0b9e1e8d124aa ]---
  note: khubd[226] exited with preempt_count 2



SLUB mem allocate failed(swapper: page allocation failure.)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

  Feb 20 21:20:06 server1 kernel: SLUB: Unable to allocate memory on node -1 (gfp=0x20)
  Feb 20 21:20:06 server1 kernel:  cache: kmalloc-4096, object size: 4096, buffer size: 4096, default order: 3, min order: 0
  Feb 20 21:20:06 server1 kernel:  node 0: slabs: 619, objs: 1641, free: 0
  Feb 20 21:20:06 server1 kernel: swapper: page allocation failure. order:0, mode:0x4020
  Feb 20 21:20:06 server1 kernel: Pid: 0, comm: swapper Not tainted 2.6.32.4 #1
  Feb 20 21:20:06 server1 kernel: Call Trace:
  Feb 20 21:20:06 server1 kernel: <IRQ>  [<ffffffff81084d3a>] ? __alloc_pages_nodemask+0x54a/0x670
  Feb 20 21:20:06 server1 kernel: [<ffffffff810b1f8a>] ? __slab_alloc+0x69a/0x6b0
  Feb 20 21:20:06 server1 kernel: [<ffffffff81710ee7>] ? __netdev_alloc_skb+0x17/0x40
  Feb 20 21:20:06 server1 kernel: [<ffffffff8178309d>] ? tcp_v4_rcv+0x6bd/0x780
  Feb 20 21:20:06 server1 kernel: [<ffffffff81710ee7>] ? __netdev_alloc_skb+0x17/0x40
  Feb 20 21:20:06 server1 kernel: [<ffffffff810b2f0b>] ? __kmalloc_track_caller+0xcb/0x110
  Feb 20 21:20:06 server1 kernel: [<ffffffff81710b6b>] ? __alloc_skb+0x6b/0x170
  Feb 20 21:20:06 server1 kernel: [<ffffffff81710ee7>] ? __netdev_alloc_skb+0x17/0x40
  Feb 20 21:20:06 server1 kernel: [<ffffffff8164fa29>] ? rtl8169_rx_fill+0xc9/0x220
  Feb 20 21:20:06 server1 kernel: [<ffffffff8164fdc0>] ? rtl8169_rx_interrupt+0x240/0x520
  Feb 20 21:20:06 server1 kernel: [<ffffffff81650236>] ? rtl8169_poll+0x56/0x240
  Feb 20 21:20:06 server1 kernel: [<ffffffff8171d513>] ? net_rx_action+0x83/0x130
  Feb 20 21:20:06 server1 kernel: [<ffffffff81049dd6>] ? __do_softirq+0xa6/0x130
  Feb 20 21:20:06 server1 kernel: [<ffffffff8100c5ec>] ? call_softirq+0x1c/0x30
  Feb 20 21:20:06 server1 kernel: [<ffffffff8100e58d>] ? do_softirq+0x4d/0x80
  Feb 20 21:20:06 server1 kernel: [<ffffffff81049c15>] ? irq_exit+0x95/0xa0
  Feb 20 21:20:06 server1 kernel: [<ffffffff8100db8e>] ? do_IRQ+0x6e/0xe0
  Feb 20 21:20:06 server1 kernel: [<ffffffff8100be53>] ? ret_from_intr+0x0/0xa
  Feb 20 21:20:06 server1 kernel: <EOI>  [<ffffffff8101f020>] ? lapic_next_event+0x0/0x20
  Feb 20 21:20:06 server1 kernel: [<ffffffff81013452>] ? default_idle+0x32/0x40
  Feb 20 21:20:06 server1 kernel: [<ffffffff81013494>] ? c1e_idle+0x34/0x100
  Feb 20 21:20:06 server1 kernel: [<ffffffff8100a14c>] ? cpu_idle+0xac/0x100


example segfault log
^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

  Jun 20 09:44:14 srv1 kernel: chttp[5849] general protection ip:7f185c076c93 sp:7fff38b79610 error:0 in libc-2.12.so[7f185c009000+153000]
  Jun 20 09:56:31 srv1 kernel: chttp[5883]: segfault at 0 ip 00007f0cc4898af0 sp 00007fff0b43d5f8 error 4 in libc-2.12.so[7f0cc481f000+153000]


cdrom errors:
^^^^^^^^^^^^^

.. code-block:: console

  Jun  7 15:32:50 Lab4 kernel: cdrom: This disc doesn't have any tracks I recognize!
  Jun  7 15:32:50 Lab4 kernel: sr 3:0:0:0: [sr0] Result: hostbyte=DID_OK driverbyte=DRIVER_SENSE
  Jun  7 15:32:50 Lab4 kernel: sr 3:0:0:0: [sr0] Sense Key : Illegal Request [current] 
  Jun  7 15:32:50 Lab4 kernel: Info fld=0x0
  Jun  7 15:32:50 Lab4 kernel: sr 3:0:0:0: [sr0] Add. Sense: Logical block address out of range
  Jun  7 15:32:50 Lab4 kernel: sr 3:0:0:0: [sr0] CDB: Read(10): 28 00 00 00 00 00 00 00 01 00
  Jun  7 15:32:50 Lab4 kernel: end_request: I/O error, dev sr0, sector 0
  Jun  7 15:32:50 Lab4 kernel: Buffer I/O error on device sr0, logical block 0



USB flash drive connect:
^^^^^^^^^^^^^^^^^^^^^^^^

Maybe use this to block if someone plugs in an usb stick and rip some data from the server.

.. code-block:: console

  Jun 27 16:42:52 Lab14 kernel: usb 3-1.2: new full speed USB device using uhci_hcd and address 6
  Jun 27 16:42:52 Lab14 kernel: usb 3-1.2: not running at top speed; connect to a high speed hub
  Jun 27 16:42:52 Lab14 kernel: scsi5 : usb-storage 3-1.2:1.0
  Jun 27 16:42:53 Lab14 kernel: scsi 5:0:0:0: Direct-Access     Ut165    USB2FlashStorage 0.00 PQ: 0 ANSI: 2
  Jun 27 16:42:53 Lab14 kernel: sd 5:0:0:0: Attached scsi generic sg2 type 0
  Jun 27 16:42:53 Lab14 kernel: sd 5:0:0:0: [sdb] 15794176 512-byte logical blocks: (8.08 GB/7.53 GiB)
  Jun 27 16:42:53 Lab14 kernel: sd 5:0:0:0: [sdb] Write Protect is off
  Jun 27 16:42:53 Lab14 kernel: sdb: unknown partition table
  Jun 27 16:42:53 Lab14 kernel: sd 5:0:0:0: [sdb] Attached SCSI removable disk
  Jun 27 16:43:01 Lab14 kernel: EXT3-fs: barriers not enabled
  Jun 27 16:43:01 Lab14 kernel: kjournald starting.  Commit interval 5 seconds
  Jun 27 16:43:01 Lab14 kernel: EXT3-fs (sdb): warning: maximal mount count reached, running e2fsck is recommended
  Jun 27 16:43:01 Lab14 kernel: EXT3-fs (sdb): using internal journal
  Jun 27 16:43:01 Lab14 kernel: EXT3-fs (sdb): mounted filesystem with writeback data mode



