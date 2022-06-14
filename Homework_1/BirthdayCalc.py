#Anthony Flores 1792816

print('When is your Birthday?')
Birth_month = int(input('Month (MM):'))
Birth_day = int(input('Day (DD):'))
Birth_year = int(input('Year (YYYY):'))

current_date = [Current_month, '/', Current_day, '/', Current_year]
date_of_birth = [Birth_month, '/', Birth_day, '/', Birth_year]

if (Current_month or Current_day in current_date) > (Birth_month or Birth_day in date_of_birth):
    age = Current_year - Birth_year
else:
    age = Current_year - Birth_year 

if (Current_month or Current_day in current_date) < (Birth_month or Birth_day in date_of_birth):
    age = Current_year - Birth_year

print('You are', age, 'years old')

if Current_month == Birth_month and Current_day == Birth_day:
    age = Current_year - Birth_year
    print('WOW today is your birthday, Happy Birthday!')
else:
    print('Today is not your Birthday.')
#I was not able to fix the age if the birthday had not passed yetz can you make a comment and fix the code so I know how to do it?
#thank you
