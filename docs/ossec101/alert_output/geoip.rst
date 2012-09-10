.. _ossec_101_alert_output_email_geoip:




cumentation for Adding GeoIP Support 
    -- added support for GeoIP lookup using Maxmind database and API (xavier)
       - support GeoIP database lookup for src/dst IP addresses 
       - converting non-private IP addresses to city names
       - output to alerts.log, and syslog forwarding, and maild output
 ------ Sample procedure to enable GeoIP (adjust as needed) 
 Step 1. get and install Maxmind GeoIP API
    wget http://www.maxmind.com/download/geoip/api/c/GeoIP-1.4.8.tar.gz
    tar xzvf GeoIP-1.4.8.tar.gz
    cd GeoIP-1.4.8
    ./configure
    make
    su
    make install"

 Step 2. get Maxmind GeoIP DB
    wget http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz
    gzip -d GeoLiteCity.dat.gz
    wget ttp://geolite.maxmind.com/download/geoip/database/GeoLiteCityv6-beta/GeoLiteCityv6.dat.gz
    gzip -d GeoLiteCityv6.dat.gz
    su
    cp GeoLiteCity*.dat /var/ossec/etc/
 
 Step 3. Compile OSSEC with GeoIP enabled, modify config
    get ossec-hids-2.7.tar.gz
    tar xzvf ossec-hids-2.7.tar.gz
    cd ossec-hids-2.7
    cd src
    make setgeoip
    cd ..
    su
    ./install.sh

  ------ modify etc/ossec.conf
  <ossec_config>
     <global>
         <!-- to specify GeoIP database file location -->
         <geoip_db_path>/etc/GeoLiteCity.dat</geoip_db_path>
         <geoip6_db_path>/etc/GeoLiteCityv6.dat</geoip6_db_path>
     </global>

     <alerts>
         <!-- to add GeoIP info in alerts -->
         <use_geoip>yes</use_geoip>
      </alerts>
  </ossec_config>

  ------ update etc/internal_options.conf
  # Maild display GeoIP data (0=disabled, 1=enabled)
  maild.geoip=1

  ------ restart OSSEC
    /var/ossec/bin/ossec-control restart


