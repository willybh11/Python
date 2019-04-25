from datetime import datetime
from sys import argv

def main():
	try:	#if user input
		day  = ['mon','tue','wed','thu','fri'].index(argv[1])	#input 1
		week = argv[2]											#input 2
	except: #auto
		day  = datetime.today().weekday()									#Auto day  num
		week = 'b' if datetime.utcnow().isocalendar()[1] % 2 == 0 else 'a'	#Auto week num

	print Schedule(week,day),'\n'

def Schedule(week,day):	#return corresponding schedule
	with open('data') as f:	weeks = f.read().split('--week--')		#[A week , B week]
	return weeks[0 if week == "a" else 1].split('--days--') [day]	#return the day's schedule

if __name__ == '__main__':
	main()
