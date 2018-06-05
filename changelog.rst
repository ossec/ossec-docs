Change Log
----------


upcoming (2015/02/21 20:11 +00:00)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  `#553 <https://github.com/ossec/ossec-hids/pull/553>`__ Use the
   MAKEBIN variable instead of hardcoded make (@ddpbsd)
-  `#551 <https://github.com/ossec/ossec-hids/pull/551>`__ Output
   alerts.json, newline delimited json, beside the alerts.log file.
   (@jondb)
-  `#547 <https://github.com/ossec/ossec-hids/pull/547>`__ Feature/nfs
   exclusion v2 (@reyjrar)
-  `#549 <https://github.com/ossec/ossec-hids/pull/549>`__ Fixed typo
   (@gustavo-gomez)
-  `#548 <https://github.com/ossec/ossec-hids/pull/548>`__ Fix
   misspelling of 'source' (@DazWorrall)
-  `#546 <https://github.com/ossec/ossec-hids/pull/546>`__ several
   Coverity fixes (@cgzones)
-  `#545 <https://github.com/ossec/ossec-hids/pull/545>`__ remove
   coverity plugin from travis, because it does not work properly
   (@cgzones)
-  `#537 <https://github.com/ossec/ossec-hids/pull/537>`__ fix most gcc
   -Wall -Wextra warnings in windows build (@cgzones)
-  `#544 <https://github.com/ossec/ossec-hids/pull/544>`__ Correct some
   spelling, and update based on ossec-docs (@ddpbsd)

2.9.0-beta03 (2015/02/09 14:01 +00:00)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  `#536 <https://github.com/ossec/ossec-hids/pull/536>`__ analysisd:
   fix compiler warnings (@cgzones)
-  `#542 <https://github.com/ossec/ossec-hids/pull/542>`__ Coverity
   fixes (@cgzones)
-  `#508 <https://github.com/ossec/ossec-hids/pull/508>`__ enable web
   attack detection for IIS with status code 200 (@ChristianBeer)
-  `#539 <https://github.com/ossec/ossec-hids/pull/539>`__ Coverity
   travis (@cgzones)
-  `#538 <https://github.com/ossec/ossec-hids/pull/538>`__ Remove unused
   windows build (@awiddersheim)
-  `#533 <https://github.com/ossec/ossec-hids/pull/533>`__ add
   information about matched and expected decoders to logtest
   (@ChristianBeer)
-  `#528 <https://github.com/ossec/ossec-hids/pull/528>`__ Add
   contributors and remove white space (@awiddersheim)
-  `#530 <https://github.com/ossec/ossec-hids/pull/530>`__ Remove old
   build files that are no longer used (@awiddersheim)
-  `#531 <https://github.com/ossec/ossec-hids/pull/531>`__ Rename
   vista\_sec.csv to vista\_sec.txt (@awiddersheim)
-  `#534 <https://github.com/ossec/ossec-hids/pull/534>`__ increase
   timeout for md5sha1 testcase, reported in #532 (@cgzones)
-  `#529 <https://github.com/ossec/ossec-hids/pull/529>`__ Fix potential
   uninitialized value (@awiddersheim)
-  `#526 <https://github.com/ossec/ossec-hids/pull/526>`__ possible fix
   to vista\_sec.csv (@ChristianBeer)
-  `#527 <https://github.com/ossec/ossec-hids/pull/527>`__ fix rule
   18138 (@martindiv)
-  `#512 <https://github.com/ossec/ossec-hids/pull/512>`__ exit on
   single unit test failure (@cgzones)
-  `#516 <https://github.com/ossec/ossec-hids/pull/516>`__ add decoder
   for ossec-logcollector messages (@ChristianBeer)
-  `#511 <https://github.com/ossec/ossec-hids/pull/511>`__ remove
   unknown code (@cgzones)
-  `#513 <https://github.com/ossec/ossec-hids/pull/513>`__ merge windows
   buildlogic into main makefile (@cgzones)

2.9.0-beta01 (2015/01/31 23:35 +00:00)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  `#515 <https://github.com/ossec/ossec-hids/pull/515>`__ fix some
   Coverity issues (@cgzones)
-  `#514 <https://github.com/ossec/ossec-hids/pull/514>`__ fix warnings
   (@cgzones)
-  `#510 <https://github.com/ossec/ossec-hids/pull/510>`__ clean up
   analysisd/output and fix #488 (@cgzones)
-  `#509 <https://github.com/ossec/ossec-hids/pull/509>`__ fix
   compilation without libssl-dev and libz-dev installed (@cgzones)
-  `#506 <https://github.com/ossec/ossec-hids/pull/506>`__ Freebsd
   inotify (@ddpbsd)
-  `#502 <https://github.com/ossec/ossec-hids/pull/502>`__ Giant
   code-formatting patch (@wclarie)
-  `#501 <https://github.com/ossec/ossec-hids/pull/501>`__ Add support
   for FQDN in csyslogd (@ccooke)
-  `#500 <https://github.com/ossec/ossec-hids/pull/500>`__ Travis builds
   (@jrossi)
-  `#499 <https://github.com/ossec/ossec-hids/pull/499>`__ less sloppy
   indenting (@ddpbsd)
-  `#494 <https://github.com/ossec/ossec-hids/pull/494>`__ Fix for issue
   #463 (rule overwrites causing a segfault) (@ddpbsd)
-  `#496 <https://github.com/ossec/ossec-hids/pull/496>`__ Fixes to
   event channel code (@awiddersheim)
-  `#497 <https://github.com/ossec/ossec-hids/pull/497>`__ Fix the wrong
   ARGV0 defined for authd causing the init script to fail (@nixfloyd)

snapshot/20150112 (2015/01/11 13:57 +00:00)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  `#493 <https://github.com/ossec/ossec-hids/pull/493>`__ Remove
   install message to email Daniel Cid for all languages (@sexybiggetje)
