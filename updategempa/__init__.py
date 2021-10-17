def ekstraksi_data():
    def ekstraksi_data():
        """
        Tanggal : 16 Oktober 2021
        Waktu : 8:13:07 WIB
        Magnitudo : 3.9
        Kedalaman : 9 km
        Lokasi : 'LS'=0.61 LS, BT=131.32
        Pusat Gempa: Pusat gempa berada di Laut 30 km TimurLaut Sorong
        Dirasakan : Dirasakan (Skala MMI): II-III Sorong
        """
        hasil = dict()
        hasil['tanggal'] = '16 Oktober 2021'
        hasil['waktu'] = '8:13:07 WIB'
        hasil['magnitudo'] = 3.9
        hasil['kedalaman'] = '9 km'
        hasil['lokasi'] = {'LS': 0.61, 'BT': 131.32}
        hasil['pusat'] = 'Pusat gempa berada di Laut 30 km TimurLaut Sorong'
        hasil['dirasakan'] = 'Dirasakan (Skala MMI): II-III Sorong'
        print(hasil)

        return hasil

    def tampilkan_data(result):
        print('Gempa terakhir berdasarkan BMKG')
        print(f"Tanggal : {result['tanggal']}")
        print(f"Waktu : {result['waktu']}")
        print(f"Magnitudo : {result['magnitudo']}")
        print(f"Lokasi : LS:{result['lokasi']['LS']}, BT:{result['lokasi']['BT']} ")
        print(f"Pusat : {result['pusat']}")
        print(f"Dirasakan : {result['dirasakan']}")