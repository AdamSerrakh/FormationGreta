
caractere_a = ord('a')
caractere_z = ord('z')
print(caractere_a, caractere_z)
minuscule = traduction = ''
for i in range(caractere_a,caractere_z+1):
    minuscule+= chr(i)
    correspondance = i + 13
    if  correspondance <= caractere_z:
        traduction += chr(correspondance)
    else :
        traduction += chr(correspondance - 26)
    
print(minuscule, traduction)
#abcdefghijklmnopqrstuvwxyz
#nopqrstuvwxyzabcdefghijklm

def rot13(text):
    return text.translate(str.maketrans(minuscule,traduction))
def main():
    txt = "ncceraqer clguba rfg ha oba cbvag q'rageér qnaf yr zbaqr zreirvyyrhk qr y'vasbezngvdhr"
    print(rot13(txt))
	
if __name__ == "__main__":
    main()
