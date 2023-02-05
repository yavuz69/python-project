       ### FIRST SOLUTION ### 

def con_vowels():
    
    string = input("enter a string: ")
    string = string.lower()
    vowels = ["a","e","i","o","u"]
    t = 0
    for i in string:
        if t < len(string)-1:
          for k in vowels:
            if i == k : 
               if string[t+1] in vowels :
                  return True
          t += 1
if con_vowels():
  print("pozitive")
else:
  print("negative") 

    ### SECOND SOLUTION ### 

# sesli_harfler = "aeıioöuüAEİIOÖUÜ"
# while True:
#     metin = input("Enter a string: ")
#     for i in range(len(metin) - 1):
#         if metin[i] in sesli_harfler and metin[i + 1] in sesli_harfler:
#             durum = "Pozitif"
#             break
#         else: 
#             durum = "Negatif"
#     print(durum)
  
  

   ## THIRD SOLUTION ### 


# word = input("Please enter a string: ")
# word = word.lower()

# vowels = ["a", "e", "i", "o", "u"]
# exist = False

# for i in range(len(word)-1):
#   if word[i] in vowels:
#     if word[i+1] in vowels:
#       exist = True
#       break
      
# if exist:
#   print("Positive")
# else:
#   print("Negative")






