def toplam():
    sonuc = 0
    while True:
        try:
            num = int(input("enter the num: "))
            if num < 1000 and num > -1000:
                sonuc += num
            else:
                break
        except ValueError:
            print("please enter only num")
    return sonuc

print("total sum:",toplam())