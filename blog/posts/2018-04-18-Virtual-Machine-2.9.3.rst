.. post:: Apr 18, 2018
   :tags: appliance
   :category: Announcements
   :author: Scott R. Shinn


===============
OSSEC Virtual Appliance 2.9.3
===============

Longtime OSSEC Contributor Vic Hargrave has released an update to the OSSEC Virtual appliance. 

**Download**

`https://ossec.github.io/downloads.html <https://ossec.github.io/downloads.html>`_


**README**


1.  This virtual appliance contains the following facilities:

    - CentOS 7.4
    - OSSEC 2.9.3
    - Elasticsearch-Logstash-Kibana (ELK) 6.1.1
    - Cerebro 0.7.2


2.  The virtual appliance is provided as an OVA which you can import into most virtual systems.
    We recommend using VirtualBox which can import the OVA image directly.  We used VirtualBox
    to create this appliance and the OVA.

3.  To unpack the appliance, unzip the package with gunzip then import the ossec-vm-2.9.3.ova
    into your virtualization application.  We recommend VirtualBox for running appliance.

4.  The appliance network interface is configured to use NAT mode.  To use this appliance as a
    regular OSSEC server you must configure the network interface on the appliance to use bridged
    mode and set a static IP address on the CentOS guest. See this UnixCraft article on how to do
    this https://www.cyberciti.biz/faq/howto-setting-rhel7-centos-7-static-ip-configuration/.


5.  The appliance features a Kibana dashboard to visualize OSSEC alerts. Once in bridged mode,
    you can access Kibana from a browser externally with the static IP of the appliance using
    port 5601:

      http://<appliance-static-ip>:5601

    Click on "Dashboard" then select "OSSEC Dashboard" to display a dashboard that has 3 panels

    - OSSEC Alerts Over Time: Bar graph displaying the number of events per unit time.
    - Top Alerts Per Agent: Pie chart showing the top 20 alerts per each of the top 20 most active agents.
    - OSSEC Alert Data: Table displaying individual alerts and their corresponding fields/values.


6.  You can use Cerebro (formally Kopf) to manage the Elasticsearch instance on the appliance by
    opening this URL in a browser:

      http://<appliance-static-ip>:9000

    Enter the Elasticsearch URL, http:///<vm-static-ip>:9200, in the node address text box on the
    Cerebro startup screen then click on the "Connect" button.

7.  Two CentOS users are defined: "ossec" and "root".  The root password is "_0ssec_".  The "ossec"
    user does not have a password.  When you start up the VM and get to the login console, just hit
    ENTER if you want to login as "ossec".

8.  OSSEC and ELK were installed with yum.  To upgrade either just run yum with the "upgrade" option:

      yum upgrade ossec-hids -y
      yum upgrade <elasticsearch|logstash|kibana> -y

9.  OSSEC is installed in /var/ossec.

10. ELK and Cerebro components are installed in /usr/share/<elasticsearch|logstash|kibana|cerebro>.

11. The Logstash pipeline ingestion file for OSSEC is /etc/logstash/conf.d/ossec.conf.

12. You can start and stop OSSEC, ELK, and Cerebro services with the systemctl command:

      systemctl <start|stop> <ossec-hids|elasticsearch|logstash|kibana|cerebro>.service


