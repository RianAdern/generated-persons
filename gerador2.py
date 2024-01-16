import random
import pandas as pd


def assign_eye_color():
    # Estimated percentage ranges for different eye colors
    eye_color_distribution = {'Brown': 80,'Blue': 10,'Green': 8,'Hazel': 5,'Gray': 1,'Amber': 1,'Violet': 0.1}

    # Generate a random number to determine the eye color
    random_number = random.uniform(0, 100)
    cumulative_percentage = 0

    for color, percentage in eye_color_distribution.items():
        cumulative_percentage += percentage
        if random_number <= cumulative_percentage:
            return color

def assign_body_type():
    # Estimated percentage distribution for different body types
    body_type_distribution = {'Slim': 20,'Average': 50,'Athletic': 20,'Curvy': 15,'Chubby': 10}

    # Generate a random number to determine the body type
    random_number = random.uniform(0, 100)
    cumulative_percentage = 0

    for body_type, percentage in body_type_distribution.items():
        cumulative_percentage += percentage
        if random_number <= cumulative_percentage:
            return body_type

def assign_height():
    # Estimated percentage distribution for different height categories
    height_distribution = {
        'Very Short': {'percentage': 5, 'height_range': (130, 159)},
        'Short': {'percentage': 20, 'height_range': (160, 165)},
        'Average Height': {'percentage': 40, 'height_range': (166, 175)},
        'Tall': {'percentage': 25, 'height_range': (176, 185)},
        'Very Tall': {'percentage': 10, 'height_range': (186, 220)}
    }

    # Generate a random number to determine the height category
    random_number = random.uniform(0, 100)
    cumulative_percentage = 0

    for category, data in height_distribution.items():
        cumulative_percentage += data['percentage']
        if random_number <= cumulative_percentage:
            return category, data['height_range']




def generate_person_list():
    women_first_names = ["Alice", "Bobbi", "Catherine", "Diana", "Emily", "Fiona", "Grace", "Haley", "Ivy", "Julia",
                         "Kelly", "Linda", "Megan", "Natalie", "Olivia", "Pamela", "Quinn", "Rachel", "Samantha", "Tracy",
                         "Ursula", "Victoria", "Wendy", "Xena", "Yvonne"]
    women_last_names = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor"]

    men_first_names = ["Adam", "Brian", "Charlie", "David", "Ethan", "Frank", "George", "Henry", "Ian", "James",
                       "Kevin", "Liam", "Michael", "Nathan", "Oscar", "Patrick", "Quentin", "Robert", "Samuel", "Tom",
                       "Ulysses", "Victor", "William", "Xavier", "Yuri"]
    men_last_names = ["Anderson", "Clark", "Hall", "Lee", "Martin", "Allen", "Young", "Lewis", "Baker", "Turner"]

    
    skin_colors = ["Fair", "Medium", "Brown", "Pale", "Asian", "Black"]
    hair_lengths = ["Short", "Long"]
    hair_colors = ["Black", "Brown", "Blonde", "Red"]

    # Define possible features for each person
    features = {
        'height': ['Tall', 'Average Tall', 'Short'],
        'body_type': assign_body_type(),
        'eye_color': assign_eye_color(),
        'age': list(range(20, 31)),
        'skin_color': skin_colors,
        'hair_length': hair_lengths,
        'hair_color': hair_colors
    }

    # Shuffle and generate names for each person
    random.shuffle(women_first_names)
    random.shuffle(women_last_names)
    random.shuffle(men_first_names)
    random.shuffle(men_last_names)

    # Generate features for each person
    person_list = []
    for name in women_first_names[:25]:
        person = {
            'gender': 'Female',
            'first_name': name,
            'middle_name': random.choice(women_first_names),
            'last_name': random.choice(women_last_names)
        }
        for feature, options in features.items():
            person[feature] = random.choice(options)
        person_list.append(person)

    for name in men_first_names[:25]:
        person = {
            'gender': 'Male',
            'first_name': name,
            'middle_name': random.choice(men_first_names),
            'last_name': random.choice(men_last_names)
        }
        for feature, options in features.items():
            person[feature] = random.choice(options)
        person_list.append(person)

    return person_list

# Example usage
#generated_list = generate_person_list()

# Export as a list
#for index, person in enumerate(generated_list, start=1):
#    print(f"{index}. {person}")

# Convert the list of dictionaries to a Pandas DataFrame
#df = pd.DataFrame(generated_list)

# Export the DataFrame to an Excel file
#df.to_excel("generated_persons.xlsx", index=False)



# Example usage
for _ in range(20):  # Generate 20 persons for demonstration
    eye_color = assign_eye_color()
    print(f"Eye Color: {eye_color}")
    body_type = assign_body_type()
    print(f"Body Type: {body_type}")
    height_category, height_range = assign_height()
    print(f"Height Category: {height_category}, Height Range: {height_range} cm")


def form_couples(person_list):
    # Separate the persons into male and female lists
    male_list = [person for person in person_list if person['gender'] == 'Male']
    female_list = [person for person in person_list if person['gender'] == 'Female']

    # Shuffle the male and female lists
    random.shuffle(male_list)
    random.shuffle(female_list)

    # Form couples by pairing a male with a female
    couples = []
    for male, female in zip(male_list, female_list):
        couple = {'Male': male, 'Female': female}
        couples.append(couple)

    return couples

# Example usage
#generated_list = generate_person_list()
#couples_list = form_couples(generated_list)

# Convert the list of dictionaries to a Pandas DataFrame
#df_couples = pd.DataFrame(couples_list)

# Export the DataFrame to an Excel file
#df_couples.to_excel("formed_couples.xlsx", index=False)