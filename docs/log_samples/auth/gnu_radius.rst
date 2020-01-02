GNU Radius
----------

Information on GNU Radius can be found `on their site <http://www.gnu.org/software/radius/>`_.

Information on the detailed accounting in GNU Radius can be found `here <http://www.gnu.org/software/radius/manual/html_mono/radius.html#SEC182>`_.

Here is a sample of the accounting records taken from the above documentation:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

  Fri Dec 15 18:00:24 2000
        Acct-Session-Id = "2193976896017"
        User-Name = "e2"
        Acct-Status-Type = Start
        Acct-Authentic = RADIUS
        Service-Type = Framed-User
        Framed-Protocol = PPP
        Framed-IP-Address = 11.10.10.125
        Calling-Station-Id = "+15678023561"
        NAS-IP-Address = 11.10.10.11
        NAS-Port-Id = 8
        Acct-Delay-Time = 0
        Timestamp = 976896024
        Request-Authenticator = Unverified

  Fri Dec 15 18:32:09 2000
        Acct-Session-Id = "2193976896017"
        User-Name = "e2"
        Acct-Status-Type = Stop
        Acct-Authentic = RADIUS
        Acct-Output-Octets = 5382
        Acct-Input-Octets = 7761
        Service-Type = Framed-User
        Framed-Protocol = PPP
        Framed-IP-Address = 11.10.10.125
        Acct-Session-Time = 1905
        NAS-IP-Address = 11.10.10.11
        NAS-Port-Id = 8
        Acct-Delay-Time = 0
        Timestamp = 976897929
        Request-Authenticator = Unverified


