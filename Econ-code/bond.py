def pv_bond():
    face_value = float(raw_input("Enter your amount:"))
    coupon = float(raw_input("Enter your coupon rate:"))
    rate = float(raw_input("Enter your intrest rate:"))
    term = float(raw_input("Enter the length of your bond:"))
    index= 1
    bond= face_value
    while index < term:
         bond += (coupon)/((1+rate)**index)
         index += 1
    bond += (coupon )/((1 + rate)**index)
    bond = bond + face_value
    return bond

def alternative_bond():
    face_value = float(raw_input("What is the amount you would like to invest amount:"))
    coupon = float(raw_input("Enter the market coupon rate:"))
    rate = float(raw_input("Enter the current intrest rate:"))
    term = float(raw_input("Enter the length of the bond you would like:"))
    index= 1
    bond= face_value
    while index < term:
         bond += (coupon)/((1+rate)**index)
         index += 1
    bond += (coupon )/((1 + rate)**index)
    bond = bond + face_value
    return bond
a = pv_bond()
al= pv_bond()


if (a - al) >= 0:
    print " You have a better deal than the market"
elif (a-al) == 0:
    print "Your equal with the market"
elif (a- al)<= 0:
    print" The market is producing better results"