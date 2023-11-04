import time
Number_in_seconds=input('Enter a number in seconds= ')
Number_in_minutes= input("Enter how many minutes= ")
z = int(Number_in_minutes) * 60
countdown_number = int(z) + int(Number_in_seconds)
while int(countdown_number) > 0:
   countdown_number=int(countdown_number) - 1
   print(countdown_number)
   time.sleep(1)
else:
    print('Blast off!')