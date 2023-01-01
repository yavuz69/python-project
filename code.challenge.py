print("###  This program converts milliseconds into hours, minutes, and seconds ###") 
print("To exit the program, please type 'exit'")

        
def time_count(user_input):
    dict={"hour/s":3600000,"minute/s":60000,"second/s":1000}
    result = 0
    yazici = ""
    for key,value in dict.items():
        if user_input >= value:
            result = user_input // value
            user_input = user_input % value
            yazici += str(result) + " " + key + " "
    return yazici

print("###  This program converts milliseconds into hours, minutes, and seconds ###")
print("To exit the program, please type 'exit'")
while True:
# Kullanıcıdan bir numara isteyin
    user_input =input("Please enter the milliseconds (should be greater than zero) :  ")
    # Kullanıcı "exit" girerse programdan çıkar
    if user_input.lower() == "exit":
        print("Exiting the program... Good Bye")
        break
    # Kullanıcı girişi geçerli bir sayı değilse, bir hata mesajı gösterin ve tekrar giriş isteyin
    if not user_input.isdigit():
        print("Not Valid Input !!!")
        continue
    if int(user_input)<1:
        print("Not Valid Input !!!")
        continue
    elif int(user_input)<1000:
        print(f"just {user_input} millisecond/s")
        continue
    else:
        print(time_count(int(user_input)))


