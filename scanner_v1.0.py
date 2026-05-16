import socket


IPList = []
PortList = []

while True:

    user = input("Please Enter or close: ").strip().lower()
  
    if user == "close":
        break

    else:
        
        
        while True:
            add = input("Add target or no: ").strip().lower()
            if add == "no":
                break

            else:
              IPscann = input("Please Enter IP :")
              Port = int(input("Please Enter Port : "))

              
              IPList.append(IPscann)
              
              PortList.append(Port)


        for target,port in zip(IPList,PortList):
         
         scan = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

         scan.settimeout(1)

         sok = scan.connect_ex((target,port))
         print("Scanning........")

         if sok == 0:
                 print("Conncted".center(40,"#"))

         else:
                 print("DsConncted".center(40,"#"))
    
         scan.close()

IPList.clear()
PortList.clear()



    


