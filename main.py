from matplotlib import pyplot as plt
import diabetesData
import sugarData



diabetes_x = diabetesData.years
diabetes_y = diabetesData.diagnosedInMillions

sugar_x = sugarData.years
sugar_y = sugarData.consumed_per_lb

plt.plot(diabetes_x, diabetes_y, label= "Diabetes Diagnosed in millions")
plt.plot(sugar_x, sugar_y, label= "Sugar Consumed per lb")

plt.xlabel("Years")
#plt.ylabel("Diagnosed in Millions")
plt.title("Trends of Diabetes Diagnoses over the years")

plt.legend()
plt.show()


