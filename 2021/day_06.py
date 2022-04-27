'''
PART I ANSWER: 374927
PART II ANSWER: 1687617803407
'''

class Lanternfish:
    
    def __init__(self, input_path = "day_06_sample.txt") -> None:
        with open(input_path) as file:
            shoal = file.read().rsplit(",")
        self.shoal = [int(item) for item in shoal]
        self.shoal_distribution = {"0": 0, 
                              "1": 0,
                              "2": 0,
                              "3": 0,
                              "4": 0,
                              "5": 0,
                              "6": 0,
                              "7": 0,
                              "8": 0}
        for item in shoal:
            self.shoal_distribution[item] = self.shoal_distribution[item] + 1
    
    
    def get_shoal_grow(self, days):
        new_shoal = self.shoal_distribution.copy()
        old_shoal = self.shoal_distribution.copy()
        count = 1
        while count<= days:
            new_shoal["0"] = old_shoal["1"]
            new_shoal["1"] = old_shoal["2"]
            new_shoal["2"] = old_shoal["3"]
            new_shoal["3"] = old_shoal["4"]
            new_shoal["4"] = old_shoal["5"]
            new_shoal["5"] = old_shoal["6"]
            new_shoal["6"] = old_shoal["0"] + old_shoal["7"]
            new_shoal["7"] = old_shoal["8"]
            new_shoal["8"] = old_shoal["0"]
            old_shoal = new_shoal.copy()
            count += 1
        return sum(new_shoal.values())
        
obj = Lanternfish("day_06_input.txt")
print(f"on the 80th we will have: {obj.get_shoal_grow(80)}")
print(f"on the 256th we will have: {obj.get_shoal_grow(256)}")