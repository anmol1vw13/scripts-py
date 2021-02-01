import requests

def send_whatsapp(api_key, number, text):
	requests.request("GET","https://api.callmebot.com/whatsapp.php?phone={}&text={}&apikey={}".format(number, text.replace(" ","+"), api_key))


def scraper(url, text):
	response = requests.request("GET", url)
	title = "{} is available now".format(text)
	message = "Jaldi se khareeeedoooooo"
	if "<div data-test=\"comingSoon\"" not in response.text:
		requests.request("GET", "https://wirepusher.com/send?id=9bzZmpX6j&title={}&message={}&type=BUY".format(title, message))
		send_whatsapp("462501", "+918884285172", title)
		send_whatsapp("337782", "+917224072497", title)
	else:
		print("{} Coming soon".format(text))

scraper("https://www.nike.com/in/t/air-force-1-07-se-shoe-G0dtLG/CV8482-600", "Red Nike Shoe")
scraper("https://www.nike.com/in/t/air-force-1-07-se-shoe-G0dtLG/CV8482-100", "White Nike Shoe")