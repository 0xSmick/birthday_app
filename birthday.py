from flask import Flask, request, redirect
import numpy as np
import twilio.twiml

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])

def message_response():
	messages = ["Your tits are amazing","You're handier than I will ever be"]
	message = np.random.choice(messages)
	resp = twilio.twiml.Response()
	resp.message(message)
	return str(resp)

if __name__ == "__main__":
	app.run(debug=True)