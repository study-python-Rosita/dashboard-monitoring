"""
Aplikasi memonitoring berita terupdate
Modularisasi dengan package
"""
import updategempa
from updategempa import tampilkan_data

if __name__ == '__main__' :
    print('Aplikasi utama')
    result = updategempa.ekstraksi_data()
    tampilkan_data(result)