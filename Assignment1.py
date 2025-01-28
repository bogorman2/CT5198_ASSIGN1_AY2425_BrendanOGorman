def main():
    daysofweek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']  # days of week
    dailynumofcustomers = []  # empty list of daily customer number
    for i in range(len(daysofweek)):  # for loop through days of week
        print('For', daysofweek[i], 'please input the number of customers')  # printing a request for the days number
        todaystr = input("?")  # taking in the input string
        todaysnum = float(todaystr)  # converting string to a float number
        dailynumofcustomers.append(todaysnum)  # putting todays value into list
    print('The highest daily number of customers is ', max(dailynumofcustomers))  # printing max value of list
    print('The lowest daily number of customers is  ', min(dailynumofcustomers))  # printing min value of list
    print('the average daily number of customers is ',
          round(sum(dailynumofcustomers) / 7, 2))  # printing average value to 2 decimals places


if __name__ == "__main__":  # checks we are in main scope
    main()