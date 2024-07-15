freetime = True
AM = True
PM = True

yuuki = [freetime, AM, PM]

if yuuki[0] and yuuki[1]:
    print("かえります")
elif yuuki[0] and yuuki[2]:
    print("かえりません")
else:
    print("寝ます")