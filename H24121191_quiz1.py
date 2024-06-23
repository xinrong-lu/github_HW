Richter_scale = input("Please input a Richter scale value: ")
richter = float(Richter_scale)
Richter_Joules = 10 ** ((1.5 * richter) + 4.8)
TNT = 4.184 * 10 ** 9
nutritious_lunch = 2930200
TNT_e= Richter_Joules / TNT
nutritious_lunch_e = Richter_Joules / nutritious_lunch

print("Richter scale value: ", richter)
print("Equivalence in Joules: ", Richter_Joules)
print("Equivalence in tons of TNT: ", TNT_e)
print("Equivalence in the number of nutritious lunches: ", nutritious_lunch_e)