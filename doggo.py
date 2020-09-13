from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import requests

app = Flask(__name__)


@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming calls with a MMS message."""
    # Get the breed the user sent our Twilio number
    breed = request.values.get('Body', None)

    # Start our TwiML response
    resp = MessagingResponse()

    str_msg = f"Here is a cute {breed} doggo!"

    # Add a text message
    msg = resp.message(str_msg)

    # API call to dog api with breed passed in as a parameter
    x = requests.get(f'https://dog.ceo/api/breed/{breed}/images/random')

    dog_img = x.json()['message']

    # Add a picture message
    msg.media(dog_img)

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
