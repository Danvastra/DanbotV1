import sys
import os
import pyfiglet
import speedtest
import random
import time
import requests
import json
import re
from colorama import Fore, Style, init

def clear():
    # Untuk Windows
    if os.name == 'nt':
        os.system('cls')
    # Untuk Mac atau Linux
    else:
        os.system('clear')

# Memanggil fungsi clear() untuk membersihkan layar
clear()

# Membuat teks ASCII Art dengan ukuran besar
welcomeTxt = pyfiglet.figlet_format("Danbot Tools v1")

#warna text welcome
GREEN = '\033[32m'
RESET = '\033[0m'  # Untuk reset ke warna normal
MERAH = '\033[31m'
HIJAU = '\033[32m'
KUNING = '\033[33m'
BIRU = '\033[34m'
MAGENTA ='\033[35m'
CYAN = '\033[36m'

print(f"{GREEN}{welcomeTxt}{RESET}")
print(" Author by Danvastra")


# data loading
def loading():
    loading_messages = [" > Danbot is loading data, please wait"," > Danbot is loading data, please wait."," > Danbot is loading data, please wait.."," > Danbot is loading data, please wait..."]

    for message in loading_messages:
        sys.stdout.write("\r" + message)
        sys.stdout.flush()
        time.sleep(1)


# di bagian bawah ini adalah tools 2 (Speedtest Network)
import speedtest

def cek_kecepatan_wifi():
    try:
        # Membuat objek Speedtest
        st = speedtest.Speedtest()

        # Mengambil daftar server
        st.get_best_server()

        loading()

        # Mengukur dan mendapatkan hasil kecepatan unduh
        unduh_speed = st.download() / 1_000_000  # Konversi dari bps ke Mbps
        # Mengukur dan mendapatkan hasil kecepatan unggah
        unggah_speed = st.upload() / 1_000_000  # Konversi dari bps ke Mbps

        # Menampilkan hasil
        print("\n")
        print(f" + Download Speed: {unduh_speed:.2f} Mbps")
        print(f" - Upload Speed: {unggah_speed:.2f} Mbps")

    except speedtest.ConfigRetrievalError as e:
        print("Gagal mengambil konfigurasi Speedtest. Pastikan koneksi internet tidak diblokir.")
        print("Error:", e)
    except Exception as e:
        print("Terjadi kesalahan:", e)


# ini bagian tools 
# Inisialisasi colorama
init(autoreset=True)

def check_ip_address():
    print(Fore.YELLOW + "Track IP Address by Danvastra")
    ipaddress = input(f"{Fore.YELLOW}Enter Target IP Address : {Style.RESET_ALL}")
    loading()
    print("\n")
    iprequest = requests.get(f"http://ip-api.com/json/{ipaddress}")
    if iprequest.status_code == 200:
        ipdata = json.loads(iprequest.text)
        if ipdata["status"] == "success":
            print("Country :", ipdata["country"], ipdata["countryCode"])
            print("Region :", ipdata["region"], ipdata["regionName"])
            print("City :", ipdata["city"])
            print("Zip :", ipdata["zip"])
            lat = ipdata["lat"]
            lon = ipdata["lon"]
            print("Location :", lat, ",", lon)

            maps = f"https://www.google.com/maps/@{lat},{lon},9z?h1=id"
            print("Maps :", maps)

            print("Timezone :", ipdata["timezone"])
            print("ISP :", ipdata["isp"])
            print("IP ADDRESS :", ipdata["query"])
        else:
            print("Error: Unable to retrieve IP data.")
    else:
        print("Error: HTTP request failed.")

def check_valid_ip(ipaddress):
    # Regex pattern to match IPv4 addresses
    ipv4_pattern = re.compile(
        r'^((25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.){3}'
        r'(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$'
    )
    # Regex pattern to match IPv6 addresses
    ipv6_pattern = re.compile(
        r'^[0-9a-fA-F:]{2,39}$'
    )

    if ipv4_pattern.match(ipaddress):
        return f"{Fore.GREEN}Valid IPv4 Address{Style.RESET_ALL}"
    elif ipv6_pattern.match(ipaddress):
       return f"{Fore.GREEN}Valid IPv6 Address{Style.RESET_ALL}"
    else:
        return f"{Fore.RED}Invalid IP Address{Style.RESET_ALL}"


