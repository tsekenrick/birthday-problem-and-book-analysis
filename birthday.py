# birthday.py
import mydate

def list_difference(first, second):
    second = set(second)
    return [date for date in first if date not in second]

def main():
    run_count = input("How many times should I run the simulation? ")
    bday_count = input("How many birthdays should I generate per trial? ")
    
    for i in range(int(run_count)):
        
        bdays = []
        for j in range(int(bday_count)):
             bdays.append(mydate.generate_date(1997, 2017))
             mydate.remove_years(bdays)!
        # bdays = [[10,1], [10,1], [3,31], [10,1], [3,31], [2, 21], [1, 5]]
        bdays = mydate.dates_to_strings_no_year(bdays)
        unique_dates = set(bdays) # removes repeats from bdays
        
        repeat_day_list = []
        # loop compares bdays to unique_dates to create a list of 
        # the dates of same-day birthdays
        for days in unique_dates:
            if(bdays.count(days) > 1): repeat_day_list.append(days)            
        repeat_count = len(repeat_day_list)
        
        print("Trial #{}: {} dates occur more than once! {}".format(i + 1, 
              repeat_count, repeat_day_list))
    
    
if __name__ == "__main__":
    main()