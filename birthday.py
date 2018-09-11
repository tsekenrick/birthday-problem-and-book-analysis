# birthday.py
import mydate

def list_difference(first, second):
    second = set(second)
    return [date for date in first if date not in second]

def main():

    run_count = input("How many times should I run the simulation?\n")
    bday_count = input("How many birthdays should I generate per trial?\n")
    
    trials_with_rpt = 0
    for i in range(int(run_count)):
        
        bdays = []
        if len(bdays) != 0: bdays.clear() 
        
        for j in range(int(bday_count)):
             bdays.append(mydate.generate_date(1997, 2017))
        
        bdays = mydate.remove_years(bdays)
             
        # bdays = [[10,1], [10,1], [3,31], [10,1], [3,31], [2, 21], [1, 5]]
        bdays = mydate.dates_to_strings_no_year(bdays)
        unique_dates = set(bdays) # removes repeats from bdays
        
        repeat_day_list = []
        if len(repeat_day_list) != 0: repeat_day_list.clear()
        # loop compares bdays to unique_dates to create a list of 
        # the dates of same-day birthdays
        for days in unique_dates:
            if(bdays.count(days) > 1): repeat_day_list.append(days)            
        repeat_count = len(repeat_day_list)
        
        repeat_day_str = ', '.join(map(str, repeat_day_list))
        
        if (repeat_count > 1):
            print("Trial #{}: {} dates occur more than once! ({})".format(i + 1, 
              repeat_count, repeat_day_str))
    
            trials_with_rpt += 1
        elif (repeat_count == 1):
            print("Trial #{}: {} date occurs more than once! ({})".format(i + 1, 
              repeat_count, repeat_day_str))
            
            trials_with_rpt += 1
        else: print("Trial #{}: No dates are the same.".format(i + 1))
    
    rpt_prob = (trials_with_rpt/int(run_count)) * 100
    
    print("\nResults:\n=====")
    print("Out of {} trials, {} had dates that were repeated.".format(
            int(run_count), trials_with_rpt))
    print("""We can conclude that you have a {:.2f}% chance of sharing a 
birthday with someone if you are in a group of {} people""".format(
          rpt_prob, int(bday_count)))
    
    
if __name__ == "__main__":
    main()