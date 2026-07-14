#input
quantity = int(input("จำนวนปืนที่รับมาขาย : "))
cost_price = int(input("ต้นทุนของปืนที่รับมา : "))
sell_price = int(input("ราคาที่จะนำไปขายต่อ : "))
team_members = int(input("จำนวนลูกน้องในทีมที่ไปทำงาน : "))

cost = quantity * cost_price
revenue = quantity * sell_price
profit = revenue - cost
boss = profit * 0.2 #คูณ 0.20
membersincome = (profit - boss) / quantity

#output
print("ต้นทุนทั้งหมด : " , cost , "บาท")
print("รายรับทั้งหมด : " , revenue , "บาท")
print("ได้กำไร : " , profit , "บาท")
print("บอสได้รับ : " , boss , "บาท")
print("มีลูกน้อง : " , team_members  , "คน" , "และจะได้คนละ" , membersincome , "บาท")


