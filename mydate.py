# mydate.py
import random

def is_valid_month_num(n):
    return n > 0 and n <= 12

def month_num_to_string(month_num):
    month_list = ['January', 'February', 'March', 'April', 'May', 'June',
                  'July', 'August', 'September', 'October', 'November', 'December']
    
    return month_list[month_num - 1]

def date_to_string(date_list):
    return "{1} {2}, {0}".format(date_list[0], 
            month_num_to_string(date_list[1]), date_list[2])

def dates_to_strings(list_of_date_lists):
    dates = []
    for date in list_of_date_lists:
        dates.append(date_to_string(date))
    
    return dates

def date_to_string_no_year(date_list):
    return "{0} {1}".format(month_num_to_string(date_list[0]), date_list[1])

def dates_to_strings_no_year(list_of_date_lists):
    dates = []
    for date in list_of_date_lists:
        dates.append(date_to_string_no_year(date))
    
    return dates

def remove_years(list_of_date_lists):
    new_date_list = []
    for date in list_of_date_lists:
        new_date_list.append(date[1:])
    
    return new_date_list

def is_leap_year(year):
    if(year % 4 == 0 and not year % 100 == 0): return True
    elif(year % 4 == 0 and year % 100 == 0 and year % 400 == 0): return True
    else: return False

def get_num_days_in_month(month_num, year):
    if(not is_valid_month_num(month_num)): return None
    
    day_count = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if(month_num != 2):
        return day_count[month_num - 1]
    elif(is_leap_year(year)): return 29
    else: return day_count[2]

def generate_date(start_year, end_year):
    year = random.randint(start_year, end_year)
    month = random.randint(1, 12)
    day = random.randint(1, get_num_days_in_month(month, year))

    return [year, month, day]