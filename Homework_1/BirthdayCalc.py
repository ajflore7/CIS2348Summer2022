#Anthony Flores 1792816

print('Birthday Calculator')
print('Enter current date below ')
Current_month = int(input('Month (MM):'))
Current_day = int(input('Day (DD):'))
Current_year = int(input('Year (YYYY):'))

print('When is your Birthday?')
Birth_month = int(input('Month (MM):'))
Birth_day = int(input('Day (DD):'))
Birth_year = int(input('Year (YYYY):'))
age = Current_year - Birth_year

if Current_month == Birth_month:
    if Current_day == Birth_day:
        print('WOW today is your birthday, Happy Birthday!', age)
else:
    print('You are', age, 'years old')
