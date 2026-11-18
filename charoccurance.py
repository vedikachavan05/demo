s=input("Enter a string:")
ascii=[0]*26
index=0
def charoccurance(s):
    for i in range(len(s)):
        c=ord(s[i])
        if 97 <= c <=122:
            index=c-97
            ascii[index]+=1
    print("the occurance of string is\n")
    print(ascii)
    
def charprint(s):
    for i in range (len(s)):
        print("the string is\n")
        if ascii[i]>0:
         char=(chr(i+97))
         print(f"{char}:{ascii[i]}")
charoccurance(s)
charprint(s)