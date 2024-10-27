#cafe managment 
menu = {
    "pizzza": 50,
    "pasta":40,
    "burger":70,
    "coffee":80
}
print("welcome to Cafe\n ")
print("pizzza: 50\n pasta:40 \n burger:70 \n coffee:80 ")

total_order= 0   # first order prize 

order1= input("enter the name of item you want to order = ")

if order1 in menu :
    total_order += menu [order1] # here, item add in total order.
    print("your item ", order1 , "has been added to your order")
    
else :
    print(order1,"is not avaialable yet")
    
other_order = input("Do you want to add another item ( Yes / No) ")

if other_order == "Yes":
    order2 = input("Enter the name of second item =")
    if order2 in menu :
        total_order += menu[order2]
        print("your order has been save")
    else:
        print(order2,"is not avaialable yet")
        
print("The total amount of item is ",total_order)
