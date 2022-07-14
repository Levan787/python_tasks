
"""import sys
from itertools import permutations

def biggerIsGreater(w):
    arr = list(w)
    # Find non-increasing suffix
    i = len(arr) - 1
    while i > 0 and arr[i - 1] >= arr[i]:
            i -= 1
    if i <= 0:
    	return 'no answer'
    
    # Find successor to pivot
    j = len(arr) - 1
    while arr[j] <= arr[i - 1]:
        j -= 1
    arr[i - 1], arr[j] = arr[j], arr[i - 1]
    
    # Reverse suffix
    arr[i : ] = arr[len(arr) - 1 : i - 1 : -1]
       
    return "".join(arr)
     

if __name__ == "__main__":
    T = int(input("enter number ").strip())
    for a0 in range(T):
        w = input("enter words ").strip()
        result = biggerIsGreater(w)
        print(result)"""

for _ in range(int(input(" enter number "))):
    s = input( " enter string ")
    s = list(s[::-1])
    done = 0
    for i in range(1,len(s)):
        if s[i-1] > s[i]:
            for j in range(i):
                if s[j] > s[i]:
                    s[j],s[i] = s[i],s[j]
                    s = sorted(s[:i])[::-1] + s[i:]
                    print("".join(s[::-1]))
                    break
            break
    else:
        print("no answer")