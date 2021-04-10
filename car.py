import datetime as dt
import days

class Car:
    def __init__(self, license_plate, date, time): #Car attributes
        self.license_plate = license_plate
        self.date = date
        self.time = time
    
    def on_the_road(self):#Method 'on_the_road'
        time_format = dt.datetime.strptime('{0}'.format(self.time), '%H:%M') #Parse the input time to the format 'H:M'
        if (time_format.time() >= dt.time(7,0) and time_format.time() <= dt.time(9, 30)): #Pico y placa in the morning
            if (self.day_license() == True):#Invocation of the 'day_license' method 
                return True
            else:
                return False   
        elif (time_format.time() >= dt.time(16,0) and time_format.time() <= dt.time(19, 30)): #Pico y placa in the afternoon
            if (self.day_license() == True): #Invocation of the 'day_license' method
                return True
            else:
                return False
        else:
            return False
    
    def day_license(self): #Method 'day_license'
        last_digit = int(self.license_plate.strip()[-1]) #Get the last digit of the plate
        day_to_consult = days.day(self.date) #Invocation of the 'day' method from 'days' to return the string day of the date
        if (day_to_consult == 'Monday' and last_digit == 1 or last_digit == 2 )\
        or (day_to_consult == 'Tuesday' and last_digit == 3 or last_digit == 4)\
        or (day_to_consult == 'Wednesday' and last_digit == 5 or last_digit == 6)\
        or (day_to_consult == 'Thursday' and last_digit == 7 or last_digit == 8)\
        or (day_to_consult == 'Friday' and last_digit == 9 or last_digit == 0): #If statements of the last digit and the different days
            return True
        else:
            return False
