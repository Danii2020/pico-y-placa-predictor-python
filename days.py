import datetime as dt

def day(date):
    try:
        date_format = dt.datetime.strptime(date, '%d/%m/%Y') #Parse the string date to a date object
        string_date = date_format.strftime("%A") #Parse the date object to a string in the day
    except ValueError:
        print("Please, enter the correct date format!")
                
    return string_date #Return the string day
