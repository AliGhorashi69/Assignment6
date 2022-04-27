

f=open("database.txt", "r")
data=f.read()

####################################################################################################################################################################################
from pyfiglet import Figlet
f=Figlet(font="standard")
print(f.renderText("Ali  Store"))
#-------------------------------------------------------------------------------------------------------

Product=[]
Product_list=[]

#####################################################################################################################################################################################

def loading():
    print("")
    print("Loading !!!!!!!")
    print("")
    f=open("database.txt", "r")
    data=f.read()
    Product=data.split("\n")
    for i in range(len(Product)):
            x=Product[i].split(",")
            print(x)
            Info={}
            Info['ID']=x[0]
            Info["type"]=x[1]
            Info["price"]=x[2]
            Info["number"]=x[3]
            Product_list.append(Info)
    return Product_list

#-----------------------------------------------------------------------------------------------------

def show_list():
    for i in range(len(Product_list)):
        print(Product_list[i])

#-----------------------------------------------------------------------------------------------------

def show_menu():
    print("1- Add Product")
    print("2- Edit Product")
    print("3- Delete Product")
    print("4- Search Product")
    print("5- Show List")
    print("6- Buy")
    print("7- Exit")

#-------------------------------------------------------------------------------------------------------
def Add_product():
    while True:
        a={}
        a["ID"]=int(input("Enter ID: "))
        F=0
        while F==0:
                for i in range(len(Product_list)):
                    if  int(Product_list[i]['ID'])== int(a['ID']):
                            F=1
                            print("This Product already exists, Please try again!!! ")
                    
                              
                if F==0:
                    a["type"]=input("Enter type: ")
                    a["price"]=input("Enter price: ")
                    a["number"]=input("Enter number: ")
                    Product_list.append(a)
                F=1
        print("")
        b=int(input("Do you want to add another Product: Enter 1 to add another number, enter 2 to exit: "))
        if b==2:
          break
      
#-----------------------------------------------------------------------------------------------------         

def Edit_Product():
    F=0
    while F==0:
        c=int(input("please enter the ID of Product: "))
        x=0
        for i in range(len(Product_list)):
            if int(Product_list[i]['ID'])==c:
                 x=1
                 Product_list[i]["ID"]=input(" Edit ID: ")
                 Product_list[i]["type"]=input(" Edit type: ")
                 Product_list[i]["price"]=input(" Edit price: ")
                 Product_list[i]["number"]=input(" Edit number: ")
        if x==0:
            print("the ID is not found !!!!")
        F=int(input("Press 0 to continue editing or  press 1 to exit !!: "))

    

        
        
        
            
                
#------------------------------------------------------------------------------------------------------





def search_Product():
    H=0
    F=input("Please enter the name of the product: ")
    for i in range(len(Product_list)):
        if Product_list[i]["type"]==F:
            print("The product is found :D ")
            print("")
            print(Product_list[i])
            print("")
            H=1
    if H==0:
       print("")
       print("The product is not found :( !!!!!")

#-----------------------------------------------------------------------------------------------------

def remove_product():
    choice=input("please enter the  --name(type)-- or --ID-- of the product that you decide to remove: ")
    F=0
    for i in range(len(Product_list)):
        if int(Product_list[i]["ID"])==int(choice) or Product_list[i]["type"]==choice:
            print("the information of product", Product_list[i]," is removed from the list !!!!!")
            Product_list.pop(i)
            F=1
            break
    if F==0:
        print("The product is not found")


def buy_product():
    f=1
    while f==1:
      choice=input("Please enter the ID or name of the product: ") 
      g=1
      for i in range(len(Product_list)) :
            if int(Product_list[i]["ID"])==int(choice) or Product_list[i]["type"]==choice:
               print("The information of this product is", Product_list[i])
               order=int(input("How many of this product (in kg) do you want ?: "))
               g=0
               if order>int(Product_list[i]["number"]):
                   print("This amount of the selected product is not available !!!")
               else:
                   Product_list[i]["number"]=str(int(Product_list[i]["number"])-order)
                   

      if g==1: 
         print("the product is not found in the list !!!")

      f=int(input("Please enter 1 to continoue, or enter 0 to exit"))

        

def save():
    a=len(Product_list)
    x=[None]*a
    h=open("database.txt", 'w')
    h.write("")

    for i in range(a):
        x[i]=Product_list[i]["ID"]+","+Product_list[i]["type"]+","+Product_list[i]["price"]+","+Product_list[i]['number']
    
    h=open("database.txt", 'a')
    h.write(x[0])
    for i in range(1,len(x)):
        
        h.write("\n"+x[i])



           





######################################################################################################################################################################

loading()
show_menu()
choice=int(input("Please choose a number: "))

if choice==1:

    print("")
    Add_product()
    print("")

elif choice==2:
    print("")
    Edit_Product()

elif choice==3:
    remove_product()
elif choice==4:
    search_Product()
elif choice==5:
    show_list()
elif choice==6:
    buy_product()
elif choice==7:
    print("Good Bye !!!")
    save()
    exit()
    
save()





    



