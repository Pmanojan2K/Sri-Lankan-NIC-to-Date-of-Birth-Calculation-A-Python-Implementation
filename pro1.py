# Srilankan NIC to date of birth calculation

# New NIC
def newNIC(newnic,mnt,d_mnt):
    year=int(newnic[0:4])
    days=int(newnic[4:7])

    # Check gender
    if days > 500:
        days-=500
        # return('Female')

    for day in range (len(mnt)):
        if days >= d_mnt[day]:
            days-=d_mnt[day]
            if days==0:
                month=mnt[day-1]
                days=d_mnt[day]
        else:
            month=mnt[day]
            break
    print("Date :",days,"\nMonth :",month,"\nYear :",year)

# Old NIC
def oldNIC(oldnic,mnt,d_mnt):

    # Concating the 19
    new_fmt="19"+oldnic

    if len(oldnic)==10 and (oldnic[-1]=="V" or oldnic[-1]=="v"):
        newNIC(new_fmt,mnt,d_mnt)
    else:
        print("Incorrect NIC formt :( Please check your NIC..") 

# Month & Days
mnt =  ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
d_mnt=[31,29,31,30,31,30,31,31,30,31,30,31]

# Ask the name
name=input("Enter your name :")

# Select the option
print("Select your NIC format\n",'='*4,"1.Old NIC",'='*4,"\n",'='*4,"2.New NIC",'='*4)
value=int(input())

if value.is_integer:
    nic_opt=['old NIC','new NIC']
    msg="you are selected format so enter your NIC number"

    if value==1:
        print(name,msg[:msg.index('format')],nic_opt[0].upper(),msg[msg.index('format'):])
        oldnic=input()
        oldNIC(oldnic,mnt,d_mnt)
    elif value==2:
        print(name,msg[:msg.index('format')],nic_opt[1].upper(),msg[msg.index('format'):])
        newnic=input()
        newNIC(newnic,mnt,d_mnt)

else:
    print("Please select a number value.")
