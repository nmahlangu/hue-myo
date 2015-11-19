import sys

def get_credentials():
	filename = "credentials.txt"
	try:
		f = open(filename)
	except:
		sys.exit("Unable to open credentials.txt")

	result = {}
	for line in f:
		buf = line.split(":")
		result[buf[0]] = buf[1].replace(" ","").replace("\n","")
	return result

if __name__ == "__main__":
	print get_credentials() 