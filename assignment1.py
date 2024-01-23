# Conor Devlin, Student id: 23201114
# This application will prompt the user to enter the number of customers they have received for each day of the week over a 7-day period. The application will then be able to calculate the average, maximum and minimum amount of customers the user had.
if __name__ == '__main__':
    number_of_customers = []  # This will create an empty list for the number of customers for each day to be added into.
    list_of_days =['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'] # A list of each day of the week

    for day in list_of_days:  # The for loop will iterate through each day of the week
        while True:  # While the for loops is iterating through the days of the week, we will use try and except to prevent non-integer values from being submitted.
            try:
                sales = int(input(f' Please enter the number of customer for {day} : ')) # Prompting the customer to enter an integer
                number_of_customers.append(sales)  # Adding the input (number of customers) to the empty list
                break
            except ValueError:  # If the value is not an integer they will be asked to input again.
                print('Invalid input, please enter number of customers as an input')

    cal_average_customers = sum(number_of_customers) / len(list_of_days) # Calculating the average number of customers for the week by dividing the total by 7
    average_customers = round(cal_average_customers) #  This will round the average number of customers to the nearest whole number.
    maximum_customers = max(number_of_customers)  # Calculating the maximum number of customers on a day throughout the week
    minimum_customers = min(number_of_customers)  # Calculating the minimum number of customers on a day throughout the week
    #  The below will print the average, maximum and minimum number of customers from throughout the week
    print('The average amount of customers for the week is ', average_customers)
    print('The maximum number of customers on a day is ', maximum_customers)
    print('The minimum number of customers on a day is ', minimum_customers)