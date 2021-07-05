import urllib.request
from  bs4 import BeautifulSoup
import webbrowser

def github():
	try:
		user = input('Enter GitHub Username: ')
		url = 'https://github.com/' + user
		html = urllib.request.urlopen(url).read()
		soup = BeautifulSoup(html, 'html.parser')

		profile_img = soup.find('img', {'alt': 'Avatar'})['src']
		print('There you go... ')
		webbrowser.open(profile_img)
	except:
		print('Oops!!Username is incorrect..')

github()
