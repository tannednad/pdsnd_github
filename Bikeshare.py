#!/usr/bin/env python
# coding: utf-8

# In[2]:


import time
import pandas as pd
import numpy as np

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
    
    city = input("Would you like to see tha data for Chicago, New York City, or Washington? ").lower()
    
    while city not in ["chicago", "new york city", "washington"]:
        city = input("Please try again and make sure you typed the name of the city correctly. ").lower()

            
    # get user input for month (all, january, february, ... , june)
    
    month = input("Enter any of the first 6 months to filter by or enter All to select all 6 months. ").lower()
    
    while month not in ["january", "february","march","april","june","all"]:
        month = input("Please make sure you typed the name of the month correctly within the first 6 months. ").lower()

    

    # get user input for day of week (all, monday, tuesday, ... sunday)
    
    day = input("Which day of the week would you like to filter by? Enter All to apply no day filter. ").title()
    
    while day not in ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","All"]:
        day = input("Please try again and make sure you typed the name of the day correctly. ").title()
      
    print('-'*40)
    return city, month, day

def load_data(city, month,day):
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
    
    months_values = {'january':1 , 'february':2 , 'march':3 , 
                     'april':4 , 'may':5 , 'june':6}
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    
    if day != "All":
        df = df[df['day_of_week'] == day]
    if month != "all":
        df = df[df['month'] == months_values[month]]
        
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    
    popular_month = df['month'].mode()


    # display the most common day of week
    
    popular_day = df['day_of_week'].mode()


    # display the most common start hour
    
    popular_start_hr = df['hour'].mode()
    
    print("Most common month: {} \n\nMost common day of the week: {} \n\n\
    Most common hour: {}".format(popular_month, popular_day, popular_start_hr))

    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def station_stats(df):
    
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()


    # display most commonly used end station
    popular_end_station = df['End Station'].mode()

    # display most frequent combination of start station and end station trip
    combinations = df[['Start Station','End Station']]
    popular_combination = combinations.value_counts().head(1)
    
    print ("\nMost Frequently Used Start Station: {}\n\n\
    Most Frequently Used End Station: {}\n\n\
    Most Frequent Combination: \n {}".format(popular_start_station,popular_end_station,popular_combination))
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def trip_duration_stats(df):
    
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    
    total_travel_time = df['Trip Duration'].sum()
    print("\nTotal travel time is: {} seconds".format(total_travel_time))

    # display mean travel time
    
    mean_travel_time = round(df['Trip Duration'].mean(),2)
    
    print("\nMean travel time is: {} seconds".format(mean_travel_time))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def user_stats(df):
    
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    
    user_type = df[['User Type']].value_counts()
    print("\n", user_type) 
    
         
    # Display counts of gender
    

    gender = df[['Gender']].value_counts()
    print("\n", gender)


    # Display earliest, most recent, and most common year of birth
    
    earliest = int(df['Birth Year'].min())
    
    most_recent = int(df['Birth Year'].max())
    
    common_year = int(df['Birth Year'].mode()) 
    
    print ("\n Earliest Birth Year: {}\n\
    Most recent birth year: {}\n\
    Most common birth year: {}".format(earliest, most_recent, common_year))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def user_stats_w(df):
    
    """Displays statistics on bikeshare users for data missing the gender and birth year info."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    
    user_type = df[['User Type']].value_counts()
    print("\n", user_type) 


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)    


def raw_data(df):
    
    """Displays 5 lines of raw data each time the user enters yes"""
    
    display_raw_data = input("Would you like to see raw data? Enter yes or no. ").lower()
    while display_raw_data not in ["yes", "no"]:
            display_raw_data = input("Please enter yes or no. ").lower()
            
    i = 1
    j = 5
    while display_raw_data == "yes":
        print(df.loc[i:j])
        i += 5
        j += 5
        display_raw_data = input("Would you like to see another 5 rows of raw data? Enter yes or no. ").lower()
        while display_raw_data not in ["yes", "no"]:
            display_raw_data = input("Please enter yes or no. ").lower()
            
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        df.index = range(1,len(df)+1)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        if city != 'washington':
            user_stats(df)
        else:
            user_stats_w(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
        while restart not in ['yes','no']:
            restart = input("Please enter yes or no. ").lower()
        if restart == "no":
            break


if __name__ == "__main__":
	main()


# In[ ]:




