k1 = ['a','e','i','o','u']
k2 = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
l = input()
if l in k1:
    print("Vowel")
elif l in k2:
    print("Consonant")
else:
    print("invalid")
