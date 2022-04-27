
def ordering_meal():
    global meal_number
    meal_number=int(input("enter the meal number you want to order: ")) 
    if meal_number in meal_index:
        entering_quantity()
    else:
        print(f"Invalid meal number {meal_number}, please enter number between 1 and 4 !") 
        ordering_meal() 
def entering_quantity():
    global meal_quantity
    meal_quantity=int(input("Enter meal quantity: "))
    if meal_quantity in range(1,101):
        meal_requested_info()
    else:
        print("Invalid quantity, Please enter quantity between 1 and 90 !")
        entering_quantity()
def meal_requested_info():
    total_amount= round(meal_price[meal_number-1]*meal_quantity,2)
    tax_amount=round(total_amount*.15,2)
    total_cost = round(total_amount+tax_amount,2)
    print("meal#     price     quantity   Subtotal price   Tax     total price","_"*50,f"{meal_number}         {meal_price[meal_number-1]}      {meal_quantity}         {total_amount}            {tax_amount}      {total_cost}",sep="\n")
    print(f"Total bill: {total_cost}")
    asking_for_another()
def asking_for_another():
    ask=input("Would you like to order another meal: [Y/N]").capitalize().strip()
    if ask =="Y":
        ordering_meal()
    elif ask not in ["Y","N"]:
        print("Invalid Input")
        asking_for_another()
print(f"{'_'*90}\n\n{'Zaki Resturant'.center(50)}\n")
print(f"meal#     meal Price     meal description\n".center(50).title())
print("_"*90)
meal_index =[i for i in range(1,5)]
meal_price=[30.00,50.00,70.35,35.00]
meal_description=["Shawirma.","Pizza.","Sea Food.","Grilled Chicken."]
for i in meal_index:
    print(f"    {i}         {meal_price[i-1]}          {meal_description[i-1]}")
print(f"{'_'*90}")  
ordering_meal()

