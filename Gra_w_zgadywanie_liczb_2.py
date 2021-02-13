def user_answers():
    """Funkcja zwraca tekst wpisany przez użytkownika.
        :rtype: str
        :return: wartość wpisaną przez użytkownika ['too small', 'too big', 'you win']
        """
    possible_answer = ['too small', 'too big', 'you win']
    while True:
        user_answer = input()
        if user_answer in possible_answer:
            break
        print("Answer is not in ['too small', 'too big', 'you win']")
    return user_answer

def guess():
    """Main function for our program.
    Funkcja w maksymalnie 10 krokach zgaduje liczbę po otrzymaniu od użytkownika informacji
    czy wskazywana przez komputer liczba jest większa lub mniejsza od szukanej."""

    print("""Pomyśl liczbę od 0 do 1000,
    a ja ją zgadnę w max 10 próbach!
    Następnie wciśnij ENTER""")
    input()
    min_number = 0
    max_number = 1000
    user_answer = ""
    while user_answer != 'you win':
        guess = int((max_number - min_number) / 2) + min_number
        print(f"I guess it is: {guess}")
        user_answer = user_answers()
        if user_answer == 'too big':
            max_number = guess
        elif user_answer == 'too small':
            min_number = guess
        else:
            print('I guess!')

if __name__ == '__main__':
    guess()
