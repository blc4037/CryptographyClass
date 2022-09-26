filename = input('name file')
final = filename + '.html'
userinput= str(input("enter text you want to input to the html file:\n"))
uupper = userinput.upper()
print(uupper)
pgo = uupper.replace(" ",'')
print(pgo)
with open (final, 'w') as file:
    file.write(pgo)
