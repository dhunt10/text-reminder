from resources.auth import getToken
from datetime import date
from datetime import timedelta
import pandas as pd
import requests
import json

class yesterdayPatients():
    def __init__(self):
        auth = getToken()
        self.token = auth.getToken()
        self.headers = {'x-api-key': '5ca254dcc3ee6372d2513de1632e35c6fcae44a29240e3d100445c8d',
                   'Cache-Control': 'no-cache',
                   'Content-Type': 'application/json',
                   'Authorization': 'Bearer ' + self.token}
        baseURL = 'https://stage.ema-api.com/ema-dev/firm/entpmsandbox258/ema/fhir/v2/Appointment'
        body = {"resourceType": "Appointment",
                "date": TWODAYS,
                "date": YESTERDAY,
                "status": 'booked',
                "status": "arrived",
                "status": 'fulfilled',
                "status": 'checked-in'}
        self.call = requests.get(url=baseURL, data=json.dumps(body), headers=self.headers).json()


    def getPatientID(self):
        self.ids = []
        for item in range(self.call['total']):
            self.ids.append(self.call['entry'][item]['resource']['participant'][0]['actor']['reference'].split('/')[-1])

        return self.ids


    def getNumbers(self):
        ids = self.getPatientID()
        baseURL = 'https://stage.ema-api.com/ema-dev/firm/entpmsandbox258/ema/fhir/v2/Patient/{}'
        patientName = []
        patientNumber = []

        for id in range(len(ids)):
            call = requests.get(url=baseURL.format(ids[id]), headers=self.headers).json()
            for telecom in range(len(call)):
                try:
                    if call['telecom'][telecom]['use'] == 'mobile':
                        if patientNumber.count(call['telecom'][telecom]['value']) == 0:
                            patientNumber.append(call['telecom'][telecom]['value'])
                            patientName.append(call['name'][0]['given'][0])
                except:
                    continue
        return patientName, patientNumber


TODAY = date.today()
YESTERDAY = TODAY - timedelta(days=1)
YESTERDAY = 'le' + str(YESTERDAY.year) + '-' + str(YESTERDAY.month).zfill(2) + '-' + str(YESTERDAY.day).zfill(2)
TWODAYS = TODAY - timedelta(days=2)
TWODAYS = 'le' + str(TWODAYS.year) + '-' + str(TWODAYS.month).zfill(2) + '-' + str(TWODAYS.day).zfill(2)

"""arrived, fulfilled, checked-in'"""