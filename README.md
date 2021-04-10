# Description
The pico y placa predictor is a small program written in Python that "predicts" whether a car will be able to circulate on the streets within a user-specified date and time. This taken of the following measures imposed by the ATM (Agencia Nacional de Tránsito del Ecuador):

Vehicles with plates 1 and 2 will not be able to circulate on Mondays, vehicles with plates 3 and 4 will not be able to circulate on Tuesdays, vehicles with plates 5 and 6 will not be able to circulate on Wednesdays, those with plates 7 and 8 on Thursdays and those with plates 9 and 0 will not be allowed on Fridays, from 07:00 am to 09:30 am and from 16:00 am to 19:30 pm.

# Observations
The Car class inside car.py, has all the logical methods of the program. The class is composed by three attributes (license_plate, date and time), and depending of the inputs from the main.py, a specific output is presented. Also in days.py, are the methods to convert the date input from string to date object and then get the day in string.

# Program execution
The program starts with the main.py file, using the command ***py main.py***

![image](https://user-images.githubusercontent.com/69876673/114285830-b1a55c00-9a1f-11eb-8962-18668ecccbe5.png)

First the user has to enter the license plate of his car, like this:

![image](https://user-images.githubusercontent.com/69876673/114285859-f16c4380-9a1f-11eb-87a4-483ba3dd8441.png)

The, the user has to enter the date that he wants to know if his car can be on the road, in the format day/month/year:

![image](https://user-images.githubusercontent.com/69876673/114285904-4c9e3600-9a20-11eb-9642-03733470bc1e.png)

Finally, the user has to enter the time that he wants to know if his car can be on the road, in the format hours:minutes 24 hours:

![image](https://user-images.githubusercontent.com/69876673/114285925-853e0f80-9a20-11eb-89ee-9114e848f8ad.png)

And the user could know if his car can be on the road or can not:

![image](https://user-images.githubusercontent.com/69876673/114285952-a56dce80-9a20-11eb-8f66-a0a16a206f26.png)
