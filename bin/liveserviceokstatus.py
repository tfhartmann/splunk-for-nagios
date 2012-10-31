#### THIS FILE MANAGED BY PUPPET ####
# Script to request a hosts' service state by accessing MK Livestatus
import socket
import sys,splunk.Intersplunk
import string
import splunk4nagios

results = []

try:

    results,dummyresults,settings = splunk.Intersplunk.getOrganizedResults()

    for r in results:
        if "_raw" in r:
            if "src_host" in r:
                    try:
		        HOST = splunk4nagios.server    # The remote nagios server
		        PORT = 6557              # The remote port on the nagios server
		        content = [ "GET services\nStats: last_hard_state = 0\n" ]
    		        query = "".join(content)
		        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		        s.connect((HOST, PORT))
		        s.send(query)
		        s.shutdown(socket.SHUT_WR)
		        data = s.recv(100000000)
		        liveserviceokstatus = string.split(data)
		        s.close()
                        r["liveserviceokstatus"] = liveserviceokstatus[0]
                    except:
                        r["liveserviceokstatus"] = "0"

except:
    import traceback
    stack =  traceback.format_exc()
    results = splunk.Intersplunk.generateErrorResults("Error : Traceback: " + str(stack))

splunk.Intersplunk.outputResults( results )

#### THIS FILE MANAGED BY PUPPET ####
