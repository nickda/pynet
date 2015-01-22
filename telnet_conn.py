import telnetlib
import time


def disable_paging(remote_conn, command = "terminal length 0\n", delay = 1):
	remote_conn.write("\n")
	remote_conn.write("terminal length 0\n")


if __name__ == '__main__':
	ip = '212.72.152.158'
	username = 'nick'
	password = 'pahasapa'

	TELNET_PORT = 23
	TELNET_TIMEOUT = 6
	READ_TIMEOUT = 6

	remote_conn = telnetlib.Telnet(ip, TELNET_PORT, TELNET_TIMEOUT)

	output = remote_conn.read_until("sername:", READ_TIMEOUT)
	remote_conn.write(username + "\n")
	print output

	output = remote_conn.read_until("ssword:", READ_TIMEOUT)
	remote_conn.write(password + "\n")
	print output

	time.sleep(1)
	output = remote_conn.read_very_eager()

	disable_paging(remote_conn)

	remote_conn.write("\n")
	remote_conn.write("show version\n")

	time.sleep(1)
	output = remote_conn.read_very_eager()
	print output

