from pyfcm import FCMNotification

api_key="AIzaSyDEm4SWptlTvV6mJkydHzaSYS5Z2fnslcs"

push_service = FCMNotification(api_key=api_key)



push_service = FCMNotification(api_key=api_key)


registration_ids = ["eYC_ggqxDQs:APA91bHma-0DUcNtp2P_GQseIjps6wF6sZwIYmSVcDuK2DoItw1NMJ0X28ndd-7Z1S5xPMt9pjnE3y1qOpemqJ69FaUEFBQTXmitT7rYHTAahAPj_IVPfnkb6ydKc7iVZv5Qkws0-Q5N"]
message_title = "Hi guys"
message_body = "this is test"



result = push_service.notify_multiple_devices(registration_ids=registration_ids, message_title=message_title, message_body=message_body)

print result