-  `#491 <https://github.com/ossec/ossec-hids/pull/491>`__ nginx tests -
   without false positives (@dangarthwaite)
-  `#492 <https://github.com/ossec/ossec-hids/pull/492>`__ Fix cleanup
   code in mkstemp\_ex() for Windows (@awiddersheim)
-  `#482 <https://github.com/ossec/ossec-hids/pull/482>`__
   Whitespace/pep8 and option to run just one test (@dangarthwaite)
-  `#476 <https://github.com/ossec/ossec-hids/pull/476>`__ Add new rule
   to proftpd ruleset (@ChristianBeer)
-  `#485 <https://github.com/ossec/ossec-hids/pull/485>`__ Update
   msauth\_rules.xml (@hyn172)
-  `#486 <https://github.com/ossec/ossec-hids/pull/486>`__ Test web
   appsec rules (@dangarthwaite)
-  `#489 <https://github.com/ossec/ossec-hids/pull/489>`__ match failed
   authentication at OSX login window (@mikedowney01)
-  `#477 <https://github.com/ossec/ossec-hids/pull/477>`__ Fix incorrect
   declaration (@awiddersheim)
-  `#474 <https://github.com/ossec/ossec-hids/pull/474>`__ Sudo rule fix
   and sample log (@ddpbsd)
-  `#439 <https://github.com/ossec/ossec-hids/pull/439>`__ Cleanup more
   makefile and some standardization for output. (@jrossi)
-  `#457 <https://github.com/ossec/ossec-hids/pull/457>`__ Fix windows
   event channel (@awiddersheim)
-  `#465 <https://github.com/ossec/ossec-hids/pull/465>`__ Added src/dst
   IP and username to the email if it exists in the alert\_data.
   (@reyjrar)
-  `#468 <https://github.com/ossec/ossec-hids/pull/468>`__
   os\_auth/main-server.c won't compile without any headers (@reyjrar)
-  `#460 <https://github.com/ossec/ossec-hids/pull/460>`__ bitrig uses
   gmake. (@ddpbsd)
-  `#458 <https://github.com/ossec/ossec-hids/pull/458>`__ Fix log
   message during client startup (@awiddersheim)
-  `#456 <https://github.com/ossec/ossec-hids/pull/456>`__ Update
   README.md (@jeffreyjackson)
-  `#452 <https://github.com/ossec/ossec-hids/pull/452>`__ catching PHP
   Notices in Apache 2.4 error log (@ChristianBeer)
-  `#450 <https://github.com/ossec/ossec-hids/pull/450>`__ fix to sshd
   rules (@ChristianBeer)
-  `#451 <https://github.com/ossec/ossec-hids/pull/451>`__ Apache tests
   added (@ChristianBeer)
-  `#449 <https://github.com/ossec/ossec-hids/pull/449>`__ Fix include
   order warnings when compiling win32 (@awiddersheim)
-  `#448 <https://github.com/ossec/ossec-hids/pull/448>`__ Fix manage
   agents error messaage compile warning (@awiddersheim)
-  `#441 <https://github.com/ossec/ossec-hids/pull/441>`__ Fix
   csyslogd-config XML syslog location definition (@mikey-austin)
-  `#440 <https://github.com/ossec/ossec-hids/pull/440>`__ Format
   breakout format options into small bit of code (@jrossi)
-  `#435 <https://github.com/ossec/ossec-hids/pull/435>`__ Installation
   (@ddpbsd)
-  `#436 <https://github.com/ossec/ossec-hids/pull/436>`__ Build
   (@ddpbsd)
-  `#433 <https://github.com/ossec/ossec-hids/pull/433>`__ fix compiler
   warnings reported in #421 (@cgzones)
-  `#428 <https://github.com/ossec/ossec-hids/pull/428>`__ fully
   integrate Apparmor rules (@ddpbsd)
-  `#427 <https://github.com/ossec/ossec-hids/pull/427>`__ Zmq (@ddpbsd)
-  `#424 <https://github.com/ossec/ossec-hids/pull/424>`__ More decoder
   testing (@jrossi)
-  `#426 <https://github.com/ossec/ossec-hids/pull/426>`__ fixes #425
   moves srandom before chroot (@jrossi)
-  `#423 <https://github.com/ossec/ossec-hids/pull/423>`__ Zeromq
   (@ddpbsd)
-  `#412 <https://github.com/ossec/ossec-hids/pull/412>`__
   [os\_csyslogd] fix some compiler warnings (@cgzones)
-  `#411 <https://github.com/ossec/ossec-hids/pull/411>`__ fix #409
   (@cgzones)
-  `#414 <https://github.com/ossec/ossec-hids/pull/414>`__ standalone
   script for firewalld on Linux (@ChristianBeer)
-  `#413 <https://github.com/ossec/ossec-hids/pull/413>`__ Decoder fix
   for Apache 2.4 (@ChristianBeer)
-  `#408 <https://github.com/ossec/ossec-hids/pull/408>`__ adding
   -Werror flag (@cgzones)
-  `#401 <https://github.com/ossec/ossec-hids/pull/401>`__ syscall
   errors (@cgzones)
-  `#407 <https://github.com/ossec/ossec-hids/pull/407>`__ rename
   memset\_s to memset\_secure (@cgzones)
-  `#397 <https://github.com/ossec/ossec-hids/pull/397>`__ enabling rule
   tests (@jrossi)
-  `#406 <https://github.com/ossec/ossec-hids/pull/406>`__ fix uid/gid
   conversions (@cgzones)
-  `#400 <https://github.com/ossec/ossec-hids/pull/400>`__ fix remaining
   -Wextra issues (@cgzones)
-  `#402 <https://github.com/ossec/ossec-hids/pull/402>`__ use memset\_s
   on sensitive data (@cgzones)
