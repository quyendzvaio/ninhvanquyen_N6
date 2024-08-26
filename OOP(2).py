class HCN:
    def __init__(self,dai, rong):
        self.dai = dai
        self.rong = rong

    def Perimeter(self):
        return (self.dai + self.rong)*2

    def Area(self):
        return self.dai * self.rong

    def dislay(self):
        print(f'chieu dai HCN = ',self.dai)
        print(f'chieu rong HCN = ',self.rong)
        print(f'chu vi HCN = ',self.Perimeter())
        print(f'Dien tich HCN = ',self.Area())

a = HCN(3,4)
a.dislay()
