
   ### Which number is bigger  ###

number = []

sayı1 = int(input("bir sayı gir :"))
number.append(sayı1)
sayı2 = int(input("bir sayı gir :"))
number.append(sayı2)
print(number)
if sayı1  > sayı2:
    print(f"{sayı1} büyüktür")
else:
    print(f"{sayı2} büyüktür")   



   ### A Different Solution   ###

bignumber = []

for sayılar in range(0,5):
    sayılar = int(input("enter no :"))
    bignumber.append(sayılar)
print(f"sayılar listesi: {bignumber}")
# print(f"en büyük sayı {max(bignumber)}")
largest = 0
for i in bignumber:
  if i > largest:
    largest = i 
print(largest)

    ### A Different Solution   ###

count=0
array=[]
while count < 7:
  number= int(input('Please enter the number: '))
  array.append(number)
  count = count +1
def findLargestNum(nums):
  largest = nums[0]
  for i in nums:
    if i > largest:
      largest = i
  return largest
print(findLargestNum(array))
    
  
    
    
