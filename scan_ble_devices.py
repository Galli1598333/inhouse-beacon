
import blescan
import sys
from firebase import firebase
import bluetooth._bluetooth as bluez

firebase = firebase.FirebaseApplication(
    'https://beacon-5d432.firebaseio.com/', None)  # database
customers = firebase.get('/', None)  # tum macler
for k, v in customers.iteritems():
    print k, v


dev_id = 0  # varsayilan bl modulu
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

	print "---------- ALAN ICERSINDE OLAN KISILER--------"
	for beacon in returnedList:
		for key, value in customers.iteritems():
			if beacon.find(str(value) != -1:
        		ad="Adi:" + str(key)
			mac=" - Mac Adresi:" + str(value)
			print ad, mac
