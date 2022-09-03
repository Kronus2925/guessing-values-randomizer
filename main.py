import random
counter = 1
chosen_numbers = []
generated_values = []
guessed_values = []

print("Witamy w symulatorze Dużego Lotka")
print("Podaj proszę 6 liczb z zakresu od 1 do 49")

while len(chosen_numbers) != 6:

    try:
        user_numbers = int(input(f'Podaj liczbę nr. {counter}:'))
    except ValueError:
        print('Podałeś nieprwidłową wartość, podaj proszę liczbę')
        continue

    if user_numbers not in range(1, 50):
        print("Liczba nie znajduje się w przedziale od 1 do 49")
    elif user_numbers not in chosen_numbers:
        user_numbers = chosen_numbers.append(user_numbers)
        print(chosen_numbers)
        counter = counter + 1
    else:
        print(f'{user_numbers} występuje już w twoich liczbach. Twoje liczby to : {chosen_numbers}')

else:
    while len(generated_values) != 6:

        value_generation = random.randrange(1, 50, 1)
        if value_generation not in generated_values:
            generated_values.append(value_generation)

    print(f'Wytypowane wartości to {generated_values}')


    def check_score(chosen_numbers, generated_values):
        x = 0
        for element in chosen_numbers:
            if element in generated_values:
                x = x + 1
                guessed_values.append(element)
        return x


    score = (check_score(chosen_numbers, generated_values))

    if score > 1 and score < 5:
        print(f'Trafiłeś {score} liczby')
        print(f'Trafione liczby to {guessed_values}')
    elif score > 4:
        print(f'Trafiłeś {score} liczb')
        print(f'Trafione liczby to {guessed_values}')
    elif score == 1:
        print("Trafiłeś 1 liczbę")
        print(f'Trafiona liczba to {guessed_values}')
    else:
        print("Niestety nie udało ci się trafić żadnej z wytypowanych liczb")

    def user_choice():

        choice = str(input("Czy chcesz zagrać jeszcze raz? Tak/Nie"))
        if choice == "Tak":
            import main
        elif choice == "Nie":
            print('Dziękuje za skorzystanie z programu')
        else:
            print("Wybacz, nie rozumiem o co chodzi, Możliwe odpowiedzi to Tak lub Nie")
            return(user_choice())

    print(user_choice())
