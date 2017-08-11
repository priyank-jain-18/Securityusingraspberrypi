import requests
from bs4 import BeautifulSoup

class sms:

	def __init__(self,username,password):


		self.url='http://site24.way2sms.com/Login1.action?'

		self.cred={'username': username, 'password': password}

		self.s=requests.Session()			# Session because we want to maintain the cookies

		

		self.s.headers['User-Agent']="Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0"

		self.q=self.s.post(self.url,data=self.cred)

		self.loggedIn=False				# a variable of knowing whether logged in or not

		if self.q.status_code!=200:			# http status 200 == OK

			self.loggedIn=False

		else:

			self.loggedIn=True

		self.jsid=self.s.cookies.get_dict()['JSESSIONID'][4:]	    # JSID is the main KEY as JSID are produced every time a session satrts

	def msgSentToday(self):

		'''
		Returns number of SMS sent today as there is a limit of 100 messages everyday..!
		'''

		self.msg_left_url='http://site24.way2sms.com/sentSMS?Token='+self.jsid

		self.q=self.s.get(self.msg_left_url)

		self.soup=BeautifulSoup(self.q.text,'html.parser')		#we want the number of messages sent which is present in the

		self.t=self.soup.find("div",{"class":"hed"}).h2.text		# div element with class "hed" -> h2

		self.sent=0

		for self.i in self.t:

			if self.i.isdecimal():

				self.sent=10*self.sent+int(self.i)

		return self.sent

	def send(self,mobile_no,msg):

		'''
		Sends the message to the given mobile number
		'''

		if len(msg)>139 or len(mobile_no)!=10 or not mobile_no.isdecimal():	

			return False							

		self.payload={'ssaction':'ss',
				'Token':self.jsid,					,
			        'mobile':mobile_no,					
       				 'message':msg,						
			        'msgLen':'129'
       			     }

		self.msg_url='http://site24.way2sms.com/smstoss.action'

		self.q=self.s.post(self.msg_url,data=self.payload)

		if self.q.status_code==200:

			return True

		else:
			return False

	def sendLater(self, mobile_no, msg, date, time):				.
											
										
		if len(msg)>139 or len(mobile_no)!=10 or not mobile_no.isdecimal():
			return False

		dateparts = date.split('/')			
		timeparts = time.split(':')
		if int(dateparts[0])<1 or int(dateparts[0])>32 or int(dateparts[1])>12 or int(dateparts[1])<1 or int(dateparts[2])<2017 or int(timeparts[0])<0 or int(timeparts[0])>23 or int(timeparts[1])>59 or int(timeparts[1])<0:
			return False
		date = dateparts[0].zfill(2) + "/" + dateparts[1].zfill(2) + "/" + dateparts[2]
		time = timeparts[0].zfill(2) + ":" + timeparts[1].zfill(2)

		self.payload={'Token':self.jsid,
				'mobile':mobile_no,
				'sdate':date,
				'stime':time,
				'message':msg,
				'msgLen':'129'
				}

		self.msg_url='http://site24.way2sms.com/schedulesms.action'
		self.q=self.s.post(self.msg_url, data=self.payload)

		if self.q.status_code==200:
			return True
		else:
			return False

	def logout(self):

		self.s.get('http://site24.way2sms.com/entry?ec=0080&id=dwks')

		self.s.close()								# close the Session

		self.loggedIn=False
