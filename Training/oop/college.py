
class College:
    def __init__(self, cname, caddr, noofdepts):
        self.cname = cname
        self.addr = caddr
        self.noofdepts = noofdepts

    def display_college_info(self):
        print(f'Name : {self.cname} \t Addr: {self.addr}, \t Department count: {self.noofdepts}')
        