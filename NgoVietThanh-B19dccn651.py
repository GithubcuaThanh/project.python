class VienChuc_Thanh:
    def __init__(self, VC_name, VC_age):
        self.VC_name = VC_name
        self.VC_age = VC_age
    def VienChuc_Hoten(self):
        print(f"{self.VC_name}")
    def VienChuc_tuoi(self):
        print(f"{self.VC_age}")
    
VienChuc1 = VienChuc_Thanh('Bui Quang Huy', 2001)
print(f"{VienChuc1.VC_name}     {VienChuc1.VC_age}")
VienChuc2 = VienChuc_Thanh('Doan Huu Quan', 2001)
print(f"{VienChuc2.VC_name}     {VienChuc2.VC_age}")