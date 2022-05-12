from flask import Flask, request, Response
from flask_restful import Resource, Api, reqparse
from twilio.twiml.messaging_response import MessagingResponse
from sendEmail import sendEmail
import os

app = Flask(__name__)

@app.route('/healthcheck', methods=['GET', 'POST'])
def healthcheck():
    return 'alive'

@app.route('/sms', methods=['GET','POST'])
def smsreminder():

    message_body = request.form['Body']
    resp = MessagingResponse() 
    if message_body == 'STOP' \
            or message_body == 'UNSUBSCRIBE'\
            or message_body == 'stop' \
            or message_body == 'unsubscribe' \
            or message_body == 'Stop'\
            or message_body == 'Unsubscribe'\
            or message_body == 'GO'\
            or message_body == 'STOP ' \
            or message_body == 'stop ' \
            or message_body == 'Stop ':
        print('patient has unsubscribed')

    elif message_body == 'START' or message_body == 'start' or message_body == 'Start':
        print("patient has resubscribed")

    else:
        print('response emailed')
        comm = sendEmail()
        comm.prepEmail(message_body, request.form['From']) #todo send phone number and name , maybe just send whole request
        resp.message('The OnSpot Team has been contacted and will be in contact with you shortly.')

    return str(resp)


@app.route('/smsreview', methods=['GET', 'POST'])
def smsreview():
    resp = MessagingResponse()
    message_body = request.form['Body']
    print(request.form)
    try:
        if int(message_body) < 4:
            resp.message('Please let us know how we can be of greater help.')
        elif int(message_body) > 6:
            resp.message('Thank you for your response, would you please take a moment to review your visit on Google? https://g.page/r/CU31ZFkIjXIbEB0/review')
        else:
            resp.message('Thank you for your response.')
    except:
        comm = sendEmail()
        resp.message('Your response has been recorded.')
        comm.prepEmail(message_body, request.form['From']) #todo send phone number and name , maybe just send whole request

    return str(resp)


if __name__ == '__main__':
    app.run(host='localhost', port='8080')
    #app.run()
