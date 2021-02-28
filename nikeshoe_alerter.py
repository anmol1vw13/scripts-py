import requests


mobile_number=os.environment.get('MOBILE_NUMBER') #Should contain area code as well Ex: +917878787878
call_me_bot_key=os.environment.get('CALL_ME_BOT_KEY')
wire_pusher_api_key=os.environment.get('WIRE_PUSHER_KEY')



def send_whatsapp(api_key, number, text):
	requests.request("GET","https://api.callmebot.com/whatsapp.php?phone={}&text={}&apikey={}".format(number, text.replace(" ","+"), api_key))

def push_notification(wirepusher_api_key, title, message):
    requests.request("GET", "https://wirepusher.com/send?id={}&title={}&message={}&type=BUY".format(wirepusher_api_key,title, message))

def scraper(url, text):
	response = requests.request("GET", url)
	title = "{} is available now".format(text)
	message = "Jaldi se khareeeedoooooo"
	if "<div data-test=\"comingSoon\"" not in response.text:
		print("Sending alert")
		push_notification(wire_pusher_api_key, title, message)
		send_whatsapp(call_me_bot_key, mobile_number, title)
	else:
		print("No alert being sent")
		print("{} Coming soon".format(text))

scraper("https://www.nike.com/in/t/air-force-1-07-se-shoe-G0dtLG/CV8482-100", "White Nike Shoe")
scraper("https://www.nike.com/in/t/air-force-1-07-se-shoe-G0dtLG/CV8482-600", "Red Nike Shoe")
