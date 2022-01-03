class Koordinat(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

#bisa dipisah menjadi dua file
def main():
    titik_c = Koordinat(4,5)
    titik_asal = Koordinat(0,0)
    print("titik c: x=",titik_c.x,"y=",titik_c.y)
    print("titik asal: x=",titik_asal.x,"y=",titik_asal.y)
    titik_c.x = 12
    print("titik c: x=",titik_c.x,"y=",titik_c.y)

if __name__ == "__main__":
    main()
