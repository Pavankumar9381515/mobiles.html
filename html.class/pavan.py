import logging
logging.basicConfig(
		filename = 'mylog.txt',
		level = logging.DEBUG,
		format = '%(asctime)s:%(levelname)s:%(message)s',
		datefmt = '%d-%m-%Y %I:%M %p'
		)
logging.info('A new request came')
try:
	x = int(input('Enter First Number:'))
	y = int(input('Enter Second Number:'))
	print(x/y)
except ZeroDivisionError as msg:
	print("can't devide with zero")
	logging.exception(msg)
except ValueError as msg:
	print("please provide int values only")
	logging.exception(msg)
logging.info('Request processing completed')
z
