def upperlower():
    sentence=input("enter a sentence :")
    sentence=sentence.replace(" ",'')
    upper_count,lower_count=0,0
    for char in sentence:
        if char.isupper(): 
            upper_count+=1
        else:
            lower_count+=1
    print("no of upper case characters :",upper_count)
    print("no of lower case characters :",lower_count)

upperlower() #calling the function

