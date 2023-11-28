import json
import logging

import azure.functions as func
import requests

telegramBotAPI="6984774906:AAHJUNg1P7AsnKdwd7MlCd3n1hkOZZEbnsE"
Receivers_id="6436866315"

def SendMessege(message):
    try:
        Url="https://api.telegram.org/bot"+str(telegramBotAPI)+"/sendMessage?chat_id="+str(Receivers_id)
        textdata={"text":message}
        requests.request("POST",Url,params=textdata)
    except Exception as e:
        Message = str(e)+":Exception  in send message "
        print(Message)


def main(event: func.EventGridEvent):
    logging.info("startin script")
    
    
    result = json.dumps({
        'id': event.id,
        'data': event.get_json(),
        'topic': event.topic,
        'subject': event.subject,
        'event_type': event.event_type,
    })
    
   
    
    result_dict = json.loads(result)
    
    
    
    
    flag= result_dict['data']['body']['Flag']
    people_count=result_dict['data']['body']['People_Count'] 
    
    
    if flag==0 and people_count==1:
        SendMessege("Some One At home......")
    elif flag==1 and people_count==0:
        SendMessege("Home is empty")

        
         
    logging.info('Python EventGrid trigger processed an event: %s', result)
