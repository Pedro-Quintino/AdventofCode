import math


# ANSWER PART I: 359648
# ANSWER PART II: 100727924

class Crab:
    
    def __init__(self, input_path = "day_07_sample.txt") -> None:
        with open(input_path) as file:
            positions = file.read().rsplit(",")
        self.positions = [int(item) for item in positions]
        self.crab_squad = self.get_crab_squad()
    
    def get_crab_squad(self):
        squad = {}
        for crab in self.positions:
            if crab in squad.keys():
                squad[crab] = squad[crab]  +1
            else:
                squad[crab] = 1
        return squad
    
    
    #Finds the position that the crabs can align using the minimum fuel possible
    #then, shows position and fuel needed
    #set fomation == 0 to consider instructions of part one
    #set any other value to formation to consider instructions of part two
    def get_align_position(self, formation = 0):
        crab_squad = self.crab_squad
        better_position = 0
        minimun_fuel = math.inf
        position = 0
        while position <= max(crab_squad.keys()):
            fuel_count = 0
            for key, value in crab_squad.items():
                if formation == 0:
                    fuel_count += (abs(position - key))*value
                else:
                    #I will let the next commented line to show what i am doing more clearly
                    #fuel_count += (sum(range(1, abs(position - key) +1)))*value
                    #to reduce the time I am using the Gauss summation
                    fuel_count += int( (abs(position - key) + 1)*abs(position - key)/2)*value
            if fuel_count <= minimun_fuel:
                minimun_fuel = fuel_count
                better_position = position
            position += 1
        print(better_position, minimun_fuel)
        
        
obj = Crab("day_07_input.txt")
obj.get_align_position(0)
obj.get_align_position(1)