-  `#403 <https://github.com/ossec/ossec-hids/pull/403>`__ update ar
   command (@cgzones)
-  `#404 <https://github.com/ossec/ossec-hids/pull/404>`__ fix recent
   coverity warnings (@cgzones)
-  `#405 <https://github.com/ossec/ossec-hids/pull/405>`__ make map
   not-static, so it is not instantiated in every translation unit
   (@cgzones)
-  `#398 <https://github.com/ossec/ossec-hids/pull/398>`__ Cppcheck
   cleanup (@jrossi)
-  `#396 <https://github.com/ossec/ossec-hids/pull/396>`__ enabling
   apparmor for new installs (@jrossi)
-  `#395 <https://github.com/ossec/ossec-hids/pull/395>`__ moving
   srandom\_init before chroot (@jrossi)
-  `#385 <https://github.com/ossec/ossec-hids/pull/385>`__ os\_auth
   (@cgzones)
-  `#393 <https://github.com/ossec/ossec-hids/pull/393>`__ remove
   obsolete Makeall script (@cgzones)
-  `#392 <https://github.com/ossec/ossec-hids/pull/392>`__ correctly
   setup slack+travis based on ossec/ossec-hids (@jrossi)
-  `#389 <https://github.com/ossec/ossec-hids/pull/389>`__ Fix
   formatting of chmod() and ErrorExit() params (@awiddersheim)
-  `#377 <https://github.com/ossec/ossec-hids/pull/377>`__ seed random
   with a real random data (@jrossi)
-  `#383 <https://github.com/ossec/ossec-hids/pull/383>`__
   [client-agent] fix compiler warnings (@cgzones)
-  `#388 <https://github.com/ossec/ossec-hids/pull/388>`__ fix chmod
   error message (@cgzones)
-  `#387 <https://github.com/ossec/ossec-hids/pull/387>`__ [reportd] fix
   compiler warnings (@cgzones)
-  `#386 <https://github.com/ossec/ossec-hids/pull/386>`__ [remoted] fix
   compiler warnings (@cgzones)
-  `#384 <https://github.com/ossec/ossec-hids/pull/384>`__ [monitord]
   fix compiler warnings (@cgzones)
-  `#382 <https://github.com/ossec/ossec-hids/pull/382>`__ [os\_auth]
   force usage of TLSv1.2 (@cgzones)
-  `#380 <https://github.com/ossec/ossec-hids/pull/380>`__ Lua loading
   paths (@jrossi)
-  `#336 <https://github.com/ossec/ossec-hids/pull/336>`__ Fix manage
   agents keys (@awiddersheim)
-  `#379 <https://github.com/ossec/ossec-hids/pull/379>`__ Remove unused
   files and moved files into correct location. (@jrossi)
-  `#378 <https://github.com/ossec/ossec-hids/pull/378>`__ integrations
   into slack (@jrossi)
-  `#376 <https://github.com/ossec/ossec-hids/pull/376>`__ Merge test
   makefile (@cgzones)
-  `#374 <https://github.com/ossec/ossec-hids/pull/374>`__ agentlessd
   (@cgzones)
-  `#373 <https://github.com/ossec/ossec-hids/pull/373>`__ My Old code
   cleanup (@jrossi)
-  `#368 <https://github.com/ossec/ossec-hids/pull/368>`__ rootcheck
   (@cgzones)
-  `#367 <https://github.com/ossec/ossec-hids/pull/367>`__ syscheck
   (@cgzones)
-  `#372 <https://github.com/ossec/ossec-hids/pull/372>`__ addagent
   (@cgzones)
-  `#371 <https://github.com/ossec/ossec-hids/pull/371>`__ util
   (@cgzones)
-  `#361 <https://github.com/ossec/ossec-hids/pull/361>`__ logcollector
   (@cgzones)
-  `#364 <https://github.com/ossec/ossec-hids/pull/364>`__ better file
   handling on update (@cgzones)
-  `#363 <https://github.com/ossec/ossec-hids/pull/363>`__ [tests] set
   timeout for OS\_GetHost() tests to 10 seconds (@cgzones)
-  `#360 <https://github.com/ossec/ossec-hids/pull/360>`__ Fix compile
   warnings printing size\_t (@awiddersheim)
-  `#357 <https://github.com/ossec/ossec-hids/pull/357>`__ Fix build
   settings (@awiddersheim)
-  `#359 <https://github.com/ossec/ossec-hids/pull/359>`__ os\_execd
   (@cgzones)
-  `#356 <https://github.com/ossec/ossec-hids/pull/356>`__ Permission
   fix (@cgzones)
-  `#355 <https://github.com/ossec/ossec-hids/pull/355>`__ Conversion
   fix (@cgzones)
-  `#354 <https://github.com/ossec/ossec-hids/pull/354>`__ fix
   displaying settings after build (@cgzones)
-  `#352 <https://github.com/ossec/ossec-hids/pull/352>`__ fix several
   -Wextra warnings (@cgzones)
-  `#353 <https://github.com/ossec/ossec-hids/pull/353>`__ fix
   compilation color (@cgzones)
-  `#351 <https://github.com/ossec/ossec-hids/pull/351>`__ display
   defaults for PREFIX and MAXAGENTS in make help (@cgzones)
-  `#350 <https://github.com/ossec/ossec-hids/pull/350>`__ Update log.c
   (@jrossi)
-  `#345 <https://github.com/ossec/ossec-hids/pull/345>`__ Makefile
   tweaks (@ddpbsd)
-  `#346 <https://github.com/ossec/ossec-hids/pull/346>`__ Output
   settings after doing a build (@awiddersheim)
-  `#347 <https://github.com/ossec/ossec-hids/pull/347>`__ clean up
   .gitignore (@cgzones)
-  `#349 <https://github.com/ossec/ossec-hids/pull/349>`__ fix spelling
   (@cgzones)
