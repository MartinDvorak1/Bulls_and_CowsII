import random


def generuj_cislo():
  list_cisel = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  list_generovanych_cisel = list()
  i = 0
  while i < 4:
    if i == 0:
      index = random.randrange(len(list_cisel))
      cislo = list_cisel[index]
      while cislo == 0:
        index = random.randrange(len(list_cisel))
        cislo = list_cisel[index]
      list_generovanych_cisel.append(str(list_cisel.pop(index)))
    else:
      index = random.randrange(len(list_cisel))
      list_generovanych_cisel.append(str(list_cisel.pop(index)))
    i += 1
  return "".join(list_generovanych_cisel)


def overeni_formatu(string_cisla):
  if string_cisla.isdecimal():
    if int(len(string_cisla)) != 4:
      return "Number is not correct lenght"
    elif int(string_cisla[0]) == 0:
      return "Number cannot start with 0"
    elif int(len(set(string_cisla))) != int(len(list(string_cisla))):
      return "Number cannot have duplicite digits"
    return True
  else:
    return "Input is not a number"


def porovnani_cisel(str_generovane_cislo, str_zadane_cislo):
  bulls, cows = 0, 0
  for index, item in enumerate(str_generovane_cislo):
    for pozice, prvek in enumerate(str_zadane_cislo):
      if str_generovane_cislo[index] == str_zadane_cislo[pozice]:
        if pozice == index:
          cows += 1
          break
        else:
          bulls += 1
          break
  if cows == 4:
    return cows, "Correct, you've guessed the right number"
  else:
    return cows, f"{bulls} bulls, {cows} cows"
