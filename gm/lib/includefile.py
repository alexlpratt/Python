import webbrowser, sys

class Webness:

	def __init__(self):
		if len(sys.argv) > 1:
			self.address = '+'.join(sys.argv[1:])


	def openAddress(self):
		webAddress = 'https://www.google.com/maps/place/' + self.address
		webbrowser.open(webAddress)
