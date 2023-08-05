PROJECT: AIRLINE PASSENGER LOADING SIMULATION PROGRAM PROJECT
PROGRAMMING LANGUAGE: PYTHON

This program simulates the loading process of 12 passengers unto a Dana airlines flight going  to Abuja. Dana Air has enough planes to carry all passengers but this particular plane gets filled up after assigning 8 more seats. We can therefore safely generate booking IDs for all 12 passengers since there are enough planes. You have been given two files, one a database file (Passengers.db) and the other a text file (Passengers.txt). 12 passengers are to fly with Dana air, 8 of which will be assigned seat numbers. The unoccupied seats are: 10, 24, 33, 15, 18, 45, 26, 30. You are to use any of the files for this project. Write a python program to generate booking ids, as well as assign seat numbers to the passengers.

WHAT YOUR PROGRAM MUST ACCOMPLISH

Your program must be able to do or accomplish the following: 
•	Generate a text file of all booking Ids for the 12 passengers. A booking Id is of the format DAXXINITIALS, where XX is a 2-digit random number, and initials represents the first name and last name initials of each passenger.

•	Assign seats to 8 out of the 12 passengers in this manner:

	i. Prompt passenger to choose a seat number from the available list of seat
	numbers that are yet to be assigned.

	ii. If the choice made has already been assigned, keep prompting for a new
	seat number input by the passenger.

•	Display a "No Seats Available" message to the last 4 passengers when they attempt to book a seat on the plane.
•	Generate a text file (Booked Passengers.txt) of the names, booking IDs, and seat numbers for the 8 passengers who were successful in booking a seat on the plane.

