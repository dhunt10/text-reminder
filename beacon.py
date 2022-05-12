from sendMessage import sendMessage
import pandas as pd

DATA = sendMessage()

message = input('What would you like to let these people know?')

contacts = pd.read_csv('resources/beacon.csv')

for i in range(len(contacts)):
    DATA.sendBeacon(contacts['number'][i], message)