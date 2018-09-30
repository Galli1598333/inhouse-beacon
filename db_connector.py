from firebase import firebase
firebase = firebase.FirebaseApplication('https://beacon-5d432.firebaseio.com/', None)
customers = firebase.get('/', None)
for k, v in customers.iteritems():
    print k, v