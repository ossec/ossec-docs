Additional rules
----------------

This is the place to store rules that are not meant for the official release, because they
are specific to an environment or customized to an internal application.


Windows: Rule to alert on password changes by another user
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

  <rule id="100155" level="10">
    <if_sid>18111</if_sid>
    <compiled_rule>comp_mswin_targetuser_calleruser_diff</compiled_rule>
    <description>User changed someone else password.</description>
  </rule>


