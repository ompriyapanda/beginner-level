# # 1.Variables

# In[4]:


#Task 1
pi = 22 / 7
print("Value of pi:", pi)
print("Data type of pi:", type(pi))

#Task 2
#Uncommenting the following lines will cause a SyntaxError because for is a reserved keyword in Python which can't be used to as a variable.
#for = 4
#print(for)

#Task 3
P=int(input("Enter the principle amount:"))
T=int(input("Enter the time period:"))
R=int(input("Enter the rate of interest:"))
simple_interest = (P * T * R) / 100
print("Simple Interest: ", simple_interest)


# # 3.List

# In[4]:


# Initial list
justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]
print("Initial Justice League:", justice_league)

# 1. Calculate the number of members in the Justice League
num_members = len(justice_league)
print("Number of members in the Justice League:", num_members)

# 2. Add Batgirl and Nightwing to the list
justice_league.append("Batgirl")
justice_league.append("Nightwing")
print("After adding Batgirl and Nightwing:", justice_league)

# 3. Move Wonder Woman to the beginning of the list
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("After making Wonder Woman the leader:", justice_league)

# 4. Separate Aquaman and Flash with Superman
justice_league.remove("Superman")
aquaman_index = justice_league.index("Aquaman")
justice_league.insert(aquaman_index + 1, "Superman")
print("After separating Aquaman and Flash with Superman:", justice_league)

# 5. Replace with new members
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("After replacing with new members:", justice_league)

# 6. Sort the Justice League alphabetically
justice_league.sort()
print("Sorted Justice League:", justice_league)
print("New leader of the Justice League:", justice_league[0])


# # 4.If Condition

# In[6]:


#Task 1:
def calculate_bmi(weight, height):
    return weight / (height ** 2)

def determine_bmi_category(bmi):
    if bmi >= 30:
        return "Obesity"
    elif 25 <= bmi < 30:
        return "Overweight"
    elif 18.5 <= bmi < 25:
        return "Normal"
    else:
        return "Underweight"

def get_user_input():
    while True:
        try:
            height = float(input("Enter height in meters: "))
            if height <= 0:
                raise ValueError("Height must be greater than 0.")
            weight = float(input("Enter weight in kilograms: "))
            if weight <= 0:
                raise ValueError("Weight must be greater than 0.")
            return height, weight
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")

def main():
    print("Welcome to the BMI Calculator!")
    height, weight = get_user_input()
    bmi = calculate_bmi(weight, height)
    category = determine_bmi_category(bmi)
    print(f"Your BMI is: {bmi:.2f}")
    print(f"BMI Category: {category}")

if __name__ == "__main__":
    main()


# In[8]:


#Task 2:
def get_country_by_city(city):
    city_to_country = {
        "Sydney": "Australia",
        "Melbourne": "Australia",
        "Brisbane": "Australia",
        "Perth": "Australia",
        "Dubai": "UAE",
        "Abu Dhabi": "UAE",
        "Sharjah": "UAE",
        "Ajman": "UAE",
        "Mumbai": "India",
        "Bangalore": "India",
        "Chennai": "India",
        "Delhi": "India"
    }

    normalized_city = city.strip().title()
    country = city_to_country.get(normalized_city)
    return country

def main():
    city = input("Enter a city name: ")
    country = get_country_by_city(city)
    
    if country:
        print(f"{city} is in {country}")
    else:
        print(f"Sorry, the city {city} is not in the list.")

if __name__ == "__main__":
    main()


# In[9]:


#Task 3:
def get_country_by_city(city):
    city_to_country = {
        "Sydney": "Australia",
        "Melbourne": "Australia",
        "Brisbane": "Australia",
        "Perth": "Australia",
        "Dubai": "UAE",
        "Abu Dhabi": "UAE",
        "Sharjah": "UAE",
        "Ajman": "UAE",
        "Mumbai": "India",
        "Bangalore": "India",
        "Chennai": "India",
        "Delhi": "India"
    }

    normalized_city = city.strip().title()
    return city_to_country.get(normalized_city)

def main():
    city1 = input("Enter the first city: ")
    city2 = input("Enter the second city: ")

    country1 = get_country_by_city(city1)
    country2 = get_country_by_city(city2)

    if country1 and country2:
        if country1 == country2:
            print(f"Both cities are in {country1}")
        else:
            print("They don't belong to the same country")
    else:
        if not country1:
            print(f"Sorry, the city {city1} is not in the list.")
        if not country2:
            print(f"Sorry, the city {city2} is not in the list.")

if __name__ == "__main__":
    main()


# # 9.Inheritence

# In[10]:


