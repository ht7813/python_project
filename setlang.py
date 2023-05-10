with open("lang") as f:
    t = f.read()
    if t[0] == "z":
        string_main_upperlimit = "请设置随机数上限:"