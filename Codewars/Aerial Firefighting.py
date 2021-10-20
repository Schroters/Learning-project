# Aerial Firefighting
# https://www.codewars.com/kata/5d10d53a4b67bb00211ca8af

def waterbombs(fire, w):
    new_string = fire.split("Y")
    result = 0
    print(new_string, w)
    for lst in new_string:
        w_cnt = lst.count("x")
        print("count W:", w_cnt)
        if w_cnt == 0:
            continue
        if w_cnt % w != 0 and w < w_cnt:
            print("first exception")
            result += (w_cnt // w) + 1
        else:
            if w < w_cnt:
                print("second first exception")
                result += w_cnt // 2
            else:
                print("second second exception")
                result += 1
    return result


print(waterbombs("xxxxYxYx", 4))    # 3
print(waterbombs("xxYxx", 3))       # 2
print(waterbombs("xxYxx", 1))       # 4
print(waterbombs("xxxxYxYx", 5))    # 3
print(waterbombs("xxxxxYxYx", 2))   # 5
print(waterbombs("xxYxYYxYxYxxxxxxY", 6))   # 5
print(waterbombs("xxxxYxYYxxxxYxxxxxx", 2))   # 8
