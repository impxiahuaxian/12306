import requests

class ZhenziSmsClient(object):
	def __init__(self, apiUrl, appId, appSecret):
		self.apiUrl = apiUrl
		self.appId = appId
		self.appSecret = appSecret

	def send(self, number, message, messageId=''):
		data = {
			'appId': self.appId,
			'appSecret': self.appSecret,
			'message': message,
			'number': number,
			'messageId': messageId
		}
		response = requests.post(self.apiUrl+'/sms/send.do', data=data, verify=False)
		result = str(response.content, 'utf-8')
		return result


	def balance(self):
		data = {
		    'appId': self.appId,
		    'appSecret': self.appSecret
		}

		response = requests.post(self.apiUrl+'/account/balance.do', data=data, verify=False)
		result = str(response.content, 'utf-8')
		return result

	def findSmsByMessageId(self, messageId):
		data = {
		    'appId': self.appId,
		    'appSecret': self.appSecret,
		    'messageId': messageId
		}
		response = requests.post(self.apiUrl+'/smslog/findSmsByMessageId.do', data=data, verify=False)
		result = str(response.content, 'utf-8')
		return result
