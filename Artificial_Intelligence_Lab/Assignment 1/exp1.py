#Convert a decimal number into binary
n = int(input("Enter any Number - "))

s = ""

if n != 0 :
     while(n != 0 ):
        x = n%2
        n  /= 2
        n = int(n)
        s = s + str(x)
else:
      s = "0"

ans = s[::-1]
print(ans)