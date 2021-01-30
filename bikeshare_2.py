import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
cities = ['chicago', 'new york city', 'washington']
month_names = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

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
    while True:
        try:
            city = input("Enter the name of the city (chicago, new york city, washington): ").lower()
        except:
            print("Sorry, I didn't understand that. Please try again")
            continue
        else:
            break



    # get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = input("Please enter the name of the month (all, january, february, ... , june): ").lower()
        except:
            print("Sorry, I didn't understand that. Please try again")
            continue
        else:
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = input("Please enter the day of the week (all, monday, tuesday, ... , sunday): ").lower()
        except:
            print("Sorry, I didn't understand that. Please try again")
            continue
        else:
            break

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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day_name()

    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month = df['month'].mode()[0]
    print("\nThe most common month is: \n{}".format(popular_month))
    # display the most common day of week
    popular_day_of_week = df['day'].mode()[0]

    print("\nThe most common day of week is: \n{}".format(popular_day_of_week))
    # display the most common start hour
    popular_start_hour = df['Start Time'].dt.hour.mode()[0]

    print("\nThe most common start hour is: \n{}".format(popular_start_hour))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print("\nThe most commonly used start station is: \n{}".format(popular_start_station))
    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print("\nThe most commonly used end station is: \n{}".format(popular_end_station))
    # display most frequent combination of start station and end station trip
    popular_start_n_end_station = df.groupby(['Start Station', 'End Station']).size().sort_values(ascending=False)
    print("\nThe most frequent combination of start station and end station trip is: \n{}".format(popular_start_n_end_station))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = sum(df['Trip Duration'])
    print("\nThe total travel time is: \n{}".format(total_travel_time))
    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("\nThe mean travel time is: \n{}".format(mean_travel_time))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print("\nThe user types have the following counts: \n{}".format(user_types))

    # Display counts of gender
    genders = df['Gender'].value_counts()
    print("\nThe genders have the following counts: \n{}".format(genders))
    # Display earliest, most recent, and most common year of birth
    earliest_birth_year = df['Birth Year'].min()
    print("\nThe earliest year of birth is: \n{}".format(earliest_birth_year))
    most_recent_birth_year = df['Birth Year'].max()
    print("\nThe most recent year of birth is: \n{}".format(most_recent_birth_year))
    most_common_birth_year = df['Birth Year'].mode()[0]
    print("\nThe most common year of birth is: \n{}".format(most_common_birth_year))

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
