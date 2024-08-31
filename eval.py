contacts = {"shashank":[1234567890, "Shfdh@vjvd.com"]}

def add(contacts):
    name = input("Enter name : ")
    phnum = input("Enter phone number : ")
    email = input("Enter Email : ")
    contacts[name] = [phnum, email]
    
def update(contacts):
    print("1. Update phone numnber : ")
    print ("2.  Update Email address : ")
    nm = input("Enter name to update : ")
    n = input("Choose Option")
    if(n == 1):
        ph = input("Enter new ph. number : ")
        contacts[nm][0] = ph
    elif(n==2):
        email = input("Ente new Email : ")
        contacts[nm][0] = email
    else:
        print("Incorrect input")
        
def delete(contacts):
    nm = input("Enter name to delete : ")
    del(contacts[nm])

def listCon(contacts):
    x = list(contacts)
    print(x)

def searchCon(contacts):
    x = list(contacts)
    n = input("Ente name to get info")
    if(n in x):
        print(contacts[n])
    else:
        print("NO such contacts found")
        
def firstletter(contacts):
    x = list(contacts)
    n = input("Enter letter : ")
    for name in x:
        if(name[0] == n):
            print(name)

print("1. Add contacts")
print("2. Update Contact")
print("3. Delete Contact")
print("4. List all Contact")
print("5. Search Contacts")
print("6. List contact by initials")

n = input("Choose Option : ")
if(n == "1"):
    add(contacts)   
elif(n == "2"):
    update(contacts)
elif(n == "3"):
    delete(contacts)
elif(n == "4"):
    listCon(contacts)
elif(n == "5"):
    searchCon(contacts)
elif(n == "6"):
    firstletter(contacts)
else:
    print("Incorrect input")
   
print(contacts)
