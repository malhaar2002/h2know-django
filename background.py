import serial

f = open("vol_data.txt","r")
old_vol = float(f.read())
f.close()

t = open("floor_data.txt","r")
dt = list((t.read()).split(" "))
for i in range(len(dt)):
    dt[i] = float(dt[i])
t.close()
o_v = dt[2]

ser = serial.Serial('/dev/ttyACM0', 9600)

def update():
    f_r = ser.readline()
    string_n = f_r.decode()
    string = string_n.rstrip()
    f = open("vol_data.txt","w+")
    t = open("floor_data.txt","w+")
    flt = float(string)
    flt1 = float(string)
    flt1 = o_v + flt1
    dt[2] = flt1
    l = str(dt[0])
    for i in dt[1:]:
        l = l + " " + str(i)
    t.write(l)
    t.close()
    flt = flt + old_vol
    f.write(str(flt))
    f.close()

while True:
    update()