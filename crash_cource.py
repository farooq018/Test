def greet_user(username):
    '''Display a greeting'''
    print(f"Hello {username},Good Morning")

# print(greet_user.__doc__)
# greet_user("Farooq")

def display_message():
    '''Display about function of this chapter'''
    print("With the help of this chapter we will learned about defining function and how to use of this to perform perticular task")

# display_message()

def favorite_book(title):
    print(f"One of my favorite book is {title} in Wonderland.")

# favorite_book("Alice")

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name}.")


# describe_pet('hamster', 'harry')

def make_shirt(size ,text):
    print(f"Dear Customer,The size of the T-Shirt is {size} and on the front side you will able to see {text}.\n")
#
# make_shirt("XL","ROGER")  #by using positional Argument.
#
# make_shirt(size="M",text="BEING HUMAN") #By using Keyword Argument.

# make_shirt('I love Python')

def make_shirt(text,size="L"):
    print(f"Dear Customer,The size of the T-Shirt is {size} and on the front side you will able to see {text}.\n")
#
# make_shirt(text="I Love Python")  #By Using Default Values(of Size).

def make_shirt(size,text="I Love Python"):
    print(f"Dear Customer,The size of the T-Shirt is {size} and on the front side you will able to see {text}.\n")

# make_shirt("L & M") # By using Default Values (of Text).

def make_shirt(size,*text):
    print(f"Dear Customer,The size of the T-Shirt is {size} and on the front side you will able to see {text}.\n")

# make_shirt("Any Size","I Love Python","Being Human","Python Developer")

'''By using Return Statement'''
def build_person(first_name,last_name):
    information=(f"{first_name} {last_name}")
    return information


# print(build_person("Farooq","Hussain"))
result=build_person("Farooq","Hussain")
# print(result)

'''return Dictionary'''

def buid_person(first_name,age,role):
    info={'Name':first_name,'age':age,'designation':role}
    return info

result=buid_person("Farooq",26,"Odoo Developer")
# print(result)
# print(type(result))

def my_data(name,age,role):
    myinfo={'Name':name,'age':age,'designation':role}
    if role:
        myinfo['designation']="Odoo Developer"
    return myinfo

# result=my_data("Farooq",26,"Developer")
# print(result)


def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person
# musician = build_person('jimi', 'hendrix',27)
# print(musician)

