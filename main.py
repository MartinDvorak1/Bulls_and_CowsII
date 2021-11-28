import functions
HLAVICKA = """Hi there!
-----------------------------------------------
I've generated a random 4 digit number for you.
Let's play a bulls and cows game."""
ODDELOVAC = "-" * 47


def main():
  generovane_cislo = functions.generuj_cislo()
  print(HLAVICKA)
  print(ODDELOVAC)
  print(f"Enter a number:\n{ODDELOVAC}""")
  pokusy = 1
  while pokusy != 0:
    zadane_cislo = input()
    if functions.overeni_formatu(zadane_cislo) == True:
      porovnani = functions.porovnani_cisel(generovane_cislo, zadane_cislo)
      if porovnani[0] == 4:
        print(f"Correct, you've guessed the right number\nin {pokusy} guesses!")
        print(ODDELOVAC)
        if pokusy < 5:
          print("Amazing moves! Keep it up!")
        elif pokusy < 10:
          print("Very good! I am proud of you!")
        elif pokusy < 20:
          print("You got it right. Finally!")
        else:
          print("At least you guess it at the end")
        break
      else:
        print(porovnani[1])
    else:
      print(functions.overeni_formatu(zadane_cislo))
    print(ODDELOVAC)
    pokusy += 1


main()