-  `#343 <https://github.com/ossec/ossec-hids/pull/343>`__ gnu make
   fallout (@ddpbsd)
-  `#344 <https://github.com/ossec/ossec-hids/pull/344>`__ fix spelling
   for clean-internals (@cgzones)
-  `#334 <https://github.com/ossec/ossec-hids/pull/334>`__ Makefile need
   love too (@jrossi)
-  `#341 <https://github.com/ossec/ossec-hids/pull/341>`__ fix several
   Coverity issues (@cgzones)
-  `#338 <https://github.com/ossec/ossec-hids/pull/338>`__ Fix include
   order warnings when compiling win32 (@awiddersheim)
-  `#339 <https://github.com/ossec/ossec-hids/pull/339>`__ Remove unused
   variable (@awiddersheim)
-  `#324 <https://github.com/ossec/ossec-hids/pull/324>`__ Better
   differentiation between web-access and pure-transfer logs (@bchavet)
-  `#337 <https://github.com/ossec/ossec-hids/pull/337>`__ Fix compile
   warnings printing size\_t (@awiddersheim)
-  `#335 <https://github.com/ossec/ossec-hids/pull/335>`__ fix
   compilation without ssl (DEFAULT\_PORT is not defined) (@cgzones)
-  `#333 <https://github.com/ossec/ossec-hids/pull/333>`__ fix postgres
   (@cgzones)
-  `#332 <https://github.com/ossec/ossec-hids/pull/332>`__ os\_dbd
   (@cgzones)
-  `#331 <https://github.com/ossec/ossec-hids/pull/331>`__ - Add CIS 1.3
   benchmark for RHEL/CentOS 6 (@atomicturtle)
-  `#330 <https://github.com/ossec/ossec-hids/pull/330>`__ Decoder and
   Rules for apache-2.4 error logs (@bchavet)
-  `#326 <https://github.com/ossec/ossec-hids/pull/326>`__ use global
   variable \_\_local\_name instead of macro ARGV0 in libraries
   (@cgzones)
-  `#328 <https://github.com/ossec/ossec-hids/pull/328>`__ [os\_regex]
   do not use static maps (@cgzones)
-  `#329 <https://github.com/ossec/ossec-hids/pull/329>`__ Update
   cis\_rhel5\_linux\_rcl.txt (@atomicturtle)
-  `#325 <https://github.com/ossec/ossec-hids/pull/325>`__ fixing
   compiler warnings with "-O2 -Wall" (@cgzones)
-  `#323 <https://github.com/ossec/ossec-hids/pull/323>`__ derp, forgot
   that the domains end in a . (@ddpbsd)
-  `#322 <https://github.com/ossec/ossec-hids/pull/322>`__ extra\_data
   doesn't seem to be a supported field for cdb lists. (@ddpbsd)
-  `#214 <https://github.com/ossec/ossec-hids/pull/214>`__ adding
   heloserver name to the options for email (@jrossi)
-  `#319 <https://github.com/ossec/ossec-hids/pull/319>`__ test
   searchAndReplace() with different sizes for search and replace string
   (@cgzones)
-  `#316 <https://github.com/ossec/ossec-hids/pull/316>`__ update
   postgresql.schema (@sechacking)
-  `#317 <https://github.com/ossec/ossec-hids/pull/317>`__ os\_maild
   (@cgzones)
-  `#318 <https://github.com/ossec/ossec-hids/pull/318>`__ fix
   searchAndReplace() (@cgzones)
-  `#315 <https://github.com/ossec/ossec-hids/pull/315>`__ Fix host deny
   (@ddpbsd)
-  `#313 <https://github.com/ossec/ossec-hids/pull/313>`__ fix 312
   (@cgzones)
-  `#309 <https://github.com/ossec/ossec-hids/pull/309>`__ fix for
   time.h time\_t on macosx. (@jrossi)
-  `#306 <https://github.com/ossec/ossec-hids/pull/306>`__ I have
   created a output dir in analysis to move some of the output plugins
   into. (@jrossi)
-  `#304 <https://github.com/ossec/ossec-hids/pull/304>`__ os\_net fixes
   (@cgzones)
-  `#273 <https://github.com/ossec/ossec-hids/pull/273>`__ shared review
   (re-up) (@cgzones)
-  `#274 <https://github.com/ossec/ossec-hids/pull/274>`__ config review
   (re-up) (@cgzones)
-  `#302 <https://github.com/ossec/ossec-hids/pull/302>`__ [os\_crypto]
   fix random value (@cgzones)
-  `#300 <https://github.com/ossec/ossec-hids/pull/300>`__ Do not
   truncate OS information in agent\_control (@awiddersheim)
-  `#249 <https://github.com/ossec/ossec-hids/pull/249>`__ mysql changes
   - all the mysql related patches from the atomic spec (@jrossi)
-  `#287 <https://github.com/ossec/ossec-hids/pull/287>`__ [os\_crypto]
   change timestamp type to time\_t (@cgzones)
-  `#286 <https://github.com/ossec/ossec-hids/pull/286>`__ [or\_regex]
   fix clang analyzer warning (@cgzones)
-  `#285 <https://github.com/ossec/ossec-hids/pull/285>`__ [os\_crypto]
   fix compiler warnings (@cgzones)
-  `#297 <https://github.com/ossec/ossec-hids/pull/297>`__ Fix
   manage\_agents help (@awiddersheim)
-  `#296 <https://github.com/ossec/ossec-hids/pull/296>`__
   [os\_csyslogd] fix pull request #246 (@cgzones)
-  `#291 <https://github.com/ossec/ossec-hids/pull/291>`__ Fix for
   CVE-2014-5284 which allows for root escalation via temp files
   (@jrossi)

2.8.1 (2014/09/09 02:03 +00:00)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  `#246 <https://github.com/ossec/ossec-hids/pull/246>`__ About
   feedback of data loss and lack of GEOIP (@rhelfter)
