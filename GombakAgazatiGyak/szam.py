import random

generaltszam=random.randint(1,50)

print(f"A generált szám: {generaltszam}")

if generaltszam%5==0 and generaltszam%3==0:
    print("A szám öttel és hárommal is osztható!")
elif generaltszam%5==0:
    print("A szám öttel osztható!")
elif generaltszam%3==0:
    print("A szám hárommal osztható!")
