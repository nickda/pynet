#######################################################
##Class 2 Exercise 1
##Sending Email when config changes
##A pickle file should be initialized with 0 as its contents
##
##<code>
##import pickle
##f = open('running.pkl', 'w')
##pickle.dump('0', f)
##</code>
##

import snmp_helper
import email_helper
import pickle

IP = '50.242.94.227'
a_user = 'pysnmp'
auth_key = 'galileo1'
encrypt_key = 'galileo1'
snmp_user = (a_user, auth_key, encrypt_key)

pynet_rtr2 = (IP, 8061)
snmp_oid = ('ccmHistoryRunningLastChanged', '1.3.6.1.4.1.9.9.43.1.1.1.0', None)

recipient = 'nickda@gmail.com'
sender = 'ktbyers@twb-tech.com'
subject = 'Config Change on pynet_rtr2'


##Get the timestamp from the router
snmp_data = snmp_helper.snmp_get_oid_v3(pynet_rtr2, snmp_user, oid=snmp_oid[1])
output = snmp_helper.snmp_extract(snmp_data)
print output


message = 'Configuration has changed at %s' % output


##Get timestamp from Pickle file
f = open("running.pkl", "r")
ts_from_pkl = pickle.load(f)
f.close()



##Compare timestamps
if ts_from_pkl < output:
	email_helper.send_mail(recipient, subject, message, sender)
	f = open('running.pkl', 'w')
	pickle.dump(output, f)
	f.close()

