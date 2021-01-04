#%%
varCeFa = input("Celcius of Fahrenheit? (C of F): ")
graden = int(input("Hoeveel graden?: "))

if (varCeFa == 'C'):
  antwoord = graden * 9 / 5 + 32
  print(graden, "C is", antwoord, "Fahrenheit")
elif (varCeFa == 'F'):
  antwoord = (graden -32) * 5/9
  print(graden, "Fahrenheit is", antwoord, "C")
# %%
