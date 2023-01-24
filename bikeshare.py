import time
import pandas as pd

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    # define city variable.
    city = ''

    #This loop has to be run to be ensure the correct input from the user
    while city not in CITY_DATA.keys():
        print("\nCould you choose the city: [Chicago, New York City or Washington]")
        #Input from user to be converted to a lower case.
        city = input().lower()

        if city not in CITY_DATA.keys(): #Check the city availability
            print("\nInput is wrong, select the correct City!!!")

    print("\nSelected city:-> {}.".format(city.title()))


    # Get month from the user
    MONTH_DATA = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'all': 7}

    # define month variable.
    month = ''
    while month not in MONTH_DATA.keys():
        print("\nCould you choose the month from January to June, or select all")
        #Input from user to be converted to a lower case.
        month = input().lower()

        if month not in MONTH_DATA.keys(): #Check the month availability
            print("\Input is wrong. select the correct Month!!!")
            print("\nRestarting...")

    print("\nSelected month:-> {}.".format(month.title()))


    # Get day from the user
    DAY_LIST = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    # define day variable.
    day = ''
    while day not in DAY_LIST:
        print("\nCould you choose a day in the week, or select all")
        #Input from user to be converted to a lower case.
        day = input().lower()

        if day not in DAY_LIST: #Check the day availability
            print("\nInput is wrong. select the correct Day!!!")
            print("\nRestarting...")

    print("\nSelected day:-> {}.".format(day.title()))
    print(f"\nInformation shall be displayed for: {city.upper()}, month/s: {month.upper()} and day/s: {day.upper()}.")
    print('-'*40)

    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    #Load city data
    print("\nThe Data is Loading...")
    df = pd.read_csv(CITY_DATA[city])

    #Format of the Start Time column to be converted to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    #Make a new column by extracting the month, day of the week from Start Time
    df['month'] = df['Start Time'].dt.month # Make a month column
    df['day_of_week'] = df['Start Time'].dt.day_name() # Make a day column

    #Check if the month not all
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1 # Get the index of the month

        #Make a new column for the selected month
        df = df[df['month'] == month]

    #Check if the day not all
    if day != 'all':
        #Make a new column for the selected day
        df = df[df['day_of_week'] == day.title()]

    #Returns the selected file as a dataframe (df) with relevant columns
    return df




def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    #Print the most common month
    mostPpopularMonth = df['month'].mode()[0]
    print(f"Most Popular Month [1 = January till 6 = June]: {mostPpopularMonth}")

    #Print the most common day of week
    mostPopularDay = df['day_of_week'].mode()[0]
    print(f"\nMost Popular Day: {mostPopularDay}")

    #Print the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    mostPopularHour = df['hour'].mode()[0]
    print(f"\nMost Popular Start Hour: {mostPopularHour}")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    #Print most commonly used start station
    mostCommonStartStation = df['Start Station'].mode()[0]
    print(f"Most common start station: {mostCommonStartStation}")


    #Print most commonly used end station
    mostCommonEndStation = df['End Station'].mode()[0]
    print(f"\nMost common end station: {mostCommonEndStation}")

    #Create a seperate 'Start To End' column
    df['Start To End'] = df['Start Station'].str.cat(df['End Station'], sep=' to ')


    #Print most frequent of start station and end station trip
    mostCommonStartEnd = df['Start To End'].mode()[0]
    print(f"\nMost common combination between [Start & End stations): {mostCommonStartEnd}.")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    #Find total travel time
    sumOfTotalDuration = df['Trip Duration'].sum()
    #Find the duration in minutes and seconds
    minute, second = divmod(sumOfTotalDuration, 60)
    #Find the duration in hour and in minutes
    hour, minute = divmod(minute, 60)
    print(f"Total trip duration: {hour} hours, {minute} minutes and {second} seconds.")


    #Find mean travel time
    meanAverageDuration = round(df['Trip Duration'].mean())
    #Find the average duration in minutes and in seconds
    mins, sec = divmod(meanAverageDuration, 60)
    #Do a test as if the mins exceed 60 to prints the time in hours, mins, sec
    if mins > 60:
        hrs, mins = divmod(mins, 60)
        print(f"\nAverage trip duration: {hrs} hours, {mins} minutes and {sec} seconds.")
    else:
        print(f"\nAverage trip duration: {mins} minutes and {sec} seconds.")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    #Print counts of user types
    userType = df['User Type'].value_counts()
    print(f"Counting each user type:\n\n{userType}")


    #Print counts of gender
    try:
        genderCount = df['Gender'].value_counts()
        print(f"\nCounting each gender:\n\n{genderCount}")
    except:
        print("\nNo 'Gender' column within this file.")


    #Print earliest, most recent, and most common year of birth
    try:
        earliestValue = int(df['Birth Year'].min())
        recentValue = int(df['Birth Year'].max())
        commonYearVal = int(df['Birth Year'].mode()[0])
        print(f"\nEarliest year of birth: {earliestValue}")
        print(f"\nMost recent year of birth: {recentValue}")
        print(f"\nMost common year of birth: {commonYearVal}")
    except:
        print("No any birth year info within this file!!!")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_raw_data(df):
    # make a list of selection yes or no
    user_response = ['yes', 'no']
    # define a rawdata string variable
    rawdata = ''
    # define an integer variable and initialize it
    counter = 0

    # apply while loop in the user response list
    while rawdata not in user_response:
        print("\nDo you want to display the raw data? Yes or No")
        rawdata = input().lower()
        
        if rawdata == "yes":
            print(df.head())
        elif rawdata not in user_response:
            print("\nPlease check your answer.")
            print("\nRestart\n")
            print(".......")

    # this part shall be occured once the user select yes
    while rawdata == 'yes':
        print("Do you want to display more raw data?")
        counter += 5
        rawdata = input().lower()
        if rawdata == "yes":
             print(df[counter:counter+5])
        elif rawdata != "yes":
             break

    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        display_raw_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
