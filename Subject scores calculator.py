import math

'''------------Python------------'''
G= 99
G2=100
Q1 = 72
O1 = 100
O2 =100
F = 79
WTA =100
TP = 0.1*G + 0.1*G2+ 0.1*Q1+ 0.4*F+ 40
#print(round(TP))
'''------------DBMS------------'''
GAA1 = 100
GAA2 = 100
GAA3 = 100
Qz1 = 100
Qz2 = 100
OP = 100
F = 80
TDBMS = 0.04*GAA1 + 0.03*GAA2 + 0.03*GAA3 + 0.2*OP + max (0.45*F+0.25*max(Qz1, Qz2),  0.4*F+(0.10*Qz1+0.20*Qz2 ))
#print(TDBMS)
'''------------PDSA------------'''
GAA = 100
Qz1 = 100
Qz2 = 100
OP = 100
F = 80
TPDSA = (0.1 * GAA) + (0.4 * F) + (0.2 * OP) + max(0.3 * max(Qz1, Qz2), (0.15 * Qz1) + (0.15 * Qz2)) 
#print(TPDSA)
'''------------AppDev1------------'''
GLA = 100
GA = 98
Qz1 = 50
Qz2 = 80
F = 100
TMAD1 = (0.15 * GLA) + (0.05 * GA) + max((0.35 * F) + (0.2 * Qz1) + (0.25 * Qz2), (0.5 * F) + (0.3 * max(Qz1, Qz2))) 
#print(TMAD1)
'''------------MLF------------'''
GAA = 100
Qz1 = 100
Qz2 =70
F = 85
TMLF = (0.1 * GAA) + max((0.6 * F) + (0.3 * max(Qz1, Qz2)), (0.4 * F) + (0.2 * Qz1) + (0.3 * Qz2))
print(TMLF)

