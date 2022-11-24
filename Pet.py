import streamlit as st
import datetime

import time
from PIL import Image

st.write("""
# Miuw-Miuw Pet Shop
Ini adalah Website Penjualan Kebutuhan Kucing
""")
col1, col2, col3 = st.columns(3)
with col1:
    st.write(" ")
with col2:
    st.image("Logo Pet.png")
with col3:
    st.write(" ")

st.write("                             List Nama Product                                   ")
st.write("Kode Product          |        Nama Product        |        Harga Product        ")
st.write(" 1.       001         |       Whiskas 1000gr       |            65000            ")
col1, col2, col3 = st.columns(3)
with col1:
    st.write(" ")
with col2:
    st.image("whiskas 1kg.png")
with col3:
    st.write(" ")
st.write(" 2.       002         |     Royal Canin 1000gr     |           200000            ")
col1, col2, col3 = st.columns(3)
with col1:
    st.write(" ")
with col2:
    st.image("royal 1kg.png")
with col3:
    st.write(" ")
st.write(" 3.       003         |      Maxi Cat Sand 5L      |            30000            ")
col1, col2, col3 = st.columns(3)
with col1:
    st.write(" ")
with col2:
    st.image("maxi cat sand.png")
with col3:
    st.write(" ")
st.write(" 4.       004         |      Aromatic Sand 5L      |            25000            ")
col1, col2, col3 = st.columns(3)
with col1:
    st.write(" ")
with col2:
    st.image("aromatic sand.png")
with col3:
    st.write(" ")
st.write(" 5.       005         |        Snack Me-O          |            25000            ")
col1, col2, col3 = st.columns(3)
with col1:
    st.write(" ")
with col2:
    st.image("snack me.png")
with col3:
    st.write(" ")
st.write(" 6.       006         |       Snack Life Cat       |            10000            ")
col1, col2, col3 = st.columns(3)
with col1:
    st.write(" ")
with col2:
    st.image("life cat.png")
with col3:
    st.write(" ")
st.write(" 7.       007         |    Vitamin Olive Care      |            80000            ")
col1, col2, col3 = st.columns(3)
with col1:
    st.write(" ")
with col2:
    st.image("olive.png")
with col3:
    st.write(" ")
st.write(" 8.       008         |  Vitamin Nutri Plus Gel    |           150000            ")
col1, col2, col3 = st.columns(3)
with col1:
    st.write(" ")
with col2:
    st.image("nutri.png")
with col3:
    st.write(" ")
st.write(" 9.       009         |     Drontal Cat 1 Pcs      |            25000            ")
col1, col2, col3 = st.columns(3)
with col1:
    st.write(" ")
with col2:
    st.image("drontal.png")
with col3:
    st.write(" ")
st.write(" 10.      010         |     Cream Scabies 15gr     |            25000            ")
col1, col2, col3 = st.columns(3)
with col1:
    st.write(" ")
with col2:
    st.image("scabies.png")
with col3:
    st.write(" ")
st.write(" 11.      011         |        Cat Necklace        |            20000            ")
col1, col2, col3 = st.columns(3)
with col1:
    st.write(" ")
with col2:
    st.image("necklace.png")
with col3:
    st.write(" ")
st.write(" 12.      012         |         Baju Kucing        |            50000            ")
col1, col2, col3 = st.columns(3)
with col1:
    st.write(" ")
with col2:
    st.image("baju kucing.png")
with col3:
    st.write(" ")
st.write("---------------------------------------------------------------------------------")
st.write("")

Nama =st.text_input("Nama Pembeli : ")
Nomor =st.text_input("Nomor Telepon : ")
Jumlah =st.number_input("Jumlah Barang Yang Dibeli : ", 0)
Kode =st.text_input("Kode Barang : ")
Barang = []
Harga = []
while Kode :
    if Kode=="001":
        Barang.append("Whiskas 1000gr")
        Harga = int(65000)
        break
    elif Kode=="002":
        Barang.append("Royal Canin 1000gr")
        Harga = int(200000)
        break
    elif Kode=="003":
        Barang.append("Maxi Cat Sand 5L")
        Harga = int(30000)
        break
    elif Kode=="004":
        Barang.append("Aromatic Sand 5L")
        Harga = int(25000)
        break
    elif Kode=="005":
        Barang.append("Snack Me-O")
        Harga = int(25000)
        break
    elif Kode=="006":
        Barang.append("Snack Life Cat")
        Harga = int(10000)
        break
    elif Kode=="007":
        Barang.append("Vitamin Olive Care")
        Harga = int(80000)
        break
    elif Kode=="008":
        Barang.append("Vitamin Nutri Plus Gel")
        Harga = int(150000)
        break
    elif Kode=="009":
        Barang.append("Drontal Cat 1 Pcs")
        Harga = int(25000)
        break
    elif Kode=="010":
        Barang.append("Cream Scabies 15gr")
        Harga = int(25000)
        break
    elif Kode=="011":
        Barang.append("Cat Necklace")
        Harga = int(20000)
        break
    elif Kode=="012":
        Barang.append("Baju kucing")
        Harga = int(50000)
        break
    else :
        Kode=st.text_input("Kode Salah, Masukan Ulang Kode Barang : ")
st.write()

Total = (Jumlah*Harga)
Jumlah_Bayar = int(Total)
def garis():
    st.write("--------------------------------------------------------------------")
garis()
st.write("Penjualan Kebutuhan Kucing")
st.write("Nama Pembeli :", Nama)
st.write("Nomor Telepon :", Nomor)
st.write("Kode Barang :", Kode)
st.write("Jumlah Yang Dibeli :", Jumlah)
st.write("Harga : Rp", Harga)
st.write("Pembayaran Pembelian Barang")
st.write("Jumlah Pembayaran : Rp", round(Total))
Uang= st.number_input("Jumlah Uang Yang Dibayarkan : Rp", 0)
garis()
Kembalian = Uang-round(Total)
st.write("Jumlah Uang Kembalian :", round(Kembalian))
garis()
st.title("TERIMA KASIH")
st.title("HAVE A NICE DAY")
