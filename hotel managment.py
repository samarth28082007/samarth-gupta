
1sel=int(input("Select rooms from the above choices(1-4):"))
n=int(input("Enter the no. of days of stay:"))
if(sel==1):
    princ=1400
elif(sel==2):
    princ=2200
elif(sel==3):
    princ=2600
else:
    princ=3500


gst=princ*n*0.2

print("Amount(exclusing gst):",princ*n)

 
print("Total Amount(excluding GST):",(princ*n)+gst)
Record={}

while True:
    print("......Guestes check in.....")
    
    name=input("~Enter Name:")
    citizen=input("~Enter the nationality of the guests:")
    addres=input("~Enter guest permanent address:")
    in_time=(input("~Enter check in date and time in formate(dd/mm/yyyy hh:mm):"))
    out_time=(input("~Enter check out date and time in formate(dd/mm/yyyy hh:mm):"))
    room_no=int(input("~Enter room number:"))
    phone=int(input("~enter guets phone number:"))
    if citizen=="Indian":
        adha=(int(input("Adhar card no:")))
    else:
        adha=("passport Needed")
    Record[room_no]={'Name':name,'Citizenship':citizen,'Phone':phone,'Address':addres,'Check in time':in_time,'Adhaar No.':adha,'Check out time':out_time,'Room no':room_no}
    next_entery=input("lets fill the next entry?(yes/no):")
    if next_entery=="no":
        break
print("Room types and their prices(per night)/n")
print(Record)