-  `#288 <https://github.com/ossec/ossec-hids/pull/288>`__ [os\_regex]
   remove unimplemented declaration of 'OS\_Match3' (@cgzones)
-  `#289 <https://github.com/ossec/ossec-hids/pull/289>`__ [os\_xml]
   remove unused and obsolete debug code (@cgzones)
-  `#284 <https://github.com/ossec/ossec-hids/pull/284>`__ [os\_xml]
   update examples (@cgzones)
-  `#283 <https://github.com/ossec/ossec-hids/pull/283>`__ [os\_regex]
   update examples (@cgzones)
-  `#282 <https://github.com/ossec/ossec-hids/pull/282>`__ reportd
   outsourcing (@cgzones)
-  `#272 <https://github.com/ossec/ossec-hids/pull/272>`__ Unbound
   (@ddpbsd)
-  `#279 <https://github.com/ossec/ossec-hids/pull/279>`__ Remove
   syscheck-baseline.c (@awiddersheim)
-  `#280 <https://github.com/ossec/ossec-hids/pull/280>`__ Remove
   extract-win-el.c (@awiddersheim)
-  `#281 <https://github.com/ossec/ossec-hids/pull/281>`__ Fix help for
   ossec-rootcheck (@awiddersheim)
-  `#277 <https://github.com/ossec/ossec-hids/pull/277>`__ Add defaults
   to help output (@awiddersheim)
-  `#270 <https://github.com/ossec/ossec-hids/pull/270>`__ Remove shared
   help (@awiddersheim)
-  `#275 <https://github.com/ossec/ossec-hids/pull/275>`__ keep repo
   clean after make all (@cgzones)
-  `#266 <https://github.com/ossec/ossec-hids/pull/266>`__ travis
   (@cgzones)
-  `#262 <https://github.com/ossec/ossec-hids/pull/262>`__ remove
   windows build related file on make clean (@cgzones)
-  `#261 <https://github.com/ossec/ossec-hids/pull/261>`__ os net unit
   tests (@cgzones)
-  `#264 <https://github.com/ossec/ossec-hids/pull/264>`__ 2.7.1 to 2.8
   (@ddpbsd)
-  `#257 <https://github.com/ossec/ossec-hids/pull/257>`__ Misc rules
   (@ddpbsd)
-  `#259 <https://github.com/ossec/ossec-hids/pull/259>`__ Random
   decoders rules (@ddpbsd)
-  `#260 <https://github.com/ossec/ossec-hids/pull/260>`__ run unit
   tests with valgrind (@cgzones)
-  `#231 <https://github.com/ossec/ossec-hids/pull/231>`__ Lines sent to
   SMTP server need to be terminated with , not . (@ibatten)
-  `#256 <https://github.com/ossec/ossec-hids/pull/256>`__ More openbsd
   (@ddpbsd)
-  `#255 <https://github.com/ossec/ossec-hids/pull/255>`__ More pam
   (@ddpbsd)
-  `#253 <https://github.com/ossec/ossec-hids/pull/253>`__ Apparmor ini2
   (@ddpbsd)
-  `#252 <https://github.com/ossec/ossec-hids/pull/252>`__ [tests] fix
   buffer overflow (@cgzones)
-  `#251 <https://github.com/ossec/ossec-hids/pull/251>`__ remove CPATH
   as it's not used by ossec build, but use used gcc (@jrossi)
-  `#250 <https://github.com/ossec/ossec-hids/pull/250>`__ Fix windows
   builds on travis. (@jrossi)
-  `#240 <https://github.com/ossec/ossec-hids/pull/240>`__ os\_ crypto
   (@cgzones)
-  `#242 <https://github.com/ossec/ossec-hids/pull/242>`__ os\_crypto
   unittest (@cgzones)
-  `#243 <https://github.com/ossec/ossec-hids/pull/243>`__ Apparmor
   (@ddpbsd)
-  `#237 <https://github.com/ossec/ossec-hids/pull/237>`__ Fixing
   hard-coded paths (@mstarks01)
-  `#241 <https://github.com/ossec/ossec-hids/pull/241>`__ fix comment
   in decoder.xml (@cgzones)
-  `#233 <https://github.com/ossec/ossec-hids/pull/233>`__
   Fix/accumulator null check (@reyjrar)
-  `#232 <https://github.com/ossec/ossec-hids/pull/232>`__ fix crash in
   is\_simple\_http\_request (@navtej)
-  `#229 <https://github.com/ossec/ossec-hids/pull/229>`__ Updated
   help.txt for Windows (@awiddersheim)
-  `#227 <https://github.com/ossec/ossec-hids/pull/227>`__ Fix Windows
   Installed Date (@awiddersheim)
-  `#226 <https://github.com/ossec/ossec-hids/pull/226>`__ Fixes to
   make.sh for Windows (@awiddersheim)
-  `#221 <https://github.com/ossec/ossec-hids/pull/221>`__ [os\_regex]
   set as the inverse of (@cgzones)
-  `#220 <https://github.com/ossec/ossec-hids/pull/220>`__ [os\_xml] fix
   209 (@cgzones)
-  `#205 <https://github.com/ossec/ossec-hids/pull/205>`__ Certificate
   verification for ossec-authd and agent-auth (@mweigel)
-  `#198 <https://github.com/ossec/ossec-hids/pull/198>`__ New Feature -
   Accumulator (Multiline logs with consistent IDs) (@reyjrar)
-  `#217 <https://github.com/ossec/ossec-hids/pull/217>`__ regex
   correction by Christian Hettler (@Nukama)
-  `#216 <https://github.com/ossec/ossec-hids/pull/216>`__ Allow + in
   valid\_email\_addresses in installer.sh (@Nukama)

v2.8.0 (2014/05/22 13:10 +00:00)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  `#208 <https://github.com/ossec/ossec-hids/pull/208>`__ bug fix of
   eventchannel timestamp (@jrossi)
