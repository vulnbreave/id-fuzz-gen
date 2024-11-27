from pyfiglet import Figlet

f = Figlet(font='slant')  
text = "ID-FUZZ-GEN"
print(f.renderText(text))
print("Author:\t(https://github.com/vulnbreave)")

print("\n\n\n")

print("Generates numbers ranging from 1 to N. Particularly made for IDOR Fuzzing.")
print("\n\n")
print("Example: 4")
print("1\n2\n3\n4\n")
x = int(input("Give your input here >> "))
f = open('payload.txt', 'w')
for y in range(x):
    y=y+1
    print(y)
    f.write(f"{y}\n")
    
print('\n\nOutput written to file "payload.txt" in your current directory. Happy Hacking ;)')
