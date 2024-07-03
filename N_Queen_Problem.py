from itertools import permutations
from colorama import init,Fore

N= 8
sol=0
cols = range(N)
for combo in permutations (cols):
    if N == len(set(combo[i]+i for i in cols)) == len(set(combo[i]-i for i in cols)):
        sol+=1
        print(Fore.LIGHTYELLOW_EX+'solution '+str(sol)+': ' +str(combo)+ '\n')
        print("\n" .join(Fore.RED+'O ' * i + Fore.CYAN+'X ' +  Fore.RED+'O ' *(N-i-1) for i in combo) + "\n\n\n\n")