class MobilePhone:
    def __init__(self, screen_type, network_type, dual_sim, front_camera, rear_camera, ram, storage):
        self.screen_type = screen_type
        self.network_type = network_type
        self.dual_sim = dual_sim
        self.front_camera = front_camera
        self.rear_camera = rear_camera
        self.ram = ram
        self.storage = storage
    
    def make_call(self, number):
        print(f"Making a call to {number} using {self.__class__.__name__}.")
    
    def receive_call(self, number):
        print(f"Receiving a call from {number} on {self.__class__.__name__}.")
    
    def take_a_picture(self):
        print(f"Taking a picture with the {self.rear_camera} rear camera on {self.__class__.__name__}.")

class Apple(MobilePhone):
    def __init__(self, model, screen_type="Touch Screen", network_type="5G", dual_sim=False, front_camera="12MP", rear_camera="12MP", ram="4GB", storage="64GB"):
        super().__init__(screen_type, network_type, dual_sim, front_camera, rear_camera, ram, storage)
        self.model = model
    
    def make_call(self, number):
        print(f"Making a FaceTime call to {number} using {self.model}.")

class Samsung(MobilePhone):
    def __init__(self, model, screen_type="Touch Screen", network_type="5G", dual_sim=True, front_camera="16MP", rear_camera="32MP", ram="4GB", storage="64GB"):
        super().__init__(screen_type, network_type, dual_sim, front_camera, rear_camera, ram, storage)
        self.model = model
    
    def make_call(self, number):
        print(f"Making a call to {number} using {self.model} with Samsung Dialer.")

# Creating objects of Apple class with different properties
iphone_12 = Apple(model="iPhone 12", network_type="5G", dual_sim=True, front_camera="12MP", rear_camera="12MP", ram="4GB", storage="64GB")
iphone_se = Apple(model="iPhone SE", network_type="4G", dual_sim=False, front_camera="7MP", rear_camera="12MP", ram="3GB", storage="64GB")

# Creating objects of Samsung class with different properties
samsung_galaxy_s21 = Samsung(model="Galaxy S21", network_type="5G", dual_sim=True, front_camera="10MP", rear_camera="64MP", ram="8GB", storage="128GB")
samsung_galaxy_a52 = Samsung(model="Galaxy A52", network_type="4G", dual_sim=True, front_camera="32MP", rear_camera="64MP", ram="6GB", storage="128GB")

# Testing functionality
iphone_12.make_call("123-456-7890")
iphone_12.receive_call("987-654-3210")
iphone_12.take_a_picture()

iphone_se.make_call("123-456-7890")
iphone_se.receive_call("987-654-3210")
iphone_se.take_a_picture()

samsung_galaxy_s21.make_call("123-456-7890")
samsung_galaxy_s21.receive_call("987-654-3210")
samsung_galaxy_s21.take_a_picture()

samsung_galaxy_a52.make_call("123-456-7890")
samsung_galaxy_a52.receive_call("987-654-3210")
samsung_galaxy_a52.take_a_picture()


# # 6.Dictionary

# In[2]:


#Task 1 : Create a list of your friends' names. The list should have at least 5 names.Create a list of tuples. Each tuple should contain a friend's name and the lengthof the name.
friends = ["Purab", "Sirsaa", "Anindita", "Lucky", "Lusi"]
lengths = [(name, len(name)) for name in friends]
print("Friends' names and their lengths:", lengths)


# In[5]:


#Task 2 :Calculate the total expenses for each of you and print the results. Determine who spent more money overall and print the result. 
your_expenses = {
    "Hotel": 1300,
    "Food": 500,
    "Transportation": 500,
    "Attractions": 600,
    "Miscellaneous": 300
}
partner_expenses = {
    "Hotel": 1300,
    "Food": 600,
    "Transportation": 500,
    "Attractions": 600,
    "Miscellaneous": 400
}
your_total_expenses = sum(your_expenses.values())
partner_total_expenses = sum(partner_expenses.values())
print("Your total expenses:", your_total_expenses)
print("Your partner's total expenses:", partner_total_expenses)
if your_total_expenses > partner_total_expenses:
    print("You spent more money overall.")
elif your_total_expenses < partner_total_expenses:
    print("Your partner spent more money overall.")
else:
    print("Both of you spent the same amount of money.")
significant_difference_category = None
significant_difference_amount = 0
for category in your_expenses:
    difference = abs(your_expenses[category] - partner_expenses[category])
    if difference > significant_difference_amount:
        significant_difference_amount = difference
        significant_difference_category = category
if significant_difference_category:
    print("The category with the significant difference in spending is",significant_difference_category,"with a difference of",significant_difference_amount)
else:
    print("There is no significant difference in any category.")
