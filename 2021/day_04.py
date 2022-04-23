
class Bingo:
    
    def __init__(self, path = 'day_04_sample.txt') -> None:
        self.path = path
        
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.path!r})"
    
    #Get a list of all bingo cards
    def get_cards(self) -> list:
        with open(self.path) as file:
            text = file.read()
            cards = [text.split()[n : n+25]  
                            for n in range(1, len(text.split()), 25)]
        return cards
    
    #Get a list of all numbers drawn
    def get_drawn_numbers(self) -> list:
        with open(self.path) as file:
            text = file.read()
            chosen_numbers = text.splitlines()[0].split(',')
        return chosen_numbers
            
    #Sees if a card won with a certain list of numbers draw.
    #returns a tuple with the card and the numbers draw if the card won
    #otherwise returns None
    def see_if_card_won(self, card, drawn_numbers) -> tuple:
        lines = [card[n:n+5] for n in range(0, 25, 5)]
        columns = [card[n:25:5] for n in range(0, 5)]
        for number in drawn_numbers:
            for line, column in zip(lines, columns):
                if number in line:
                    line.remove(number)
                    if line == []:
                        return (card, drawn_numbers)
                if number in column:
                    column.remove(number)
                    if column == []:
                        return (card, drawn_numbers)
        return None
    
    #Finds the  card who won the bingo
    def get_winner(self, cards, drawn_numbers, inicial_number = 0) -> tuple:
        for quantity_numbers in range(inicial_number, len(drawn_numbers)):
            for card in cards:
                result = self.see_if_card_won(card, drawn_numbers[0:quantity_numbers])
                if result != None:
                    return result
    
    
    def calculate_winner_score(self, card, numbers):
        unmarked_numbers = [int(item) for item in card if item not in numbers]
        last_number = int(numbers[-1])
        score = sum(unmarked_numbers)*last_number
        return score
    
    #Finds the card that wins last
    def last_winner(self, cards, numbers) -> tuple:
        quantity_numbers = 0
        for card in cards:
            winners = self.get_winner([card], numbers)
            if len(winners[1]) >= quantity_numbers:
                last_winner = winners
                quantity_numbers = len(last_winner[1])
        return last_winner
            
obj = Bingo("day_04_input.txt")
cards = obj.get_cards()
drawn_numbers = obj.get_drawn_numbers()

winner = obj.get_winner(cards, drawn_numbers)
print(f"Part I: {obj.calculate_winner_score(winner[0], winner[1])}")

last_winner = obj.last_winner(cards, drawn_numbers)
print(f"Part II: {obj.calculate_winner_score(last_winner[0], last_winner[1])}")