-  `#202 <https://github.com/ossec/ossec-hids/pull/202>`__ fix
   active-response on mac os installation (@jknockaert)
-  `#203 <https://github.com/ossec/ossec-hids/pull/203>`__ Align
   eventchannel log format with eventlog, fixes #155 (@gaelmuller)
-  `#200 <https://github.com/ossec/ossec-hids/pull/200>`__ os\_net fixes
   (@cgzones)
-  `#197 <https://github.com/ossec/ossec-hids/pull/197>`__ Fixes #194.
   Checks for both paths of openssl (@harshilmathur)
-  `#195 <https://github.com/ossec/ossec-hids/pull/195>`__ os\_regex
   review (@cgzones)
-  `#191 <https://github.com/ossec/ossec-hids/pull/191>`__ os\_regex
   unit tests #2 (@cgzones)
-  `#189 <https://github.com/ossec/ossec-hids/pull/189>`__ Windows agent
   UI version and Copyright update (@jbcheng)
-  `#188 <https://github.com/ossec/ossec-hids/pull/188>`__ os\_regex
   unit tests (@cgzones)
-  `#187 <https://github.com/ossec/ossec-hids/pull/187>`__ [tests]
   explicit enable branch coverage for new version of lcov (@cgzones)
-  `#186 <https://github.com/ossec/ossec-hids/pull/186>`__ [os\_xml] fix
   possible array underflows: see coverity (@cgzones)
-  `#185 <https://github.com/ossec/ossec-hids/pull/185>`__ Avoid a crash
   of agentd on Solaris. (@danpop60)
-  `#173 <https://github.com/ossec/ossec-hids/pull/173>`__ os\_xml
   refresh2 (@cgzones)
-  `#180 <https://github.com/ossec/ossec-hids/pull/180>`__ Use the
   environment for the CC binary (@jrossi)
-  `#179 <https://github.com/ossec/ossec-hids/pull/179>`__ Fixes to
   win32 installation (@awiddersheim)
-  `#176 <https://github.com/ossec/ossec-hids/pull/176>`__ Fix windows
   agent compile error/warnings #define ENOBUFS, ALERT\_SYSTEM\_ERR
   (@jbcheng)
-  `#175 <https://github.com/ossec/ossec-hids/pull/175>`__ Moving
   ossec-lua back to posix so that we do no have a libreadline dep
   (@jrossi)
-  `#159 <https://github.com/ossec/ossec-hids/pull/159>`__ Fixes to
   win32 (un)installation process (@awiddersheim)
-  `#160 <https://github.com/ossec/ossec-hids/pull/160>`__ Added
   #include for errno.h in os\_net.c (@denied39)
-  `#163 <https://github.com/ossec/ossec-hids/pull/163>`__ Added more
   Vista+-associated event IDs for existing rules (@mstarks01)
-  `#157 <https://github.com/ossec/ossec-hids/pull/157>`__ Removing
   event ID 676 (@mstarks01)
-  `#142 <https://github.com/ossec/ossec-hids/pull/142>`__ os\_xml
   review (@cgzones)
-  `#150 <https://github.com/ossec/ossec-hids/pull/150>`__ Added option
   to ossec.conf (additional email header) (@dopefish)
-  `#151 <https://github.com/ossec/ossec-hids/pull/151>`__ Remove event
   ID 672 (@mstarks01)
-  `#145 <https://github.com/ossec/ossec-hids/pull/145>`__ Fix make.sh
   files for win32 (@awiddersheim)
-  `#144 <https://github.com/ossec/ossec-hids/pull/144>`__ Continue
   removing the bro-ids stuff (@ddpbsd)
-  `#120 <https://github.com/ossec/ossec-hids/pull/120>`__ ossec-lua lua
   interpreter (@jrossi)
-  `#139 <https://github.com/ossec/ossec-hids/pull/139>`__ Unittest os
   regex (@jrossi)
-  `#136 <https://github.com/ossec/ossec-hids/pull/136>`__ Fix compile
   warnings with win32 (@awiddersheim)
-  `#134 <https://github.com/ossec/ossec-hids/pull/134>`__ Remove win32
   service start and stop executables (@awiddersheim)
-  `#133 <https://github.com/ossec/ossec-hids/pull/133>`__ os\_zlib
   update (@cgzones)
-  `#132 <https://github.com/ossec/ossec-hids/pull/132>`__ enable full
   clang support and remove gcc dependencies (@cgzones)
-  `#121 <https://github.com/ossec/ossec-hids/pull/121>`__ removing
   deploy from travis-ci (@jrossi)
-  `#131 <https://github.com/ossec/ossec-hids/pull/131>`__ Added error
   checking to ossec.conf installation (@awiddersheim)
-  `#129 <https://github.com/ossec/ossec-hids/pull/129>`__ Fixes to
   win32 services (@awiddersheim)
-  `#125 <https://github.com/ossec/ossec-hids/pull/125>`__ Fixes to
   ossec-installer.nsi (@awiddersheim)
-  `#124 <https://github.com/ossec/ossec-hids/pull/124>`__ SetDateSave
   off in ossec-installer.nsi (@awiddersheim)
-  `#126 <https://github.com/ossec/ossec-hids/pull/126>`__ Use file
   command in ossec-installer.nsi (@awiddersheim)
-  `#130 <https://github.com/ossec/ossec-hids/pull/130>`__ Show details
   during win32 installation (@awiddersheim)
-  `#127 <https://github.com/ossec/ossec-hids/pull/127>`__ Update
   manage\_keys.c (@awiddersheim)
-  `#128 <https://github.com/ossec/ossec-hids/pull/128>`__ Added /? as a
   parameter to ossec-agent on win32 (@awiddersheim)
-  `#123 <https://github.com/ossec/ossec-hids/pull/123>`__ Grandstream
   ATA decoder (@mstarks01)
