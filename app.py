import requests
import re
import time
from telegram.ext import Updater, CommandHandler as CH
from threading import Thread
#from bs4 import BeautifulSoup as bs

__author__ = "Billal Fauzan"
__version__ = "0.1"

class app:
	def __init__(self):
		self.token = "827809056:AAHkwMFzBLQJ1UAzdqxnuc3altegIh4juc8"
		self.url = "https://api.telegram.org/bot"+self.token
		self.api = "https://hashid.blackcodercrush.com/"

	def totalView(self):
		r = requests.get(self.api)
		find = re.findall('Total views: <span class="float-right">(.*)</span>', r.text)
		return find[0]

	def sha512(self, update, hash):
                if update.message.from_user.username:
                        user = update.message.from_user.username
                else:
                        user = "unknown"
                print ("[#] @%s Cracking sha512|%s" % (user, hash))
                self.log("@%s Crack sha512|%s" % (user, hash))
                self.reply(update, "Cracking, Please wait...")
                r = requests.get(self.api+"/api/decrypt.php?type=sha512&hash=%s" % (hash)).json()
                if r["error"] == False:
                        print ("[#] Success %s|%s" % (hash, r["result"]["text"]))
                        self.log("Found: %s|%s" % (hash, r["result"]["text"]))
                        self.reply(update, """

✅  Success  ✅

Result:
  Text: %s
  Hash: %s
  Type: sha512

        """ % (r["result"]["text"], hash))
                else:
                        self.log(" [ERROR] %s %s" % (user, r["message"]))
                        self.reply(update, r["message"])

	def sha1(self, update, hash):
                if update.message.from_user.username:
                        user = update.message.from_user.username
                else:
                        user = "unknown"
                print ("[#] @%s Cracking sha1|%s" % (user, hash))
                self.log("@%s Crack sha1|%s" % (user, hash))
                self.reply(update, "Cracking, Please wait...")
                r = requests.get(self.api+"/api/decrypt.php?type=sha1&hash=%s" % (hash)).json()
                if r["error"] == False:
                        print ("[#] Success %s|%s" % (hash, r["result"]["text"]))
                        self.log("Found: %s|%s" % (hash, r["result"]["text"]))
                        self.reply(update, """

✅  Success  ✅

Result:
  Text: %s
  Hash: %s
  Type: sha1

        """ % (r["result"]["text"], hash))
                else:
                        self.log(" [ERROR] %s %s" % (user, r["message"]))
                        self.reply(update, r["message"])

	def md5(self, update, hash):
		if update.message.from_user.username:
			user = update.message.from_user.username
		else:
			user = "unknown"
		print ("[#] @%s Cracking md5|%s" % (user, hash))
		self.log("@%s Crack md5|%s" % (user, hash))
		self.reply(update, "Cracking, Please wait...")
		r = requests.get(self.api+"/api/decrypt.php?type=md5&hash=%s" % (hash)).json()
		if r["error"] == False:
			print ("[#] Success %s|%s" % (hash, r["result"]["text"]))
			self.log("Found: %s|%s" % (hash, r["result"]["text"]))
			self.reply(update, """

✅  Success  ✅

Result: 
  Text: %s
  Hash: %s
  Type: md5

	""" % (r["result"]["text"], hash))
		else:
			self.log(" [ERROR] %s %s" % (user, r["message"]))
			self.reply(update, r["message"])

	def crack(self, update, context):
		arg = context.args
		try:
			hash = arg[1]
			if arg[0] == "md5":
				th = Thread(target=self.md5, args=(update, hash,))
				th.start()
			elif arg[0] == "sha1":
				th = Thread(target=self.sha1, args=(update, hash))
				th.start()
			elif arg[0] == "sha512":
				th = Thread(target=self.sha512, args=(update, hash))
				th.start()
			else:
				self.log("%s Not supported")
				self.reply(update, "Type not supported 😰")
		except IndexError:
			self.log("Hash or Type not found")
			self.reply(update, "/crack <type> <hash>")

	def reply(self, update, text):
		update.message.reply_text(text)

	def getMe(self):
		r = requests.get(self.url+"/getMe").json()["result"]
		self.username = r["username"]
		self.name = r["first_name"]
		print ("[#] ID: %d" % (r["id"]))
		print ("[#] Name: %s" % (r["first_name"]))
		print ("[#] Username: %s" % (r["username"]))
		if r["is_bot"] == True:
			print ("[#] Bot: True")
		else:
			print ("[#] Bot: False")

	def getTime(self):
		t = time.ctime(time.time()).split(" ")[4]
		return t

	def log(self, text):
		o = open("console.log", "a")
		o.write("["+self.getTime()+"] "+text+"\n")
		o.close()

	def start(self, update, context):
		if update.message.from_user.username:
			user = update.message.from_user.username
		else:
			user = "unknown"
		print ("[#] @%s Started" % (user))
		self.log("%s Started" % ( user))
		send = """
Hallo broo!

Welcome to @hashidcracker_bot

Commands:
  /enc <type> <hash> = Encrypt Text to Hash
  /crack <type> <hash> = Decrypt Hash to Text

Examples:
  /crack md5 45d28beb770202b785d40fb6210e6f4d
  /crack sha1 aa1684b1cc62e51900e4a4e3655bef416a74e5e8
  /enc md5 billal
  /enc sha1 blackcodecrush

Type Hash:
   - md5
   - sha1
   - sha512
   - whirlpool

Author: %s
Version: %s

Thanks to using this my tool 😊
		""" % (__author__, __version__)
		self.reply(update, send)

	def enc(self, update, context):
		arg = context.args
		try:
			hash = arg[1]
			if arg[0] == "md5":
				r = requests.get(self.api+"/api/encrypt.php?type=md5&text=%s" % (hash)).json()
				if r["result"]["hash"]:
					self.reply(update, """

✅  Success  ✅

Result:
  Text: %s
  Hash: %s
  Type: md5

        """ % (hash, r["result"]["hash"]))
			elif arg[0] == "sha1":
				r = requests.get(self.api+"/api/encrypt.php?type=sha1&text=%s" % (hash)).json()
				if r["result"]["hash"]:
					self.reply(update, """

✅  Success  ✅

Result:
  Text: %s
  Hash: %s
  Type: sha1

        """ % (hash, r["result"]["hash"]))
			elif arg[0] == "sha512":
				r = requests.get(self.api+"/api/encrypt.php?type=sha512&text=%s" % (hash)).json()
				if r["result"]["hash"]:
					self.reply(update, """

✅  Success  ✅

Result:
  Text: %s
  Hash: %s
  Type: sha512

        """ % (hash, r["result"]["hash"]))
		except IndexError:
			self.log("Hash or Type not found")
			self.reply(update, "/enc <type> <text>")

	def main(self):
		print ("[!] Bot Started [!]")
		up = Updater(self.token, use_context=True)
		dis = up.dispatcher
		dis.add_handler(CH("start", self.start))
		dis.add_handler(CH("crack", self.crack))
		dis.add_handler(CH("enc", self.enc))
		up.start_polling()

main = app()
main.getMe()
main.main()
