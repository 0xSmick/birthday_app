from oauth2client.service_account import ServiceAccountCredentials
from flask import Flask, request, redirect
import gspread
import os
import numpy as np
import twilio.twiml


app = Flask(__name__)

@app.route("/", methods=['GET','POST'])

def message_response():

  os.chdir('/Users/sheldon.smickley/.googleApps')
  scope = ['https://spreadsheets.google.com/feeds']

  credentials = ServiceAccountCredentials.from_json_keyfile_name('google-drive-access-8ced2fb70bb4.json', scope)
  gc = gspread.authorize(credentials)
  sh = gc.open_by_key("17F7M5eBlT6uecv3oTSPnVnrTbSbdk-8g-GoySHQ7RuY")
  worksheet = sh.get_worksheet(0)

  submitters = worksheet.col_values(1)
  submitters = filter(None, submitters)
  submitters.pop(0)

  comments = worksheet.col_values(2)
  comments = filter(None, comments)
  comments.pop(0)

  randomNumber = np.random.randint(0, len(comments))

  message = "{} - {}".format(comments[randomNumber], submitters[randomNumber])
  resp = twilio.twiml.Response()
  resp.message(message)
  return str(resp)

if __name__ == "__main__":
  app.run(debug=True)

