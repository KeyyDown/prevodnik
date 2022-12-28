src_units = ['mm', 'cm', 'mm', 'cm', 'dm', 'mm', 'km', 'cm', 'km', 'dm', 'km', 'mm', 'cm', 'dm', 'm', 'm', 'm', 'm', 'km', 'km', 'ly', 'g', 'g', 'kg', 'kg', 't', 't', 'B', 'B', 'B', 'B', 'kB', 'kB', 'kB', 'kB', 'MB', 'MB', 'MB', 'MB', 'GB', 'GB', 'GB', 'GB', 'TB', 'TB', 'TB', 'TB', 'l', 'l', 'l', 'ml', 'ml', 'ml', 'm³', 'm³', 'm³', 'hl', 'hl', 'hl']
dest_units = ['cm', 'mm', 'dm', 'dm', 'cm', 'km', 'mm', 'km', 'cm', 'km', 'dm', 'm', 'm', 'm', 'mm', 'cm', 'dm', 'km', 'm', 'ly', 'km', 'kg', 't', 'g', 't', 'g', 'kg', 'kB', 'MB', 'GB', 'TB', 'MB', 'GB', 'TB', 'B', 'B', 'kB', 'GB', 'TB', 'B', 'kB', 'MB', 'TB', 'B', 'kB', 'MB', 'GB', 'ml', 'm³', 'hl', 'l', 'm³', 'hl', 'l', 'ml', 'hl', 'l', 'ml', 'm³']
transform_units = [0.1, 10, 0.01, 0.1, 10, 0.000001, 1000, 0.00001, 10000, 0.0001, 10000, 0.001, 0.01, 0.1, 1000, 100, 10, 0.01, 1000, 1.050008340247048e-13, 9460730472580, 0.001, 0.000001, 1000, 0.001, 1000000, 1000, 0.0009765625, 0.000000954, 9.3132257e-10, 9.094947e-13, 0.0009765625, 0.000000954, 9.3132257e-10, 1024, 1048576, 1024, 0.0009765625, 0.000000954, 1073741824, 1048576, 1024, 0.0009765625, 1,099511628e12, 1073741824, 1048576, 1024, 1000, 0.001, 0.01, 0.001, 0.000001, 1000, 1000000, 10, 100, 100000, 0.1]
a = 0



def MainMenu():
    print("                                                                                                                                                      ")
    print("______________________________________________________________________________________________________________________________________________________")
    print("Wlecome! Select what do you want to convert:")
    print("Please type a ID number what do you want to convert (the ID number is writen before each option for converting.)")
    print("1[Lenght]")
    print("2[Mass]")
    print("3[Data size]")
    print("4[Capacity]")

def numid():
    return str(input("Write ID number:"))

def DataMenu():
    print("_______________________________________________________________________________________")
    print("Please write down ID number again. NOTE: this is for the  submenu not for the main menu!")
    print("27  [B to kB]")
    print("28  [B to MB]")
    print("29  [B to GB]")
    print("30  [B to TB]")
    print("31 [kB to MB]")
    print("32 [kB to GB]")
    print("33 [kB to TB]")
    print("34  [kB to B]")
    print("35  [MB to B]")
    print("36 [MB to kB]")
    print("37 [MB to GB]")
    print("38 [MB to TB]")
    print("39  [GB to B]")
    print("40 [GB to kB]")
    print("41 [GB to MB]")
    print("42 [GB to TB]")
    print("43  [TB to B]")
    print("44 [TB to kB]")
    print("45 [TB to MB]")
    
    

def MassMenu():
    print("_______________________________________________________________________________________")
    print("Please write down ID number again. NOTE: this is for the  submenu not for the main menu!")
    print(" 21[g to kg]")
    print("  22[g to t]")
    print(" 23[kg to g]")
    print(" 24[kg to t]")
    print("  25[t to g]")

def CapMenu():
    print("_______________________________________________________________________________________")
    print("Please write down ID number again. NOTE: this is for the  submenu not for the main menu!")
    print("47[l to ml]")
    print("48[l to m³]")
    print("49[l to hl]")
    print("50[ml to l]") 
    print("51[ml to m³]") 
    print("52[ml to hl]") 
    print("53[m³ to l]") 
    print("54[m³ to ml]") 
    print("55[m³ to hl]") 
    print("56[hl to l]") 
    print("57[hl to ml]") 
    

def LenghtMenu():
    print("_______________________________________________________________________________________")
    print("Please write down ID number again. NOTE: this is for the second menu not for the first!")
    print("  0[mm to cm]")
    print("  1[cm to mm]")
    print("  2[mm to dm]")
    print("  3[cm to dm]")
    print("  4[dm to cm]")
    print("  5[mm to km]")
    print("  6[km to mm]")
    print("  7[cm to km]")
    print("  8[km to cm]")
    print(" 9[dm to km]")
    print(" 10[km to dm]")
    print("  11[mm to m]")
    print("  12[cm to m]")
    print("  13[dm to m]")
    print("  14[m to mm]")
    print("  15[m to cm]")
    print("  16[m to dm]")
    print("  17[m to km]")
    print("  18[km to m]")
    print(" 19[km to ly]")


def convert(src_unit, dest_unit, transform_unit):
    print("                                    ")
    c = input("Write how many " + src_unit + " do you want to convert:")
    d = float(c) * transform_unit
    print(str(d) + " " + dest_unit)

e = "y"
while e == "y" or e == "Y":
    MainMenu()
    a = numid()
    

    if a == "2":
        MassMenu()
        b = int(input(" 26[t to kg]"))
        if b < 22:
            exit(1)
        
    if a == "1":
        LenghtMenu()
        b = int(input(" 21[ly to km]"))
        if b > 21:
            exit(1)
    if a == "3":
        DataMenu()
        b = int(input("46 [TB to GB]"))
        
    if a == "4":
        CapMenu()
        b = int(input("58[hl to m³]"))
          
    src_unit = src_units[b]
    dest_unit = dest_units[b]
    transform_unit = transform_units[b]
    convert(src_unit, dest_unit, transform_unit) 

    e = input("Do you want to continue? [Y/N]")