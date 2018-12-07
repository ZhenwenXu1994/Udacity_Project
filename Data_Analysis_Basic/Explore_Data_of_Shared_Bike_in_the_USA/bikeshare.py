import time
import pandas as pd
import numpy as np
import datetime

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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('\nWould you like to see data for Chicago, New York City, or Washington ?\n').lower()
        if city in ['chicago', 'new york city', 'washington']:
            break
        else:
            print('Sorry, your input is invaild, please try again.')

    # TO DO: get user input if the data to be filtered by month, day, both or none
    while True:
        filter = input('\nWould you like to filter by month,day,both or none?\n').lower()
        if filter in ['month', 'day', 'both', 'none']:
            break
        else:
            print('Sorry, your input is invaild, please try again.')

    # TO DO: get user input for month (all, january, february, ... , june)
    if filter == 'month' or filter == 'both':
        while True:
            day = ''
            month = input('\nWhich month do you want to see?January, February, March, April, May, or June?\n').title()
            if month in ['January', 'February', 'March', 'April', 'May', 'June']:
                break
            else:
                print('Sorry, your input is invaild, please try again.')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    if filter == 'day' or filter == 'both':
        while True:
            day = input('\nWhich day do you want to see? Monday, Tuesday, ..., or Sunday?\n').title()
            month = ''
            if day in ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday', 'All']:
                break
            else:
                print('Sorry, your input is invaild, please try again.')
    # If user choose none then setting month and day variables as blank
    if filter == 'none':
        day = ''
        month = ''

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
    print('Loading data from ' + CITY_DATA[city] + ' , please wait ...')
    # Load data from .csv file which need to replace some character to match the file's name
    df = pd.read_csv(city.replace(' ', '_') + '.csv')
    # Convert the Start time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # Extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # Use if judgement to filter and load the data by specified input
    if filter == 'both':
        df = df[(df['month'] == month) & (df['day_of_week'] == day)]
    elif filter == 'month':
        df = df[df['month'] == month]
    elif filter == 'day':
        df = df[df['day_of_week'] == day]
    else:
        df = df

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    # Define DataFrame filtering by month
    month = df['Start Time'].dt.month
    # Use DataFrame.mode() to find most frequent month
    most_common_month = month.mode()[0]
    # Print the result
    print('The most common month: {} \n'.format(most_common_month))

    # TO DO: display the most common day of week
    # Define DataFrame filtering by day
    day = df['Start Time'].dt.weekday_name
    # Use DataFrame.mode() to find most frequent day
    most_common_day = day.mode()[0]
    # Print the result
    print('The most common day: {} \n'.format(most_common_day))

    # TO DO: display the most common start hour
    # Define DataFrame filtering by hour
    hour = df['Start Time'].dt.hour
    # Use DataFrame.mode() to find most frequent hour
    most_common_hour = hour.mode()[0]
    # Print the result
    print('The most common hour: {}'.format(most_common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    # First of all, counting all start station by using .value_counts()
    start_station = df['Start Station'].value_counts()
    start_count = start_station.max()
    # Then, output the most frequent start station by output the index matching the count
    most_common_start_station = start_station.idxmax()
    # Print the results
    print('The most commonly used start station was: {}, Count: {}'.format(most_common_start_station, start_count))

    # TO DO: display most commonly used end station
    # First of all, counting all end station by using .value_counts()
    end_station = df['End Station'].value_counts()
    end_count = end_station.max()
    # Then, output the most frequent start station by output the index matching the count
    most_common_end_station = end_station.idxmax()
    # Print the results
    print('The most commonly used end station was: {}, Count: {}'.format(most_common_end_station, end_count))

    # TO DO: display most frequent combination of start station and end station trip
    # First, combine start station column and end station column and counting all trip by using .value_counts()
    df['Start End'] = df['Start Station'] + ' to ' + df['End Station']
    start_end = df['Start End'].value_counts()
    start_end_count = start_end.max()
    # Then, output the most frequent combination of start station and end station trip by output the index matching the count
    most_frequent_combination = start_end.idxmax()
    # Print the results
    print('The most frequent combination of start station and end station trip : {}, Count : {}'.format(most_frequent_combination,start_end_count))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    # Just calculating total time by using sum() of 'Trip Duration' column
    total_travel = df['Trip Duration'].sum()
    # Print the result
    print('The total travel time was: {} \n'.format(total_travel))

    # TO DO: display mean travel time
    # Just calculating average time by using mean() of 'Trip Duration' column
    mean_travel = df['Trip Duration'].mean()
    # Print the result
    print('The mean travel time was: {}'.format(mean_travel))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    # Three cities all have user types column, so just using DataFrame.value_counts() to show result
    user_types = df['User Type'].value_counts()
    # Print series to show the results
    print('This is counts of user types: \n{}'.format(user_types))

    # TO DO: Display counts of gender
    # Because washington doesn't include 'Gender' column in .csv file, it must use if judgement
    if 'Gender' in df.columns:
        gender = df['Gender'].value_counts()
        # Print series to show the results
        print('\nThis is counts of gender: \n{}'.format(gender))

    # TO DO: Display earliest, most recent, and most common year of birth
    # As same as 'Gender', we need to do the same type of judement for 'Birth Year'
    if 'Birth Year' in df.columns:
        earlist_year = df['Birth Year'].min()
        most_recent_year = df['Birth Year'].max()
        # Using .mode() method to sort years from most frequent to least frequent, then get the most frequent one
        most_common_year = df['Birth Year'].mode()[0]
        # Print all results
        print('\nThis is earlist year of birth: {}'.format(earlist_year))
        print('\nThis is most recent year of birth: {}'.format(most_recent_year))
        print('\nThis is most common year of birth: {}'.format(most_common_year))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
