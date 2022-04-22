#PART I ANSWER = 841526
#PART II ANSWER = 4790390


class BinaryCouter:
    
    
    def __init__(self, input_path = 'day_03_sample.txt') -> None:
        with open(input_path) as file:
            self.coordenates = file.read().splitlines()
        self.len_word = len(self.coordenates[0])
        self.input_size = len(self.coordenates)
    
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.input_path!r})"
    
    
    def calculate_power_consumtion(self) -> int:
        gr_er = self.generate_gr_er()
        gamma = int(gr_er[0], 2)
        epsilon = int(gr_er[1], 2)
        return gamma * epsilon
    
    #method tha returns a list with the gamma_rate and the epsilon_rate values
    def generate_gr_er(self) -> list:
        gamma_rate = ""
        epsilon_rate = ""
        count_ones = [0] * self.len_word
        for item in self.coordenates:
            for index in range(self.len_word):
                count_ones[index] = count_ones[index] + int(item[index])
        for item in count_ones:
            if item > (self.input_size - item):
                gamma_rate = gamma_rate + "1"
                epsilon_rate = epsilon_rate + "0"
            else:
                gamma_rate = gamma_rate + "0"
                epsilon_rate = epsilon_rate + "1"
        return [gamma_rate, epsilon_rate]
    
    #method tha returns the most common number in a position if value_to_keep == 1
    #or returns the last common number in a position if value_to_keep == 0
    #if the quantity of zeros and ones are equal we return value_to_keep
    def count_number_position(self, my_list, my_position, value_to_keep):
        count = 0
        for item in my_list:
            count = count + int(item[my_position])
        if count == (len(my_list) - count):
            return value_to_keep
        elif count > (len(my_list) - count):
            if value_to_keep == 1:
                return 1
            else:
                return 0
        else:
            if value_to_keep == 1:
                return 0
            else:
                return 1
        
    #method that returns oxygen_generator_rating if set == 1
    #and returns CO2_scrubber_rating if set == 0
    def generate_ogr_csr(self, set):
        my_list = self.coordenates[:]
        count = 0
        while len(my_list) > 1:
            value = self.count_number_position(my_list, count, set)
            new_list = [item for item in my_list if int(item[count]) == value]
            my_list = new_list[:]
            count += 1
        return(int(my_list[0], 2))


obj = BinaryCouter("day_03_input.txt")
gr_er = obj.generate_gr_er()
power_consumption = obj.calculate_power_consumtion()
print(f"gamma_rate = {gr_er[0]}, epsilon_rate = {gr_er[1]}")
print(f"Power Consumption = {power_consumption}")
oxygen_generator_rating = obj.generate_ogr_csr(1)
CO2_scrubber_rating =  obj.generate_ogr_csr(0)
print(f"Oxygen generator rating = {oxygen_generator_rating}, CO2 scrubber rating = {CO2_scrubber_rating}" )
life_support_rating = oxygen_generator_rating*CO2_scrubber_rating
print(f"Life support rating = {life_support_rating}")