from pyfcm import FCMNotification

api_key = 'AAAAB-eMknM:APA91bEaFHgk_34Tjpl-Kb9a1d7ZW5_CS4rG4vnLePCmkR3mpRfukkoBRaf0eyg1PNh97xe6yPyAW6h5g210hg7FWMWP7QDI1hn6q_iObyR06MLT7NnOZSn7V2WkYBLTDRwG1fBcVf2b'

push_service = FCMNotification(api_key=api_key)

# OR initialize with proxies

#proxy_dict = {
   #       "http"  : "http://127.0.0.1",
  #        "https" : "http://127.0.0.1",
 #       }
#push_service = FCMNotification(api_key=api_key, proxy_dict=proxy_dict)

# Your api-key can be gotten from:  https://console.firebase.google.com/project/<project-name>/settings/cloudmessaging

registration_id = "33949520499"
message_title = "Uber update"
message_body = "Hi Tejas, your customized news for today is ready"
result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)

print(result)
 
# Send to multiple devices by passing a list of ids.
#registration_ids = ["<device registration_id 1>", "<device registration_id 2>", ...]
#message_title = "Uber update"
#message_body = "Hope you're having fun this weekend, don't forget to check today's news"
#result = push_service.notify_multiple_devices(registration_ids=registration_ids, message_title=message_title, message_body=message_body)

#print result