-  `#122 <https://github.com/ossec/ossec-hids/pull/122>`__ A simple
   script to calculate OSSEC events-per-second (@mstarks01)
-  `#119 <https://github.com/ossec/ossec-hids/pull/119>`__ Fixing
   route-null active response on Windows (@mstarks01)
-  `#96 <https://github.com/ossec/ossec-hids/pull/96>`__ Remove annoying
   win32ui dialog box (@awiddersheim)
-  `#118 <https://github.com/ossec/ossec-hids/pull/118>`__ Remove ui.nsi
   (@awiddersheim)
-  `#117 <https://github.com/ossec/ossec-hids/pull/117>`__ Fixes to
   ossec-installer.nsi (@awiddersheim)
-  `#102 <https://github.com/ossec/ossec-hids/pull/102>`__ Remove debug
   messages it src/win32/ui/common.c (@awiddersheim)
-  `#107 <https://github.com/ossec/ossec-hids/pull/107>`__ Make
   manage\_agents.exe work on win32 (@awiddersheim)
-  `#116 <https://github.com/ossec/ossec-hids/pull/116>`__ Fixes to
   ossec-installer.nsi (@awiddersheim)
-  `#103 <https://github.com/ossec/ossec-hids/pull/103>`__ Free
   install\_date pointer (@awiddersheim)
-  `#115 <https://github.com/ossec/ossec-hids/pull/115>`__ add
   eventchannel (again) with proper build (@gaelmuller)
-  `#108 <https://github.com/ossec/ossec-hids/pull/108>`__ enable geoip
   in travis build (@cgzones)
-  `#114 <https://github.com/ossec/ossec-hids/pull/114>`__ remove unused
   source code files (@cgzones)
-  `#111 <https://github.com/ossec/ossec-hids/pull/111>`__ Fix win32
   ARGV0 names (@awiddersheim)
-  `#92 <https://github.com/ossec/ossec-hids/pull/92>`__ fix problem
   with umlaut in date string when pre-decoding the log message
   (@ChristianBeer)
-  `#98 <https://github.com/ossec/ossec-hids/pull/98>`__ Add install
   date to win32ui (@awiddersheim)
-  `#106 <https://github.com/ossec/ossec-hids/pull/106>`__ Remove
   os\_auth from win-files.txt (@awiddersheim)
-  `#100 <https://github.com/ossec/ossec-hids/pull/100>`__ Fix
   permissions and privilege detection (@awiddersheim)
-  `#97 <https://github.com/ossec/ossec-hids/pull/97>`__ Add better
   version handling to win32ui (@awiddersheim)
-  `#94 <https://github.com/ossec/ossec-hids/pull/94>`__ Fix win32 OS
   detection (@awiddersheim)
-  `#113 <https://github.com/ossec/ossec-hids/pull/113>`__ Remove local
   file additions in setup-win.c (@awiddersheim)
-  `#109 <https://github.com/ossec/ossec-hids/pull/109>`__ fix clang
   -Wall warnings (@cgzones)
-  `#110 <https://github.com/ossec/ossec-hids/pull/110>`__ simplify
   cJSON makefile (@cgzones)
-  `#104 <https://github.com/ossec/ossec-hids/pull/104>`__ Fix win32ui
   messages (@awiddersheim)
-  `#99 <https://github.com/ossec/ossec-hids/pull/99>`__ Fix win32 setup
   log message (@awiddersheim)
-  `#93 <https://github.com/ossec/ossec-hids/pull/93>`__ Fix the client
   status exit code (@pdrakeweb)
-  `#95 <https://github.com/ossec/ossec-hids/pull/95>`__ Add to
   .gitignore (@awiddersheim)
-  `#105 <https://github.com/ossec/ossec-hids/pull/105>`__ Adding a new
   sshd rule for bad packet lengths (@joshgarnett)
-  `#87 <https://github.com/ossec/ossec-hids/pull/87>`__ Fix comment in
   win32/ui/common.c (@awiddersheim)
-  `#86 <https://github.com/ossec/ossec-hids/pull/86>`__ OpenBSD deluser
   rule and remove bro-ids garbage (@ddpbsd)
-  `#85 <https://github.com/ossec/ossec-hids/pull/85>`__ fix to segfault
   introduced by pull request #81 (@ChristianBeer)
-  `#81 <https://github.com/ossec/ossec-hids/pull/81>`__ fix resource
   leaks in active-response.c (@ChristianBeer)
-  `#68 <https://github.com/ossec/ossec-hids/pull/68>`__ ignore warning
   about assignment in condition (@cgzones)
-  `#82 <https://github.com/ossec/ossec-hids/pull/82>`__ fix gcc wall
   warnings seen on travis (@cgzones)
-  `#71 <https://github.com/ossec/ossec-hids/pull/71>`__ fix missing
   returns reported by eclipse (@cgzones)
-  `#72 <https://github.com/ossec/ossec-hids/pull/72>`__ surround binary
   expression with parenthesis (@cgzones)
-  `#73 <https://github.com/ossec/ossec-hids/pull/73>`__ fix missing
   breaks (@cgzones)
-  `#74 <https://github.com/ossec/ossec-hids/pull/74>`__ remove unused
   declarations (@cgzones)
-  `#75 <https://github.com/ossec/ossec-hids/pull/75>`__ rename syscheck
   config struct (@cgzones)
-  `#76 <https://github.com/ossec/ossec-hids/pull/76>`__ rename global
   agent struct (@cgzones)
-  `#77 <https://github.com/ossec/ossec-hids/pull/77>`__ fix cyclic
   header relationship mem\_op.h <-> shared.h (@cgzones)
-  `#80 <https://github.com/ossec/ossec-hids/pull/80>`__ fixing gcc
   -Wall warnings (@cgzones)
-  `#78 <https://github.com/ossec/ossec-hids/pull/78>`__ exit on error
   during making zlib or cJSON (@cgzones)
