import streamlit as st

st.header("Contoh Program Sederhana")
st.subheader("Muhammad Sultan Al Faritz")
st.subheader("")


st.subheader("SILAHKAN PILIH MENU ANDA")
makan1 = st.number_input("Nasi goreng polos Rp.15.000",0)
makan2 = st.number_input("Nasi goreng ayam geprek Rp.25.000",0)
makan3 = st.number_input("Nasi putih ayam geprek Rp.20.000",0)
makan4 = st.number_input("Mie goreng Rp.18.000",0)
makan5 = st.number_input("Mie rebus Rp.18.000",0)
minum1 = st.number_input("Coca cola Rp.10.000",0)
minum2 = st.number_input("Teh dingin Rp.10.000",0)
minum3 = st.number_input("Sanger dingin Rp.15.000",0)
minum4 = st.number_input("Sanger panas Rp.10.000",0)
minum5 = st.number_input("Coklat panas Rp.10.000",0)

hitung = st.button("hitung")
if (hitung):
    st.subheader("PESANAN ANDA")
    if makan1 > 0:
        st.success(f"Nasi goreng polos, Jumlah: {makan1}, Total harga: Rp.{15000*makan1}")
    if makan2 > 0:
        st.success(f"Nasi goreng ayam geprek, Jumlah: {makan2}, Total harga: Rp.{25000*makan2}")
    if makan3 > 0:
        st.success(f"Nasi putih ayam geprek, Jumlah: {makan3},Total harga: Rp.{20000*makan3}")
    if makan4 > 0:
        st.success(f"Mie goreng, Jumlah: {makan4}, Total harga: Rp.{18000*makan4}")
    if makan5 > 0:
        st.success(f"Mie rebus, Jumlah: {makan5}, Total harga: Rp.{18000*makan5}")
    if minum1 > 0:
        st.success(f"Coca cola, Jumlah: {minum1}, Total harga: Rp.{10000*minum1}")
    if minum2 > 0:
        st.success(f"Teh dingin, Jumlah: {minum2}, Total harga: Rp.{10000*minum2}")
    if minum3 > 0:
        st.success(f"Sanger dingin, Jumlah: {minum3}, Total harga: Rp.{15000*minum3}")
    if minum4 > 0:
        st.success(f"Sanger panas, Jumlah: {minum4}, Total harga: Rp.{10000*minum4}")
    if minum5 > 0:
        st.success(f"Coklat panas, Jumlah: {minum5}, Total harga: Rp.{10000*minum5}")

    st.success(f"Total harga seluruh pesanan Rp.{15000*makan1+25000*makan2+20000*makan3+18000*makan4+18000*makan5+10000*minum1+10000*minum2+15000*minum3+10000*minum4+10000*minum5}")
    st.header("TERIMAKASIH TELAH BERKUNJUNG")
    st.balloons()