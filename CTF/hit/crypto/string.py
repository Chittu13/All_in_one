#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sympy import isprime

str="fe7l1Owa85YA9g8CELs3F{H11s1o258p6hOo77di7Y0V83M1feBdNeP3QuS9G7LVjd8EZUei9NOi3p3p9jKcbiUYsy4zA6P88Y7NP73jiLFW4nl8m6xN3LcHttxA2ML73J68g2PtR52926v1sDi22KE9VhBT8kgc26581q2pP77_bTZ6XPBR3iRT7Jbo9YvsEUiXE6Lv4y790z5wu145p6W8Mc6l38tCBPfCq30P7fXD2652g1INKDF3EeUnXm6gLUWOZ9NKhFr19gAaVldd7FkjlMuqSaNW3E0BEt4_6y8C35pI6y7IWQoimXQgkIZTR19Z21e33er4YENvt4paILApj4nwPiDpLFJP8UP0wTZNGN2grACDd6h5MfTWlxpdY8iF79uK38Rn7lFzU15Y6gTA2FSz5163C4eWTI80c5o9OANDD6WZ0T8M5SC42t6CANB4rDNJH49J9aQQdE6ylWR23c7337ex7vp4KLI9xYpvBDC0E7VgSZXkE186uDA93lMRNeZ1ynL31hntD9vZQ4V18sd9lWyt433B2jX843A77E8Sl22ds46y640C1q3QthAov3LuB24n9nq3y5f0pJ9E67ECu5g8w29PIuUR2VLhwX1b3IdhykJ8p8mimNxRPYrGEnMeXoWulV0tTtz_DBz56b3GXi29LWfyw0AkSDIYCG583yCQcEepP1Sj8LL76R0tKMo38K099uGz17S8N84e1h1Z5576xa0u46e083hHN2m368wN34Eigw5VjG1Gh315UqjQr9ff3Ip0m82m8Rm8JT380miS8aC61zS2K4W6o1ymg0nWB977XNc0iu7ee9b142UJhprY4Hh35s1TaKc221Q2ip1KX02p6ny96Ay3TIyn9m30qXxc4lKQZxK899BhD98RuX32B03dJUi5iL3kQA0B0o4D4Tgq4FTD5JNKJg8Kg5aibRsn9GeOq3E8big7nPKWqUM8SlHd70iHD8Ciw4XhntUTM9dBPPspkbYL783096NUMRG766Av9A4B3fn1o2CYTO9sG8u2Kqk0VekGq20inkHM141pogz69Ng91dnk5wWQRJ8i0Q14MtfFA0hORWW775bM0jJ2R1sb24KhbbD42V1Qb5s9N36fZ2BpFJR7mR6cKE8Ot7drG92BQ692PLrPbHfbV8QxH4rc9SpTb5RGchC5kB5}c1CHsMd05v3Fmo3YeT7EaduRD2Q6eOrKbAWn"

flag = 'f'
primes = []
for i in range(1,300):
    if isprime(i):
        primes.append(i)
i = 1
for k in range(26):
   i += primes[k]
   flag += str[i]
   i += 1


print(flag)
