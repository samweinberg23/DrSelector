import subprocess
from excelReader import updateDb

def main():
	try:
		module = __import__("xlrd")
	except ImportError:
		subprocess.check_call(['sudo', 'pip3', 'install', "xlrd"])
		module = __import__("xlrd")
	db = {}	
	updateDb(db)		

if __name__== "__main__":
	main()

