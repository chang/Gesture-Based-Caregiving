from twilio.rest import TwilioRestClient
import auth

class Notification:
	def __init__(self):
		self.email_address_list = []
		self.phone_number_list = []

	def add_email(self, val):
		self.email_address_list.append(val)
 
	def add_phone(self, val):
		val = str(val)
		if len(val) == 10:
			val = "+1" + val
			self.phone_number_list.append(val)
		else:
			print('Please enter 10 digit phone number.')

	def send_sms(self, message):
		'''
		Sends message to all phone numbers in phone_number_list.
		'''
		client = self.create_twilio()

		for phone_number in self.phone_number_list:
			client.messages.create(
				to=phone_number,
				from_=auth.VNUM,
				body=message
				)

	def create_twilio(self):
		ACCOUNT_SID = auth.ACCOUNT_SID
		AUTH_TOKEN = auth.AUTH_TOKEN
		return TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

if __name__ == "__main__":
	MESSAGE = "Vibhor you're so"

	msg = Notification()
	msg.add_phone(4844772716)
	msg.send_sms(MESSAGE)
