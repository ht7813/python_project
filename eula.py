def CheckEula():
    EggIsOn = 0
    AllowEula = 0
    with open("eula") as f:
      t = f.read()
      if t[0] == "t":
          AllowEula = 1
def Egg():
    EggIsOn = 1