-  `#69 <https://github.com/ossec/ossec-hids/pull/69>`__ fix buffer
   overflow (@cgzones)
-  `#79 <https://github.com/ossec/ossec-hids/pull/79>`__ fix spelling
   preventing building geoip support (@cgzones)
-  `#66 <https://github.com/ossec/ossec-hids/pull/66>`__ fix spelling
   (@cgzones)
-  `#67 <https://github.com/ossec/ossec-hids/pull/67>`__ remove static
   cJSON library on make clean (@cgzones)
-  `#70 <https://github.com/ossec/ossec-hids/pull/70>`__ remove complete
   bin directory on make clean and ignore failure by removi...
   (@cgzones)
-  `#65 <https://github.com/ossec/ossec-hids/pull/65>`__ ignore eclipse
   project files (@cgzones)
-  `#61 <https://github.com/ossec/ossec-hids/pull/61>`__ correct deploy
   to s3 so that we can test win32 agents. (@jrossi)
-  `#59 <https://github.com/ossec/ossec-hids/pull/59>`__ Readme update
   (@jrossi)
-  `#58 <https://github.com/ossec/ossec-hids/pull/58>`__ Make
   remoted.debug in internal\_options.conf work (@awiddersheim)
-  `#57 <https://github.com/ossec/ossec-hids/pull/57>`__ removing hg
   files (@jrossi)
-  `#56 <https://github.com/ossec/ossec-hids/pull/56>`__ Cherry-picking
   in @cgzones geoip clean (@jrossi)
-  `#55 <https://github.com/ossec/ossec-hids/pull/55>`__ Merging in
   changes from @cgzones (@jrossi)
-  `#53 <https://github.com/ossec/ossec-hids/pull/53>`__ Travis ci build
   windows and fix for setenv not being available on win32 (@jrossi)
-  `#49 <https://github.com/ossec/ossec-hids/pull/49>`__ Use cJSON
   instead of writing a custom JSON output format. (@reyjrar)
-  `#44 <https://github.com/ossec/ossec-hids/pull/44>`__ Feature:
   activeresponse with filename (@reyjrar)
-  `#45 <https://github.com/ossec/ossec-hids/pull/45>`__ Disable
   /var/ossec/queue/diff/\*state.$epoch files, they were not used.
   (@reyjrar)
-  `#43 <https://github.com/ossec/ossec-hids/pull/43>`__ Adding some
   additional sshd rules (@joshgarnett)
-  `#16 <https://github.com/ossec/ossec-hids/pull/16>`__ Allow NIX agent
   to use "-f" option and run in foreground (@jrossi)
-  `#11 <https://github.com/ossec/ossec-hids/pull/11>`__ Fix the removal
   of start menu shortcuts for windows agent (@jrossi)
-  `#8 <https://github.com/ossec/ossec-hids/pull/8>`__ Add remove agent
   cmd line option to manage\_agents (@jrossi)
-  `#7 <https://github.com/ossec/ossec-hids/pull/7>`__ Fix potential
   infinite loop when adding new agent using file input (@jrossi)
-  `#9 <https://github.com/ossec/ossec-hids/pull/9>`__ Add TimeGenerated
   to the output of Windows Event Logs (@jrossi)
-  `#21 <https://github.com/ossec/ossec-hids/pull/21>`__ HandleClient
   should try to open the m\_queue in WRITE mode instead of READ
   (@jrossi)
-  `#20 <https://github.com/ossec/ossec-hids/pull/20>`__ Labrown remoted
   child pid (@jrossi)
-  `#17 <https://github.com/ossec/ossec-hids/pull/17>`__ Fix timeout
   comment in receiver-win.c (@jrossi)
-  `#40 <https://github.com/ossec/ossec-hids/pull/40>`__ eventchannel:
   fix bug with bookmarks (@gaelmuller)
-  `#34 <https://github.com/ossec/ossec-hids/pull/34>`__ better install
   for eventchannel support (now only 1 installer) (@gaelmuller)
-  `#38 <https://github.com/ossec/ossec-hids/pull/38>`__ Output
   unformatted JSON and include the file path for syscheck alerts in
   ZeroMQ JSON output (@justintime32)
-  `#35 <https://github.com/ossec/ossec-hids/pull/35>`__ Removed
   keepalive message from win\_agent.c when not in debug (@awiddersheim)
-  `#33 <https://github.com/ossec/ossec-hids/pull/33>`__ Fix debug level
   message used by NIX daemons to be more clear (@awiddersheim)
-  `#14 <https://github.com/ossec/ossec-hids/pull/14>`__ Make
   syscheck.debug in internal\_options.conf work (@jrossi)
-  `#13 <https://github.com/ossec/ossec-hids/pull/13>`__ Awiddersheim
   fix ossec agent debug internal option nix (@jrossi)
-  `#18 <https://github.com/ossec/ossec-hids/pull/18>`__ Make
   analysisd.debug in internal\_options.conf work (@jrossi)
-  `#2 <https://github.com/ossec/ossec-hids/pull/2>`__ ZeroMQ Json
   Output (@jrossi)
-  `#4 <https://github.com/ossec/ossec-hids/pull/4>`__ fix openssl
   operations on non blocking socket (@jrossi)
-  `#28 <https://github.com/ossec/ossec-hids/pull/28>`__ add
   eventchannel support for ossec agent on windows vista or greater
   (@gaelmuller)
-  `#25 <https://github.com/ossec/ossec-hids/pull/25>`__ Validate if a
   file is readable text when report\_changes is set (@northox)
-  `#12 <https://github.com/ossec/ossec-hids/pull/12>`__ Made the
   command line debug level take precedence over what is specified
   (@jrossi)
-  `#6 <https://github.com/ossec/ossec-hids/pull/6>`__ agent\_config
   profiles for windows (@jrossi)
