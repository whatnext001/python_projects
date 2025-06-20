class Human:
    def __init__(self,color,race,language):
        self.color = color
        self.race = race
        self.language = language

    def african(self):
        return f"The human race differs based on {self.color},{self.race},{self.language}"

    def european(self):
        return f"The human race differs based on {self.color},{self.race},{self.language}"

    def asian(self):
        return f"The human race differs based on {self.color},{self.race},{self.language}"

class Giant(Human):   #this denotes that class Giant is a subclass of the superclass Human,
     def __init__(self,color,race,language,blood): #another __init__ can also be added or extended for the subclass
         super().__init__(color,race,language) #this is to avoid repeating the argument of the superclass
         self.blood = blood

new_human = Giant("red","caucasian","kinari","neutral")

print(new_human.blood)