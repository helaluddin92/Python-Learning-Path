class LetterNumber:
    def __init__(self, mylists):
        self.mylists = mylists

    def letters(self, letters=[]):  # Letters list
        for letter in self.mylists:
            if type(letter) == str:
                letters.append(letter)
        return letters

    def numbers(self, numbers=[]):  # Number List
        for number in self.mylists:
            if type(number) == int:
                numbers.append(number)
        return numbers


result = LetterNumber([1, 2, 3, 4, 5, 'a', 'b', 'c'])
print(result.letters())
print(result.numbers())
