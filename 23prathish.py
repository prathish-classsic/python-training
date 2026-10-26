s=input('enter a word:')
c=input('enter a character:')

count=0

for i in s:
    if i==c:
        count+=1
print(f"git addthe word is {s} and it repated {count} times")
