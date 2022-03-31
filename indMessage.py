from twilio.rest import Client
from createData import getContactList
import pandas as pd
import time
import datetime


ACCOUNT_SID = 'AC0b05fedb690adfe083e62b44a42ffa33'
AUTH = 'a85b60ce346f33a158053ff0194f4a14'
TWILIO = '+19036260048'
CLIENT = Client(ACCOUNT_SID, AUTH)

number = input('what number do you wish to send to?  ')
message = input('what do you wish to say?  ')

try:
    CLIENT.messages \
                .create(
                     body=message,
                     from_= TWILIO,
                     status_callback='http://postb.in/1234abcd',
                     to=number
                 )
    print('Sent to {}'.format(number))
except Exception as e:
    print(e)



