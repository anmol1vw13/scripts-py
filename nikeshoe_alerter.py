import requests

def scraper(url, text):
	response = requests.request("GET", url)
	title = "{} is available now".format(text)
	message = "Jaldi se khareeeedoooooo"
	if "<div data-test=\"comingSoon\"" not in response.text:
		requests.request("GET", "https://wirepusher.com/send?id=9bzZmpX6j&title={}&message={}&type=BUY".format(title, message))
	else:
		print("{} Coming soon".format(text))


scraper("https://www.nike.com/in/t/air-force-1-07-se-shoe-G0dtLG/CV8482-600", "Red Nike Shoe")
scraper("https://www.nike.com/in/t/air-force-1-07-se-shoe-G0dtLG/CV8482-100", "White Nike Shoe")