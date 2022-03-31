from twilio.rest import Client
from createData import getContactList
import pandas as pd
import time
import datetime

class sendMessage:

    def __init__(self):
        """

        """
        self.numbers = []
        self.time = []
        self.message = []
        self.name = []
        self.count = 0


    def sendMessage(self, number, first_name, last_name, months):
        message = 'Hello {}, it has been {} months since you have been seen at OnSpot Dermatology. To book another appointment visit our website at www.onspotdermatology.com/booknow or call us at (941) 444-0011'.format(first_name, months)
        CLIENT.messages \
            .create(
                 body=message,
                 from_= TWILIO,
                 status_callback='http://postb.in/1234abcd',
                 to=number
             )
        self.numbers.append(number)
        self.time.append(datetime.datetime.now())
        self.message.append(message)
        self.name.append((last_name, first_name))
        self.count = self.count + 1

    def sendMessages(self, option):
        file = 'resources/contacts_{}.csv'.format(option)
        contacts = getContactList(option, file)
        for i in range(len(contacts)):
            try:
                #self.sendMessage(contacts['numbers'][i], contacts['contact first name'][i],
                #                 contacts['contact last name'][i], contacts['months since last visit'][i])
                print('sent to {} {} at {}, {}/{}'.format(contacts['contact first name'][i], contacts['contact last name'][i], contacts['numbers'][i], i+1, len(contacts)))
            except Exception as e:
                print(e)
                continue

        data = {""
                "date_sent": self.time,
                "message": self.message,
                "phone_number": self.numbers,
                "name": self.name}

        df = pd.DataFrame(data)
        df.to_csv('resources/sendLog.csv', mode='a', index=False, header=False)
        print('Successfully Sent to {}/{}'.format(self.count, len(contacts)))
        self.count = 0


ACCOUNT_SID = 'AC0b05fedb690adfe083e62b44a42ffa33'
AUTH = 'a85b60ce346f33a158053ff0194f4a14'
TWILIO = '+19036260048'
CLIENT = Client(ACCOUNT_SID, AUTH)
