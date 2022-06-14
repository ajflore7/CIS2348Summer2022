# Anthony Flores 1792816 CIS2348
services = {'-': 0, 'Oil change': 35, 'Tire rotation': 19, 'Car wash': 7, 'Car wax': 12}
print('Davy\'s auto shop services')
print('Oil change -- $35')
print('Tire rotation -- $19')
print('Car wash -- $7')
print('Car wax -- $12')
print()

Oil_change = 35
Tire_rotation = 19
Car_wash = 7
Car_wax = 12
first_service = input('Select first service:''\n')
second_service = input('Select second service:''\n')
print()

cost_first_service = services[first_service]
cost_second_service = services[second_service]
print('Davy\'s auto shop invoice')
print()

if first_service == '-':
    print('Service 1: No service')
else:
    print('Service 1:', first_service + ',', '${:,.0f}'.format(cost_first_service))

if second_service == '-':
    print('Service 2: No service')
else:
    print('Service 2:', second_service + ',', '${:,.0f}'.format(cost_second_service))

print()
total = cost_first_service + cost_second_service
print('Total:', ('${:,.0f}'.format(total)))
