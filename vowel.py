s=input("enter the word:")
vow=['a', 'e', 'i', 'o', 'u',
          'A', 'E', 'I', 'O', 'U']
consonent=[
    'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm',
    'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z',
    'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M',
    'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z'
]
vcount=0
ccount=0
for i in s:
     if i in vow:
         vcount+=1
     if i in consonent:
         ccount+=1
print("vow:",vcount)
print("consonent",ccount)
