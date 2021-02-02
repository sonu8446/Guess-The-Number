import random
def difficultyAttempts(Attempts):
    ans=random.randint(1,100)
    for i in range(Attempts,0,-1):
        print(f"You have {i} attempts remaining to gess the number.")
        guess=int(input("Make a Guess: "))
        if guess==ans:
            print(f"Correct {guess}")
            break
        elif ans<guess:
            print("Too high.")
        elif ans>guess:
            print("Too low.")
    print(ans)
level=input("Choose a difficulty. Type 'easy' or 'hard': ")
if level.lower()=='hard':
    difficultyAttempts(5)
else:
    difficultyAttempts(10)