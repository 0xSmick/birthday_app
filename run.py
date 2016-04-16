from flask import Flask, request, redirect
import twilio.twiml
import numpy as np
 
app = Flask(__name__)

messages = ["Your tits are amazing, even if they cause back problems #worthit", "You're handier than I will ever be, and I watch HGTV. I mean that kitchen doe" ,"Your milkshake brings all the boys to the yard]"

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
		message = np.random.choice(messages)
    resp = twilio.twiml.Response()
    resp.message(message)
    return str(resp)
 
if __name__ == "__main__":
    app.run(debug=True)