"""
Aplikasi memonitoring berita terupdate
Modularisasi dengan package
"""
from updategempa import ekstraksi_data
from updategempa import tampilkan_data

if __name__ == '__main__' :
    print('Aplikasi utama')
    result = ekstraksi_data()
    tampilkan_data(result)