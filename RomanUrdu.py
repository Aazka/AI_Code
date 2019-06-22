Array=["sifar","aik","dou","teen","chaar","panch","chay","saat","aath","nou","dass",
       "giarah","barah","terah","chaudah","pandrah","solah","satarah","aatharah","unnees",
       "bees","ikkees","baais","taees","chaubees","pachis","chabbis","stais","athais","untees",
       "tees","iktees","battis","tantees","chauntis","pantees","chatees","santees","arthees","untaalis","chalis",
       "iktalis","bialis","tantails","chavalis","pantalis","chiyalis","santalis","artalis","unchaass","pachas",
       "ikyavan","bavan","tarippan","chawwan","pachpan","chappan","stavan","athavan","unsathh","saath",
       "iksath","basath","traisath","chaunsath","painsath","chiyasath","sarsath","arsath","unhattar","sattar",
       "ikhattart","behattar","tihattar","chauhattar","pechatter","chihattar","sathattar","athhattar","unasi",
       "assi","Ikaasi","Bayasi","tiraasi","chaurassi","pechaasi","chiaasi","sataasi","athassi","navassi","Navvay",
       "Ikaanvey","Baanvay","Tiraanvay","Chauraanvay","Pachaanvay","Chiyaanvay","Sataanvay","Athaanvay","Ninaanvay"]

def InputAndValidation():
   while True: 
    I = input("Enter the integer number from range 0 to 9999 " )
    #value=int(I)
    try:
        value=int(I);
        if(value>=0 and value<=9999):
            return I
        else:
            print("Invalid")
    except ValueError:
        print("invalid")
   

Input=InputAndValidation()
#val=int(Input)
if(len(Input)==1):
    print(Array[int(Input[0])])
elif(len(Input)==2):
    val=int(Input[0])
    val=(val*10)+int(Input[1])
    print(Array[val])
elif(len(Input)==3):
    if(int(Input[0])==0):
        val=int(Input[1])
        val=(val*10)+int(Input[2])
        print(Array[val])
    elif(int(Input[0])==0 and int(Input[1])==0):
            print(Array[val])
    elif(int(Input[1])==0 and int(Input[2])==0):
            print(Array[int(Input[0])],"so")
    else:
        val=(int(Input[1])*10)+int(Input[2])
        print(Array[int(Input[0])],"so",Array[val])
elif(len(Input)==4):
    if(int(Input[0])==0 and int(Input[1])!=0):#case 0100
        val=(int(Input[2])*10)+int(Input[3])
        if(val==0):
            {
                    print(Array[int(Input[1])],"so")
            }
        else:
            print(Array[int(Input[1])],"so",Array[val])
        
    elif(int(Input[0])==0 and int(Input[1])==0 and int(Input[2])!=0):#case 0010
        val=int(Input[2])
        val=(val*10)+int(Input[3])
        print(Array[val])
    elif(int(Input[0])==0 and int(Input[1])==0 and int(Input[2])==0):#case 0001
        print(Array[int(Input[3])])
    elif(int(Input[1])==0 and int(Input[2])==0 and int(Input[0])!=0 and int(Input[3])!=0):#case 1001
        print(Array[int(Input[0])],"hazar",Array[int(Input[3])])
    elif(int(Input[1])==0 and int(Input[2])!=0):#case 1010
        print(Array[int(Input[0])],"hazar",Array[int(Input[2])*10+int(Input[3])])
    elif(int(Input[0])!=0 and int(Input[1])!=0 and int(Input[2])==0 and int(Input[3])==0):
        # a=int(Input[2])*10+int(Input[3])
         print(Array[int(Input[0])],"hazar",Array[int(Input[1])],"so")
    else:
        a=int(Input[2])*10+int(Input[3])
        #print(a)
        if(a == 0):
            {
                    print(Array[int(Input[0])],"hazar")
            }
        else:
             print(Array[int(Input[0])],"hazar",Array[int(Input[1])],"so",Array[a])
     