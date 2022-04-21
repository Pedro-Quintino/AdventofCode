class Sonar:
    '''
    For the fist part of the puzzle we have a method get_increase_measurement who counts the number of thimes a 
    depth measurement increases from the previous measurement.
    For the second part we have the method get_sum_comparation who compares windows of three consecutive measurements
    and count the times the sums have increased. 
    PART I ANSWER: 1715.
    PART II ANSWER: 1739.
    '''
    
    def __init__(self, input_path = "day_01_sample.txt") -> None:
        self.input_path = input_path
        with open(input_path) as text:
            self.input = text.read().split()
        self.first_value = int(self.input[0])


    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.input_path!r})"
    
    
    def get_increase_measurement(self) -> int:
        count_large = 0
        for index, measurement in enumerate(self.input):
            if index != 0:
                if int(measurement) > int(self.input[index-1]):
                    count_large += 1
        return count_large
    
    
    def get_sum_comparation(self) -> int:
        count_large_sum = 0
        for index in range(len(self.input)):
            if index !=0 and index < len(self.input) - 2:
                A = int(self.input[index-1]) + int(self.input[index]) + int(self.input[index+1])
                B = int(self.input[index]) + int(self.input[index+1]) + int(self.input[index+2])
                if B > A:
                    count_large_sum += 1
        return count_large_sum   

if __name__ == "__main__":
    obj = Sonar("day_01_input.txt")
    print(f"The number of times the measure increased was {obj.get_increase_measurement()}")
    print(f"There are {obj.get_sum_comparation()} sums that are larger than the previus measurement")  