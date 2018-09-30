
import blescan
import sys

import bluetooth._bluetooth as bluez

dev_id = 0 #varsayilan bl modulu
try:
	sock = bluez.hci_open_dev(dev_id)
	print "ble thread started"

except:
	print "ERROR BLUETOOTH MODULE NOT FOUND!"
    	sys.exit(1)

blescan.hci_le_set_scan_parameters(sock)
blescan.hci_enable_le_scan(sock)

while True:
	returnedList = blescan.parse_events(sock, 10)
	print "----------SONUC--------"
	for beacon in returnedList:
		print beacon

