public Sonuc Dizilim()
{
    int i;
    // Önceki dizilimden dolayı hepsi dizilmiş gözükecek. Bu yüzden hepsini dizilmedi haline getiriyoruz.
    for (i = 0; i < sekiller.Count; i++)
        sekiller[i].dizildiMi = false;

    Fonksiyonlar.TablaSifirla(tabla, TABLA_ENI, TABLA_BOYU);

    int kullanilmayanPikselSayisi = 0;
    int tablaSayisi = 0;
    Sonuc sonuc = new Sonuc(tablaSayisi, kullanilmayanPikselSayisi = 0, sekiller);

    int sekillerIndis = 0;
    int tablaX;
    int tablaY;
    int dizilenSekilSayisi = 0;
    bool yeniBolum = true;
    bool yeniTabla = true;
    bool bolumeYeniSekilDizilebiliyor;

    int bolumBaslangici = 0;
    int bolumEni = 0;

    while (dizilenSekilSayisi < sekiller.Count())
    {
        bolumeYeniSekilDizilebiliyor = false;

        if (yeniTabla == true)
        {
            tablaSayisi++;
            //DiziFonksiyonlari.cokBoyutluDiziSifirla(tabla, TABLA_ENI, TABLA_BOYU);
            yeniBolum = true;
            yeniTabla = false;
            bolumBaslangici = 0;
        }

        if (yeniBolum == true)
        {
            bolumEni = sekiller[sekillerIndis].en;
            yeniBolum = false;
        }

        for (tablaY = 0; tablaY <= TABLA_BOYU - sekiller[sekillerIndis].boy; tablaY++)
        {
            for (tablaX = bolumBaslangici; tablaX <= bolumBaslangici + bolumEni - sekiller[sekillerIndis].en; tablaX++)
            {
                if (sekilKontrol(sekiller[sekillerIndis], tablaX, tablaY, tabla) == true)
                {
                    //Console.WriteLine("--Şeklin yerleştiği yerin sol üst köşesinin x koordinatı:  " + tablaX + " y koordinatı:  " + tablaY + "\n");
                    sekilYerlestir(sekiller[sekillerIndis], tablaX, tablaY, tabla);
                    sekiller[sekillerIndis].dizildiMi = true;
                    dizilenSekilSayisi++;
                    goto cik1;
                }
            }
        }
        cik1: { }

        if (dizilenSekilSayisi == sekiller.Count())
        {
            sonuc.tablaSayisi = tablaSayisi;
            sonuc.kullanilmayanPikselSayisi = kullanilmayanPikselSayisi;
            //sonuc.yazdir();
            kullanilmayanPikselSayisi = 0;
            return sonuc;
        }

        for (i = 0; i < sekiller.Count(); i++)
        {
            if (sekiller[i].dizildiMi == false)
            {
                //Console.WriteLine("--Numara: " + sekiller[i].numara + " ----En: " + sekiller[i].en + " ----Boy: " + sekiller[i].boy);
                for (tablaY = 0; tablaY <= TABLA_BOYU - sekiller[i].boy; tablaY++)
                {
                    for (tablaX = bolumBaslangici; tablaX <= bolumBaslangici + bolumEni - sekiller[i].en; tablaX++)
                    {
                        if (sekilKontrol(sekiller[i], tablaX, tablaY, tabla) == true)
                        {
                            bolumeYeniSekilDizilebiliyor = true;
                            //Console.WriteLine("----" + sekiller[i].numara + " numaralı şekil bulunulan bölüme yerleşebiliyor!\n");
                            sekillerIndis = i;
                            goto cik2;
                        }
                    }
                }
            }
        }
        cik2: { }

        if (bolumeYeniSekilDizilebiliyor == false)
        {
            yeniBolum = false;
            bolumBaslangici += bolumEni;

            for (i = 0; i < sekiller.Count(); i++)
            {
                if (sekiller[i].dizildiMi == false)
                {
                    if (bolumBaslangici + sekiller[i].en <= TABLA_ENI)
                    {
                        //Console.WriteLine("----Yeni bölüme geçiliyor! " + sekiller[i].numara + " numaralı şekil yeni bölümün ilk şeklidir.\n");
                        yeniBolum = true;
                        sekillerIndis = i;
                        goto cik3;
                    }
                }
            }
            cik3: { }

            if (yeniBolum == false)
            {
                yeniTabla = true;
                kullanilmayanPikselSayisi += Fonksiyonlar.KullanilmayanPikselSayisi(tabla, TABLA_ENI, TABLA_BOYU);
                Fonksiyonlar.TablaSifirla(tabla, TABLA_ENI, TABLA_BOYU);
                //Console.WriteLine("------Yeni tablaya geçiliyor!");
                i = 0;
                while (sekiller[i].dizildiMi == true)
                    i++;
                sekillerIndis = i;
                //Console.WriteLine(" " + sekiller[sekillerIndis].numara + " numaralı şekil yeni tablanın ilk şeklidir.\n");
            }
        }
    }
    return sonuc;
}

public bool YeniBolumOlusturulabiliyorMu(int bolumBaslangici)
{
    int sekillerIndis;           

    for(sekillerIndis = 0; sekillerIndis < sekiller.Count; sekillerIndis++)
    {
        if(sekiller[sekillerIndis].dizildiMi == false)
        {
            if ((TABLA_ENI - sekiller[sekillerIndis].en) >= bolumBaslangici)
                return true;
        }
    }

    return false;
}

public bool sekilKontrol(Sekil sekil, int x, int y, int[,] tabla) // sekil -> kontrol edilecek sekil, (x,y) -> kontrolün yapılacağı yerin sol alt köşesinin x ve y koordinatları
{
    int i, j;

    for (i = 0; i < sekil.boy; i++)
    {
        for (j = 0; j < sekil.en; j++)
        {
            if (tabla[x + j, y + i] != 0)
                return false;
        }
    }            
    return true;
}

public void sekilYerlestir(Sekil sekil, int x, int y, int[,] tabla) // sekil -> kontrol edilecek sekil, (x,y) -> kontrolün yapılacağı yerin sol alt köşesinin x ve y koordinatları
{
    int i, j;

    for (i = 0; i < sekil.boy; i++)
    {
        for (j = 0; j < sekil.en; j++)
        {
            if (sekil.yapi[j, i] == 1)
                tabla[x + j, y + i] = sekil.numara;
            else
                tabla[x + j, y + i] = 0;
        }
    }
}