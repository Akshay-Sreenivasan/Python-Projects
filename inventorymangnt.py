class inventory:
    def __init__(self):
        self.items=[]
        self.quantity=[]

    def add_item(self):
        item=input("Enter item Name:")
        self.items.append(item)
        print("\n item added to Inventory Successfully")

    def add_quantity(self):
        item=input("Enter item Quantity:")
        self.quantity.append(item)
        print("\n item Quantity added to Inventory Successfully")

    def show_items(self):
        print("\n Items in Inventory: ")
        for item in self.items:
            print(item)
    
    def show_quantity(self):
        for item,qty in zip(self.items,self.quantity):
            print(f"\n Item name: {item} & It\'s Quantity is :{qty}")

        # for item in self.items:
        #     print("\n Item Name:",item)
        # for qty in self.quantity:
        #     print("\n Inventory item Quantity: ",qty)


    def sale_item(self):
        item=input("Enter the Needed item :")
        qty=int(input("Enter the Quantity of item:"))
        if item in self.items:
            index=self.items.index(item)
            if qty <=int(self.quantity[index]):
                self.quantity[index]=str(int(self.quantity[index])-qty)
                print("\n Item Sold Successfully")
            else:
                print("\n Not enough Quantity avilable")
        else:
            print("\n Item not found in inventory")
            



Inventory = inventory()
while True:
    print("\n===== Store Inventory =====")
    print("1. Add Item")
    print("2. Add Quantity")
    print("3. Show Items")
    print("4. Show Quantity")
    print("5. Sale")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        Inventory.add_item()
    elif choice == 2:
        Inventory.add_quantity()
    elif choice == 3:
        Inventory.show_items()
    elif choice == 4:
        Inventory.show_quantity()
    elif choice == 5:
        Inventory.sale_item()
    elif choice == 6:
        print("Thank you")
        break
    else:
        print("Invalid choice")