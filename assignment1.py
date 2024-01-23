# Conor Devlin, Student id: 23201114
if __name__ == '__main__':
    number_of_customer = []  # This will create an empty loop for the number of customers for each day to be added into.
    list_of_days =['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'] # A list of each day of the week

    for day in list_of_days:  # The for loop will iterate through each day of the week
        sales = int(input(f' Please enter the number of customer for {day} : '))
        number_of_customer.append(sales)  # Adding the input (number of customers) to the empty list

    Average_customers = sum(number_of_customer) / 7  # Calculating the average number of customers for the week by dividing the total by 7
    Maximum_customers = max(number_of_customer)  # Calculating the maximum number of customers on a day throughout the week
    Minimum_customers = min(number_of_customer)  # Calculating the minimum number of customers on a day throughout the week
    print('The average amount of customers for the week is ', Average_customers)
    print('The maximum number of customers on a day is ', Maximum_customers)
    print('The minimum number of customers on a day is ', Minimum_customers)