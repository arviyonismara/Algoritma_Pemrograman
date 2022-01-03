def pasanganNimNama(nim,nama):
    return nim,nama

def tukarNamaNim(tNimNama):
    # nim = tNimNama[0]
    # nama = tNimNama[1]
    # (nim,nama) = (nama,nim)
    return (tNimNama[0],tNimNama[1])

def main():
    (nm,nam) = pasanganNimNama("A11.222.22","Adi")
    print(nm," ",nam)
    (nm,nam) = tukarNamaNim((nm,nam))
    print(nm," ",nam)

if __name__ == "__main__":
    main()