# ini bagian tools ke 4 (Chat ai Dialogue) menggunakan bahasa indonesia si AI nya
def chat_ai_dialogue():
    print(" = Hallo, Salam Kenal, nama saya Danbot, Assistant ai Dialogue.")
    loading()
    print("\n")
    namaUser = str(input(" + Siapa Nama Mu? : "))
    if namaUser.strip():
        loading()
        print("\n")
        print(" = Hallo " + namaUser + ", Salam Kenal yahh :) ")
        loading()
        print("\n")
        hobi = input(" + Apa hobi kamu? : ")
        if hobi.strip():
            loading()
            print("\n")
            print(" = Sepertinya Hobi Danbot &" + namaUser + "lebih baik darimu, wkwkw")
            loading()
            print("\n")
            print(" = Udah dulu cik, lagi males nanya. bye.")
            print("\n")
            backorNot = str(input(" + Apakah kamu ingin kembali ke menu tools lagi? (y/n) "))
            if backorNot == "y":
                pilihanSatu()
            elif backorNot == "n":
                print("Thank you for using our program!")
            else:
                print("There is an error, retry the program.")

    else:
        print("There is an error, retry the program.")


# ini bagian tools 5 (Calculator)
def kalkulator():
    print("Simple Calculator v1.0")
    print("\n")
    nilai1 = int(input("Masukkan Nilai 1 : "))
    nilai2 = int(input("Masukkan Nilai 2 : "))
    hasil = nilai1 + nilai2
    hasil2 = nilai1 - nilai2
    hasil3 = nilai1 * nilai2
    hasil4 = nilai1 / nilai2

    loading()
    print("\n")
    print("Result : ")
    print(f" > Pertambahan : Hasil dari {nilai1} + {nilai2} adalah {hasil}")
    print(f" > Pengurangan : Hasil dari {nilai1} - {nilai2} adalah {hasil2}")
    print(f" > Perkalian   : Hasil dari {nilai1} * {nilai2} adalah {hasil3}")
    print(f" > Pembagian   : Hasil dari {nilai1} / {nilai2} adalah {hasil4}")
    print("\n")
    loading()
    print("\n")
    backorNot = str(input(" + Apakah kamu ingin kembali ke menu tools lagi? (y/n) "))
    if backorNot == "y":
        pilihanSatu()
    elif backorNot == "n":
        print("Thank you for using our program!")
    else:
        print("There is an error, retry the program.")   


# ini bagian pilihan menu tools nya
def pilihanSatu():
    while True:
        print("")
        print(f"{KUNING} + Tools Menu : ")
        print("===============")
        print("")
        print("[1] Random Number")
        print("[2] Speedtest Network")
        print("[3] Track IP Address")
        print("[4] Chat ai dialogue")
        print("[5] Simple Calculator")
        print("[6] Exit tools")
        pilihanTools = str(input(" + Please Select Tools, (ex 1/2) : "))
        print("")
        print("===============")
        if pilihanTools == "1" :
            print("\n")
            loading()
            print("\n")
            angka_acak = str(random.randrange(1, 1000))
            print(" + Your random number is : " + angka_acak)
            print("\n")
            print("===============")
        elif pilihanTools == "2":
            cek_kecepatan_wifi()
            print("\n")
            print("===============")
        elif pilihanTools == "3":
            check_ip_address()
        elif pilihanTools == "4":
            chat_ai_dialogue()
            break
        elif pilihanTools == "5":
            kalkulator()
            break
        elif pilihanTools == "6":
            print("\n")
            print("Thank you for using our program!")
            print("\n")
            print("===============")
            break        
        else:
            print("There is an error, retry the program.")


pilihanSatu()