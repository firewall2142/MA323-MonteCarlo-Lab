import numpy as np


print("| M\t\t| Im\t\t| Im^\t\t| Im 95% conf\t\t| Im^ 95% conf\t\t| ratio\t\t|")
print("-"*90)

for M in [100, 1000, 10000, 100000]:
    U = np.random.uniform(size=M)
    Y = np.exp(np.sqrt(U))
    Yh = (np.exp(np.sqrt(U)) + np.exp(np.sqrt(1-U)))/2

    I = Y.mean()
    sigma = Y.std()
    conf_left  = I - 1.96*sigma/np.sqrt(M)
    conf_right = I + 1.96*sigma/np.sqrt(M)

    Ih = Yh.mean()
    sigmah = Yh.std()
    confh_left  = Ih - 1.96*sigmah/np.sqrt(M)
    confh_right = Ih + 1.96*sigmah/np.sqrt(M)

    ratio = (conf_right-conf_left)/(confh_right-confh_left)
    
    print(f"|{M}\t| {I:.4f}\t| {Ih:.4f}\t| [{conf_left:.4f},{conf_right:.4f}]\t| [{confh_left:.4f},{confh_right:.4f}]\t| {ratio:.4f}\t|")