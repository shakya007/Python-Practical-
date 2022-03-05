# python application 5

print("THE NEWS PAPER DISTRIBUTION SYSTEM")

# student name
Delivery_Boy1 = input("Enter Delivery Boy Name 1 : ")
Delivery_Boy2 = input("Enter Delivery Boy Name 2 : ")

# Total paper
paper_1 = int(input("Enter Divy Bhaskar : "))
paper_2 = int(input("Enter Sandesh Paper : "))
paper_3 = int(input("Enter Economics Paper : "))
paper_4 = int(input("Enter Times of India : "))
paper_5 = int(input("Enter Sanj Samachar : "))
paper_6 = int(input("Enter Jansatta : "))

# give paper to boy 1
Boy1_Divyabhasker = int(input("Enter Quantity of divyabhasker to boy1 : "))
Boy1_Sandesh = int(input("Enter Quantity of Sandesh to boy 1 : "))
Boy1_Economics = int(input(" Enter Quantity Economics to boy 1 : "))
Boy1_Timesofindia = int(input(" Enter Quantity Times of india to boy 1 : "))
Boy1_Sanjsamachar = int(input(" Enter Qantity of Sanjsamachar to boy 1: "))
Boy1_Jansatta = int(input(" Enter Quantity of Jansatta to boy 1 : "))

# boy 1 sell all paper
totalpaper_1 = Boy1_Economics + Boy1_Jansatta + Boy1_Sanjsamachar + Boy1_Sandesh + Boy1_Timesofindia + Boy1_Jansatta

# give paper to boy 2
Boy2_Divyabhasker = int(input("Enter Quantity of divyabhasker to boy 2 : "))
Boy2_Sandesh = int(input("Enter Quantity of Sandesh to boy 2 : "))
Boy2_Economics = int(input(" Enter Quantity Economics to boy 2 : "))
Boy2_Timesofindia = int(input(" Enter Quantity Times of india to boy 2 : "))
Boy2_Sanjsamachar = int(input(" Enter Qantity of Sanjsamachar to boy 2 : "))
Boy2_Jansatta = int(input(" Enter Quantity of Jansatta to boy 2 : "))

# boy 2 sell paper
totalpaper_2 = Boy2_Jansatta + Boy2_Sanjsamachar + Boy2_Sandesh + Boy2_Timesofindia + Boy2_Economics + Boy2_Divyabhasker

# total remaining paper for boy 1
remainingpaper_1 = int(input("enter remaining paper for boy 1 : "))
remainingpaper_2 = int(input("enter remaining paper for boy 1 : "))
remainingpaper_3 = int(input("enter remaining paper for boy1 : "))
remainingpaper_4 = int(input("enter remaining paper for boy 1 : "))
remainingpaper_5 = int(input("enter remaining paper for boy 1 : "))
remainingpaper_6 = int(input("enter remaining paper for boy 1 : "))
# boy1 total remaining paper
totalremainingpaper_boy_1 = remainingpaper_6 + remainingpaper_5 + remainingpaper_4 + remainingpaper_3 + remainingpaper_2 + remainingpaper_1

# total remaining paper for boy 2
remainingpaper_1 = int(input("enter remaining paper for boy 2 : "))
remainingpaper_2 = int(input("enter remaining paper for boy 2 : "))
remainingpaper_3 = int(input("enter remaining paper for boy2 : "))
remainingpaper_4 = int(input("enter remaining paper for boy 2 : "))
remainingpaper_5 = int(input("enter remaining paper for boy 2 : "))
remainingpaper_6 = int(input("enter remaining paper for boy 2 : "))

# boy2 remaining all paper
totalremainingpaper_boy_2 = remainingpaper_6 + remainingpaper_5 + remainingpaper_4 + remainingpaper_3 + remainingpaper_2 + remainingpaper_1

totalsale_boy_1 = totalpaper_1 - totalremainingpaper_boy_1
totalsale_boy_2 = totalpaper_2 - totalremainingpaper_boy_2

# boy1 and boy2 salary
salary1 = 10000
salary2 = 10000

# boy1 and boy2 commision
commision1 = (totalsale_boy_1 * 10 * 0.02)
commision2 = (totalsale_boy_2 * 10 * 0.02)

# total salary boy1 and boy2
totalsalary1 = commision1 + salary1
totalsalary2 = commision1 + salary2

print(totalsalary1)
print(totalsalary1)
