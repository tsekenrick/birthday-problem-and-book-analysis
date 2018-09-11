# mydate.py
def is_valid_month_num(n):
    return n > 0 and n <= 12

def month_num_to_string(month_num):
    month_list = ['January', 'February', 'March', 'April', 'May', 'June',
                  'July', 'August', 'September', 'October', 'November', 'December']
    
    return month_list[month_num - 1]

def date_to_string(date_list):
    return "{1} {2}, {0}".format(date_list[0], month_num_to_string(date_list[1]),
            date_list[2])