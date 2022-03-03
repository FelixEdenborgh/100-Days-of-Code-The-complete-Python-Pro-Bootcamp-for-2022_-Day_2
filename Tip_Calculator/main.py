print("Welcome to the tip Calculator.")

Total_Bil = input("Whats the total bill? \n")
How_Many_People_Are_Spliting = input("How many people are spliting the bill? \n")

Precentage_To_Tip = input("What tip would you like to give: 10, 12 or 15 \n")

Sum_Of_Price = float(Total_Bil) / float(How_Many_People_Are_Spliting)

if(Precentage_To_Tip == "10"):
    print("Each person should pay: ", Sum_Of_Price * 1.10)

elif(Precentage_To_Tip == "12"):
    print("Each person should pay: ", Sum_Of_Price * 1.12)

else:
    ("Each person should pay: ", Sum_Of_Price * 1.15)

