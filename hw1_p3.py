input_v = input("Input velocity: ")
v = int(input_v)
c = 299792458
percent = v / c
factor = 1 / (1 - v ** 2 / c ** 2) ** (1 / 2)
timeAC = 4.3 / factor
timeBS = 6.0 / factor
timeBe = 309 / factor
timeAG = 2000000 / factor
print("Percentage of light speed =", percent)
print("Travel time to Alpha Centauri =", timeAC)
print("Travel time to Barnard's Star =", timeBS)
print("Travel time to Betelgeuse (in the Milky Way) =", timeBe)
print("Travel time to Andromeda Galaxy (closest galaxy) =", timeAn)
