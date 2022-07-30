def rev_string():
    word=input("Enter a string : ")
    reverse=''
    for char in word:
        reverse=char+reverse
    return reverse
print("Reversed string :",rev_string())
