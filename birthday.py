# birthday.py
import mydate

def main():
    runCount = input("How many times should I run the simulation? ")
    bdayCount = input("How many birthdays should I generate per trial? ")
    print(mydate.date_to_string([1979, 10, 7]))
    for year in [1988, 1992, 1996, 1600, 2000, 2400]:
        print(mydate.is_leap_year(year)) # True for each one!

    for year in [1700, 1800, 1900, 2100, 2200, 2300, 2500, 2600]:
        print(mydate.is_leap_year(year)) # False for each one!
    
if __name__ == "__main__":
    main()