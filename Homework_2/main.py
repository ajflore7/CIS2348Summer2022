# Anthony Flores 1792816

change_amount = int(input())
if change_amount <= 0:
    print('no change')

dollars = change_amount // 100
if dollars > 0 and change_amount > 0:
    change_amount = change_amount - (dollars * 100)
if dollars == 1:
    print(dollars, 'dollar')
elif dollars > 1:
    print(dollars, 'dollars')

quarters = change_amount // 25
if quarters > 0 and change_amount > 0:
    change_amount = change_amount - (quarters * 25)
if quarters == 1:
    print(quarters, 'quarter')
elif quarters > 1:
    print(quarters, 'quarters')

dimes = change_amount // 10
if dimes > 0 and change_amount > 0:
    change_amount = change_amount - (dimes * 10)
if dimes == 1:
    print(dimes, 'dime')
elif dimes > 1:
    print(dimes, 'dimes')

nickels = change_amount // 5
if nickels > 0 and change_amount > 0:
    change_amount = change_amount - (nickels * 5)
if nickels == 1:
    print(nickels, 'nickel')
elif nickels > 1:
    print(nickels, 'nickels')

pennies = change_amount // 1
if pennies > 0 and change_amount > 0:
    change_amount = change_amount - (pennies * 1)
if pennies == 1:
    print(pennies, 'penny')
elif pennies > 1:
    print(pennies, 'pennies')


def exact_change(user_total):
    num_dollar = user_total // 100
    num_quarter = user_total // 25
    num_dime = user_total // 10
    num_nickel = user_total // 5
    num_penny = user_total
    return num_dollar, num_quarter, num_dime, num_nickel, num_penny


if __name__ == '__main__':
    input_val = int(input())
    num_dollars, num_pennies, num_nickels, num_dimes, num_quarters = exact_change(input_val)

    if input_val <= 0:
        print('No change')
    else:
        if num_dollars > 1:
            print(num_dollars, 'dollars')
        if num_dollars == 1:
            print(num_dollars, 'dollar')

        if num_quarters > 1:
            print(num_quarters, 'quarters')
        if num_quarters == 1:
            print(num_quarters, 'quarter')

        if num_dimes > 1:
            print(num_dimes, 'dimes')
        if num_dimes == 1:
            print(num_dimes, 'dime')

        if num_nickels > 1:
            print(num_nickels, 'nickles')
        if num_nickels == 1:
            print(num_nickels, 'nickel')

        if num_pennies > 1:
            print(num_pennies, 'pennies')
        if num_pennies == 1:
            print(num_pennies, 'penny')
