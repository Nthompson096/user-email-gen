from flask import Flask, render_template, request
import random, string

app = Flask(__name__)

d = ['cock.li', 'airmail.cc', 'firemail.cc', 'tfwno.gf', 'cock.lu', 'aaathats3as.com', 'national.shitposting.agency', 'cumallover.me']
n = [
    'John', 'Jane', 'Michael', 'Emily', 'David', 'Sarah', 'Robert', 'Emma', 'William', 'Olivia',
    'James', 'Linda', 'Charles', 'Sophia', 'Daniel', 'Chloe', 'Matthew', 'Lily', 'Joseph', 'Grace',
    'Christopher', 'Zoe', 'Anthony', 'Mia', 'Joshua', 'Avery', 'Andrew', 'Ellie', 'Ryan', 'Harper',
    'Nicholas', 'Aria', 'Tyler', 'Amelia', 'Jacob', 'Hannah', 'Benjamin', 'Abigail', 'Elijah', 'Ella',
    'Logan', 'Madison', 'Lucas', 'Scarlett', 'Samuel', 'Riley', 'Henry', 'Victoria', 'Alexander', 'Penelope',
    'Jackson', 'Layla', 'Sebastian', 'Nora', 'Jack', 'Lillian', 'Dylan', 'Brooklyn', 'Aiden', 'Addison',
    'Mason', 'Maya', 'Ethan', 'Savannah', 'Isaac', 'Claire', 'Caleb', 'Samantha', 'Christian', 'Anna',
    'Eli', 'Paisley', 'Jonathan', 'Aubrey', 'Aaron', 'Hazel', 'Adam', 'Genesis', 'Connor', 'Skylar',
    'Cameron', 'Isla', 'Luke', 'Sadie', 'Evan', 'Violet', 'Nathan', 'Aurora', 'Isaiah', 'Mila',
    'Owen', 'Elena', 'Adrian', 'Autumn', 'Brayden', 'Ariana', 'Nolan', 'Jasmine', 'Hunter', 'Piper',
    'Lincoln', 'Stella', 'Gavin', 'Leah', 'Jason', 'Nevaeh', 'Cooper', 'Madelyn', 'Carson', 'Bella',
    'Chase', 'Gabriella', 'Jaxon', 'Kennedy', 'Blake', 'Aurora', 'Leo', 'Ruby', 'Asher', 'Eva',
    'Ryder', 'Naomi', 'Bentley', 'Serenity', 'Sawyer', 'Everly', 'Brody', 'Alice', 'Xavier', 'Luna',
    'Jeremiah', 'Hadley', 'Declan', 'Peyton', 'Mateo', 'Sophie', 'Ayden', 'Natalia', 'Hudson', 'Ivy',
    'Easton', 'Aaliyah', 'Jordan', 'Arianna', 'Brandon', 'Vivian', 'Dominic', 'Willow', 'Austin', 'Eliana',
    'Cole', 'Julia', 'Jaden', 'Josephine', 'Justin', 'Delilah', 'Leo', 'Clara', 'Grayson', 'Liliana',
    'Robert', 'Melanie', 'Kevin', 'Cora', 'Landon', 'Quinn', 'Zachary', 'Bailey', 'Tyler', 'Andrea',
    'Jose', 'Kaylee', 'Nathaniel', 'Charlie', 'Ayden', 'Kimberly', 'Eli', 'Katherine', 'Carson', 'Jade',
    'Diego', 'Alexandra', 'Bryson', 'Morgan', 'Aiden', 'Lauren', 'Damian', 'Rylee', 'Weston', 'Aubree',
    'Max', 'Alexa', 'Leo', 'Arianna', 'Carlos', 'Isabelle', 'Vincent', 'Hailey', 'Micah', 'Jocelyn',
    'Juan', 'Kinsley', 'Cole', 'Isabel', 'Elliot', 'Jordyn', 'Malachi', 'Faith', 'Miles', 'Ximena',
    'Maxwell', 'Eliza', 'Eric', 'Adeline', 'Ashton', 'Gabrielle', 'Graham', 'Emery', 'George', 'Cecilia',
    'Joel', 'Reagan', 'Everett', 'Valeria', 'Grant', 'Makayla', 'Jameson', 'Raelynn', 'Tristan', 'Athena',
    'Jonah', 'Maria', 'Maverick', 'Jade', 'Rylan', 'Lyla', 'Kayden', 'Brynn', 'Harrison', 'Emilia',
    'Ryder', 'Maeve', 'Axel', 'Brielle', 'Avery', 'Eloise', 'Beau', 'Sydney', 'Kai', 'Jordyn',
    'Rowan', 'Laila', 'Sawyer', 'Rosalie', 'Brady', 'Kylie', 'Silas', 'Catherine', 'Emmett', 'Adalyn',
    'Brantley', 'Vera', 'Ezekiel', 'Holly', 'Bentley', 'Alyssa', 'Jax', 'Juliette', 'Parker', 'Lola',
    'Roman', 'Brynlee', 'Camden', 'Lia', 'Knox', 'Daisy', 'Bennett', 'London', 'Xander', 'Alyvia',
    'Chandler', 'Talia', 'Tanner', 'Journey', 'Corbin', 'Alina', 'Hugo', 'Sabrina', 'Zane', 'Amiyah',
    'Cruz', 'Sienna', 'Cade', 'Bristol', 'Marshall', 'Liana', 'Maddox', 'Nylah', 'Nash', 'Aspen',
    'Griffin', 'Malia', 'Rhett', 'Sarai', 'Dalton', 'Avianna', 'Hendrix', 'Lainey', 'Jett', 'Tatum',
    'Wade', 'Makenna', 'Paxton', 'Winter', 'Knox', 'Myla', 'Titus', 'Lena', 'Duke', 'Charlee',
    'Gideon', 'Amara', 'Atticus', 'Mae', 'Damon', 'Nina', 'Franklin', 'Palmer', 'Anderson', 'Nadia',
    'Enzo', 'Lennox', 'Princeton', 'Ada', 'Emerson', 'Ophelia', 'Reid', 'Samara', 'Rhys', 'Demi',
    'Erik', 'Jolie', 'Ellis', 'Milani', 'Clark', 'Amalia', 'Rowan', 'Esme', 'Zander', 'Karter',
    'Grady', 'Sage', 'Brooks', 'Ember', 'Cason', 'Fiona', 'Porter', 'Adrianna', 'Jasper', 'Gracie',
    'Lennon', 'Daniella', 'Remy', 'Giselle', 'Finn', 'Yaretzi', 'Braylon', 'Jazlyn', 'Moses', 'Kamila',
    'Stephen', 'Veronica', 'Waylon', 'Alejandra', 'Warren', 'Leila', 'Royce', 'Catalina', 'Roy', 'Danica',
    'Archer', 'Aniyah', 'Clayton', 'Kaia', 'Malcolm', 'Myra', 'Ari', 'Amina', 'Kyler', 'Alondra',
    'Tatum', 'Selah', 'Phoenix', 'Evangeline', 'Kobe', 'Annabella', 'Winston', 'Adelina', 'Rocco', 'Ivory',
    'Ares', 'Noelle', 'Edwin', 'Magnolia', 'Rylan', 'Mariam', 'Milan', 'Oaklynn', 'Ridge', 'Rosie',
    'Callum', 'Selena', 'Kellan', 'Jayla', 'Reed', 'Aviana', 'Colby', 'Harlow', 'Quentin', 'Alayna',
    'Zane', 'Annalise', 'Drake', 'Scarlet', 'Kane', 'Ivanna', 'Skyler', 'Amelie', 'Emmitt', 'Elianna',
    'Briggs', 'Renata', 'Madden', 'Kaitlyn', 'Zayden', 'Charleigh', 'Kyson', 'Saylor', 'Samson', 'Francesca',
    'Kason', 'Marina', 'Jamison', 'Malaya', 'Zeke', 'Julianna', 'Cohen', 'Frances', 'Emory', 'Nala',
    'Omari', 'Dahlia', 'Reece', 'Kelsey', 'Zachariah', 'Elaina', 'Kendrick', 'Carmen', 'Adonis', 'Brylee',
    'Dax', 'Leilani', 'Cyrus', 'Paris', 'Dorian', 'Kiera', 'Bodhi', 'Elliana', 'Nico', 'Remington',
    'Kian', 'Wren', 'Colt', 'Noa', 'Abram', 'Mercy', 'Troy', 'Keira', 'Luciano', 'Louisa',
    'Cullen', 'Ellianna', 'Alaric', 'Salem', 'Harlan', 'Belen', 'Mekhi', 'Raina', 'Shane', 'Dayana',
    'Dillon', 'Isabela', 'Jonas', 'Regina', 'Johan', 'Averie', 'Kamden', 'Aisha', 'Jaiden', 'Janelle',
    'Saul', 'Kiana', 'Milo', 'Ariella', 'Jaxson', 'Novalee', 'Nelson', 'Armani', 'Johnny', 'Laney',
    'Rafael', 'Malani', 'Wade', 'Dulce', 'Leon', 'Matilda', 'Moses', 'Stevie', 'Dawson', 'Anaya',
    'Leonidas', 'Braelynn', 'Derek', 'Yasmin', 'Finley', 'Madilynn', 'Sullivan', 'Faye', 'Walker', 'Layne',
    'Royce', 'Kensley', 'Alec', 'Mina', 'Alvin', 'Leyla', 'Lawson', 'Antonella', 'Jensen', 'Aleah',
    'Harvey', 'Mabel', 'Baylor', 'Lilian', 'Hendrix', 'Bryanna', 'Callen', 'Monroe', 'Makai', 'Gianna'
]

