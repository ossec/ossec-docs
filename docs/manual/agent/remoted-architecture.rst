.. _manual-remoted:

Remoted architecture and tuning
===============================

``ossec-remoted`` receives events from OSSEC agents (secure mode) and from remote syslog
senders (UDP/TCP). Understanding its threading model helps when sizing syslog TCP
forwarders and tuning ``internal_options.conf``.

Process model
-------------

One ``ossec-remoted`` process runs one detached thread per ``<remote>`` block in
``ossec.conf`` (secure, syslog UDP, or syslog TCP). All listener sockets bind in the
main thread before the process drops privileges (setuid/chroot), so every listener can
use privileged ports in a single process.

Threading
---------

* **Main thread** — binds listeners, drops privileges, starts listener threads, waits
  on ``SIGTERM``. On shutdown it closes listener FDs and waits for syslog TCP pool work
  to finish.
* **One thread per ``<remote>`` listener** — secure, syslog UDP, or syslog TCP accept/read loop.
* **Syslog TCP only** — each accepted client connection is handled by a bounded worker
  pool on that listener (not one process per connection).

Constraints
-----------

* At most **one secure** ``<remote>`` listener per ``ossec-remoted`` process. Secure mode
  uses process-global keystore state and helper threads for active response forwarding.
* UDP syslog and secure listeners do not use the syslog TCP worker pool.

Secure mode internals
---------------------

The secure listener uses three cooperating threads:

1. **Receiver** — reads agent data; logs go to ``ossec-analysisd``, control messages to
   the manager thread.
2. **AR forward** — receives active-response commands from ``ossec-analysisd`` locally and
   forwards them to agents.
3. **Manager** — sends outbound messages to agents.

Syslog TCP
----------

A bounded thread pool handles each persistent TCP client (typical syslog forwarders).
When the pool is at capacity (``remoted.syslog_tcp_worker_pool`` or
``remoted.syslog_tcp_max_tasks``), new connections are closed (backpressure). Size the
worker pool to match your expected number of concurrent forwarders.

Syslog UDP
----------

The listener thread receives datagrams and forwards them to ``ossec-analysisd`` with no
worker pool.

Shutdown
--------

On ``SIGTERM``/``SIGHUP``, ``ossec-remoted`` closes listener sockets. Syslog TCP workers
use ``remoted.syslog_tcp_read_timeout`` so blocked ``recv()`` calls return periodically,
allowing graceful drain within about 60 seconds.

Tuning options
--------------

Set these in ``/var/ossec/etc/local_internal_options.conf``:

+-------------------------------+---------+------------------------------------------+
| Option                        | Default | Purpose                                  |
+===============================+=========+==========================================+
| ``ossec.thread_stack_size``   | 2048    | Thread stack size (KiB)                  |
| ``remoted.syslog_tcp_worker_pool`` | 16 | TCP worker threads per listener       |
| ``remoted.syslog_tcp_max_tasks``   | 64 | Max queued + active TCP tasks         |
| ``remoted.syslog_tcp_read_timeout``| 30 | TCP read timeout (seconds)            |
+-------------------------------+---------+------------------------------------------+

See :ref:`intopt_remoted` and :ref:`intopt_ossec` for full option reference.

See also
--------

* :ref:`ossec_config.remote`
* :ref:`ossec-remoted`
* :ref:`intopt_remoted`
