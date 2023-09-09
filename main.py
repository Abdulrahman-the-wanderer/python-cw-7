class person :
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"My name is {self.name} and I am {self.age} years old"
    #name = "ali"
    #age = 15

    #def is_adult(self):
        #if self.age > 18 :
            #print("you have too much responsibilites")
        #else:
            #print("lucky")
#first_person = person()
#print(first_person.name)
#print(first_person.age)
#first_person.is_adult()
first_person = person("john",22)
print(first_person)

