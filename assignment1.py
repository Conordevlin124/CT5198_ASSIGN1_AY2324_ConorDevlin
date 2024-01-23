# Conor Devlin, Student id: 23201114
if __name__ == '__main__':
    number_of_customer = []
    list_of_days =['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    for day in list_of_days:
        sales = int(input(f' Please enter the number of customer for {day} : '))
        number_of_customer.append(sales)

    Average_customers = sum(number_of_customer) / 7
    Maximum_customers = max(number_of_customer)
    Minimum_customers = min(number_of_customer)
    print('The average amount of customers for the week is ', Average_customers)
    print('The maximum number of customers on a day is ', Maximum_customers)
    print('The minimum number of customers on a day is ', Minimum_customers)