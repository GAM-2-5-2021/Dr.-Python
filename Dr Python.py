import information as i

print("Pozdrav! Ja sam Dr. Python i ja Vam pomažem u imenovanju dijelova tijela na latinskom jeziku!")
print("Samo upiši redni broj ispred opcije koju želiš odabrati.")

general=input("1.Trup\n2.Gornji ud\n3.Donji ud\n")

if general=="1.":
    trup=input("1.Prednji trup\n2.Stražnji dio\n")
    if trup=="1.":
        print(i.prednji_dio)
    if trup=="2.":
        print(i.straznji_dio)
if general=="2.":
    udGornji=input("1.Nadlaktica (brachium)\n2.Podlaktica (ante-brachum)\n3.Dlan (manus)\n")
    if udGornji=="1.":
        print(i.nadlaktica)
    if udGornji=="2.":
        print(i.podlaktica)
    if udGornji=="3.":
        print(i.dlan)

    
