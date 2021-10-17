"""
Aplikasi memonitoring berita terupdate
Modularisasi dengan package
"""
from gempaterkini import ekstraksi_data

if __name__ == '__main__' :
    print('Aplikasi utama')
    result = ekstraksi_data()
    tampilkan_data(result)