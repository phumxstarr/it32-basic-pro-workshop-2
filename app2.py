name = input("Enter name : ")
age = int(input("Enter age : "))
hei = int(input("Enter height : "))
pow = int(input("Enter power : "))
mon = int(input("Enter money : "))
if name == name and age <= 14 and hei <= 155 and pow <= 4 and mon <= 4 :
    print("---------------- ผลพิจารณา ----------------")
    print(f"ยินดีต้อนรับ {name} ตำแหน่งคือ : ภารโรงล้างจาน")
elif name == name and age <= 18 and hei <= 175 and pow <= 8 and mon <= 15 :
    print("---------------- ผลพิจารณา ----------------")
    print(f"ยินดีต้อนรับ {name} ตำแหน่งคือ : ลูกกระจ๊อก")
else :
    print("---------------- ผลพิจารณา ----------------")
    print(f"ยินดีต้อนรับ {name} ตำแหน่งคือ : ลูกน้องมาเฟีย")