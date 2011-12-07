Log Samples from pacman
-----------------------

pacman install log
^^^^^^^^^^^^^^^^^^

.. code-block:: console

  [2010-05-28 14:41] installed filesystem (2010.02-4)
  [2010-05-28 14:41] installed util-linux-ng (2.17.2-2)
  [2010-05-28 14:41] installed e2fsprogs (1.41.11-1)
  [2010-05-28 14:41] installed cryptsetup (1.1.0-2)
  [2010-05-28 14:41] installed dash (0.5.5.1-2)
  [2010-05-28 14:41] installed dcron (4.4-2)
  [2010-05-28 14:41] installed dhcpcd (5.2.2-1)
  [2010-05-28 14:41] installed diffutils (3.0-1)
  [2010-05-28 14:41] installed file (5.04-2)
  [2010-05-28 14:41] installed findutils (4.4.2-2)
  [2010-05-28 14:41] installed gawk (3.1.8-1)
  [2010-05-28 14:41] installed gen-init-cpio (2.6.32-1)
  [2010-05-28 14:41] installed gettext (0.17-4)
  [2010-05-28 14:41] installed pcre (8.02-1)
  [2010-05-28 14:41] installed grep (2.6.3-1)
  [2010-05-28 14:41] installed sed (4.2.1-2)
  [2010-05-28 14:41] installed grub (0.97-17)
  [2010-05-28 14:41] installed gzip (1.4-1)
  [2010-05-28 14:41] installed libusb (0.1.12-4)
  [2010-05-28 14:41] installed glib2 (2.24.1-1)
  [2010-05-28 14:41] installed module-init-tools (3.11.1-2)
  [2010-05-28 14:41] installed udev (151-3)
  [2010-05-28 14:41] installed net-tools (1.60-14)
  [2010-05-28 14:41] installed kbd (1.15.2-1)
  [2010-05-28 14:41] installed sysvinit (2.86-5)
  [2010-05-28 14:41] installed initscripts (2010.05-3)
  [2010-05-28 14:41] installed iputils (20100214-2)
  [2010-05-28 14:41] installed jfsutils (1.1.14-1)
  [2010-05-28 14:41] installed kernel26-firmware (2.6.33.4-1)
  [2010-05-28 14:41] installed mkinitcpio-busybox (1.16.1-3)
  [2010-05-28 14:41] installed which (2.20-3)
  [2010-05-28 14:41] installed mkinitcpio (0.6.4-1)
  [2010-05-28 12:41] >>> Updating module dependencies. Please wait ...
  [2010-05-28 12:41] >>> MKINITCPIO SETUP
  [2010-05-28 12:41] >>> ----------------
  [2010-05-28 12:41] >>> If you use LVM2, Encrypted root or software RAID,
  [2010-05-28 12:41] >>> Ensure you enable support in /etc/mkinitcpio.conf .
  [2010-05-28 12:41] >>> More information about mkinitcpio setup can be found here:
  [2010-05-28 12:41] >>> http://wiki.archlinux.org/index.php/Mkinitcpio
  [2010-05-28 12:41] 
  [2010-05-28 12:41] >>> Generating initial ramdisk, using mkinitcpio.  Please wait...
  [2010-05-28 12:41] > Building image "default"
  [2010-05-28 12:41] > Running command: /sbin/mkinitcpio -k 2.6.33-ARCH -c /etc/mkinitcpio.conf -g /boot/kernel26.img
  [2010-05-28 12:41] :: Begin build
  [2010-05-28 12:41] :: Parsing hook [base]
  [2010-05-28 12:41] :: Parsing hook [udev]
  [2010-05-28 12:41] :: Parsing hook [autodetect]
  [2010-05-28 12:41] :: Parsing hook [pata]
  [2010-05-28 12:41] :: Parsing hook [scsi]
  [2010-05-28 12:41] :: Parsing hook [sata]
  [2010-05-28 12:41] :: Parsing hook [filesystems]
  [2010-05-28 12:41] :: Generating module dependencies
  [2010-05-28 12:41] :: Generating image '/boot/kernel26.img'...SUCCESS
  [2010-05-28 12:41] > SUCCESS
  [2010-05-28 12:41] > Building image "fallback"
  [2010-05-28 12:41] > Running command: /sbin/mkinitcpio -k 2.6.33-ARCH -c /etc/mkinitcpio.conf -g /boot/kernel26-fallback.img -S autodetect
  [2010-05-28 12:41] :: Begin build
  [2010-05-28 12:41] :: Parsing hook [base]
  [2010-05-28 12:41] :: Parsing hook [udev]
  [2010-05-28 12:41] :: Parsing hook [pata]
  [2010-05-28 12:41] :: Parsing hook [scsi]
  [2010-05-28 12:41] :: Parsing hook [sata]
  [2010-05-28 12:41] :: Parsing hook [filesystems]
  [2010-05-28 12:41] :: Generating module dependencies
  [2010-05-28 12:41] :: Generating image '/boot/kernel26-fallback.img'...SUCCESS
  [2010-05-28 12:41] > SUCCESS
  [2010-05-28 14:41] installed kernel26 (2.6.33.4-1)
  [2010-05-28 14:41] installed less (436-1)
  [2010-05-28 14:41] installed licenses (2.6-1)
  [2010-05-28 14:41] installed logrotate (3.7.8-1)
  [2010-05-28 14:41] installed lvm2 (2.02.62-1)
  [2010-05-28 14:41] installed lzo2 (2.03-1)
  [2010-05-28 14:41] installed mailx (8.1.1-7)
  [2010-05-28 14:41] installed gdbm (1.8.3-7)
  [2010-05-28 14:41] installed perl (5.10.1-5)
  [2010-05-28 14:42] installed texinfo (4.13a-4)
  [2010-05-28 14:42] installed groff (1.20.1-4)
  [2010-05-28 12:42] it's recommended to create an initial
  [2010-05-28 12:42] database running as root:
  [2010-05-28 12:42] "/usr/bin/mandb --quiet"
  [2010-05-28 14:42] installed man-db (2.5.7-1)
  [2010-05-28 14:42] installed man-pages (3.24-1)
  [2010-05-28 14:42] installed mdadm (3.1.2-2)
  [2010-05-28 14:42] installed nano (2.2.4-1)
  [2010-05-28 14:42] installed xz-utils (4.999.9beta-2)
  [2010-05-28 14:42] installed openssl (1.0.0-2)
  [2010-05-28 14:42] installed expat (2.0.1-5)
  [2010-05-28 14:42] installed libarchive (2.8.3-3)
  [2010-05-28 14:42] installed libfetch (2.30-3)
  [2010-05-28 14:42] installed pacman-mirrorlist (20100131-1)
  [2010-05-28 14:42] installed pacman (3.3.3-5)
  [2010-05-28 14:42] installed pciutils (3.1.7-1)
  [2010-05-28 14:42] installed sysfsutils (2.1.0-5)
  [2010-05-28 14:42] installed pcmciautils (016-1)
  [2010-05-28 14:42] installed libnl (1.1-2)
  [2010-05-28 14:42] installed libpcap (1.1.1-1)
  [2010-05-28 14:42] installed ppp (2.4.5-1)
  [2010-05-28 14:42] installed procps (3.2.8-1)
  [2010-05-28 14:42] installed psmisc (22.11-1)
  [2010-05-28 14:42] installed reiserfsprogs (3.6.21-2)
  [2010-05-28 12:42] >>> The kernel-mode plugin has a new place.
  [2010-05-28 12:42] >>> It's now located under /usr/lib/rp-pppoe/rp-pppoe.so
  [2010-05-28 12:42] >>> Change LINUX_PLUGIN to the new path in your /etc/ppp/pppoe.conf
  [2010-05-28 14:42] installed rp-pppoe (3.10-5)
  [2010-05-28 14:42] installed eventlog (0.2.9-1)
  [2010-05-28 14:42] installed tcp_wrappers (7.6-11)
  [2010-05-28 14:42] installed syslog-ng (3.1.0-1)
  [2010-05-28 14:42] installed tar (1.23-1)
  [2010-05-28 14:42] installed usbutils (0.87-1)
  [2010-05-28 14:42] installed vi (050325-3)
  [2010-05-28 14:42] installed wget (1.12-2)
  [2010-05-28 14:42] installed dbus-core (1.2.24-1)
  [2010-05-28 14:42] installed wpa_supplicant (0.6.10-2)
  [2010-05-28 14:42] installed xfsprogs (3.1.1-1)
  [2010-05-28 14:42] installed m4 (1.4.14-1)
  [2010-05-28 14:42] installed autoconf (2.65-2)
  [2010-05-28 14:42] installed automake (1.11.1-1)
  [2010-05-28 14:42] installed bin86 (0.16.17-4)
  [2010-05-28 14:42] installed bison (2.4.2-1)
  [2010-05-28 14:42] installed ed (1.4-2)
  [2010-05-28 14:42] installed fakeroot (1.14.4-2)
  [2010-05-28 14:42] installed flex (2.5.35-3)
  [2010-05-28 14:42] installed mpfr (2.4.2-2)
  [2010-05-28 14:42] installed libmpc (0.8.1-2)
  [2010-05-28 14:42] installed ppl (0.10.2-3)
  [2010-05-28 14:42] installed cloog-ppl (0.15.9-1)
  [2010-05-28 14:42] installed libelf (0.8.13-1)
  [2010-05-28 14:42] installed gcc (4.5.0-1)
  [2010-05-28 14:42] installed libtool (2.2.6b-3)
  [2010-05-28 14:42] installed make (3.81-5)
  [2010-05-28 14:42] installed patch (2.6.1-1)
  [2010-05-28 14:42] installed pkgconfig (0.23-2)
  [2010-05-28 14:42] installed ar9170-fw (1.0-2)
  [2010-05-28 14:42] installed b43-fwcutter (013-1)
  [2010-05-28 14:42] installed bridge-utils (1.4-3)
  [2010-05-28 14:42] installed run-parts (3.2.2-1)
  [2010-05-28 12:42] Clearing symlinks in /etc/ssl/certs...done.
  [2010-05-28 12:42] Updating certificates in /etc/ssl/certs... 141 added, 0 removed; done.
  [2010-05-28 12:42] Running hooks in /etc/ca-certificates/update.d....done.
  [2010-05-28 14:42] installed ca-certificates (20090814-3)
  [2010-05-28 14:42] installed wireless-regdb (2009.11.25-1)
  [2010-05-28 14:42] installed iw (0.9.18-1)
  [2010-05-28 12:42] Uncomment the right regulatory domain in /etc/conf.d/wireless-regdom.
  [2010-05-28 12:42] It will automatically be set when necessary.
  [2010-05-28 14:42] installed crda (1.1.0-1)
  [2010-05-28 14:42] installed dialog (1.1_20100119-2)
  [2010-05-28 14:42] installed dmraid (1.0.0.rc16+CVS-2)
  [2010-05-28 14:42] installed dnsutils (9.6.1-3)
  [2010-05-28 14:42] installed gcc-ada (4.5.0-1)
  [2010-05-28 14:42] installed gcc-fortran (4.5.0-1)
  [2010-05-28 14:42] installed gcc-objc (4.5.0-1)
  [2010-05-28 14:42] installed gpm (1.20.6-5)
  [2010-05-28 14:42] installed hdparm (9.28-1)
  [2010-05-28 14:42] installed sqlite3 (3.6.23.1-1)
  [2010-05-28 14:42] installed heimdal (1.3.2-1)
  [2010-05-28 14:42] installed ifenslave (1.1.0-5)
  [2010-05-28 14:42] installed inetutils (1.7-3)
  [2010-05-28 14:42] installed linux-atm (2.5.1-1)
  [2010-05-28 14:42] installed iproute2 (2.6.33-1)
  [2010-05-28 14:42] installed iptables (1.4.7-1)
  [2010-05-28 14:42] installed kernel26-headers (2.6.33.4-1)
  [2010-05-28 14:42] installed udev-compat (151-3)
  [2010-05-28 12:42] >>> Updating module dependencies. Please wait ...
  [2010-05-28 12:42] >>> MKINITCPIO SETUP
  [2010-05-28 12:42] >>> ----------------
  [2010-05-28 12:42] >>> If you use LVM2, Encrypted root or software RAID,
  [2010-05-28 12:42] >>> Ensure you enable support in /etc/mkinitcpio.conf .
  [2010-05-28 12:42] >>> More information about mkinitcpio setup can be found here:
  [2010-05-28 12:42] >>> http://wiki.archlinux.org/index.php/Mkinitcpio
  [2010-05-28 12:42] 
  [2010-05-28 12:42] >>> Generating initial ramdisk, using mkinitcpio.  Please wait...
  [2010-05-28 12:42] > Building image "default"
  [2010-05-28 12:42] > Running command: /sbin/mkinitcpio -k 2.6.27-lts -c /etc/mkinitcpio.conf -g /boot/kernel26-lts.img
  [2010-05-28 12:42] :: Begin build
  [2010-05-28 12:42] :: Parsing hook [base]
  [2010-05-28 12:42] :: Parsing hook [udev]
  [2010-05-28 12:42] :: Parsing hook [autodetect]
  [2010-05-28 12:42] :: Parsing hook [pata]
  [2010-05-28 12:42] :: Parsing hook [scsi]
  [2010-05-28 12:42] :: Parsing hook [sata]
  [2010-05-28 12:42] :: Parsing hook [filesystems]
  [2010-05-28 12:42] :: Generating module dependencies
  [2010-05-28 12:42] :: Generating image '/boot/kernel26-lts.img'...SUCCESS
  [2010-05-28 12:42] > SUCCESS
  [2010-05-28 12:42] > Building image "fallback"
  [2010-05-28 12:42] > Running command: /sbin/mkinitcpio -k 2.6.27-lts -c /etc/mkinitcpio.conf -g /boot/kernel26-lts-fallback.img -S autodetect
  [2010-05-28 12:42] :: Begin build
  [2010-05-28 12:42] :: Parsing hook [base]
  [2010-05-28 12:42] :: Parsing hook [udev]
  [2010-05-28 12:42] :: Parsing hook [pata]
  [2010-05-28 12:42] :: Parsing hook [scsi]
  [2010-05-28 12:42] :: Parsing hook [sata]
  [2010-05-28 12:42] :: Parsing hook [filesystems]
  [2010-05-28 12:42] :: Generating module dependencies
  [2010-05-28 12:42] :: Generating image '/boot/kernel26-lts-fallback.img'...SUCCESS
  [2010-05-28 12:42] > SUCCESS
  [2010-05-28 14:42] installed kernel26-lts (2.6.27.46-1)
  [2010-05-28 14:42] installed kernel26-lts-headers (2.6.27.46-1)
  [2010-05-28 14:42] installed libevent (1.4.13-1)
  [2010-05-28 14:42] installed libgssglue (0.1-2)
  [2010-05-28 14:42] installed libsasl (2.1.23-4)
  [2010-05-28 14:42] installed libldap (2.4.21-2)
  [2010-05-28 14:42] installed librpcsecgss (0.19-3)
  [2010-05-28 14:42] installed libtirpc (0.2.1-1)
  [2010-05-28 14:42] installed links (2.2-4)
  [2010-05-28 14:42] installed mkinitcpio-nfs-utils (0.2-1)
  [2010-05-28 12:42] mlocate command is technically locate, but slocate is symlinked and still works.
  [2010-05-28 12:42] You should run updatedb as root.
  [2010-05-28 14:42] installed mlocate (0.22.4-1)
  [2010-05-28 14:42] installed wireless_tools (29-3)
  [2010-05-28 14:42] installed netcfg (2.5.4-1)
  [2010-05-28 14:42] installed rpcbind (0.2.0-1)
  [2010-05-28 14:42] installed nfsidmap (0.23-3)
  [2010-05-28 12:42]   > PLEASE NOTE:
  [2010-05-28 12:42]   > Extended configuration options for NFS (clients & server) are available in
  [2010-05-28 12:42]   > /etc/conf.d/nfs-common.conf and in /etc/conf.d/nfs-server.conf
  [2010-05-28 12:42]   >
  [2010-05-28 12:42]   > Please refer to http://wiki.archlinux.org/index.php/Nfs
  [2010-05-28 12:42]   > for further information on NFS; for NFSv4, refer to
  [2010-05-28 12:42]   > http://wiki.archlinux.org/index.php/NFSv4   
  [2010-05-28 14:42] installed nfs-utils (1.2.2-2)
  [2010-05-28 14:42] installed openssh (5.4p1-4)
  [2010-05-28 14:42] installed openvpn (2.1.1-2)
  [2010-05-28 14:42] installed pptpclient (1.7.2-2)
  [2010-05-28 14:42] installed procinfo-ng (2.0.304-1)
  [2010-05-28 14:42] installed rfkill (0.4-1)
  [2010-05-28 14:42] installed sdparm (1.05-1)
  [2010-05-28 14:42] installed sudo (1.7.2p6-1)
  [2010-05-28 14:42] installed vpnc (0.5.3-2)
  [2010-05-28 14:42] installed wpa_actiond (1.1-1)
  [2010-05-28 13:44] synchronizing package lists
  [2010-05-28 13:44] starting full system upgrade
  [2010-05-28 13:47] upgraded bash (4.1.005-1 -> 4.1.007-1)
  [2010-05-28 13:47] upgraded dash (0.5.5.1-2 -> 0.5.6-1)
  [2010-05-28 13:47] upgraded dialog (1.1_20100119-2 -> 1.1_20100428-1)
  [2010-05-28 13:47] upgraded e2fsprogs (1.41.11-1 -> 1.41.12-1)
  [2010-05-28 13:47] upgraded libmpc (0.8.1-2 -> 0.8.2-1)
  [2010-05-28 13:47] upgraded gcc (4.5.0-1 -> 4.5.0-2)
  [2010-05-28 13:47] upgraded gcc-ada (4.5.0-1 -> 4.5.0-2)
  [2010-05-28 13:47] upgraded gcc-fortran (4.5.0-1 -> 4.5.0-2)
  [2010-05-28 13:47] upgraded gcc-libs (4.5.0-1 -> 4.5.0-2)
  [2010-05-28 13:47] upgraded gcc-objc (4.5.0-1 -> 4.5.0-2)
  [2010-05-28 13:47] upgraded gettext (0.17-4 -> 0.18-1)
  [2010-05-28 13:47] upgraded inetutils (1.7-3 -> 1.8-1)
  [2010-05-28 13:47] upgraded openssh (5.4p1-4 -> 5.5p1-1)
  [2010-05-28 13:47] upgraded syslog-ng (3.1.0-1 -> 3.1.1-1)
  [2010-05-28 13:47] upgraded tar (1.23-1 -> 1.23-2)
  [2010-05-28 16:04] installed xcb-proto (1.6-1)
  [2010-05-28 16:04] installed xproto (7.0.17-1)
  [2010-05-28 16:04] installed libxdmcp (1.0.3-1)
  [2010-05-28 16:04] installed libxau (1.0.5-1)
  [2010-05-28 16:04] installed libxcb (1.6-1)
  [2010-05-28 16:04] installed kbproto (1.0.4-1)
  [2010-05-28 16:04] installed libx11 (1.3.3-1)
  [2010-05-28 16:04] installed xextproto (7.1.1-1)
  [2010-05-28 16:04] installed fixesproto (4.1.1-1)
  [2010-05-28 16:04] installed libxfixes (4.0.4-1)
  [2010-05-28 16:04] installed renderproto (0.11-1)
  [2010-05-28 16:04] installed libxrender (0.9.5-1)
  [2010-05-28 16:04] installed libxcursor (1.1.10-1)
  [2010-05-28 16:04] installed libxkbfile (1.0.6-1)
  [2010-05-28 16:04] installed libpng (1.4.2-1)
  [2010-05-28 16:04] installed freetype2 (2.3.12-1)
  [2010-05-28 16:04] updating font cache... done.
  [2010-05-28 16:04] installed fontconfig (2.8.0-1)
  [2010-05-28 16:04] installed libxft (2.1.14-1)
  [2010-05-28 16:04] installed libfontenc (1.0.5-1)
  [2010-05-28 16:04] installed libxext (1.1.1-1)
  [2010-05-28 16:04] installed libice (1.0.6-1)
  [2010-05-28 16:04] installed libsm (1.1.1-1)
  [2010-05-28 16:04] installed libxt (1.0.8-1)
  [2010-05-28 16:04] installed libxmu (1.0.5-1)
  [2010-05-28 16:04] installed libxpm (3.5.8-1)
  [2010-05-28 16:04] installed libxaw (1.0.7-1)
  [2010-05-28 16:04] installed xorg-apps (7.5-3)
  [2010-05-28 16:04] installed xorg-xkb-utils (7.5-2)
  [2010-05-28 16:04] installed damageproto (1.2.0-1)
  [2010-05-28 16:04] installed libxdamage (1.1.2-1)
  [2010-05-28 16:04] installed libdrm (2.4.19-2)
  [2010-05-28 16:04] installed xf86vidmodeproto (2.3-1)
  [2010-05-28 16:04] installed libxxf86vm (1.1.0-1)
  [2010-05-28 16:04] installed libgl (7.7.1-1)
  [2010-05-28 16:04] installed videoproto (2.3.0-1)
  [2010-05-28 16:04] installed libxv (1.0.5-1)
  [2010-05-28 16:04] installed libxvmc (1.0.5-1)
  [2010-05-28 16:04] installed audiofile (0.2.7-1)
  [2010-05-28 16:04] installed alsa-lib (1.0.23-1)
  [2010-05-28 16:04] installed esound (0.2.41-1)
  [2010-05-28 16:04] installed libogg (1.2.0-1)
  [2010-05-28 16:04] installed flac (1.2.1-2)
  [2010-05-28 16:04] installed libvorbis (1.3.1-1)
  [2010-05-28 16:04] installed sdl (1.2.14-4)
  [2010-05-28 16:04] installed libjpeg (8.0.1-1)
  [2010-05-28 16:04] installed libmng (1.0.10-3)
  [2010-05-28 16:04] installed libtheora (1.1.1-1)
  [2010-05-28 16:04] installed wavpack (4.60.1-1)
  [2010-05-28 16:04] installed faad2 (2.7-1)
  [2010-05-28 16:04] installed lame (3.98.4-1)
  [2010-05-28 16:04] installed libmp4v2 (1.9.1-1)
  [2010-05-28 16:04] installed faac (1.28-2)
  [2010-05-28 16:04] installed xvidcore (1.2.2-1)
  [2010-05-28 16:04] installed x264 (20100524-1)
  [2010-05-28 16:04] installed opencore-amr (0.1.2-1)
  [2010-05-28 16:04] installed libvdpau (0.4-1)
  [2010-05-28 16:04] installed orc (0.4.4-1)
  [2010-05-28 16:04] installed schroedinger (1.0.9-1)
  [2010-05-28 16:04] installed ffmpeg (23328-1)
  [2010-05-28 16:04] installed xine-lib (1.1.18.1-1)
  [2010-05-28 16:04] installed atk (1.30.0-1)
  [2010-05-28 16:04] installed pixman (0.18.2-1)
  [2010-05-28 16:04] installed xcb-util (0.3.6-1)
  [2010-05-28 16:04] installed cairo (1.8.10-1)
  [2010-05-28 16:04] installed libdatrie (0.2.3-1)
  [2010-05-28 16:04] installed libthai (0.1.14-1)
  [2010-05-28 16:04] installed pango (1.28.0-1)
  [2010-05-28 16:04] installed xineramaproto (1.2-1)
  [2010-05-28 16:04] installed libxinerama (1.1-1)
  [2010-05-28 16:04] installed randrproto (1.3.1-1)
  [2010-05-28 16:04] installed libxrandr (1.3.0-1)
  [2010-05-28 16:04] installed inputproto (2.0-1)
  [2010-05-28 16:04] installed libxi (1.3-2)
  [2010-05-28 16:04] installed compositeproto (0.4.1-1)
  [2010-05-28 16:04] installed libxcomposite (0.4.1-1)
  [2010-05-28 16:04] installed libtasn1 (2.6-1)
  [2010-05-28 16:04] installed gnutls (2.8.6-1)
  [2010-05-28 16:04] installed libxml2 (2.7.7-1)
  [2010-05-28 16:04] installed shared-mime-info (0.71-1)
  [2010-05-28 16:04] installed libtiff (3.9.2-2)
  [2010-05-28 16:04] installed dbus (1.2.24-1)
  [2010-05-28 16:04] installed libdaemon (0.14-1)
  [2010-05-28 16:04] adding avahi system group... adding avahi system user... > The following daemons may be added to DAEMONS in /etc/rc.conf:
  [2010-05-28 16:04]  -> avahi-daemon   - the mdns responder, you probably want this.
  [2010-05-28 16:04]                      dbus needs to be running when you start it.
  [2010-05-28 16:04]  -> avahi-dnsconfd - daemon used for peer-to-peer automatic dns
  [2010-05-28 16:04]                      configuration on dhcp-less networks.
  [2010-05-28 16:04] 
  [2010-05-28 16:04] > To use some of the client applications you will have to install python.
  [2010-05-28 16:04]  -> In addition, pygtk is required for the graphical ones and
  [2010-05-28 16:04]     twisted-web for avahi-bookmarks.
  [2010-05-28 16:04] 
  [2010-05-28 16:04] installed avahi (0.6.25-3)
  [2010-05-28 16:04] installed libcups (1.4.3-2)
  [2010-05-28 16:04] installed gtk2 (2.20.1-2)
  [2010-05-28 16:04] installed nspr (4.8.4-1)
  [2010-05-28 16:04] installed spidermonkey (1.7.0-3)
  [2010-05-28 16:04] installed dbus-glib (0.86-1)
  [2010-05-28 16:04] installed hal-info (0.20091130-1)
  [2010-05-28 16:04] installed eject (2.1.5-4)
  [2010-05-28 16:04] installed dmidecode (2.10-1)
  [2010-05-28 16:04] installed libx86 (1.1-2)
  [2010-05-28 16:04] installed vbetool (1.1-1)
  [2010-05-28 16:04] installed pm-quirks (0.20100316-1)
  [2010-05-28 16:04] installed pm-utils (1.3.0-2)
  [2010-05-28 16:04] installed eggdbus (0.6-1)
  [2010-05-28 16:04] installed polkit (0.96-2)
  [2010-05-28 16:04] installed consolekit (0.4.1-2)
  [2010-05-28 16:04] installed hal (0.5.14-2)
  [2010-05-28 16:04] installed desktop-file-utils (0.16-1)
  [2010-05-28 16:04] installed hicolor-icon-theme (0.12-1)
  [2010-05-28 16:04] installed gxine (0.5.905-1)
  [2010-05-28 16:04] installed alsaplayer (0.99.80-3)
  [2010-05-28 16:04] installed alsa-utils (1.0.23-2)
  [2010-05-28 16:04] Install jack-audio-connection-kit, libsamplerate, ffmpeg
  [2010-05-28 16:04] or pulseaudio to get their respective plugins working
  [2010-05-28 16:04] installed alsa-plugins (1.0.23-1)
  [2010-05-28 16:04] installed acpi (1.4-2)
  [2010-05-28 16:04] installed acpid (1.0.10-3)
  [2010-05-28 16:04] installed libstdc++5 (3.3.6-3)
  [2010-05-28 16:04] installed acpitool (0.5.1-1)
  [2010-05-28 16:04] installed rrdtool (1.4.3-1)
  [2010-05-28 16:04] warning: /etc/sensors3.conf saved as /etc/sensors3.conf.pacorig
  [2010-05-28 16:04] >>> to control the lm_sensors daemon type
  [2010-05-28 16:04] >>> "/etc/rc.d/sensors start|stop|restart" 
  [2010-05-28 16:04] >>> --------------------------------------
  [2010-05-28 16:04] >>> before you can use the fancontrol daemon
  [2010-05-28 16:04] >>> first create a fancontrol config file, use "pwmconfig"
  [2010-05-28 16:04] >>> then type "/etc/rc.d/fancontrol start|stop|restart" 
  [2010-05-28 16:04] >>> --------------------------------------
  [2010-05-28 16:04] >>> to decode memory SPD timings modprobe eeprom module
  [2010-05-28 16:04] >>> and get this perl script from
  [2010-05-28 16:04] >>> "http://www.lm-sensors.org/browser/lm-sensors/trunk/prog/eeprom/decode-dimms.pl"
  [2010-05-28 16:04] installed lm_sensors (3.1.2-3)
  [2010-05-28 16:04] installed smartmontools (5.39.1-1)
  [2010-05-28 16:04] installed neon (0.29.3-2)
  [2010-05-28 16:04] installed apr (1.4.2-1)
  [2010-05-28 16:04] installed unixodbc (2.3.0-1)
  [2010-05-28 16:04] installed apr-util (1.3.9-4)
  [2010-05-28 16:04] installed subversion (1.6.9-5)
  [2010-05-28 16:04] installed python (2.6.5-3)
  [2010-05-28 16:04] installed ruby (1.9.1_p378-2)
  [2010-05-28 16:04] installed ntp (4.2.6-3)
  [2010-05-28 16:04] installed curl (7.20.1-1)
  [2010-05-28 16:04] installed hunspell (1.2.11-1)
  [2010-05-28 16:04] installed libgsf (1.14.18-1)
  [2010-05-28 16:04] installed libwpd (0.8.14-1)
  [2010-05-28 16:04] installed icu (4.4.1-1)
  [2010-05-28 16:04] installed hsqldb-java (1.8.1.2-1)
  [2010-05-28 16:04] installed libxslt (1.1.26-1)
  [2010-05-28 16:04] installed recordproto (1.14-1)
  [2010-05-28 16:04] installed libxtst (1.1.0-1)
  [2010-05-28 16:04] The jre package is licensed software.
  [2010-05-28 16:04] You MUST read and agree to the license stored in
  [2010-05-28 16:04] /opt/java/jre/LICENSE before using it.
  [2010-05-28 16:04] installed jre (6u20-1)
  [2010-05-28 16:04] installed beanshell (2.0b4-1)
  [2010-05-28 16:04] installed saxon (9.2.0.6-1)
  [2010-05-28 16:04] installed hdf5 (1.8.4_patch1-1)
  [2010-05-28 16:04] installed fftw (3.2.2-1)
  [2010-05-28 16:04] installed vigra (1.7.0-1)
  [2010-05-28 16:04] installed libgraphite (2.3.1-1)
  [2010-05-28 16:04] installed hyphen (2.5-1)
  [2010-05-28 16:04] installed lpsolve (5.5.0.15-1)
  [2010-05-28 16:04] installed libmspack (0.0.20060920alpha-2)
  [2010-05-28 16:04] installed lucene (2.9.2-1)
  [2010-05-28 16:04]  * check /etc/profile.d/openoffice.sh, then relogin or "source" the file
  [2010-05-28 16:04]  * see http://wiki.archlinux.org/index.php/Openoffice
  [2010-05-28 16:04]    how to use extensions, e.g. for spell checking
  [2010-05-28 16:04]    see /usr/lib/openoffice/share/extension/install what
  [2010-05-28 16:04]    is shipped with this package
  [2010-05-28 16:04]  * make sure you have installed a ttf font (ttf-dejavu recommended)
  [2010-05-28 16:04] installed openoffice-base (3.2.0-3)
  [2010-05-28 16:04] installed openoffice-de (3.2.0-1)
  [2010-05-28 16:04] installed vuze (4.4.0.4-1)
  [2010-05-28 16:04] relogin or source /etc/profile.d/mozilla-common.sh
  [2010-05-28 16:04] installed mozilla-common (1.4-1)
  [2010-05-28 16:04] installed nss (3.12.6-3)
  [2010-05-28 16:04] installed flashplugin (10.0.45.2-1)
  [2010-05-28 16:04] installed libidl2 (0.8.14-1)
  [2010-05-28 16:04] installed orbit2 (2.14.18-1)
  [2010-05-28 16:04] installed gconf (2.28.1-1)
  [2010-05-28 16:04] installed gtksourceview2 (2.10.1-1)
  [2010-05-28 16:04] installed libglade (2.6.4-1)
  [2010-05-28 16:04] installed pycairo (1.8.8-1)
  [2010-05-28 16:04] installed libffi (3.0.9-1)
  [2010-05-28 16:04] installed pygobject (2.21.1-1)
  [2010-05-28 16:04] installed pygtk (2.17.0-1)
  [2010-05-28 16:04] installed pygtksourceview2 (2.10.1-1)
  [2010-05-28 16:04] > aspell comes with no default dictionary
  [2010-05-28 16:04] installed aspell (0.60.6-4)
  [2010-05-28 16:04] installed enchant (1.6.0-1)
  [2010-05-28 16:04] installed iso-codes (3.14-1)
  [2010-05-28 16:04] installed gedit (2.30.2-1)
  [2010-05-28 16:04] installed vte (0.24.1-1)
  [2010-05-28 16:04] installed gucharmap (2.30.1-1)
  [2010-05-28 16:04] installed pyorbit (2.24.0-2)
  [2010-05-28 16:04] installed libart-lgpl (2.3.21-1)
  [2010-05-28 16:04] installed libgnomecanvas (2.30.1-1)
  [2010-05-28 16:04] installed fam (2.7.0-14)
  [2010-05-28 16:04] installed tdb (1.2.1-1)
  [2010-05-28 16:04] installed talloc (2.0.1-1)
  [2010-05-28 16:04] installed smbclient (3.5.2-1)
  [2010-05-28 16:04] installed gnome-mime-data (2.18.0-4)
  [2010-05-28 16:04] installed gnome-vfs (2.24.3-2)
  [2010-05-28 16:04] installed libbonobo (2.24.3-1)
  [2010-05-28 16:04] installed gnome-keyring (2.30.1-2)
  [2010-05-28 16:04] installed libgnome-keyring (2.30.1-1)
  [2010-05-28 16:04] installed libsoup (2.30.1-1)
  [2010-05-28 16:04] installed libproxy (0.3.1-1)
  [2010-05-28 16:04] installed libsoup-gnome (2.30.1-1)
  [2010-05-28 16:04] installed libunique (1.1.6-2)
  [2010-05-28 16:04] installed sg3_utils (1.28-1)
  [2010-05-28 16:04] installed parted (2.2-1)
  [2010-05-28 16:04] installed libatasmart (0.17-1)
  [2010-05-28 16:04] installed lsof (4.83-1)
  [2010-05-28 16:04] installed udisks (1.0.1-1)
  [2010-05-28 16:04] installed libnotify (0.4.5-1)
  [2010-05-28 16:04] installed gnome-disk-utility (2.30.1-1)
  [2010-05-28 16:04] installed libcddb (1.3.2-2)
  [2010-05-28 16:04] installed libcdio (0.82-1)
  [2010-05-28 16:04] > You must load the fuse kernel module to use FUSE.
  [2010-05-28 16:04]  -> Run 'modprobe fuse' to load the module now.
  [2010-05-28 16:04]  -> Add fuse to $MODULES in /etc/rc.conf to load on every boot.
  [2010-05-28 16:04] > You will need a /dev/fuse device node to use FUSE.
  [2010-05-28 16:04]  -> If you use udev, nothing needs to be done
  [2010-05-28 16:04]  -> For a static /dev, run: mknod /dev/fuse -m 0666 c 10 229
  [2010-05-28 16:04] installed fuse (2.8.4-1)
  [2010-05-28 16:04] installed gvfs (1.6.2-1)
  [2010-05-28 16:05] installed libgnome (2.30.0-1)
  [2010-05-28 16:05] installed libbonoboui (2.24.3-1)
  [2010-05-28 16:05] installed libgnomeui (2.24.3-1)
  [2010-05-28 16:05] installed gnome-python (2.28.1-1)
  [2010-05-28 16:05] installed gedit-plugins (2.30.0-1)
  [2010-05-28 16:05] installed dbus-python (0.83.1-1)
  [2010-05-28 16:05] installed gedit-plugins-extra (2.24.1-5)
  [2010-05-28 16:05] installed giflib (4.1.6-3)
  [2010-05-28 16:05] installed libid3tag (0.15.1b-4)
  [2010-05-28 16:05] installed imlib2 (1.4.4-1)
  [2010-05-28 16:05] installed fluxbox (1.1.1-1)
  [2010-05-28 16:05] installed unzip (6.0-5)
  [2010-05-28 16:05] installed unrar (3.9.10-1)
  [2010-05-28 16:05] installed htop (0.8.3-1)
  [2010-05-28 16:05] installed wireshark (1.2.8-1)
  [2010-05-28 16:05] installed zsh (4.3.10-3)
  [2010-05-28 16:05] installed sdl_ttf (2.0.9-2)
  [2010-05-28 16:05] installed sdl_net (1.2.7-3)
  [2010-05-28 16:05] installed libmikmod (3.1.12-3)
  [2010-05-28 16:05] installed smpeg (0.4.4-5)
  [2010-05-28 16:05] installed sdl_mixer (1.2.11-2)
  [2010-05-28 16:05] installed sdl_image (1.2.10-2)
  [2010-05-28 16:05] installed fribidi (0.19.2-1)
  [2010-05-28 16:05] installed boost (1.41.0-1)
  [2010-05-28 16:05] installed lua (5.1.4-4)
  [2010-05-28 16:05] Note:
  [2010-05-28 16:05] > If you experience sound problems try setting your SDL_AUDIODRIVER environment variable to "dma"
  [2010-05-28 16:05] > eg. export SDL_AUDIODRIVER="dma" ; wesnoth
  [2010-05-28 16:05] > If "dma" doesn't work,other options are: dsp,alsa,artsc,esd,nas try to find the right output.
  [2010-05-28 16:05] installed wesnoth (1.8.1-1)
  [2010-05-28 16:05] installed gd (2.0.36RC1-3)
  [2010-05-28 16:05] installed libcroco (0.6.2-1)
  [2010-05-28 16:05] installed librsvg (2.26.3-1)
  [2010-05-28 16:05] installed dri2proto (2.1-2)
  [2010-05-28 16:05] installed mesa (7.7.1-1)
  [2010-05-28 16:05] installed freeglut (2.6.0-1)
  [2010-05-28 16:05] installed jasper (1.900.1-5)
  [2010-05-28 16:05] installed ghostscript (8.71-3)
  [2010-05-28 16:05] installed graphviz (2.26.3-1)
  [2010-05-28 16:06] The jdk package is licensed software.
  [2010-05-28 16:06] You MUST read and agree to the license stored in
  [2010-05-28 16:06] /opt/java/LICENSE before using it.
  [2010-05-28 16:06] installed jdk (6u20-1)
  [2010-05-28 16:06] installed startup-notification (0.10-1)
  [2010-05-28 16:06] warning: /etc/mime.types saved as /etc/mime.types.pacorig
  [2010-05-28 16:06] installed mime-types (1.0-3)
  [2010-05-28 16:06] installed xulrunner (1.9.2.3-1)
  [2010-05-28 16:06] installed firefox (3.6.3-1)
  [2010-05-28 16:06] installed thunderbird (3.0.4-1)
  [2010-05-28 16:06] installed eclipse (3.5.2-1)
  [2010-05-28 16:06] installed eclipse-cdt (6.0.2-1)
  [2010-05-28 16:06] installed lcms (1.18-3)
  [2010-05-28 16:06] installed fontsproto (2.1.0-1)
  [2010-05-28 16:06] installed libxfont (1.4.1-1)
  [2010-05-28 16:06] installed xorg-font-utils (7.5-2)
  [2010-05-28 16:06] Updating font cache... done.
  [2010-05-28 16:06] installed gsfonts (1.0.7pre44-2)
  [2010-05-28 16:06] installed libwmf (0.2.8.4-7)
  [2010-05-28 16:06] installed libexif (0.6.19-1)
  [2010-05-28 16:06] installed babl (0.1.2-1)
  [2010-05-28 16:06] installed gegl (0.1.2-1)
  [2010-05-28 16:06] installed gimp (2.6.8-4)
  [2010-05-28 16:06] installed kdeaccessibility-colorschemes (4.4.3-1)
  [2010-05-28 16:06] installed kdeaccessibility-iconthemes (4.4.3-1)
  [2010-05-28 16:06] installed ilmbase (1.0.1-1)
  [2010-05-28 16:06] installed openexr (1.6.1-1)
  [2010-05-28 16:06] installed xdg-utils (1.0.2.20100303-1)
  [2010-05-28 16:06] installed qt (4.6.2-4)
  [2010-05-28 16:06] installed clucene (0.9.21b-1)
  [2010-05-28 16:06] installed exiv2 (0.19-1)
  [2010-05-28 16:06] installed strigi (0.7.2-2)
  [2010-05-28 16:06] installed raptor (1.4.21-1)
  [2010-05-28 16:06] installed postgresql-libs (8.4.4-1)
  [2010-05-28 16:06] installed libmysqlclient (5.1.46-2)
  [2010-05-28 16:06] installed rasqal (0.9.19-1)
  [2010-05-28 16:06] installed redland (1.0.10-2)
  [2010-05-28 16:06] installed libiodbc (3.52.7-3)
  [2010-05-28 16:06] installed virtuoso (6.1.1-1)
  [2010-05-28 16:06] installed soprano (2.4.3-1)
  [2010-05-28 16:06] installed qca (2.0.2-2)
  [2010-05-28 16:06] installed polkit-qt (0.95.1-1)
  [2010-05-28 16:06] installed scrnsaverproto (1.2.0-1)
  [2010-05-28 16:06] installed libxss (1.2.0-1)
  [2010-05-28 16:06] installed gstreamer0.10 (0.10.29-1)
  [2010-05-28 16:06] installed liboil (0.3.17-1)
  [2010-05-28 16:06] installed gstreamer0.10-base (0.10.29-1)
  [2010-05-28 16:06] installed cdparanoia (10.2-2)
  [2010-05-28 16:06] installed libvisual (0.4.0-3)
  [2010-05-28 16:06] installed gstreamer0.10-base-plugins (0.10.29-1)
  [2010-05-28 16:06] installed phonon-gstreamer (4.4.1-1)
  [2010-05-28 16:06] installed phonon (4.4.1-1)
  [2010-05-28 16:06] installed shared-desktop-ontologies (0.5-1)
  [2010-05-28 16:06] installed attica (0.1.4-1)
  [2010-05-28 16:07] installed kdelibs (4.4.3-2)
  [2010-05-28 16:07] installed oxygen-icons (4.4.3-1)
  [2010-05-28 16:07] installed xorg-xauth (1.0.4-1)
  [2010-05-28 16:07] installed rarian (0.8.1-1)
  [2010-05-28 16:07] installed libssh (0.4.1-3)
  [2010-05-28 16:07] installed kdebase-runtime (4.4.3-1)
  [2010-05-28 16:07] installed kdeaccessibility-kmag (4.4.3-1)
  [2010-05-28 16:07] installed kdeaccessibility-kmousetool (4.4.3-1)
  [2010-05-28 16:07] installed kdeaccessibility-kmouth (4.4.3-1)
  [2010-05-28 16:07] installed kdeadmin-kcron (4.4.3-1)
  [2010-05-28 16:07] installed kdeadmin-ksystemlog (4.4.3-1)
  [2010-05-28 16:07] installed mysql-clients (5.1.46-2)
  [2010-05-28 16:07] warning: /etc/mysql/my.cnf saved as /etc/mysql/my.cnf.pacorig
  [2010-05-28 16:07] WARNING: The host 'Lab1' could not be looked up with resolveip.
  [2010-05-28 16:07] This probably means that your libc libraries are not 100 % compatible
  [2010-05-28 16:07] with this binary MySQL version. The MySQL daemon, mysqld, should work
  [2010-05-28 16:07] normally with the exception that host name resolving will not work.
  [2010-05-28 16:07] This means that you should use IP addresses instead of hostnames
  [2010-05-28 16:07] when specifying MySQL privileges !
  [2010-05-28 16:07] Installing MySQL system tables...
  [2010-05-28 16:07] OK
  [2010-05-28 16:07] Filling help tables...
  [2010-05-28 16:07] OK
  [2010-05-28 16:07] 
  [2010-05-28 16:07] To start mysqld at boot time you have to copy
  [2010-05-28 16:07] support-files/mysql.server to the right place for your system
  [2010-05-28 16:07] 
  [2010-05-28 16:07] PLEASE REMEMBER TO SET A PASSWORD FOR THE MySQL root USER !
  [2010-05-28 16:07] To do so, start the server, then issue the following commands:
  [2010-05-28 16:07] 
  [2010-05-28 16:07] /usr/bin/mysqladmin -u root password 'new-password'
  [2010-05-28 16:07] /usr/bin/mysqladmin -u root -h Lab1 password 'new-password'
  [2010-05-28 16:07] 
  [2010-05-28 16:07] Alternatively you can run:
  [2010-05-28 16:07] /usr/bin/mysql_secure_installation
  [2010-05-28 16:07] 
  [2010-05-28 16:07] which will also give you the option of removing the test
  [2010-05-28 16:07] databases and anonymous user created by default.  This is
  [2010-05-28 16:07] strongly recommended for production servers.
  [2010-05-28 16:07] 
  [2010-05-28 16:07] See the manual for more instructions.
  [2010-05-28 16:07] 
  [2010-05-28 16:07] You can start the MySQL daemon with:
  [2010-05-28 16:07] cd /usr ; /usr/bin/mysqld_safe &
  [2010-05-28 16:07] 
  [2010-05-28 16:07] You can test the MySQL daemon with mysql-test-run.pl
  [2010-05-28 16:07] cd /usr/mysql-test ; perl mysql-test-run.pl
  [2010-05-28 16:07] 
  [2010-05-28 16:07] Please report any problems with the /usr/bin/mysqlbug script!
  [2010-05-28 16:07] 
  [2010-05-28 16:07] installed mysql (5.1.46-2)
  [2010-05-28 16:07] installed akonadi (1.3.1-3)
  [2010-05-28 16:07] installed libical (0.44-1)
  [2010-05-28 16:07] installed pth (2.0.7-3)
  [2010-05-28 16:07] installed gnupg (1.4.10-2)
  [2010-05-28 16:07] installed libksba (1.0.7-1)
  [2010-05-28 16:07] installed libassuan (2.0.0-1)
  [2010-05-28 16:07] installed pinentry (0.8.0-1)
  [2010-05-28 16:07] installed dirmngr (1.1.0rc1-1)
  [2010-05-28 16:07] installed gnupg2 (2.0.15-1)
  [2010-05-28 16:07] installed gpgme (1.3.0-1)
  [2010-05-28 16:07] installed kdepimlibs (4.4.3-1)
  [2010-05-28 16:07] installed kdepim-runtime (4.4.3-1)
  [2010-05-28 16:07] installed kdeadmin-kuser (4.4.3-1)
  [2010-05-28 16:07] installed sip (4.10.2-1)
  [2010-05-28 16:07] installed qscintilla (2.4.3-1)
  [2010-05-28 16:07] installed pyqt (4.7.3-1)
  [2010-05-28 16:07] installed kdebindings-python (4.4.3-1)
  [2010-05-28 16:07] installed pycups (1.9.49-1)
  [2010-05-28 16:07] installed pysmbc (1.0.6-3)
  [2010-05-28 16:07] installed system-config-printer-common (1.2.1-1)
  [2010-05-28 16:07] installed kdeadmin-system-config-printer-kde (4.4.3-1)
  [2010-05-28 16:07] installed kdeartwork-colorschemes (4.4.3-1)
  [2010-05-28 16:07] installed kdeartwork-desktopthemes (4.4.3-1)
  [2010-05-28 16:07] installed kdeartwork-emoticons (4.4.3-1)
  [2010-05-28 16:07] installed kdeartwork-iconthemes (4.4.3-1)
  [2010-05-28 16:07] installed polkit-kde (0.95.1-2)
  [2010-05-28 16:07] installed qimageblitz (0.0.5-1)
  [2010-05-28 16:07] installed xf86miscproto (0.9.3-1)
  [2010-05-28 16:07] installed libxxf86misc (1.0.2-1)
  [2010-05-28 16:07] installed xkeyboard-config (1.8-1)
  [2010-05-28 16:07] installed libxklavier (5.0-1)
  [2010-05-28 16:07] installed xf86dgaproto (2.1-1)
  [2010-05-28 16:07] installed libxxf86dga (1.1.1-1)
  [2010-05-28 16:07] installed dmxproto (2.3-1)
  [2010-05-28 16:07] installed libdmx (1.1.0-1)
  [2010-05-28 16:07] installed xorg-utils (7.6-1)
  [2010-05-28 16:07] installed kdebase-workspace (4.4.3-2)
  [2010-05-28 16:07] installed kdeartwork-kscreensaver (4.4.3-1)
  [2010-05-28 16:07] installed kdeartwork-sounds (4.4.3-1)
  [2010-05-28 16:07] installed kdeartwork-styles (4.4.3-1)
  [2010-05-28 16:07] installed kdeartwork-wallpapers (4.4.3-1)
  [2010-05-28 16:07] installed kdeartwork-weatherwallpapers (4.4.3-1)
  [2010-05-28 16:07] installed kdebase-lib (4.4.3-1)
  [2010-05-28 16:07] installed kdebase-dolphin (4.4.3-1)
  [2010-05-28 16:07] installed kdebase-kappfinder (4.4.3-1)
  [2010-05-28 16:07] installed kdebase-kdepasswd (4.4.3-1)
  [2010-05-28 16:07] installed kdebase-kdialog (4.4.3-1)
  [2010-05-28 16:07] installed kdebase-kfind (4.4.3-1)
  [2010-05-28 16:07] installed libraw1394 (2.0.5-1)
  [2010-05-28 16:07] installed kdebase-kinfocenter (4.4.3-1)
  [2010-05-28 16:07] installed kdebase-konqueror (4.4.3-1)
  [2010-05-28 16:07] installed kdebase-konsole (4.4.3-1)
  [2010-05-28 16:07] installed kdebase-kwrite (4.4.3-1)
  [2010-05-28 16:07] installed kdebase-plasma (4.4.3-1)
  [2010-05-28 16:07] installed kdeedu-libkdeedu (4.4.3-1)
  [2010-05-28 16:07] installed kdeedu-blinken (4.4.3-1)
  [2010-05-28 16:07] installed libspectre (0.2.4-1)
  [2010-05-28 16:07] installed kdeedu-cantor (4.4.3-1)
  [2010-05-28 16:07] installed kdeedu-kalgebra (4.4.3-1)
  [2010-05-28 16:07] installed openbabel (2.2.3-1)
  [2010-05-28 16:07] installed kdeedu-kalzium (4.4.3-1)
  [2010-05-28 16:07] installed kdeedu-data (4.4.3-1)
  [2010-05-28 16:07] installed kdeedu-kanagram (4.4.3-1)
  [2010-05-28 16:07] installed kdeedu-kbruch (4.4.3-1)
  [2010-05-28 16:07] installed kdeedu-kgeography (4.4.3-1)
  [2010-05-28 16:07] installed kdeedu-khangman (4.4.3-1)
  [2010-05-28 16:07] installed kdeedu-kig (4.4.3-1)
  [2010-05-28 16:07] installed kdeedu-kiten (4.4.3-1)
  [2010-05-28 16:07] installed kdeedu-klettres (4.4.3-1)
  [2010-05-28 16:07] installed kdeedu-kmplot (4.4.3-1)
  [2010-05-28 16:07] installed libnova (0.13.0-1)
  [2010-05-28 16:07] installed cfitsio (3240-1)
  [2010-05-28 16:07] installed libindi (0.6.1-1)
  [2010-05-28 16:07] installed kdeedu-kstars (4.4.3-1)
  [2010-05-28 16:07] installed kdeedu-ktouch (4.4.3-1)
  [2010-05-28 16:07] installed kdeedu-kturtle (4.4.3-1)
  [2010-05-28 16:07] installed kdeedu-kwordquiz (4.4.3-1)
  [2010-05-28 16:07] installed kdeedu-marble (4.4.3-1)
  [2010-05-28 16:07] installed kdeedu-parley (4.4.3-1)
  [2010-05-28 16:07] installed kdeedu-rocs (4.4.3-1)
  [2010-05-28 16:07] installed gsl (1.14-1)
  [2010-05-28 16:07] installed cln (1.2.2-3)
  [2010-05-28 16:07] installed libqalculate (0.9.7-1)
  [2010-05-28 16:07] installed kdeedu-step (4.4.3-1)
  [2010-05-28 16:07] installed kdegames-libkdegames (4.4.3-1)
  [2010-05-28 16:07] installed kdegames-bomber (4.4.3-1)
  [2010-05-28 16:07] installed kdegames-bovo (4.4.3-1)
  [2010-05-28 16:08] installed kdegames-granatier (4.4.3-1)
  [2010-05-28 16:08] installed kdegames-kapman (4.4.3-1)
  [2010-05-28 16:08] installed kdegames-katomic (4.4.3-1)
  [2010-05-28 16:08] installed libggz (0.0.14.1-1)
  [2010-05-28 16:08] installed ggz-client-libs (0.0.14.1-1)
  [2010-05-28 16:08] installed kdegames-kbattleship (4.4.3-1)
  [2010-05-28 16:08] installed kdegames-kblackbox (4.4.3-1)
  [2010-05-28 16:08] installed kdegames-kblocks (4.4.3-1)
  [2010-05-28 16:08] installed kdegames-kbounce (4.4.3-1)
  [2010-05-28 16:08] installed kdegames-kbreakout (4.4.3-1)
  [2010-05-28 16:08] installed kdegames-kdiamond (4.4.3-1)
  [2010-05-28 16:08] installed kdegames-kfourinline (4.4.3-1)
  [2010-05-28 16:08] installed kdegames-kgoldrunner (4.4.3-1)
  [2010-05-28 16:08] installed gnugo (3.8-1)
  [2010-05-28 16:08] installed kdegames-kigo (4.4.3-1)
  [2010-05-28 16:08] installed kdegames-killbots (4.4.3-1)
  [2010-05-28 16:08] installed kdegames-kiriki (4.4.3-1)
  [2010-05-28 16:08] installed kdegames-kjumpingcube (4.4.3-1)
  [2010-05-28 16:08] installed kdegames-klines (4.4.3-1)
  [2010-05-28 16:08] installed kdegames-libkmahjongg (4.4.3-1)
  [2010-05-28 16:08] installed kdegames-kmahjongg (4.4.3-1)
  [2010-05-28 16:08] installed kdegames-kmines (4.4.3-1)
  [2010-05-28 16:08] installed kdegames-knetwalk (4.4.3-1)
  [2010-05-28 16:08] installed kdegames-kolf (4.4.3-1)
  [2010-05-28 16:08] installed kdegames-kollision (4.4.3-1)
  [2010-05-28 16:08] installed kdegames-konquest (4.4.3-1)
  [2010-05-28 16:08] installed kdegames-kpat (4.4.3-1)
  [2010-05-28 16:08] installed kdegames-kreversi (4.4.3-1)
  [2010-05-28 16:08] installed kdegames-ksame (4.4.3-1)
  [2010-05-28 16:08] installed kdegames-kshisen (4.4.3-1)
  [2010-05-28 16:08] installed kdegames-ksirk (4.4.3-1)
  [2010-05-28 16:08] installed kdegames-kspaceduel (4.4.3-1)
  [2010-05-28 16:08] installed kdegames-ksquares (4.4.3-1)
  [2010-05-28 16:08] installed kdegames-ksudoku (4.4.3-1)
  [2010-05-28 16:08] installed kdegames-ktron (4.4.3-1)
  [2010-05-28 16:08] installed kdegames-ktuberling (4.4.3-1)
  [2010-05-28 16:08] installed kdegames-kubrick (4.4.3-1)
  [2010-05-28 16:08] installed kdegames-lskat (4.4.3-1)
  [2010-05-28 16:08] installed kdegames-palapeli (4.4.3-1)
  [2010-05-28 16:08] NOTE
  [2010-05-28 16:08] ----
  [2010-05-28 16:08] Add your user to group 'camera' to use camera devices.
  [2010-05-28 16:08] installed libgphoto2 (2.4.9-1)
  [2010-05-28 16:08] installed libieee1284 (0.2.11-2)
  [2010-05-28 16:08] installed libv4l (0.6.4-1)
  [2010-05-28 16:08] warning: /etc/sane.d/epjitsu.conf saved as /etc/sane.d/epjitsu.conf.pacorig
  [2010-05-28 16:08] warning: /etc/sane.d/gt68xx.conf saved as /etc/sane.d/gt68xx.conf.pacorig
  [2010-05-28 16:08] warning: /etc/sane.d/genesys.conf saved as /etc/sane.d/genesys.conf.pacorig
  [2010-05-28 16:08] warning: /etc/sane.d/canon_dr.conf saved as /etc/sane.d/canon_dr.conf.pacorig
  [2010-05-28 16:08] warning: /etc/sane.d/dll.conf saved as /etc/sane.d/dll.conf.pacorig
  [2010-05-28 16:08] warning: /etc/sane.d/cardscan.conf saved as /etc/sane.d/cardscan.conf.pacorig
  [2010-05-28 16:08] warning: /etc/sane.d/hp3900.conf saved as /etc/sane.d/hp3900.conf.pacorig
  [2010-05-28 16:08] warning: /etc/sane.d/fujitsu.conf saved as /etc/sane.d/fujitsu.conf.pacorig
  [2010-05-28 16:08] NOTE
  [2010-05-28 16:08] ----
  [2010-05-28 16:08] Add your user to group 'scanner' to use scanner devices.
  [2010-05-28 16:08] installed sane (1.0.21-2)
  [2010-05-28 16:08] installed kdegraphics-libs (4.4.3-2)
  [2010-05-28 16:08] installed kdegraphics-gwenview (4.4.3-2)
  [2010-05-28 16:08] installed kdegraphics-kamera (4.4.3-2)
  [2010-05-28 16:08] installed kdegraphics-kcolorchooser (4.4.3-2)
  [2010-05-28 16:08] installed kdegraphics-kgamma (4.4.3-2)
  [2010-05-28 16:08] installed kdegraphics-kolourpaint (4.4.3-2)
  [2010-05-28 16:08] installed kdegraphics-kruler (4.4.3-2)
  [2010-05-28 16:08] installed kdegraphics-ksnapshot (4.4.3-2)
  [2010-05-28 16:08] installed openjpeg (1.3-3)
  [2010-05-28 16:08] installed poppler (0.12.4-1)
  [2010-05-28 16:08] installed poppler-qt (0.12.4-1)
  [2010-05-28 16:08] installed chmlib (0.40-1)
  [2010-05-28 16:08] installed libdjvu (3.5.22-3)
  [2010-05-28 16:08] installed libzip (0.9.3-1)
  [2010-05-28 16:08] installed ebook-tools (0.1.1-1)
  [2010-05-28 16:08] installed kdegraphics-okular (4.4.3-2)
  [2010-05-28 16:08] installed kdemultimedia-dragonplayer (4.4.3-1)
  [2010-05-28 16:08] installed musicbrainz (2.1.5-3)
  [2010-05-28 16:08] installed libmad (0.15.1b-4)
  [2010-05-28 16:08] installed libmpcdec (1.2.6-2)
  [2010-05-28 16:08] installed libofa (0.9.3-2)
  [2010-05-28 16:08] installed taglib (1.6.3-1)
  [2010-05-28 16:08] installed tunepimp (0.5.3-7)
  [2010-05-28 16:08] installed kdemultimedia-juk (4.4.3-1)
  [2010-05-28 16:08] installed kdemultimedia-kioslave (4.4.3-1)
  [2010-05-28 16:08] installed kdemultimedia-kmix (4.4.3-1)
  [2010-05-28 16:08] installed kdemultimedia-kscd (4.4.3-1)
  [2010-05-28 16:08] installed aalib (1.4rc5-6)
  [2010-05-28 16:08] installed libsndfile (1.0.21-1)
  [2010-05-28 16:08] installed libsamplerate (0.1.7-1)
  [2010-05-28 16:08] installed jack (0.118.0-3)
  [2010-05-28 16:08] installed libcaca (0.99.beta17-1)
  [2010-05-28 16:08] installed libftdi (0.16-1)
  [2010-05-28 16:08] installed lirc-utils (0.8.6-3)
  [2010-05-28 16:08] Regenerating font encodings... done.
  [2010-05-28 16:08] installed xorg-fonts-encodings (1.0.3-1)
  [2010-05-28 16:08] installed ttf-dejavu (2.30-2)
  [2010-05-28 16:08] installed recode (3.6-4)
  [2010-05-28 16:08] installed enca (1.13-1)
  [2010-05-28 16:08] installed libdca (0.0.5-2)
  [2010-05-28 16:08] installed a52dec (0.7.4-4)
  [2010-05-28 16:08] warning: /etc/mplayer/codecs.conf saved as /etc/mplayer/codecs.conf.pacorig
  [2010-05-28 16:08] warning: /etc/mplayer/input.conf saved as /etc/mplayer/input.conf.pacorig
  [2010-05-28 16:08] installed mplayer (31147-2)
  [2010-05-28 16:08] installed kdemultimedia-mplayerthumbs (4.4.3-1)
  [2010-05-28 16:08] installed kdenetwork-filesharing (4.4.3-2)
  [2010-05-28 16:08] installed kdenetwork-kdnssd (4.4.3-2)
  [2010-05-28 16:08] installed kdenetwork-kget (4.4.3-2)
  [2010-05-28 16:08] installed qca-ossl (2.0.0-3)
  [2010-05-28 16:08] installed libotr (3.2.0-1)
  [2010-05-28 16:08] installed libmsn (4.1-2)
  [2010-05-28 16:08] installed libidn (1.16-1)
  [2010-05-28 16:08] installed libgadu (1.9.0-1)
  [2010-05-28 16:08] installed kdenetwork-kopete (4.4.3-2)
  [2010-05-28 16:08] installed kdenetwork-kppp (4.4.3-2)
  [2010-05-28 16:08] installed libvncserver (0.9.7-3)
  [2010-05-28 16:08] warning: /etc/libao.conf saved as /etc/libao.conf.pacorig
  [2010-05-28 16:08] installed libao (1.0.0-1)
  [2010-05-28 16:08] installed rdesktop (1.6.0-5)
  [2010-05-28 16:08] installed telepathy-glib (0.10.6-1)
  [2010-05-28 16:08] installed libnice (0.0.12-1)
  [2010-05-28 16:08] installed gstreamer0.10-python (0.10.18-1)
  [2010-05-28 16:08] installed farsight2 (0.0.19-1)
  [2010-05-28 16:08] installed telepathy-farsight (0.0.14-1)
  [2010-05-28 16:08] installed telepathy-qt4 (0.3.3-1)
  [2010-05-28 16:08] installed kdenetwork-krdc (4.4.3-2)
  [2010-05-28 16:08] installed kdenetwork-krfb (4.4.3-2)
  [2010-05-28 16:08] installed kde-agent (20090801-2)
  [2010-05-28 16:08] installed kdepim-libkdepim (4.4.3-2)
  [2010-05-28 16:08] installed kdepim-akonadiconsole (4.4.3-2)
  [2010-05-28 16:08] installed kdepim-akregator (4.4.3-2)
  [2010-05-28 16:08] installed kdepim-blogilo (4.4.3-2)
  [2010-05-28 16:08] installed kdepim-console (4.4.3-2)
  [2010-05-28 16:08] installed kdepim-kaddressbook (4.4.3-2)
  [2010-05-28 16:08] installed kdepim-kalarm (4.4.3-2)
  [2010-05-28 16:08] installed kdepim-kjots (4.4.3-2)
  [2010-05-28 16:08] installed kdepim-kleopatra (4.4.3-2)
  [2010-05-28 16:08] installed kdepim-kmail (4.4.3-2)
  [2010-05-28 16:08] installed kdepim-knode (4.4.3-2)
  [2010-05-28 16:08] installed kdepim-knotes (4.4.3-2)
  [2010-05-28 16:08] installed kdepim-korganizer (4.4.3-2)
  [2010-05-28 16:08] installed kdepim-kontact (4.4.3-2)
  [2010-05-28 16:08] installed kdepim-kresources (4.4.3-2)
  [2010-05-28 16:08] installed kdepim-ktimetracker (4.4.3-2)
  [2010-05-28 16:08] installed kdepim-wizards (4.4.3-2)
  [2010-05-28 16:08] installed kdeplasma-addons-applets-bball (4.4.3-1)
  [2010-05-28 16:08] installed kdeplasma-addons-applets-binary-clock (4.4.3-1)
  [2010-05-28 16:08] installed kdeplasma-addons-applets-blackboard (4.4.3-1)
  [2010-05-28 16:08] installed kdeplasma-addons-applets-bubblemon (4.4.3-1)
  [2010-05-28 16:08] installed kdeplasma-addons-applets-calculator (4.4.3-1)
  [2010-05-28 16:08] installed kdeplasma-addons-applets-charselect (4.4.3-1)
  [2010-05-28 16:08] installed kdeplasma-addons-libs (4.4.3-1)
  [2010-05-28 16:08] installed kdeplasma-addons-applets-comic (4.4.3-1)
  [2010-05-28 16:08] installed kdeplasma-addons-applets-dict (4.4.3-1)
  [2010-05-28 16:08] installed kdeplasma-addons-applets-eyes (4.4.3-1)
  [2010-05-28 16:08] installed kdeplasma-addons-applets-fifteenpuzzle (4.4.3-1)
  [2010-05-28 16:08] installed kdeplasma-addons-applets-filewatcher (4.4.3-1)
  [2010-05-28 16:08] installed kdeplasma-addons-applets-frame (4.4.3-1)
  [2010-05-28 16:08] installed kdeplasma-addons-applets-fuzzy-clock (4.4.3-1)
  [2010-05-28 16:08] installed kdeplasma-addons-applets-incomingmsg (4.4.3-1)
  [2010-05-28 16:08] installed qwt (5.2.0-2)
  [2010-05-28 16:08] installed kdeplasma-addons-applets-kdeobservatory (4.4.3-1)
  [2010-05-28 16:08] installed kdeplasma-addons-applets-kimpanel (4.4.3-1)
  [2010-05-28 16:08] installed kdeplasma-addons-applets-knowledgebase (4.4.3-1)
  [2010-05-28 16:08] installed kdeplasma-addons-applets-kolourpicker (4.4.3-1)
  [2010-05-28 16:08] installed kdeplasma-addons-applets-konqprofiles (4.4.3-1)
  [2010-05-28 16:08] installed kdeplasma-addons-applets-konsoleprofiles (4.4.3-1)
  [2010-05-28 16:08] installed kdeplasma-addons-applets-lancelot (4.4.3-1)
  [2010-05-28 16:08] installed kdeplasma-addons-applets-leavenote (4.4.3-1)
  [2010-05-28 16:08] installed kdeplasma-addons-applets-life (4.4.3-1)
  [2010-05-28 16:08] installed kdeplasma-addons-applets-luna (4.4.3-1)
  [2010-05-28 16:08] installed kdeplasma-addons-applets-magnifique (4.4.3-1)
  [2010-05-28 16:08] installed kdeplasma-addons-applets-mediaplayer (4.4.3-1)
  [2010-05-28 16:08] installed kdeplasma-addons-applets-microblog (4.4.3-1)
  [2010-05-28 16:08] installed kdeplasma-addons-applets-news (4.4.3-1)
  [2010-05-28 16:08] installed kdeplasma-addons-applets-notes (4.4.3-1)
  [2010-05-28 16:08] installed kdeplasma-addons-applets-nowplaying (4.4.3-1)
  [2010-05-28 16:08] installed kdeplasma-addons-applets-opendesktop (4.4.3-1)
  [2010-05-28 16:08] installed kdeplasma-addons-applets-opendesktop-activities (4.4.3-1)
  [2010-05-28 16:08] installed kdeplasma-addons-applets-paste (4.4.3-1)
  [2010-05-28 16:08] installed kdeplasma-addons-applets-pastebin (4.4.3-1)
  [2010-05-28 16:08] installed kdeplasma-addons-applets-plasmaboard (4.4.3-1)
  [2010-05-28 16:08] installed kdeplasma-addons-applets-previewer (4.4.3-1)
  [2010-05-28 16:08] installed kdeplasma-addons-applets-qalculate (4.4.3-1)
  [2010-05-28 16:08] installed kdeplasma-addons-applets-rememberthemilk (4.4.3-1)
  [2010-05-28 16:08] installed kdeplasma-addons-applets-rssnow (4.4.3-1)
  [2010-05-28 16:08] installed kdeplasma-addons-applets-showdashboard (4.4.3-1)
  [2010-05-28 16:08] installed kdeplasma-addons-applets-showdesktop (4.4.3-1)
  [2010-05-28 16:08] installed kdeplasma-addons-applets-spellcheck (4.4.3-1)
  [2010-05-28 16:08] installed kdeplasma-addons-applets-systemloadviewer (4.4.3-1)
  [2010-05-28 16:08] installed kdeplasma-addons-applets-timer (4.4.3-1)
  [2010-05-28 16:08] installed kdeplasma-addons-applets-unitconverter (4.4.3-1)
  [2010-05-28 16:08] installed kdeplasma-addons-applets-weather (4.4.3-1)
  [2010-05-28 16:08] installed kdeplasma-addons-applets-weatherstation (4.4.3-1)
  [2010-05-28 16:08] installed kdeplasma-addons-applets-webslice (4.4.3-1)
  [2010-05-28 16:08] installed kdeplasma-addons-runners-audioplayercontrol (4.4.3-1)
  [2010-05-28 16:08] installed kdeplasma-addons-runners-browserhistory (4.4.3-1)
  [2010-05-28 16:08] installed kdeplasma-addons-runners-contacts (4.4.3-1)
  [2010-05-28 16:08] installed kdeplasma-addons-runners-converter (4.4.3-1)
  [2010-05-28 16:08] installed kdeplasma-addons-runners-katesessions (4.4.3-1)
  [2010-05-28 16:08] installed kdeplasma-addons-runners-konquerorsessions (4.4.3-1)
  [2010-05-28 16:08] installed kdeplasma-addons-runners-konsolesessions (4.4.3-1)
  [2010-05-28 16:08] installed kdeplasma-addons-runners-kopete (4.4.3-1)
  [2010-05-28 16:08] installed kdeplasma-addons-runners-mediawiki (4.4.3-1)
  [2010-05-28 16:08] installed kdeplasma-addons-runners-spellchecker (4.4.3-1)
  [2010-05-28 16:08] installed kdeplasma-addons-wallpapers-mandelbrot (4.4.3-1)
  [2010-05-28 16:08] installed kdeplasma-addons-wallpapers-marble (4.4.3-1)
  [2010-05-28 16:08] installed kdeplasma-addons-wallpapers-pattern (4.4.3-1)
  [2010-05-28 16:08] installed kdeplasma-addons-wallpapers-virus (4.4.3-1)
  [2010-05-28 16:08] installed kdeplasma-addons-wallpapers-weather (4.4.3-1)
  [2010-05-28 16:08] installed kdesdk-cervisia (4.4.3-1)
  [2010-05-28 16:09] installed kdesdk-kapptemplate (4.4.3-1)
  [2010-05-28 16:09] installed kdesdk-kate (4.4.3-1)
  [2010-05-28 16:09] installed kdesdk-kbugbuster (4.4.3-1)
  [2010-05-28 16:09] installed kdesdk-kcachegrind (4.4.3-1)
  [2010-05-28 16:09] installed kdesdk-kdeaccounts-plugin (4.4.3-1)
  [2010-05-28 16:09] installed kdesdk-kdepalettes (4.4.3-1)
  [2010-05-28 16:09] installed kdesdk-kioslave (4.4.3-1)
  [2010-05-28 16:09] installed kdesdk-kmtrace (4.4.3-1)
  [2010-05-28 16:09] installed kdesdk-kompare (4.4.3-1)
  [2010-05-28 16:09] installed kdesdk-kpartloader (4.4.3-1)
  [2010-05-28 16:09] installed kdesdk-kprofilemethod (4.4.3-1)
  [2010-05-28 16:09] installed kdesdk-kstartperf (4.4.3-1)
  [2010-05-28 16:09] installed kdesdk-kuiviewer (4.4.3-1)
  [2010-05-28 16:09] installed kdesdk-lokalize (4.4.3-1)
  [2010-05-28 16:09] installed kdesdk-poxml (4.4.3-1)
  [2010-05-28 16:09] installed kdesdk-scripts (4.4.3-1)
  [2010-05-28 16:09] installed kdesdk-strigi-analyzer (4.4.3-1)
  [2010-05-28 16:09] installed kdesdk-umbrello (4.4.3-1)
  [2010-05-28 16:09] installed kdetoys-amor (4.4.3-1)
  [2010-05-28 16:09] installed kdetoys-kteatime (4.4.3-1)
  [2010-05-28 16:09] installed kdetoys-ktux (4.4.3-1)
  [2010-05-28 16:09] installed kdetoys-kweather (4.4.3-1)
  [2010-05-28 16:09] installed kdeutils-ark (4.4.3-1)
  [2010-05-28 16:09] installed kdeutils-kcalc (4.4.3-1)
  [2010-05-28 16:09] installed kdeutils-kcharselect (4.4.3-1)
  [2010-05-28 16:09] installed kdeutils-kdelirc (4.4.3-1)
  [2010-05-28 16:09] installed kdeutils-kdf (4.4.3-1)
  [2010-05-28 16:09] installed kdeutils-kfloppy (4.4.3-1)
  [2010-05-28 16:09] installed kdeutils-kgpg (4.4.3-1)
  [2010-05-28 16:09] installed kdeutils-ktimer (4.4.3-1)
  [2010-05-28 16:09] installed kdeutils-kwallet (4.4.3-1)
  [2010-05-28 16:09] installed kdeutils-okteta (4.4.3-1)
  [2010-05-28 16:09] installed kdeutils-printer-applet (4.4.3-1)
  [2010-05-28 16:09] installed kdeutils-superkaramba (4.4.3-1)
  [2010-05-28 16:09] installed kdeutils-sweeper (4.4.3-1)
  [2010-05-28 16:09] installed kdewebdev-kfilereplace (4.4.3-1)
  [2010-05-28 16:09] installed kdewebdev-kimagemapeditor (4.4.3-1)
  [2010-05-28 16:09] installed tidyhtml (1.46-1)
  [2010-05-28 16:09] installed kdewebdev-klinkstatus (4.4.3-1)
  [2010-05-28 16:09] installed kdewebdev-kommander (4.4.3-1)
  [2010-05-28 16:09] installed kde-l10n-ar (4.4.3-1)
  [2010-05-28 16:09] installed kde-l10n-bg (4.4.3-1)
  [2010-05-28 16:09] installed kde-l10n-ca (4.4.3-1)
  [2010-05-28 16:09] installed kde-l10n-ca@valencia (4.4.3-1)
  [2010-05-28 16:09] installed kde-l10n-cs (4.4.3-1)
  [2010-05-28 16:09] installed kde-l10n-csb (4.4.3-1)
  [2010-05-28 16:09] installed kde-l10n-da (4.4.3-1)
  [2010-05-28 16:09] installed kde-l10n-de (4.4.3-1)
  [2010-05-28 16:09] installed kde-l10n-el (4.4.3-1)
  [2010-05-28 16:09] installed kde-l10n-en_gb (4.4.3-1)
  [2010-05-28 16:09] installed kde-l10n-eo (4.4.3-1)
  [2010-05-28 16:09] installed kde-l10n-es (4.4.3-1)
  [2010-05-28 16:09] installed kde-l10n-et (4.4.3-1)
  [2010-05-28 16:09] installed kde-l10n-eu (4.4.3-1)
  [2010-05-28 16:09] installed kde-l10n-fi (4.4.3-1)
  [2010-05-28 16:09] installed kde-l10n-fr (4.4.3-1)
  [2010-05-28 16:09] installed kde-l10n-fy (4.4.3-1)
  [2010-05-28 16:09] installed kde-l10n-ga (4.4.3-1)
  [2010-05-28 16:09] installed kde-l10n-gl (4.4.3-1)
  [2010-05-28 16:09] installed kde-l10n-gu (4.4.3-1)
  [2010-05-28 16:09] installed kde-l10n-he (4.4.3-1)
  [2010-05-28 16:09] installed kde-l10n-hi (4.4.3-1)
  [2010-05-28 16:09] installed kde-l10n-hr (4.4.3-1)
  [2010-05-28 16:09] installed kde-l10n-hu (4.4.3-1)
  [2010-05-28 16:09] installed kde-l10n-id (4.4.3-1)
  [2010-05-28 16:09] installed kde-l10n-is (4.4.3-1)
  [2010-05-28 16:09] installed kde-l10n-it (4.4.3-1)
  [2010-05-28 16:09] installed kde-l10n-ja (4.4.3-1)
  [2010-05-28 16:09] installed kde-l10n-kk (4.4.3-1)
  [2010-05-28 16:09] installed kde-l10n-km (4.4.3-1)
  [2010-05-28 16:09] installed kde-l10n-kn (4.4.3-1)
  [2010-05-28 16:09] installed kde-l10n-ko (4.4.3-1)
  [2010-05-28 16:09] installed kde-l10n-lt (4.4.3-1)
  [2010-05-28 16:09] installed kde-l10n-lv (4.4.3-1)
  [2010-05-28 16:09] installed kde-l10n-mai (4.4.3-1)
  [2010-05-28 16:09] installed kde-l10n-mk (4.4.3-1)
  [2010-05-28 16:09] installed kde-l10n-ml (4.4.3-1)
  [2010-05-28 16:09] installed kde-l10n-nb (4.4.3-1)
  [2010-05-28 16:09] installed kde-l10n-nds (4.4.3-1)
  [2010-05-28 16:09] installed kde-l10n-nl (4.4.3-1)
  [2010-05-28 16:09] installed kde-l10n-nn (4.4.3-1)
  [2010-05-28 16:09] installed kde-l10n-pa (4.4.3-1)
  [2010-05-28 16:09] installed kde-l10n-pl (4.4.3-1)
  [2010-05-28 16:09] installed kde-l10n-pt (4.4.3-1)
  [2010-05-28 16:10] installed kde-l10n-pt_br (4.4.3-1)
  [2010-05-28 16:10] installed kde-l10n-ro (4.4.3-1)
  [2010-05-28 16:10] installed kde-l10n-ru (4.4.3-1)
  [2010-05-28 16:10] installed kde-l10n-si (4.4.3-1)
  [2010-05-28 16:10] installed kde-l10n-sk (4.4.3-1)
  [2010-05-28 16:10] installed kde-l10n-sl (4.4.3-1)
  [2010-05-28 16:10] installed kde-l10n-sr (4.4.3-1)
  [2010-05-28 16:10] installed kde-l10n-sv (4.4.3-1)
  [2010-05-28 16:10] installed kde-l10n-tg (4.4.3-1)
  [2010-05-28 16:10] installed kde-l10n-tr (4.4.3-1)
  [2010-05-28 16:10] installed kde-l10n-uk (4.4.3-1)
  [2010-05-28 16:10] installed kde-l10n-wa (4.4.3-1)
  [2010-05-28 16:10] installed kde-l10n-zh_cn (4.4.3-1)
  [2010-05-28 16:10] installed kde-l10n-zh_tw (4.4.3-1)
  [2010-05-28 16:10] installed kde-meta-kdeaccessibility (4.4-3)
  [2010-05-28 16:10] installed kde-meta-kdeadmin (4.4-3)
  [2010-05-28 16:10] installed kde-meta-kdeartwork (4.4-3)
  [2010-05-28 16:10] installed kde-meta-kdebase (4.4-3)
  [2010-05-28 16:10] installed kde-meta-kdeedu (4.4-3)
  [2010-05-28 16:10] installed kde-meta-kdegames (4.4-3)
  [2010-05-28 16:10] installed kde-meta-kdegraphics (4.4-3)
  [2010-05-28 16:10] installed kde-meta-kdemultimedia (4.4-3)
  [2010-05-28 16:10] installed kde-meta-kdenetwork (4.4-3)
  [2010-05-28 16:10] installed kde-meta-kdepim (4.4-3)
  [2010-05-28 16:10] installed kde-meta-kdeplasma-addons (4.4-3)
  [2010-05-28 16:10] installed kde-meta-kdesdk (4.4-3)
  [2010-05-28 16:10] installed kde-meta-kdetoys (4.4-3)
  [2010-05-28 16:10] installed kde-meta-kdeutils (4.4-3)
  [2010-05-28 16:10] installed kde-meta-kdewebdev (4.4-3)
  [2010-05-28 16:10] installed qtcurve-gtk2 (1.4.1-1)
  [2010-05-28 16:10] installed qt3 (3.3.8-17)
  [2010-05-28 16:10] installed kdelibs3 (3.5.10-10)
  [2010-05-28 16:10] installed qtcurve-kde3 (1.4.1-1)
  [2010-05-28 16:10] installed qtcurve-kde4 (1.4.2-1)
  [2010-05-28 16:10] installed compiz-core (0.8.6-2)
  [2010-05-28 16:10] installed libcompizconfig (0.8.4-2)
  [2010-05-28 16:10] installed pyrex (0.9.8.5-2)
  [2010-05-28 16:10] installed compizconfig-python (0.8.4-1)
  [2010-05-28 16:10] installed ccsm (0.8.4-1)
  [2010-05-28 16:10] installed libcanberra (0.23-1)
  [2010-05-28 16:10] installed zenity (2.30.0-1)
  [2010-05-28 16:10] installed libgtop (2.28.1-1)
  [2010-05-28 16:10] installed metacity (2.30.1-1)
  [2010-05-28 16:10] installed libgnomekbd (2.30.1-1)
  [2010-05-28 16:10] installed gnome-desktop (2.30.0-1)
  [2010-05-28 16:10] installed gnome-settings-daemon (2.30.1-1)
  [2010-05-28 16:10] installed sound-theme-freedesktop (0.7-1)
  [2010-05-28 16:10] installed gnome-menus (2.30.0-1)
  [2010-05-28 16:10] installed perlxml (2.36-2)
  [2010-05-28 16:10] installed perl-xml-simple (2.18-2)
  [2010-05-28 16:10] installed icon-naming-utils (0.8.90-1)
  [2010-05-28 16:10] installed gnome-icon-theme (2.30.3-1)
  [2010-05-28 16:10] installed libgweather (2.30.0-1)
  [2010-05-28 16:10] installed evolution-data-server (2.30.1-1)
  [2010-05-28 16:10] Unknown media type in type 'all/all'
  [2010-05-28 16:10] 
  [2010-05-28 16:10] Unknown media type in type 'all/allfiles'
  [2010-05-28 16:10] 
  [2010-05-28 16:10] Unknown media type in type 'uri/mms'
  [2010-05-28 16:10] 
  [2010-05-28 16:10] Unknown media type in type 'uri/mmst'
  [2010-05-28 16:10] 
  [2010-05-28 16:10] Unknown media type in type 'uri/mmsu'
  [2010-05-28 16:10] 
  [2010-05-28 16:10] Unknown media type in type 'uri/pnm'
  [2010-05-28 16:10] 
  [2010-05-28 16:10] Unknown media type in type 'uri/rtspt'
  [2010-05-28 16:10] 
  [2010-05-28 16:10] Unknown media type in type 'uri/rtspu'
  [2010-05-28 16:10] 
  [2010-05-28 16:10] Unknown media type in type 'fonts/package'
  [2010-05-28 16:10] 
  [2010-05-28 16:10] Unknown media type in type 'interface/x-winamp-skin'
  [2010-05-28 16:10] 
  [2010-05-28 16:10] installed gnome-control-center (2.30.1-1)
  [2010-05-28 16:10] installed libxres (1.0.4-1)
  [2010-05-28 16:10] installed libwnck (2.30.0-1)
  [2010-05-28 16:10] installed compiz-decorator-gtk (0.8.6-2)
  [2010-05-28 16:10] installed compiz-decorator-kde (0.8.6-2)
  [2010-05-28 16:10] installed compiz-bcop (0.8.4-1)
  [2010-05-28 16:10] installed compiz-fusion-plugins-main (0.8.6-1)
  [2010-05-28 16:10] installed compiz-fusion-plugins-extra (0.8.6-1)
  [2010-05-28 16:10] installed compizconfig-backend-gconf (0.8.4-1)
  [2010-05-28 16:10] installed compizconfig-backend-kconfig (0.8.4-1)
  [2010-05-28 16:10] Unknown media type in type 'all/all'
  [2010-05-28 16:10] 
  [2010-05-28 16:10] Unknown media type in type 'all/allfiles'
  [2010-05-28 16:10] 
  [2010-05-28 16:10] Unknown media type in type 'uri/mms'
  [2010-05-28 16:10] 
  [2010-05-28 16:10] Unknown media type in type 'uri/mmst'
  [2010-05-28 16:10] 
  [2010-05-28 16:10] Unknown media type in type 'uri/mmsu'
  [2010-05-28 16:10] 
  [2010-05-28 16:10] Unknown media type in type 'uri/pnm'
  [2010-05-28 16:10] 
  [2010-05-28 16:10] Unknown media type in type 'uri/rtspt'
  [2010-05-28 16:10] 
  [2010-05-28 16:10] Unknown media type in type 'uri/rtspu'
  [2010-05-28 16:10] 
  [2010-05-28 16:10] Unknown media type in type 'fonts/package'
  [2010-05-28 16:10] 
  [2010-05-28 16:10] Unknown media type in type 'interface/x-winamp-skin'
  [2010-05-28 16:10] 
  [2010-05-28 16:10] installed emerald (0.8.4-2)
  [2010-05-28 16:10] installed emerald-themes (0.6.0-2)
  [2010-05-28 16:10] > Updating icon cache.....
  [2010-05-28 16:10] installed fusion-icon (20091023-1)
  [2010-05-28 16:10] installed libwebkit (1.2.1-1)
  [2010-05-28 16:10] installed gnome-js-common (0.1.2-1)
  [2010-05-28 16:10] installed gobject-introspection (0.6.12-1)
  [2010-05-28 16:10] installed seed (2.30.0-1)
  [2010-05-28 16:10] installed epiphany (2.30.2-1)
  [2010-05-28 16:10] installed gnome-panel (2.30.0-1)
  [2010-05-28 16:10] warning: /etc/conf.d/cpufreq saved as /etc/conf.d/cpufreq.pacorig
  [2010-05-28 16:10] installed cpufrequtils (007-1)
  [2010-05-28 16:10] installed gnome-applets (2.30.0-1)
  [2010-05-28 16:10] installed gnome-backgrounds (2.30.0-1)
  [2010-05-28 16:10] installed gstreamer0.10-good (0.10.22-1)
  [2010-05-28 16:10] installed libavc1394 (0.5.3-3)
  [2010-05-28 16:10] installed libiec61883 (1.2.0-1)
  [2010-05-28 16:10] installed speex (1.2rc1-1)
  [2010-05-28 16:10] installed libshout (2.2.2-3)
  [2010-05-28 16:10] installed libdv (1.0.0-3)
  [2010-05-28 16:10] installed gstreamer0.10-good-plugins (0.10.22-1)
  [2010-05-28 16:10] installed gnome-media (2.30.0-2)
  [2010-05-28 16:10] installed gnome-screensaver (2.30.0-1)
  [2010-05-28 16:10] installed upower (0.9.4-1)
  [2010-05-28 16:10] installed polkit-gnome (0.96-3)
  [2010-05-28 16:10] installed gnome-session (2.30.0-1)
  [2010-05-28 16:10] installed gtk-engines (2.20.1-1)
  [2010-05-28 16:10] installed gnome-themes (2.30.1-1)
  [2010-05-28 16:10] installed docbook-xml (4.5-4)
  [2010-05-28 16:10] installed gnome-doc-utils (0.20.1-1)
  [2010-05-28 16:10] installed yelp (2.30.1-1)
  [2010-05-28 16:11] installed gnome2-user-docs (2.30.0-1)
  [2010-05-28 16:11] installed at-spi (1.30.1-1)
  [2010-05-28 16:11] installed libgail-gnome (1.20.2-1)
  [2010-05-28 16:11] installed exempi (2.1.1-1)
  [2010-05-28 16:11] installed nautilus (2.30.1-1)
  [2010-05-28 16:11] installed libsexy (0.1.11-2)
  [2010-05-28 16:11] installed notification-daemon (0.4.0-4)
  [2010-05-28 16:11] installed alacarte (0.13.1-1)
  [2010-05-28 16:11] installed bug-buddy (2.30.0-1)
  [2010-05-28 16:11] installed cheese (2.30.1-1)
  [2010-05-28 16:11] installed gnome-speech (0.4.25-1)
  [2010-05-28 16:11] installed dasher (4.10.1-2)
  [2010-05-28 16:11] installed gnome-python-desktop (2.30.0-1)
  [2010-05-28 16:11] installed deskbar-applet (2.30.1-1)
  [2010-05-28 16:11] installed ptlib (2.6.5-2)
  [2010-05-28 16:11] installed opal (3.6.6-2)
  [2010-05-28 16:11] installed libsigc++2.0 (2.2.7-1)
  [2010-05-28 16:11] installed ekiga (3.2.6-1)
  [2010-05-28 16:11] installed telepathy-mission-control (5.4.2-1)
  [2010-05-28 16:11] > To use Empathy you need to install at least one Telepathy connection 
  [2010-05-28 16:11] manager.
  [2010-05-28 16:11] >
  [2010-05-28 16:11] installed empathy (2.30.1-1)
  [2010-05-28 16:11] installed eog (2.30.1-1)
  [2010-05-28 16:11] installed poppler-glib (0.12.4-1)
  [2010-05-28 16:11] installed t1lib (5.1.2-2)
  [2010-05-28 16:11] installed evince (2.30.1-2)
  [2010-05-28 16:11] installed gtkhtml (3.30.1-1)
  [2010-05-28 16:11] warning: /etc/bluetooth/main.conf saved as /etc/bluetooth/main.conf.pacorig
  [2010-05-28 16:11] warning: /etc/bluetooth/audio.conf saved as /etc/bluetooth/audio.conf.pacorig
  [2010-05-28 16:11] installed bluez (4.65-1)
  [2010-05-28 16:11] installed pilot-link (0.12.5-1)
  [2010-05-28 16:11] installed gnome-pilot (2.0.17-2)
  [2010-05-28 16:11] installed libpst (0.6.41-4)
  [2010-05-28 16:11] installed libytnef (1.5-2)
  [2010-05-28 16:11] installed gtkimageview (1.6.4-1)
  [2010-05-28 16:11] installed evolution (2.30.1.2-1)
  [2010-05-28 16:11] installed evolution-exchange (2.30.1-1)
  [2010-05-28 16:11] installed evolution-webcal (2.28.1-1)
  [2010-05-28 16:11] installed file-roller (2.30.1.1-1)
  [2010-05-28 16:11] installed gcalctool (5.30.1-1)
  [2010-05-28 16:11] installed gconf-editor (2.30.0-1)
  [2010-05-28 16:11] installed gdm (2.30.2-2)
  [2010-05-28 16:11] installed gnome-audio (2.22.0-1)
  [2010-05-28 16:11] installed guile (1.8.7-2)
  [2010-05-28 16:11] installed clutter (1.2.8-1)
  [2010-05-28 16:11] installed clutter-gtk (0.10.2-2)
  [2010-05-28 16:11] installed gir-repository (0.6.6-0.20100311)
  [2010-05-28 16:11] installed gnome-games (2.30.1-1)
  [2010-05-28 16:12] installed gnome-games-extra-data (2.30.0-1)
  [2010-05-28 16:12] installed gnome-mag (0.16.1-1)
  [2010-05-28 16:12] installed gnome-netstatus (2.28.1-1)
  [2010-05-28 16:12] installed xinetd (2.3.14-5)
  [2010-05-28 16:12] installed netkit-bsd-finger (0.17-5)
  [2010-05-28 16:12] installed whois (5.0.4-1)
  [2010-05-28 16:12] installed gnome-nettool (2.30.0-1)
  [2010-05-28 16:12] installed gnome-power-manager (2.30.1-1)
  [2010-05-28 16:12] installed libgksu (2.0.12-2)
  [2010-05-28 16:12] installed glibmm (2.24.2-1)
  [2010-05-28 16:12] installed cairomm (1.8.4-1)
  [2010-05-28 16:12] installed pangomm (2.26.2-1)
  [2010-05-28 16:12] installed gtkmm (2.20.3-1)
  [2010-05-28 16:12] installed gnome-system-monitor (2.28.1-1)
  [2010-05-28 16:12] installed gnome-terminal (2.30.1-1)
  [2010-05-28 16:12] installed gnome-utils (2.30.0-1)
  [2010-05-28 16:12] installed gok (2.30.0-1)
  [2010-05-28 16:12] installed python-pysqlite (2.5.5-1)
  [2010-05-28 16:12] installed pyxdg (0.19-1)
  [2010-05-28 16:12] installed hamster-applet (2.30.1-1)
  [2010-05-28 16:12] installed mousetweaks (2.30.1-1)
  [2010-05-28 16:12] installed nautilus-sendto (2.28.4-1)
  [2010-05-28 16:12] installed tcl (8.5.8-1)
  [2010-05-28 16:12] installed brltty (4.1-3)
  [2010-05-28 16:12] installed orca (2.30.1-1)
  [2010-05-28 16:12] installed seahorse (2.30.1-1)
  [2010-05-28 16:12] installed seahorse-plugins (2.30.1-1)
  [2010-05-28 16:12] installed gmime (2.4.17-1)
  [2010-05-28 16:12] installed totem-plparser (2.30.1-1)
  [2010-05-28 16:12] installed libbeagle (0.3.9-1)
  [2010-05-28 16:12] installed cdrkit (1.1.10-1)
  [2010-05-28 16:12] installed cdrdao (1.2.3-4)
  [2010-05-28 16:12] installed dvd+rw-tools (7.1-2)
  [2010-05-28 16:12] installed brasero (2.30.1-1)
  [2010-05-28 16:12] installed sound-juicer (2.28.2-1)
  [2010-05-28 16:12] installed gtkspell (2.0.16-1)
  [2010-05-28 16:12] installed libgdiplus (2.6.4-1)
  [2010-05-28 16:12] installed mono (2.6.4-2)
  [2010-05-28 16:12] installed ndesk-dbus (0.6.0-2)
  [2010-05-28 16:12] installed ndesk-dbus-glib (0.4.1-2)
  [2010-05-28 16:12] installed gtk-sharp-2 (2.12.10-1)
  [2010-05-28 16:12] installed gnome-sharp (2.24.1-1)
  [2010-05-28 16:12] installed mono-addins (0.4-4)
  [2010-05-28 16:12] installed gnome-desktop-sharp (2.26.0-5)
  [2010-05-28 16:12] Unknown media type in type 'all/all'
  [2010-05-28 16:12] 
  [2010-05-28 16:12] Unknown media type in type 'all/allfiles'
  [2010-05-28 16:12] 
  [2010-05-28 16:12] Unknown media type in type 'uri/mms'
  [2010-05-28 16:12] 
  [2010-05-28 16:12] Unknown media type in type 'uri/mmst'
  [2010-05-28 16:12] 
  [2010-05-28 16:12] Unknown media type in type 'uri/mmsu'
  [2010-05-28 16:12] 
  [2010-05-28 16:12] Unknown media type in type 'uri/pnm'
  [2010-05-28 16:12] 
  [2010-05-28 16:12] Unknown media type in type 'uri/rtspt'
  [2010-05-28 16:12] 
  [2010-05-28 16:12] Unknown media type in type 'uri/rtspu'
  [2010-05-28 16:12] 
  [2010-05-28 16:12] Unknown media type in type 'fonts/package'
  [2010-05-28 16:12] 
  [2010-05-28 16:12] Unknown media type in type 'interface/x-winamp-skin'
  [2010-05-28 16:12] 
  [2010-05-28 16:12] installed tomboy (1.2.1-1)
  [2010-05-28 16:12] installed totem (2.30.2-1)
  [2010-05-28 16:12] installed gtk-vnc (0.3.10-1)
  [2010-05-28 16:12] installed vinagre (2.30.1-1)
  [2010-05-28 16:12] installed vino (2.28.2-1)
  [2010-05-28 16:12] installed xf86-video-vesa (2.3.0-1)
  [2010-05-28 16:12] installed xorg-docs (1.5-1)
  [2010-05-28 16:12] installed xorg-fonts-alias (1.0.2-1)
  [2010-05-28 16:13] Updating font cache... done.
  [2010-05-28 16:13] installed xorg-fonts-100dpi (1.0.1-3)
  [2010-05-28 16:13] Updating font cache... done.
  [2010-05-28 16:13] installed xorg-fonts-75dpi (1.0.1-3)
  [2010-05-28 16:13] installed xorg-res-utils (1.0.3-3)
  [2010-05-28 16:13] installed libpciaccess (0.11.0-1)
  [2010-05-28 16:13] installed xcursor-themes (1.0.2-1)
  [2010-05-28 16:13] installed fontcacheproto (0.1.3-1)
  [2010-05-28 16:13] installed libxfontcache (1.0.5-1)
  [2010-05-28 16:13] installed mcpp (2.7.2-2)
  [2010-05-28 16:13] installed xorg-server-utils (7.5-3)
  [2010-05-28 16:13] Updating font cache... done.
  [2010-05-28 16:13] installed xorg-fonts-misc (1.0.1-1)
  [2010-05-28 16:13] installed xbitmaps (1.1.0-1)
  [2010-05-28 16:13] installed xf86-input-evdev (2.3.2-1)
  [2010-05-28 16:13] 
  [2010-05-28 16:13]   Input device handling has changed since xorg-server 1.5.
  [2010-05-28 16:13]   Please read http://wiki.archlinux.org/index.php/Xorg_input_hotplugging.
  [2010-05-28 16:13] 
  [2010-05-28 16:13] installed xorg-server (1.7.6-3)
  [2010-05-28 16:13] installed xorg-twm (1.0.4-3)
  [2010-05-28 16:13] warning: /etc/X11/xinit/xinitrc saved as /etc/X11/xinit/xinitrc.pacorig
  [2010-05-28 16:13] installed xorg-xinit (1.2.1-1)
  [2010-05-28 16:13] installed xterm (258-2)
  [2010-05-28 16:13] installed xf86-video-apm (1.2.2-2)
  [2010-05-28 16:13] installed xf86-video-ark (0.7.2-1)
  [2010-05-28 16:13] installed ati-dri (7.7.1-1)
  [2010-05-28 16:13] installed xf86-video-ati (6.12.192-1)
  [2010-05-28 16:13] installed xf86-video-chips (1.2.2-2)
  [2010-05-28 16:13] installed xf86-video-cirrus (1.3.2-2)
  [2010-05-28 16:13] installed xf86-video-dummy (0.3.2-2)
  [2010-05-28 16:13] installed xf86-video-fbdev (0.4.1-2)
  [2010-05-28 16:13] installed xf86-video-glint (1.2.4-2)
  [2010-05-28 16:13] installed xf86-video-i128 (1.3.3-2)
  [2010-05-28 16:13] installed xf86-video-i740 (1.3.2-2)
  [2010-05-28 16:13] installed intel-dri (7.7.1-1)
  [2010-05-28 16:13] installed xf86-video-intel (2.10.0-1)
  [2010-05-28 16:13] installed mach64-dri (7.7.1-1)
  [2010-05-28 16:13] installed xf86-video-mach64 (6.8.2-2)
  [2010-05-28 16:13] installed mga-dri (7.7.1-1)
  [2010-05-28 16:13] installed xf86-video-mga (1.4.11-2)
  [2010-05-28 16:13] installed xf86-video-neomagic (1.2.4-3)
  [2010-05-28 16:13] installed xf86-video-nv (2.1.17-1)
  [2010-05-28 16:13] installed r128-dri (7.7.1-1)
  [2010-05-28 16:13] installed xf86-video-r128 (6.8.1-2)
  [2010-05-28 16:13] installed xf86-video-radeonhd (1.3.0-1)
  [2010-05-28 16:13] installed xf86-video-rendition (4.2.3-1)
  [2010-05-28 16:13] installed xf86-video-s3 (0.6.3-1)
  [2010-05-28 16:13] installed xf86-video-s3virge (1.10.4-1)
  [2010-05-28 16:13] installed savage-dri (7.7.1-1)
  [2010-05-28 16:13] installed xf86-video-savage (2.3.1-2)
  [2010-05-28 16:13] installed xf86-video-siliconmotion (1.7.3-2)
  [2010-05-28 16:13] installed sis-dri (7.7.1-1)
  [2010-05-28 16:13] installed xf86-video-sis (0.10.2-3)
  [2010-05-28 16:13] installed xf86-video-sisusb (0.9.3-1)
  [2010-05-28 16:13] installed tdfx-dri (7.7.1-1)
  [2010-05-28 16:13] installed xf86-video-tdfx (1.4.3-2)
  [2010-05-28 16:13] installed xf86-video-trident (1.3.3-3)
  [2010-05-28 16:13] installed xf86-video-tseng (1.2.3-1)
  [2010-05-28 16:13] installed xf86-video-v4l (0.2.0-4)
  [2010-05-28 16:13] installed xf86-video-vmware (10.16.9-1)
  [2010-05-28 16:13] installed xf86-video-voodoo (1.2.3-1)
  [2010-05-28 16:13] installed xf86-input-acecad (1.4.0-1)
  [2010-05-28 16:13] installed xf86-input-aiptek (1.3.0-1)
  [2010-05-28 16:13] installed xf86-input-elographics (1.2.3-3)
  [2010-05-28 16:13] installed xf86-input-fpit (1.3.0-3)
  [2010-05-28 16:13] installed xf86-input-hyperpen (1.3.0-3)
  [2010-05-28 16:13] installed xf86-input-joystick (1.5.0-1)
  [2010-05-28 16:13] installed xf86-input-keyboard (1.4.0-1)
  [2010-05-28 16:13] installed xf86-input-mouse (1.5.0-1)
  [2010-05-28 16:13] installed xf86-input-mutouch (1.2.1-4)
  [2010-05-28 16:13] installed xf86-input-penmount (1.4.1-1)
  [2010-05-28 16:13] installed xf86-input-synaptics (1.2.1-1)
  [2010-05-28 16:13] installed xf86-input-vmmouse (12.6.5-3)
  [2010-05-28 16:13] installed xf86-input-void (1.3.0-1)
  [2010-05-28 16:16] warning: directory permissions differ on etc/privoxy/
