import time
import pandas as pd
import numpy as np

CITIES_DATA = { 'chicago': 'chicago.csv',
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
    city=input("Enter the city's name\n")
    city=city.lower()
    Cities= ['chicago','new york city','washington']
    while city not in Cities:
      city=input("Invalid Input, Enter the correct city name\n") 
    # TO DO: get user input for month (all, january, february, ... , june)
    months = [ 'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    month=input("Enter the month\n")
    while month not in months+['all']:
        month=input("Invalid Month , Enter the correct month\n")    

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day=input("Enter the day\n")
    while day not in ['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']:
      day=input("Invalid day , Enter the correct day\n")

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
    df = pd.read_csv(CITIES_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    
    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    common_month = df['month'].mode()[0]
    print("Most common month: {}".format(common_month))

    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    common_day = df['day_of_week'].mode()[0]
    print("Most common day of week: {}".format(common_day))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print("Most common start hour: {}".format(common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    com_start_station = df['Start Station'].mode()[0]
    print("The most common Start Station is: {}".format(com_start_station))

    # TO DO: display most commonly used end station
    com_end_station = df['End Station'].mode()[0]
    print("The most common End Station is: {}".format(com_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    common_combo = df.groupby(['Start Station','End Station'])['Start Station'].agg(['count']).sort_values('count', ascending = False).head(1).reset_index()
    print("The most common trip is:\n\n {}".format(common_combo))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total Travel Time: {}".format(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("Mean Travel Time: {}".format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("User Types corresponds to \n",df['User Type'].value_counts(),"\n")

    # TO DO: Display counts of gender
    try:
        print("Information regarding the different Gender\n",df['Gender'].value_counts(),"\n")
    except:
        print("Information regarding Gender not availaible\n")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        print("The person with earliest Birth Year was born on",min(df['Birth Year']),"\n")
        print("The person with most recent Birth Year was born on",max(df['Birth Year']),"\n")
        print("The Most Common Year the people were born corresponds to",df['Birth Year'].mode()[0],"\n")
    except:
        print("Information regarding the Birth not availaible","\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data():
    answer=input("Do you want to see raw data? Type yes to continue\n")
    if(answer=="yes"):
        return True
    else:
        return False

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        for functions in [time_stats,station_stats,trip_duration_stats,user_stats]: 
            if (display_data()):
                functions(df)  
                x = 0
                y = 5
                response = input('Display 5 rows?: yes or no? ')
                while response.lower() == 'yes':
                  print((df.iloc[x:y]))
                  x += 5
                  y += 5
                  response = input('Display 5 rows?: yes or no?  ')
                starting_row = 0
                ending_row = 5
                response = input('Display 5 rows? yes or no? ')
                while response.lower() == 'yes':
                  print((df.iloc[starting_row:ending_row]))
                  starting_row += 5
                  ending_row += 5
                  response = input('Display 5 rows? yes or no?  ')

                restart = input('\nWould you like to restart?: Enter yes or no.\n')
                if restart.lower() != 'yes':
                  break


if __name__ == "__main__":
	main()
