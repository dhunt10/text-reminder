import pandas as pd
from datetime import datetime
import math

def getContactList(monthValue=12, filename='resources/contacts_12.csv'):
    df = pd.read_csv(filename)
    sendNumber = []
    contactName = []
    contactLastName = []
    location = []
    months = []
    email = []

    for i in range(len(df['patient_name'])):
        if df['last_visit_date'][i] == '-':
            continue
        date = str(df['last_visit_date'][i])
        next_date = datetime.strptime(date, '%m/%d/%Y').date()
        diff = (abs(next_date - TODAY))
        month = math.ceil(diff.days / 30)
        if monthValue == 6:
            if month >= 5:
                if df['patient_phone'][i] == '-':
                    continue
                sendNumber.append(str(df['patient_phone'][i]).replace('(','').replace(')', '').replace(' ', '').replace('-',''))
                contactName.append(df['patient_name'][i].split(', ')[1])
                contactLastName.append(df['patient_name'][i].split(', ')[0])
                months.append(month)
                email.append(df['patient_email'][i])
                location.append(df['last_location'][i])

        else:
            if month >= 11:
                if df['patient_phone'][i] == '-':
                    continue
                sendNumber.append(str(df['patient_phone'][i]).replace('(','').replace(')', '').replace(' ', '').replace('-',''))
                contactName.append(df['patient_name'][i].split(', ')[1])
                contactLastName.append(df['patient_name'][i].split(', ')[0])
                months.append(month)
                email.append(df['patient_email'][i])
                location.append(df['last_location'][i])

    new_data = pd.DataFrame()
    new_data['numbers'] = sendNumber
    new_data['contact first name'] = contactName
    new_data['contact last name'] = contactLastName
    new_data['months since last visit'] = months
    new_data['email'] = email
    new_data['location'] = location

    if monthValue == 6:
        new_data.to_csv('resources/cleaned_data_6.csv')
    elif monthValue == 'test':
        new_data.to_csv('resources/test.csv')
    else:
        new_data.to_csv('resources/cleaned_data_12.csv')
    print(len(new_data))
    return new_data

TODAY = datetime.today().date()
