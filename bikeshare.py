#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
from time import strptime
import pandas as pd
import numpy as np


# In[2]:


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }


# In[3]:


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
        city = input('Please enter your prefered city:')
        try:
            if city.lower() not in ['chicago', 'new york', 'washington']:
                raise ValueError
            break
        except ValueError:
            print ("Please enter a valid city")

    print ("The mark entered was", city)
    
    
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
            month = input('Please enter your prefered month:')   
            try:
                if month.lower()  not in ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']:
                    raise ValueError
                break
            except ValueError:
                print ("Please enter a valid month")

    print ("The mark entered was", month)


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
            day = input('Please enter your prefered day:')    
            try:
                if day.lower()  not in ['sunday','monday','tuesday','wendesday','thursday','friday','saturday']:
                    raise ValueError
                break
            except ValueError:
                print ("Please enter a valid day")

    print ("The mark entered was", day)

    

    print('-'*40)
    return city, month, day


# In[4]:


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
    # Converting name to numerical correspondent.
    month = strptime(month,'%B').tm_mon
    day = strptime(day,'%A').tm_mon
    
    file = CITY_DATA.get(city)
    df = pd.read_csv(file)
    df['Start Time'] =  pd.to_datetime(df['Start Time'], infer_datetime_format=True)
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day

    if month != "all":
        df[df.month==month]
    if day != "all":
        df=df[df.day==day]
    return df


# In[5]:


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df.month.mode()
    print('most common month: ',common_month)
    # TO DO: display the most common day of week
    common_day = df.day.mode()
    print('most common day: ',common_day)

    # TO DO: display the most common start hour
    common_hour = df['Start Time'].dt.hour.mode()
    print('most common hour: ',common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[6]:


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    start_time
    # TO DO: display most commonly used start station
    common_ss= df['Start Station'].mode()
    print('most common start',common_ss)
    # TO DO: display most commonly used end station
    common_es= df['End Station'].mode()
    print('most common end',common_es)

    # TO DO: display most frequent combination of start station and end station trip
    common_comb=df.groupby(['Start Station','End Station']).size().idxmax()
    print('most common combination',common_comb[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[7]:


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('total travel time: ',df['Trip Duration'].sum())
    # TO DO: display mean travel time
    print('Average travel time: ',df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[8]:


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    cus,sub= df.groupby(['User Type']).size()
    print('users counts: customer,subscriber',cus,sub)
    # TO DO: Display counts of gender
    if city.lower() != 'washington' :
        female,male = df.groupby(['Gender']).size()
        print('genders female,male',female,male)

        # TO DO: Display earliest, most recent, and most common year of birth
        print('earliest, most recent, and most common year of birth',df['Birth Year'].min(),df['Birth Year'].max(),df['Birth Year'].mode())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
 

    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    index = 0
    while (True):
        print(df.iloc[index:index+5])
        index += 5
        view_data = input("Do you wish to continue?: ").lower()  
        if view_data != 'yes':
            break
# In[ ]:


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()


# In[ ]:





# In[ ]:




