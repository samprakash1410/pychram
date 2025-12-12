with open("sample.txt","r") as f:
     
     data=f.read()
     print(data)
     print(type(data))

     with open("sample.txt","w")as f:
          data=f.write("iam buying a new macbook m5 pro")
          print(data)
          