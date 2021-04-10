from car import Car as C
import days


def main():
    print("""Welcome to the Pico y Placa Predictor!\n
Check when your car can be on the road and 
take the necessary measures
    """)
    license_plate = input("Enter your license plate: ") #User license plate input
    date = input("Enter the date in day/month/year: ") #Date input
    time = input("Enter the time in hour:minutes (24H):  ") #Time input
    day_to_consult = days.day(date) 
    c = C(license_plate, date, time)
    if (c.on_the_road() != False): #Invocation of the 'on_the_road' method
        print(f"The {day_to_consult}, your car can not be on the road at {time} hours!") 
    else:
        print(f"The {day_to_consult}, your car can be on the road at {time} hours!")

if __name__ == '__main__':
    main()