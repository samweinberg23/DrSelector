import subprocess
from excelReader import updateDb
from time import sleep
from threading import Thread
from case_manager import CaseManager

def lifespan():
	try:
		module = __import__("xlrd")
	except ImportError:
		subprocess.check_call(['sudo', 'pip3', 'install', "xlrd"])
		module = __import__("xlrd")
	db = CaseManager()
	updateDb(db, module)		
	print(db)


def main():
	t = Thread(target=lifespan)
	t.daemon = True
	t.start()	
	sleep(43200)
	
if __name__== "__main__":
	main()

