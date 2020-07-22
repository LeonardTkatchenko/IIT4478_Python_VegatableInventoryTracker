import pickle

def main():
    vegetables = loadData()
    while True:
        displayMenu()
        choice = getMenuChoice()
        if choice == 1:
            listVegetables(vegetables)
        elif choice == 2:
            vegetables = addVegetable(vegetables)
        elif choice == 3:
            vegetables = modifyVegetable(vegetables)
        elif choice == 4:
            vegetables = deleteVegetable(vegetables)
        elif choice == 0:
            print("Exiting Program!")
            storeData(vegetables)
            print("Storage File Updated!")
            break
        else:
            print("Something Went Wrong!")
            break          
  
def storeData(vegetables): 
    # database 
    db = {'vegetablesDB':vegetables}  
    dbfile = open('vegetablePickleFile', 'wb') 
    pickle.dump(db, dbfile)
    dbfile.close()
  
def loadData(): 
    # for reading also binary mode is important
    try:
        dbfile = open('vegetablePickleFile', 'rb')      
        db = pickle.load(dbfile) 
        for keys in db: 
            print(keys, '=>', db[keys])

        vegetables = db["vegetablesDB"]
        print("Pickle File Retrieved!\n")
        dbfile.close()
        return vegetables
        
    except FileNotFoundError:
        print("No Pickle File Found! Starting with empty.\n")
        return {}

def displayMenu():
    print("1: List All Vegetables")
    print("2: Add Vegetable")
    print("3: Change Vegetable Price")
    print("4: Remove Vegetable")
    print("0: Exit\n")

def getMenuChoice():
    while True:
        try:
            choice = int(input("Enter Menu Action: "))
            if (choice in [x for x in range(0,5)]):
                print(choice, "Selected!\n")
                return choice
            else:
                raise ValueError
        except ValueError:
            print("Invalid Choice!\n")
                
def listVegetables(vegs):
    print("-Listing Vegetables-")
    print("{0:^20s}|{1:^20s}".format("Vegetable", "Price ($)"))
    print('-'*40)
    for veg in vegs:
       print("{0:^20s}|{1:^20g}".format(veg, vegs[veg]))
    print()
    
def addVegetable(vegs):
    print("-Adding Vegetable-")
    vegetable = input("Enter Vegetable: ")#check for empty string?
    while True:
        try:
            price = int(input("Enter Vegetable Price: "))
            if (price < 0):
                raise ValueError
            else:
                if vegetable in vegs:
                    print("Vegetable already exists! Price updated!\n")
                else:
                    print("Vegetable Added!\n")
                vegs[vegetable] = price
                return vegs
        except ValueError:
            print("Invalid Price!\n")
        
def modifyVegetable(vegs):
    print("-Modifying Vegetable Price-")
    while True:
        vegetable = input("Enter Vegetable: ")#check for empty string?
        if vegetable == "exit":
            return vegs
        elif vegetable not in vegs:
            print("Vegatable does not exist and must be added first!")
            print("Enter 'exit' to go back to menu\n")
        else:
            break
    while True:
        try:
            price = int(input("Enter New Price: "))
            if (price < 0):
                raise ValueError
            else:
                vegs[vegetable] = price
                print("Vegetable Price Modified!\n")
                return vegs
        except ValueError:
            print("Invalid Price!\n")
            
def deleteVegetable(vegs):
    print("-Deleting Vegetable")
    while True:
        vegetable = input("Enter Vegetable: ")#check for empty string?
        if vegetable == "exit":
            return vegs
        elif vegetable not in vegs:
            print("Cannot delete vegetable that does not exist!")
            print("Enter 'exit' to go back to menu\n")
        else:
            del vegs[vegetable]
            print("Vegetable: '{}' removed!\n".format(vegetable))
            return vegs

if __name__ == '__main__': 
    main()
