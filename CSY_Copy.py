print("-------Input Following Value ------")
Denier = int(input("Enter Denier to be Start : "))
moist = float(input("Enter considerable moisture : "))
mc_speed = int(input("Enter Machine speed : "))
Glue  = eval(input('''Enter Glue "LG"/"XG"/"SG" : '''))
FPC = eval(input("Finish Pump Capacity : "))
SpGravity = eval(input("Current Specific Gravity of Viscose or default( 1.1 ): "))
VPC = eval(input("Viscose Pump Capacity : "))

print("==============================================\n")

print("--------Parameter To be Set--------------")






# Finish Rate

# 1. Controlled Denier (CD)


moisture = moist / 100
CD = Denier - (Denier * moisture)
# print(CD)

# 2.  Production/module/min
PMD = (CD * mc_speed * 4) / 9000
# print("Production per module per minute = ", PMD)

# 3. Finish Required
# Glue

if Glue == "LG" and Denier <= 60:
    TSC = 0.04
elif Glue == "LG" and Denier > 60:
    TSc = 0.025
elif Glue == "SG":
    TSC = 0.0475
elif Glue == "XG":
    TSC = 0.07
else:
    TSC  =  float(Glue / 100)

FR = TSC * PMD
# print("Finish Required : ", FR, "Module/min")

# 4. Actual Finish Required on Module per minute

AFR = FR / (7/100)
print("Actual Finish Required on Module : ", AFR, "/ minute")

# Finish RPM
FRPM = AFR / FPC
print("Finish RPM : ", FRPM)


# Spinning RPM

# 1.  Spinning Controlled Denier(SCD)
SCD =  Denier - (Denier * (moisture + TSC))
# print("Spinning Controlled Denier : ",SCD)

# 2. Gram of Viscose (GV)
    # CC = Cellulose content
CC = 8.7
GV = (SCD / CC)*100
# print("Gram of Viscose : ",(GV))

# 3. Volume of Viscose(VV)
VV = GV / SpGravity
# print("Volume of Viscose : ", VV, "cc")

# 4. Time required for 9000 meter
# length of yarn per minute(LY)
LY = 9000
TR = LY / mc_speed
# print("Time required for 9000 meter : ", TR , "minute")

# 5. Viscose Pump Throw (VP_Throw)
VP_Throw = VV / TR
print("Viscose Pump Throw : ", VP_Throw , " cc/min")

# 6. Spinning RPM (SRPM)
SRPM = VP_Throw / VPC
print("Spinning RPM : ",SRPM)