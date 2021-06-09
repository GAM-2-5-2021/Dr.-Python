import information as i

print("Pozdrav! Ja sam Dr. Python i ja Vam pomažem u imenovanju dijelova tijela na latinskom jeziku!")
print("Samo upiši redni broj ispred opcije koju želiš odabrati.")

general=input("1.Trup\n2.Gornji ud\n3.Donji ud\n")

if general in ["1.","1"]:
    trup=input("1.Prednji trup\n2.Stražnji dio\n")
    if trup in ["1.","1"]:
        print(i.prednji_dio)
    if trup in ["2.","2"]:
        print(i.straznji_dio)

if general in ["2.","2"]:
    udGornji=input("1.Nadlaktica (brachium)\n2.Podlaktica (ante-brachum)\n3.Dlan (manus)\n")
    if udGornji in ["1.","1"]:
        print(i.nadlaktica)
    if udGornji in ["2.","2"]:
        print(i.podlaktica)
    if udGornji in ["3.","3"]:
        print(i.dlan)

if general in ["3.","3"]:
    udDonji=input("1.Natkoljenica (femur)\n2.Potkoljenica (crus)\n3.Stopalo (pes)\n")
    if udDonji in ["1.","1"]:
        print(i.nadkoljenica)
    if udDonji in ["2.","2"]:
        print(i.potkoljenica)
    if udDonji in ["3.","3"]:
        print(i.stopalo)