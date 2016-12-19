if __name__ == '__main__':

	import sys

	if len(sys.argv) > 1:

		from lib import includefile as webb

		webObj = webb.Webness()
		webObj.openAddress()

	else:
		try:
			raise Exception()

		except Exception:
			print('You have not input an address.')
