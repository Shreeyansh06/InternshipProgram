userName_predefined = "ShreeyanshJagdale"
Password_predefined = "Shreerj1706"
account_active = True

userName = input("Enter the Username: ")
password = input("Enter the Password: ")

if(userName == userName_predefined and password == Password_predefined ):
    print("Access Granted ")

elif(userName == userName_predefined and password == Password_predefined and not account_active ):
    print("Accounnt is  disabled " )

else:
    print("Username or Password is incorrect" )