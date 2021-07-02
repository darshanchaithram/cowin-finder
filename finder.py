import time
from twilio.rest import Client
from cowin_api import CoWinAPI
import datetime


district_id_pkd = '308'  #Enter your district id 
date = datetime.datetime.now().strftime("%d/%m/%y")   #Today's date

centre = []
cowin = CoWinAPI()

def send_message(centre, district_id):
    account_sid = 'xxxxxxxxxxxxxxxx'   #Enter your twilio account id here
    auth_token = 'xxxxxxxxxxxxxxxxx'   #Enter your twilio authorisation token here

    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='000000000',   #Enter phone number provided by twilio
        body=(f'Hello xxxxx, Covid-19 vaccine available in your district now! {centre}'),
        to='0000000000' #Enter your phone number here
    )
    print(message.sid)

def vaccine_find(district_id,date):
    centre = []
    found = 0
    available_centers = cowin.get_availability_by_district(district_id, date)
    print(f"Available Centers [ {district_id} ] : ")
    for i in range(30):
        try:
            availability = (available_centers['centers'][i]['sessions'][0]['available_capacity'])
            if(availability >= 1):
                centre.append(available_centers['centers'][i]['name'])
                print(centre)
                found=1
        except:
            p=1
    if (found == 1):
        send_message(centre, district_id)
    else:
        print(f"NOT THIS TIME, (count is {count})")
count = 1
while 1:
    vaccine_find(district_id_pkd, date)
    time.sleep(120)       #The script repeats after every 2 minutes
    count +=1
