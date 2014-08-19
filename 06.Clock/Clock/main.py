start_year = 2014
start_month = 8
start_day = 19
start_weekday = 2 # Tuesday (1-7 is Monday to Sunday)
start_hours = 23
start_minutes = 22
start_seconds = 45
start_subseconds = 255 # this is a value that counts down from 255 to 0

clock = pyb.RTC()

# datetime() takes one parameter (an 8-tuple) hence the double bracket (()) below
clock.datetime((start_year, start_month, start_day, start_weekday, start_hours, start_minutes, start_seconds, start_subseconds))

# weekday in datetime() understands Monday as 1 and Sunday as 7
days_of_the_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday' ]

while True:
	# clock.datetime() returns an 8-tuple
	clock_tuple = clock.datetime()
	'''
	year = clock_tuple()[0]
	month = clock_tuple()[1]
	day = clock_tuple()[2]
	weekday = clock_tuple()[3]
	hour = clock_tuple()[4]
	min = clock_tuple()[5]
	sec = clock_tuple()[6]
	# subsec = clock_tuple()[7] # likely we wont be using this hence it's commented
	'''
	#print('The time is', hour,':',min,':',sec)
	#print('Today\'s date is', day,'.',month,'.',year)
	#print('Today is a', days_of_the_week[weekday])
	pyb.delay(100)
	