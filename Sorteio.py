import random
number_choice = random.randint(1, 100)
number_try = int(0)
try_ = int(101)

while try_ != number_choice:
    try_ = int(input('Qual o seu palpite? '))
    distance = int(abs(number_choice-try_))

    if distance <= 99 and distance >= 69:
        print("Seu palpite foi muito distante do número\n")

    elif distance < 69 and distance >= 39:
        print("Seu palpite foi distante do número\n")

    elif distance < 39 and distance >= 10:
        print("Seu palpite está perto do número\n")

    elif distance < 10 and distance != 0:
        print("Seu palpite está muito próximo do número\n")

    number_try += 1

print(f"Parabéns! Você acertou na sua tentativa número {number_try}")