s = [
    'Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis', 'Rodriguez', 'Martinez',
    'Hernandez', 'Lopez', 'Gonzalez', 'Wilson', 'Anderson', 'Thomas', 'Taylor', 'Moore', 'Jackson', 'Martin',
    'Lee', 'Perez', 'Thompson', 'White', 'Harris', 'Sanchez', 'Clark', 'Ramirez', 'Lewis', 'Robinson',
    'Walker', 'Young', 'Allen', 'King', 'Wright', 'Scott', 'Torres', 'Nguyen', 'Hill', 'Flores',
    'Green', 'Adams', 'Nelson', 'Baker', 'Hall', 'Rivera', 'Campbell', 'Mitchell', 'Carter', 'Roberts',
    'Gomez', 'Phillips', 'Evans', 'Turner', 'Diaz', 'Parker', 'Cruz', 'Edwards', 'Collins', 'Reyes',
    'Stewart', 'Morris', 'Morales', 'Murphy', 'Cook', 'Rogers', 'Gutierrez', 'Ortiz', 'Morgan', 'Cooper',
    'Peterson', 'Bailey', 'Reed', 'Kelly', 'Howard', 'Ramos', 'Kim', 'Cox', 'Ward', 'Richardson',
    'Watson', 'Brooks', 'Chavez', 'Wood', 'James', 'Bennett', 'Gray', 'Mendoza', 'Ruiz', 'Hughes',
    'Price', 'Alvarez', 'Castillo', 'Sanders', 'Patel', 'Myers', 'Long', 'Ross', 'Foster', 'Jimenez',
    'Powell', 'Jenkins', 'Perry', 'Russell', 'Sullivan', 'Bell', 'Coleman', 'Butler', 'Henderson', 'Barnes',
    'Gonzales', 'Fisher', 'Vasquez', 'Simmons', 'Romero', 'Jordan', 'Patterson', 'Alexander', 'Hamilton', 'Graham',
    'Reynolds', 'Griffin', 'Wallace', 'Moreno', 'West', 'Cole', 'Hayes', 'Bryant', 'Herrera', 'Gibson',
    'Ellis', 'Tran', 'Medina', 'Aguilar', 'Stevens', 'Murray', 'Ford', 'Castro', 'Marshall', 'Owens',
    'Harrison', 'Fernandez', 'McDonald', 'Woods', 'Washington', 'Kennedy', 'Wells', 'Vargas', 'Henry', 'Chen',
    'Freeman', 'Webb', 'Tucker', 'Guzman', 'Burns', 'Crawford', 'Olson', 'Simpson', 'Porter', 'Hunter',
    'Gordon', 'Mendez', 'Silva', 'Shaw', 'Snyder', 'Mason', 'Dixon', 'Munoz', 'Hunt', 'Hicks',
    'Holmes', 'Palmer', 'Wagner', 'Black', 'Robertson', 'Boyd', 'Rose', 'Stone', 'Salazar', 'Fox',
    'Warren', 'Mills', 'Meyer', 'Rice', 'Schmidt', 'Garza', 'Daniels', 'Ferguson', 'Nichols', 'Stephens',
    'Soto', 'Weaver', 'Ryan', 'Gardner', 'Payne', 'Grant', 'Dunn', 'Kelley', 'Spencer', 'Hawkins',
    'Arnold', 'Pierce', 'Vazquez', 'Hansen', 'Peters', 'Santos', 'Hart', 'Bradley', 'Knight', 'Elliott',
    'Cunningham', 'Duncan', 'Armstrong', 'Hudson', 'Carroll', 'Lane', 'Riley', 'Andrews', 'Alvarado', 'Ray',
    'Delgado', 'Berry', 'Perkins', 'Hoffman', 'Johnston', 'Matthews', 'Pena', 'Richards', 'Contreras', 'Willis',
    'Carpenter', 'Lawrence', 'Sandoval', 'Guerrero', 'George', 'Chapman', 'Rios', 'Estrada', 'Ortega', 'Watkins',
    'Greene', 'Nunez', 'Wheeler', 'Valdez', 'Harper', 'Burke', 'Larson', 'Santiago', 'Maldonado', 'Morrison',
    'Franklin', 'Carlson', 'Austin', 'Dominguez', 'Carr', 'Lawson', 'Jacobs', 'Obrien', 'Lynch', 'Singh',
    'Vega', 'Bishop', 'Montgomery', 'Oliver', 'Jensen', 'Harvey', 'Williamson', 'Gilbert', 'Dean', 'Sims',
    'Espinoza', 'Howell', 'Li', 'Wong', 'Reid', 'Hanson', 'Le', 'Mckinney', 'Cameron', 'Berry',
    'Fowler', 'Carrillo', 'Stokes', 'Hopkins', 'Fleming', 'Reynolds', 'Newton', 'Garner', 'Hicks', 'Crawford',
    'Price', 'Nguyen', 'Patterson', 'Richards', 'Ford', 'Porter', 'Castro', 'Perez', 'Reid', 'Barnes',
    'Foster', 'Watkins', 'Ford', 'Lawrence', 'Mason', 'West', 'Reyes', 'Ward', 'Grant', 'Perry',
    'Gibson', 'Kim', 'Duncan', 'Bryant', 'Hill', 'Burke', 'Curtis', 'Sanders', 'Simmons', 'Butler',
    'Cunningham', 'Lawson', 'Robertson', 'Terry', 'Cook', 'Hudson', 'Dixon', 'Henry', 'Lane', 'Payne',
    'Soto', 'Knight', 'Hudson', 'Weaver', 'Marshall', 'Peters', 'Gomez', 'Miles', 'Jordan', 'Perry',
    'Fisher', 'Ramos', 'Johnston', 'Reid', 'Wright', 'Roberts', 'Martinez', 'Hughes', 'Weaver', 'Pierce',
    'Hamilton', 'Sullivan', 'Parker', 'Brooks', 'Wells', 'Foster', 'Bennett', 'King', 'Mills', 'Morris',
    'Rogers', 'Russell', 'Murphy', 'Ferguson', 'Arnold', 'Peterson', 'Palmer', 'Stevens', 'Harrison', 'Simmons',
    'Butler', 'Phillips', 'Graham', 'Soto', 'Mason', 'Spencer', 'Porter', 'Morris', 'Stewart', 'Sanchez',
    'Sanders', 'Stevens', 'Coleman', 'White', 'Perry', 'Patterson', 'Lawson', 'Long', 'Nguyen', 'Walker',
    'Gonzalez', 'Young', 'Brooks', 'Bailey', 'Jenkins', 'Wheeler', 'Rodriguez', 'Wallace', 'Patterson', 'Knight',
    'Simmons', 'Holmes', 'Roberts', 'Porter', 'Campbell', 'Gomez', 'Mitchell', 'Edwards', 'Flores', 'Bennett',
    'Clark', 'Russell', 'Coleman', 'Gomez', 'Harris', 'Wheeler', 'Roberts', 'Cole', 'Long', 'King',
    'White', 'Perry', 'Watson', 'Jenkins', 'Young', 'Wright', 'Cooper', 'Bailey', 'Flores', 'Cruz'
]


def g(l):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=l))

def p():
    return ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(64))

def e(d):
    return (f"{random.choice(n).lower()}{random.choice(s).lower()}{g(random.randint(2,4))}@{d}", p())

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    selected_domains = d.copy()  # Default to all domains selected

    if request.method == 'POST':
        selected_domains = request.form.getlist('domains')
        
        results = []
        for domain in selected_domains:
            c, cp = e(domain)
            results.append(f"{domain.capitalize()}:\nEmail: {c}\nPassword: {cp}\n")
        
        pm, pmp = e('proton.me')
        results.append(f"ProtonMail:\nEmail: {pm}\nPassword: {pmp}")
        
        result = "\n".join(results)
    
    return render_template('index.html', domains=d, selected_domains=selected_domains, result=result)

if __name__ == '__main__':
    app.run(debug=True)