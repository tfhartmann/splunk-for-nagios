#### THIS FILE MANAGED BY PUPPET ####
# Display all devices in nagios
import os
import splunk4nagios as s4n
os.system("/usr/bin/nc "+s4n.server+" "+s4n.mk_port+" < nagios-hosts")
#### THIS FILE MANAGED BY PUPPET ####
