# birthday.py
import mydate

def main():
    runCount = input("How many times should I run the simulation? ")
    bdayCount = input("How many birthdays should I generate per trial? ")
    print(mydate.date_to_string([1979, 10, 7]))
    
if __name__ == "__main__":
    main()