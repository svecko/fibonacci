from functools import lru_cache

@lru_cache(maxsize = 1000)
def fibonacci(n):
  # Preveri, da je vnos pozitivno celo število
  if type(n) != int:
    raise TypeError("n mora biti pozitivno celo število")
  if n < 1:
    raise TypeError("n mora biti pozitivno celo število")

  # Izračuna n-ti člen fibonaccijevega zaporedja
  if n == 1:
    return 1
  elif n == 2:
    return 1
  elif n > 2:
    return fibonacci(n-1) + fibonacci(n-2)

for n in range(1, 51):
  print(fibonacci(n))