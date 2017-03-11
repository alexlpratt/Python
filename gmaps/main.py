"""
This small app is used for opening a google maps page for an address given in the arguments.
Example:

python main.py 123 Google Drive California USA
"""

import webbrowser, sys

class Webness:

        def __init__(self):
                if len(sys.argv) > 1:
                        self.address = '+'.join(sys.argv[1:])


        def openAddress(self):
                webAddress = 'https://www.google.com/maps/place/' + self.address
                webbrowser.open(webAddress)

if __name__ == '__main__':

	if len(sys.argv) > 1:

		webObj = Webness()
		webObj.openAddress()

	else:
		try:
			raise Exception()

		except Exception:
			print('You have not input an address.')
