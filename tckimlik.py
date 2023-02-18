
               ### FIRST SOLUTION  ###

def trueTc(tckimlikno):

    if tckimlikno[0] == 0:
      return False
    if len(tckimlikno) != 11:
      return False 
    islem_1 = (((sum(tckimlikno[0:9:2])) * 7 ) - (sum(tckimlikno[1:8:2]))) % 10
    if tckimlikno[9] != islem_1:
      return False
    islem_2 = (sum(tckimlikno[0:10])) % 10
    if tckimlikno[10] != islem_2:
      return False
    return True 

print("Please enter numeric value! ")
tc = list(input("lütfen tc no gir: "))

tckimlikno = []
i = 0
while i < len(tc):
   tckimlikno.append(int(tc[i]))
   i += 1
if trueTc(tckimlikno):
  print("your tc is valid")
else:
  print("your tc is in valid") 


         ### SECOND SOLUTION  ###
        

def isValidTCID(value):
    value = str(value)
    
    # 11 hanelidir.
    if not len(value) == 11:
        return False
    
    # Sadece rakamlardan olusur.
    if not value.isdigit():
        return False
    
    # Ilk hanesi 0 olamaz.
    if int(value[0]) == 0:
        return False
    
    digits = [int(d) for d in str(value)]
         # digits = []
         # for d in str(value):
         #   digits.append(int(d))
    # 1. 2. 3. 4. 5. 6. 7. 8. 9. ve 10. hanelerin toplamından elde edilen sonucun
    # 10'a bölümünden kalan, yani Mod10'u bize 11. haneyi verir.
    if not sum(digits[:10]) % 10 == digits[10]:
        return False
    
    # 1. 3. 5. 7. ve 9. hanelerin toplamının 7 katından, 2. 4. 6. ve 8. hanelerin toplamı çıkartıldığında,
    # elde edilen sonucun 10'a bölümünden kalan, yani Mod10'u bize 10. haneyi verir.
    if not (((7 * sum(digits[:9][-1::-2])) - sum(digits[:9][-2::-2])) % 10) == digits[9]:
        return False
    
    # Butun kontrollerden gecti.
    return True



# tc = input("tc'nizi giriniz...")
# print(isValidTCID(tc))
