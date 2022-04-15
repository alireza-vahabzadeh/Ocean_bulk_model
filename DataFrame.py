import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
N = int(input('How many densities do we want to find: '))
list_S = []
list_T = []
list_P = []
list_D = []
for i in range(N):
    S = int(input(f'Salinity{i+1}(ppt):'))
    list_S.append(S)
    T = int(input(f'Temperature{i+1}(C):'))
    list_T.append(T)
    P = int(input(f'Pressure{i+1}(bars):'))
    list_P.append(P)
# D_w=? / in D_w, S is zero(S=0)
    D_w = 999.842594 + 6.793952 * 10**(-2) * T - 9.095290 * 10**(-3) * T**2 + 1.001685 * \
        10**(-4) * T**3 - 1.120083 * 10**(-6) * \
        T**4 + 6.536332 * 10**(-9) * T**5

# P_st , density at one standard atmosphere(effecively P=0)
    D_st = D_w + S * (0.824493 - 4.0899 * 10**(-3) * T + 7.6438 * 10**(-5) * T**2 - 8.2467 * 10**(-7) * T**3 + 5.3875 * 10 **
                      (-9) * T**4) + S**(3/2) * (-5.72466 * 10**(-3)+1.0227 * 10**(-4)*T - 1.6546 * 10**(-6) * T**2) + 4.8314 * 10**(-4) * S**2

# K_w / in K_w, S is zero(S=0)
    K_w = 19652.21 + 148.4206 * T - 2.327105 * T**2 + \
        1.360447 * 10**(-2) * T**3 - 5.155288 * T**4 * 10**(-5)

# K_st , density at one standard atmosphere(effecively P=0)
    K_st = K_w + S * (54.6746 - 0.603459 * T + 1.09987 * 10**(-2) * T**2 - 6.1670 * 10**(-5)
                      * T**3) + S**(3/2) * (7.944 * 10**(-2) + 1.6483 * 10**(-2) * T - 5.3009 * 10**(-4) * T**2)

# K_stp, (S, T, P)
    K_stp = K_st + P * (3.239908 + 1.43713 * 10**(-3) * T + 1.16092 * 10**(-4) * T**2 - 5.77905 * 10**(-7) * T**3) + P * S * (2.2838 * 10**(-3) - 1.0981 * 10**(-5) * T - 1.6078 * 10**(-6) * T**2) + 1.91075 * \
        10**(-4) * P * S**(3/2) + P**2 * (8.50935 * 10**(-5) - 6.12293 * 10**(-6) * T + 5.2787 * 10**(-8)
                                          * T**2) + P**2 * S * (-9.9348 * 10**(-7) + 2.0816 * 10**(-8) * T + 9.1697 * 10**(-10) * T**2)

# P_stp, (S, T, P)
    D_stp = D_st / (1 - (P/K_stp))
    list_D.append(D_stp)
    

# DataFrame
list_O = []
list_O.append(list_S)
list_O.append(list_T)
list_O.append(list_P)
list_O.append(list_D)
list_O
df = pd.DataFrame(data=list_O, index=[
                  'Salinity', 'Temperature', 'Pressure', 'Density'])
df.index.name = 'feature'
df.columns.name = 'Number'

print(df)
plt.boxplot(list_D)
plt.grid()
plt.show()
input("Press enter to exit ;)")
