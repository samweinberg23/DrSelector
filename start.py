import subprocess

def main():
	try:
		module = __import__("pickledb")
	except ImportError:
		subprocess.check_call(['sudo', 'pip3', 'install', "pickledb"])
		module = __import__("pickledb")
	pickledb = module
		
	db = pickledb.load('local.db', False)
		

if __name__== "__main__":
	main()

