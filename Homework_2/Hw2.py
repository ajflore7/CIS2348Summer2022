# Anthony Flores 1792816
import datetime
# file = open('inputDates.txt', r)
month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
         'September', 'October', 'November', 'December']

date = input('Enter date as Month DD, YYYY:\n')


today = datetime.datetime.now()

print(today.strftime('%B/%d/%Y'))
