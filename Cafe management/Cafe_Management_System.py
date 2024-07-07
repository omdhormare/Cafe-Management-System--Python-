print("\n---------------------------------------------------------------------------\n")
print("  \n......          Welcome To OM Cafe            ......\n")
print("\n---------------------------------------------------------------------------\n")

menu={
    'masala chai': 100,
    'filter coffee': 200,
    'green tea': 500,
    'lassi': 600,
    'sandwiches': 50,
    'burgers': 80,
    'samosa': 90,
    'paneer butter masala': 30,
    'chole bhature': 45,
    'jalebi': 20,
    'kheer': 50,
    'chocolate cake': 45,
    'cheesecake': 65,
    'ice cream': 80,
}

for item in menu:
    print(item.capitalize(), ':', menu[item])

total = 0
print("\n------------------------------------------------------------------\n")

order = input("Enter Your Order Name: ").strip().lower()  
if order in menu:
    total += menu[order]
    print("Your Item Is Added...")
else:
    print("Your Order Is Not Found In Menu...")

print("\n------------------------------------------------------------------\n")

order1 = input("Do You Want Another Item? (Yes/No): ").strip().lower() 
if order1 == "yes":
    n = input("Enter The Second Item Name: ").strip().lower() 
    if n in menu:
        total += menu[n]
        print("Item Added To Order...")
    else:
        print("Item Not Found...")
        
print("\n------------------------------------------------------------------\n")
        
print("The Total Amount Of Items: ", total)
