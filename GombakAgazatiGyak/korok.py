korok=[]

for i in range(5):
    kor=int(input("Adj meg korokat: "))
    korok.append(kor)

hetvenfelett=0
for szam in korok:
    if szam >70:
        hetvenfelett=szam
        break

index=korok.index(hetvenfelett)
print(f"Az első 70 feletti kor indexe: {index}")
print(":".join(str(k) for k in korok))

with open("korok.txt","w",encoding='utf-8') as f:
    f.write(f"Az első 70 feletti kor indexe: {index}")