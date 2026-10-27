s="An apple is on the table"
s=s.split()

vowel=['a','e','i','o','u','A','E','I','O','U']
count=0
vol=[]
for i in s:

      if i[0] in vowel:
          count+=1
          vol.append(i)
          
print("number of vowel:",count,vol)       
      
