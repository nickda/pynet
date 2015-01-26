########################################################################################
##Class 2 Exercise 2
##Drawing SNMP Graphs from the data taken from a Router

import snmp_helper
import pygal
import time

IP = '50.242.94.227'
a_user = 'pysnmp'
auth_key = 'galileo1'
encrypt_key = 'galileo1'
snmp_user = (a_user, auth_key, encrypt_key)

pynet_rtr1 = (IP, 7961)

##Setting the interval for samples and the time when collection should end (seconds)
INTERVAL = 300
END_TIME = 3600


##Initializing lists
fa4_in_octets = []
fa4_out_octets = []
fa4_in_packets = []
fa4_out_packets = []
timelist_str = []

snmp_oids = (
	('sysUptime', '1.3.6.1.2.1.1.3.0', None),
	('ifDescr_fa4', '1.3.6.1.2.1.2.2.1.2.5', None),
	('ifInOctets_fa4', '1.3.6.1.2.1.2.2.1.10.5', True),
	('ifInUcastPkts_fa4', '1.3.6.1.2.1.2.2.1.11.5', True),
	('ifOutOctets_fa4', '1.3.6.1.2.1.2.2.1.16.5', True),
	('ifOutUcastPkts_fa4', '1.3.6.1.2.1.2.2.1.17.5', True),
)

##Creating a time scale
timelist = range(0, END_TIME+INTERVAL, INTERVAL)

##Conversion to strings for pygal
for point in timelist:
	timelist_str.append(str(point))

##Fetching the readings from the router
for point in timelist:
	print point
	for desc,an_oid,is_count in snmp_oids:
			snmp_data = snmp_helper.snmp_get_oid_v3(pynet_rtr1, snmp_user, oid=an_oid)
			output = snmp_helper.snmp_extract(snmp_data)
			print "%s %s" % (desc, output)
			if desc == 'ifInOctets_fa4':
				fa4_in_octets.append(output)
			elif desc == 'ifOutOctets_fa4':
				fa4_out_octets.append(output)
			elif desc == 'ifInUcastPkts_fa4':
				fa4_in_packets.append(output)
			elif desc == 'ifOutUcastPkts_fa4':
				fa4_out_packets.append(output)
	time.sleep(INTERVAL)

##Converting the readings to int
datasets = (fa4_in_octets,fa4_out_octets,fa4_in_packets,fa4_out_packets)

for dataset in datasets:
	for strng in dataset:
		dataset[dataset.index(strng)] = int(dataset[dataset.index(strng)])


##Drawing the octets graph
line_chart = pygal.Line()

line_chart.title = 'Input/Output Bytes'

line_chart.x_labels = timelist_str

line_chart.add('In Bytes', fa4_in_octets)
line_chart.add('Out Bytes', fa4_out_octets)

line_chart.render_to_file('octets.svg')


##Drawing the packets graph
line_chart_2 = pygal.Line()

line_chart_2.title = 'Input/Output Packets'

line_chart_2.x_labels = timelist_str

line_chart_2.add('In Packets', fa4_in_packets)
line_chart_2.add('Out Packets', fa4_out_packets)

line_chart_2.render_to_file('packets.svg')


