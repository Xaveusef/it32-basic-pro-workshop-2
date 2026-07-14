quantity = int(input("จำนวนที่รับมาขาย: "))
cost_price = int(input("ต้นทุนของปืนที่รับมา: "))
sell_price = float(input("ราคาที่จะนำไปขายต่อ: "))
team_member = int(input("จำนวนลูกน้องในทีมที่ไปทำงาน: "))

total_gun = cost_price * quantity
total_gun = float(total_gun)
print (f"ต้นทุนทั้งหมด {total_gun} บาท")

transfer = quantity * sell_price
transfer = float(transfer)
print (f"รายรับทั้งหมด {transfer} บาท")

real_m = transfer - total_gun
print (f"กำไรสุทธิ {real_m} บาท") 

transfer_boss = real_m * 0.2
transfer_boss = float(transfer_boss)
print (f"จำนวนเงินที่หักไปให้บอส {transfer_boss} บาท")

transfer_team = real_m * 0.8
transfer_team /= team_member
transfer_team = float(transfer_team)
print (f"จำนวนเงินที่ลูกน้องแต่ละคนได้ {transfer_team} บาท")
print ("------------------------------------")

name = input("ชื่อ: ")
age = input("อายุ: ")
height = input("ส่วนสูง: ")
pocket = input("เงินติดตัว: ")

if age > 18 :
    print (f"คุณผ่านเกณฑ์")
else :
    print (f"คุณไม่ผ่านเกณฑ์เนื่อจากคุณอายุ {age} ปี")
##print (f"{quantity} กระบอก")
##print (f"{cost_price} บาท")
##print (f"{sell_price} บาท")
##print (f"{team_member} บาท")