filesystem: 750  package: 770
  [2010-05-28 16:16] warning: /etc/privoxy/default.action saved as /etc/privoxy/default.action.pacorig
  [2010-05-28 16:16] warning: /etc/privoxy/default.filter saved as /etc/privoxy/default.filter.pacorig
  [2010-05-28 16:16] warning: /etc/privoxy/config saved as /etc/privoxy/config.pacorig
  [2010-05-28 16:16] warning: directory permissions differ on etc/privoxy/templates/
filesystem: 750  package: 770
  [2010-05-28 16:16] installed privoxy (3.0.16-1)
  [2010-05-28 16:18] installed lynx (2.8.7-2)
  [2010-05-28 16:18] warning: /etc/lighttpd/lighttpd.conf saved as /etc/lighttpd/lighttpd.conf.pacorig
  [2010-05-28 16:18] installed lighttpd (1.4.26-3)
  [2010-05-28 16:18] upgraded mysql (5.1.46-2 -> 5.1.46-2)
  [2010-05-28 16:19] upgraded lua (5.1.4-4 -> 5.1.4-4)
  [2010-05-28 16:19] installed xine-ui (0.99.6-1)
  [2010-05-28 16:20] upgraded mplayer (31147-2 -> 31147-2)
  [2010-05-28 16:20] installed smplayer (0.6.9-2)
  [2010-05-28 16:20] installed mutagen (1.19-1)
  [2010-05-28 16:20] installed exaile (0.3.1.1-1)
  [2010-05-28 16:22] upgraded exaile (0.3.1.1-1 -> 0.3.1.1-1)
  [2010-05-28 16:25] installed gstreamer0.10-bad (0.10.18-5)
  [2010-05-28 16:25] installed libusb1 (1.0.8-1)
  [2010-05-28 16:25] installed libdc1394 (2.1.2-1)
  [2010-05-28 16:25] installed libmms (0.5-2)
  [2010-05-28 16:25] installed libcdaudio (0.99.12-4)
  [2010-05-28 16:25] installed mjpegtools (1.9.0-3)
  [2010-05-28 16:25] installed libdvdread (4.1.3-2)
  [2010-05-28 16:25] installed libdvdnav (4.1.3-2)
  [2010-05-28 16:25] installed libmodplug (0.8.8.1-1)
  [2010-05-28 16:25] installed ladspa (1.13-2)
  [2010-05-28 16:25] installed liblrdf (0.4.0-6)
  [2010-05-28 16:25] installed soundtouch (1.5.0-1)
  [2010-05-28 16:25] installed libass (0.9.9-1)
  [2010-05-28 16:25] installed gstreamer0.10-bad-plugins (0.10.18-5)
  [2010-05-28 16:25] installed gstreamer0.10-ffmpeg (0.10.10-1)
  [2010-05-28 16:25] installed gstreamer0.10-ugly (0.10.14-4)
  [2010-05-28 16:25] installed libmpeg2 (0.5.1-1)
  [2010-05-28 16:25] installed libsidplay (1.36.59-4)
  [2010-05-28 16:25] installed gstreamer0.10-ugly-plugins (0.10.14-4)
  [2010-05-28 16:59] upgraded qt3 (3.3.8-17 -> 3.3.8-17)
  [2010-05-28 16:59] upgraded qt (4.6.2-4 -> 4.6.2-4)
  [2010-05-28 18:33] installed gtk-qt-engine (1.1-2)
  [2010-05-28 18:33] Change /etc/conf.d/vde to your needs.
  [2010-05-28 18:33] vde config files should be placed in /etc/vde, sample files are provided.
  [2010-05-28 18:33] iptables and dhcpd sample files have been installed to '/usr/share/vde2'.
  [2010-05-28 18:33] Merge those examples, if needed to the according config files.
  [2010-05-28 18:33] installed vde2 (2.2.2-6)
  [2010-05-28 18:33] >>> PLEASE READ FOR KVM USAGE!
  [2010-05-28 18:33] >>>  Load the correct KVM module, you will need a KVM capable CPU!
  [2010-05-28 18:33] >>>  Add yourself to the group 'kvm'.
  [2010-05-28 18:33] >>>  Use 'qemu -enable-kvm' to use KVM.
  [2010-05-28 18:33] 
  [2010-05-28 18:33] installed qemu (0.12.4-1)
  [2010-05-28 18:33] installed qtemu (1.0.5-3)
  [2010-05-28 18:33] installed qtcreator (1.3.1-1)
  [2010-05-28 18:33] installed recordmydesktop (0.3.8.1-4)
  [2010-05-28 18:33] installed qt-recordmydesktop (0.3.8-1)
  [2010-05-28 18:33] installed qtpfsgui (1.9.3-5)
  [2010-05-28 18:33] installed kvirc (3.4.2-4)
  [2010-05-28 18:33] installed xchat (2.8.6-6)
  [2010-05-28 18:33] installed silc-toolkit (1.1.10-1)
  [2010-05-28 18:33] installed cyrus-sasl-plugins (2.1.23-2)
  [2010-05-28 18:33] installed libpurple (2.7.0-1)
  [2010-05-28 18:33] installed pidgin (2.7.0-1)
  [2010-05-28 18:33] installed perl-error (0.17016-1)
  [2010-05-28 18:33] installed git (1.7.1-1)
  [2010-05-28 18:33] installed qgit (2.3-2)
  [2010-05-28 18:33] installed avidemux-cli (2.5.3-1)
  [2010-05-28 18:33] installed avidemux-qt (2.5.3-1)
  [2010-05-28 18:33] installed noyau (2.1-2)
  [2010-05-28 18:33] 
  [2010-05-28 18:33] The correct device mode and /dev device file will need to be set in
  [2010-05-28 18:33] /etc/conf.d/inputattach.conf before starting /etc/rc.d/inputattach
  [2010-05-28 18:33] 
  [2010-05-28 18:33] installed inputattach (1.24-2)
  [2010-05-28 18:33] installed inotail (0.5-3)
  [2010-05-28 18:33] installed quota-tools (3.17-1)
  [2010-05-28 18:33] installed xsensors (0.60-2)
  [2010-05-28 18:33] installed ksensors (0.7.3-5)
  [2010-05-28 18:33] installed ruby-glib2 (0.19.3-1)
  [2010-05-28 18:33] installed ruby-atk (0.19.3-1)
  [2010-05-28 18:33] installed ruby-pango (0.19.3-2)
  [2010-05-28 18:33] installed ruby-gdkpixbuf2 (0.19.3-2)
  [2010-05-28 18:33] installed ruby-rcairo (1.8.0-2)
  [2010-05-28 18:33] installed ruby-gtk2 (0.19.3-1)
  [2010-05-28 18:33] installed glib (1.2.10-8.1)
  [2010-05-28 18:33] installed gtk (1.2.10-10)
  [2010-05-28 18:33] installed gtk-theme-switch2 (2.1.0-1)
  [2010-05-28 18:33] installed gtk-theme-switch (1.0.1-3)
  [2010-05-28 18:33] installed gtk-xfce-engine (2.6.0-1)
  [2010-05-28 18:33] installed imlib (1.9.15-9)
  [2010-05-28 18:33] installed gtk1-engines (0.12-2)
  [2010-05-28 18:33] installed glib-perl (1.222-1)
  [2010-05-28 18:33] installed cairo-perl (1.061-1)
  [2010-05-28 18:33] installed pango-perl (1.221-1)
  [2010-05-28 18:33] installed gtk2-perl (1.221-1)
  [2010-05-28 20:00] installed cmake (2.8.1-2)
  [2010-05-28 20:01] installed cabextract (1.2-2)
  [2010-05-28 20:01] extracting fonts... done.
  [2010-05-28 20:02] rebuilding font cache... done.
  [2010-05-28 20:02] installed ttf-ms-fonts (2.0-3)
  [2010-05-28 20:03] removed boost (1.41.0-1)
  [2010-05-28 20:30] installed freeimage (3.13.1-1)
  [2010-05-28 20:30] installed zziplib (0.13.58-2)
  [2010-05-28 21:11] installed openal (1.12.854-1)
  [2010-05-28 21:11] installed freealut (1.1.0-3)
  [2010-05-28 21:36] removed freeimage (3.13.1-1)
  [2010-05-28 22:14] installed strace (4.5.20-1)
  [2010-05-29 06:23] installed gdb (7.1-2)
  [2010-05-29 09:36] installed gnome-alsamixer (0.9.6-3)
  [2010-05-29 09:36] installed alsa-firmware (1.0.23-1)
  [2010-05-29 13:20] NOTE:
  [2010-05-29 13:20]   If you experience any problems after installing xsane 
  [2010-05-29 13:20]   it may help to remove the setup and preferences files
  [2010-05-29 13:20]   of xsane:
  [2010-05-29 13:20] 
  [2010-05-29 13:20]     $ rm -rf ~/.sane/xsane
  [2010-05-29 13:20] 
  [2010-05-29 13:20] installed xsane (0.997-2)
  [2010-05-29 13:28] installed gimmage (0.2.3-2)
  [2010-05-29 22:23] installed libgnomecups (0.2.3-7)
  [2010-05-29 22:23] installed libgnomeprint (2.18.7-2)
  [2010-05-29 22:23] installed libgnomeprintui (2.18.5-1)
  [2010-05-29 22:23] installed ghex (2.24.0-1)
  [2010-05-30 10:05] synchronizing package lists
  [2010-05-30 10:05] starting full system upgrade
  [2010-05-30 10:07] synchronizing package lists
  [2010-05-30 10:07] starting full system upgrade
  [2010-05-30 10:11] upgraded linux-api-headers (2.6.33.2-1 -> 2.6.34-1)
  [2010-05-30 10:11] warning: /etc/locale.gen installed as /etc/locale.gen.pacnew
  [2010-05-30 10:11] Generating locales...
  [2010-05-30 10:11]   en_GB.UTF-8... done
  [2010-05-30 10:11]   en_GB.ISO-8859-1... done
  [2010-05-30 10:11] Generation complete.
  [2010-05-30 10:11] upgraded glibc (2.11.1-3 -> 2.12-2)
  [2010-05-30 10:11] upgraded binutils (2.20.1-2 -> 2.20.1-3)
  [2010-05-30 10:11] upgraded gcc (4.5.0-2 -> 4.5.0-3)
  [2010-05-30 10:11] upgraded gcc-ada (4.5.0-2 -> 4.5.0-3)
  [2010-05-30 10:11] upgraded gcc-fortran (4.5.0-2 -> 4.5.0-3)
  [2010-05-30 10:11] upgraded gcc-libs (4.5.0-2 -> 4.5.0-3)
  [2010-05-30 10:11] upgraded gcc-objc (4.5.0-2 -> 4.5.0-3)
  [2010-05-30 10:11] upgraded libmysqlclient (5.1.46-2 -> 5.1.47-1)
  [2010-05-30 10:11] upgraded mysql-clients (5.1.46-2 -> 5.1.47-1)
  [2010-05-30 10:11] upgraded mysql (5.1.46-2 -> 5.1.47-1)
  [2010-05-30 10:11] Fixing gshadow file ...
  [2010-05-30 10:11] upgraded shadow (4.1.4.2-2 -> 4.1.4.2-3)
  [2010-05-30 10:11] upgraded tar (1.23-2 -> 1.23-3)
  [2010-05-30 10:11] upgraded udisks (1.0.1-1 -> 1.0.1-2)
  [2010-05-30 10:11] upgraded whois (5.0.4-1 -> 5.0.5-1)
  [2010-06-03 10:41] synchronizing package lists
  [2010-06-03 10:42] starting full system upgrade
  [2010-06-03 10:43] installed cvs (1.11.23-5)
  [2010-06-03 10:43] installed libnet (1.1.4-1)
  [2010-06-03 10:43] installed ettercap (NG_0.7.3-15)
  [2010-06-03 10:43] installed ettercap-gtk (NG_0.7.3-7)
  [2010-06-03 10:43] installed libnids (1.24-1)
  [2010-06-03 10:43] installed dsniff (2.4b1-17)
  [2010-06-03 10:51] synchronizing package lists
  [2010-06-03 10:52] installed kdebindings-smoke (4.4.4-1)
  [2010-06-03 10:52] installed kdebindings-ruby (4.4.4-1)
  [2010-06-03 10:52] installed mysql-ruby (2.8.1-2)
  [2010-06-03 10:52] installed ruby-docs (1.9.1_p378-2)
  [2010-06-03 10:52] installed ruby-gconf2 (0.19.3-2)
  [2010-06-03 10:52] installed ruby-locale (2.0.5-1)
  [2010-06-03 10:52] installed ruby-gettext (2.1.0-1)
  [2010-06-03 10:52] installed ruby-libart (0.19.3-2)
  [2010-06-03 10:52] installed ruby-gnomecanvas (0.19.3-3.1)
  [2010-06-03 10:52] installed ruby-gnome2 (0.19.4-1)
  [2010-06-03 10:52] installed ruby-hpricot (0.8.2-1)
  [2010-06-03 10:52] installed ruby-libglade (0.19.3-1)
  [2010-06-03 10:52] installed ruby-mpd (0.2.3-1)
  [2010-06-03 10:52] installed ruby-ncurses (1.2.4-1)
  [2010-06-03 10:52] installed ruby-sqlite3 (1.2.4-2)
  [2010-06-03 10:52] warning: /etc/vimrc saved as /etc/vimrc.pacorig
  [2010-06-03 10:52] installed vim-runtime (7.2-1)
  [2010-06-03 10:52] installed vim (7.2-1)
  [2010-06-03 10:52] updating Vim help tags... done.
  [2010-06-03 10:52] installed vim-rails (4.2-1)
  [2010-06-03 11:06] synchronizing package lists
  [2010-06-03 11:07] starting full system upgrade
  [2010-06-03 12:43] starting full system upgrade
  [2010-06-03 14:50] starting full system upgrade
  [2010-06-04 08:27] upgraded gcc (4.5.0-3 -> 4.5.0-4)
  [2010-06-04 08:27] upgraded gcc-libs (4.5.0-3 -> 4.5.0-4)
  [2010-06-04 08:27] upgraded gcc-ada (4.5.0-3 -> 4.5.0-4)
  [2010-06-04 08:27] upgraded gcc-objc (4.5.0-3 -> 4.5.0-4)
  [2010-06-04 08:27] upgraded gcc-fortran (4.5.0-3 -> 4.5.0-4)
  [2010-06-05 08:49] installed macchanger (1.5.0-3)
  [2010-06-07 15:19] installed k3b (1.92.0rc3-1)
  [2010-06-07 15:21] installed vcdimager (0.7.23-7)
  [2010-06-07 15:21] installed imagemagick (6.6.2.0-1)
  [2010-06-07 15:21] installed transcode (1.1.5-3)
  [2010-06-07 15:21] installed emovix (0.9.0-4)
  [2010-06-08 08:51] installed dia (0.97-3)
  [2010-06-11 07:03] synchronizing package lists
  [2010-06-11 07:07] upgraded thunderbird (3.0.4-1 -> 3.0.4-1)
  [2010-06-11 07:10] upgraded pango (1.28.0-1 -> 1.28.0-1)
  [2010-06-11 07:10] upgraded pangomm (2.26.2-1 -> 2.26.2-1)
  [2010-06-11 08:19] installed zip (3.0-1)
  [2010-06-11 08:19] upgraded unzip (6.0-5 -> 6.0-5)
  [2010-06-13 09:15] synchronizing package lists
  [2010-06-13 09:17] installed qca-gnupg (2.0.0-1)
  [2010-06-13 09:17] installed psi (0.14-3)
  [2010-06-13 12:00] installed wxgtk (2.8.11-1)
  [2010-06-13 12:00] installed filezilla (3.3.2.1-1)
  [2010-06-13 12:44] upgraded libpurple (2.7.0-1 -> 2.7.1-1)
  [2010-06-13 12:44] upgraded pidgin (2.7.0-1 -> 2.7.1-1)
  [2010-06-16 09:09] synchronizing package lists
  [2010-06-25 11:48] installed printproto (1.0.4-2)
  [2010-06-25 11:48] installed libxp (1.0.0-3)
  [2010-06-25 11:48] installed lesstif (0.95.2-2)
  [2010-06-25 11:48] installed xpdf (3.02_pl4-2)
  [2010-06-25 11:53] upgraded silc-toolkit (1.1.10-1 -> 1.1.10-1)
  [2010-06-25 12:44] installed giblib (1.2.4-4)
  [2010-06-25 12:44] installed scrot (0.8-4)
  [2010-06-26 14:27] synchronizing package lists
  [2010-06-26 14:28] warning: /etc/pacman.conf installed as /etc/pacman.conf.pacnew
  [2010-06-26 14:28] warning: /etc/makepkg.conf installed as /etc/makepkg.conf.pacnew
  [2010-06-26 14:28] upgraded pacman (3.3.3-5 -> 3.4.0-2)
  [2010-06-26 14:28] Running 'pacman -S --noconfirm xfce4'
  [2010-06-26 14:29] upgraded gtk-xfce-engine (2.6.0-1 -> 2.6.0-1)
  [2010-06-26 14:29] installed libxfce4util (4.6.2-1)
  [2010-06-26 14:29] installed xfconf (4.6.2-1)
  [2010-06-26 14:29] installed libxfcegui4 (4.6.4-1)
  [2010-06-26 14:29] installed mousepad (0.2.16-2)
  [2010-06-26 14:29] installed exo (0.3.107-1)
  [2010-06-26 14:29] installed xfce4-panel (4.6.4-1)
  [2010-06-26 14:29] installed orage (4.6.1-1)
  [2010-06-26 14:29] installed terminal (0.4.5-1)
  [2010-06-26 14:29] installed thunar (1.0.2-1)
  [2010-06-26 14:29] NOTE
  [2010-06-26 14:29] ----
  [2010-06-26 14:29]  > xfce can run on top of a framebuffer. However, for most users it is
  [2010-06-26 14:29]  > best to install xorg as an x-server. Please install either xorg-xinit
  [2010-06-26 14:29]  > as minimal environment or the xorg meta package.
  [2010-06-26 14:29]  pacman -S xorg-xinit
  [2010-06-26 14:29]       -- or --
  [2010-06-26 14:29]  pacman -S xorg
  [2010-06-26 14:29] installed xfce-utils (4.6.2-1)
  [2010-06-26 14:29] installed libxfce4menu (4.6.2-1)
  [2010-06-26 14:29] installed xfce4-appfinder (4.6.2-1)
  [2010-06-26 14:29] installed xfce4-mixer (4.6.1-1)
  [2010-06-26 14:29] installed xfce4-session (4.6.2-1)
  [2010-06-26 14:29] installed tango-icon-theme (0.8.90-2)
  [2010-06-26 14:29] installed xfce4-settings (4.6.5-1)
  [2010-06-26 14:30] installed xfdesktop (4.6.2-1)
  [2010-06-26 14:30] installed psutils (1.17-2)
  [2010-06-26 14:30] installed a2ps (4.14-1)
  [2010-06-26 14:30] installed xfprint (4.6.1-3)
  [2010-06-26 14:30] installed xfwm4 (4.6.2-1)
  [2010-06-26 14:30] installed xfwm4-themes (4.6.0-1)
  [2010-06-26 16:36] Running 'pacman -Sy'
  [2010-06-26 16:36] synchronizing package lists
  [2010-06-26 16:38] Running 'pacman -Scc'



