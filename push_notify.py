from pyfcm import FCMNotification

api_key="AAAA_4CCsfU:APA91bFyBB2Rm4JDT4rHez2lgxgmqun1AytQH0VIZ7ux_WQnhlFs6T68HniZSrr22i4m1KfaNZcSktUWbkjN-aj0sodI74NC5ifHaacMhT6v651WCOc-l3-8_wY5cFFb_iyiLCxM-oC-"

push_service = FCMNotification(api_key=api_key)




registration_id = "eYC_ggqxDQs:APA91bHma-0DUcNtp2P_GQseIjps6wF6sZwIYmSVcDuK2DoItw1NMJ0X28ndd-7Z1S5xPMt9pjnE3y1qOpemqJ69FaUEFBQTXmitT7rYHTAahAPj_IVPfnkb6ydKc7iVZv5Qkws0-Q5N"
message_title = "Hosgeldiniz"
message_body = "Merhaba"+"Sira Almak Ister misiniz?"



result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)

print result