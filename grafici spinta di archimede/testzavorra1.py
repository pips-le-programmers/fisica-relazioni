import find_x as fx


class Measure:
    def __init__(self , measure:str) -> None:
        self.measure = measure.replace("," , ".").split("±")
        self.inc = float(self.measure[1])
        self.m = float(self.measure[0])

class Point:
    def __init__(self , x ,y , name , dist_x=0 , dist_y=0):
        self.x_measure = Measure(x)
        self.y_measure = Measure(y)
        self.x = self.x_measure.m
        self.y = self.y_measure.m
        self.inc_x = self.x_measure.inc
        self.inc_y = self.y_measure.inc
        self.name = name
        self.dist_x = dist_x
        self.dist_y = dist_y


a1 = Point("0,000012	±	0,000001", "0,11	±	0,02","1cm")
a2 = Point("0,000023	±	0,000001","0,21	±	0,02","2cm")
a3= Point('0,000035	±	0,000001','0,31	±	0,02','3cm')
a4= Point('0,000046	±	0,000001','0,40	±	0,02','4 cm')
a5= Point('0,000058	±	0,000002','0,51	±	0,02','5 cm')
a6= Point('0,000069	±	0,000002','0,61 ±	0,02','6 cm')

dati = [a1, a2, a3, a4, a5, a6]
dati_x = [h.x for h in dati]
dati_y = [h.y for h in dati]
inc_x_0 = [h.inc_x for h in dati]
inc_y = [h.inc_y for h in dati]

#chi quadro media
#treshold= valore max chi quadro
coef = 8690

print(fx.find_m(dati_x, dati_y, inc_y,inc_x_0, 13, coef))