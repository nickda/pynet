COMMUNITY_STRING = 'galileo'
SNMP_PORT = 7961
IP = '50.242.94.227'

a_device = (IP, COMMUNITY_STRING, SNMP_PORT)

from snmp_helper import snmp_get_oid,snmp_extract

OID = '1.3.6.1.2.1.1.3.0'
snmp_data = snmp_get_oid(a_device, oid=OID)
uptime = snmp_extract(snmp_data)
#print "System uptime is "+uptime

OID = '1.3.6.1.4.1.9.9.43.1.1.1.0'
snmp_data = snmp_get_oid(a_device, oid=OID)
rchg = snmp_extract(snmp_data)
#print "Running config changed at "+rchg

OID = '1.3.6.1.4.1.9.9.43.1.1.2.0'
snmp_data = snmp_get_oid(a_device, oid=OID)
rsvd = snmp_extract(snmp_data)
#print "Running config saved/displayed at "+rsvd


OID = '1.3.6.1.4.1.9.9.43.1.1.3.0'
snmp_data = snmp_get_oid(a_device, oid=OID)
ssvd = snmp_extract(snmp_data)
#print "Startup config saved at "+ssvd


if ssvd == 0:
	print "Startup config not saved since last reboot"
elif ssvd < rchg:
	print "Running change with no save"
else:
	print "Running config saved"