# 3. WAP to distribute K apples to N students

N= int(input("Enter number of students, 'N': "))
K= int(input("Enter number of apples, 'K': "))

print("Each students will get "+str(int(K/N))+" apples with "+ str(K%N) + " remaining in the basket")
