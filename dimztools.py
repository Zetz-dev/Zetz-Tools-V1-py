import time
import sys
import re
import threading
import random
import webbrowser
import socket
import datetime
import os
import sys as sys_module
from colorama import Fore, Style, init

# Inisialisasi colorama
init(autoreset=True)

# Variabel global untuk menghentikan DDoS
stop_ddos = False
correct_password = "DimzGanteng"

def clear_terminal():
    """Membersihkan layar terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

def loading_animation():
    print(Fore.YELLOW + "Loading", end="")
    for _ in range(10):
        time.sleep(0.5)  # Jeda 0.5 detik
        print(Fore.YELLOW + ".", end="", flush=True)  # Menampilkan titik loading
    print(Fore.GREEN + "\nLoading selesai!")  # Pesan selesai loading

def display_access_message():
    print(Fore.CYAN + "Akses telah diterima")
    print(Fore.GREEN + " _____    _         _____      ___  _              __     ___ ")
    print(Fore.GREEN + "|__  /___| |_ ____ |_   _|__  / _ \\| |____         \\ \\   / / |")
    print(Fore.GREEN + "  / // _ \\ __|_  /   | |/ _ \\| | | | |_  /  _____   \\ \\ / /| |")
    print(Fore.GREEN + " / /|  __/ |_ / /    | | (_) | |_| | |/ /  |_____|   \\ V / | |")
    print(Fore.GREEN + "/____\\___|\\__/___|   |_|\___/ \\___/|_/___|            \\_/  |_|")
    print(Fore.MAGENTA + "\n○ －－－－SCRIPT INFORMATION－－－－－＜／＞")
    print(Fore.MAGENTA + " |")
    print(Fore.MAGENTA + " | Name：Zetz To0lz － V1")
    print(Fore.MAGENTA + " | Developer：DeemZet")
    print(Fore.MAGENTA + " | Made In：Indonesian")
    print(Fore.MAGENTA + " |")
    print(Fore.MAGENTA + "○ －－－－－－－－－－－－－－－－－－－－＜／＞")

def get_ip_address():
    # Mendapatkan alamat IP lokal
    hostname = socket.gethostname()
    return socket.gethostbyname(hostname)

def get_current_date_and_day():
    # Mendapatkan tanggal dan hari saat ini
    now = datetime.datetime.now()
    current_date = now.strftime("%d %B %Y")
    current_day = now.strftime("%A")
    
    # Mengubah nama hari
    days_translation = {
        "Monday": "Senin",
        "Tuesday": "Selasa",
        "Wednesday": "Rabu",
        "Thursday": "Kamis",
        "Friday": "Jum'at",
        "Saturday": "Sabtu",
        "Sunday": "Ahad"
    }
    return current_date, days_translation.get(current_day, current_day)

def track_ip(ip):
    # Validasi format IP
    ip_pattern = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
    if ip_pattern.match(ip):
        try:
            response = requests.get(f"https://ipinfo.io/{ip}/json")
            data = response.json()
            location = data.get("loc", "Lokasi tidak ditemukan")
            city = data.get("city", "Kota tidak ditemukan")
            region = data.get("region", "Region tidak ditemukan")
            country = data.get("country", "Negara tidak ditemukan")
            print(Fore.GREEN + f"IP Address: {ip}")
            print(Fore.GREEN + f"Kota: {city}, Region: {region}, Negara: {country}, Lokasi: {location}")
        except Exception as e:
            print(Fore.RED + f"Terjadi kesalahan saat melacak IP: {e}")
    else:
        print(Fore.RED + "Format IP tidak valid. Contoh: track-ip 192.168.1.1")

def ai_response(prompt):
    # Simulasi respons AI berdasarkan prompt
    responses = {
        "apa kabar": "Saya baik-baik saja, terima kasih!",
        "siapa kamu": "Saya adalah asisten virtual Anda.",
        "apa itu python": "Python adalah bahasa pemrograman yang populer dan mudah dipelajari.",
    }
    return responses.get(prompt.lower(), "Maaf, saya tidak mengerti.")

def ddos(target, port, duration):
    global stop_ddos
    print(Fore.YELLOW + f"Memulai DDoS ke {target} pada port {port} selama {duration} detik...")
    end_time = time.time() + duration
    while time.time() < end_time:
        if stop_ddos:
            print(Fore.RED + "Serangan DDoS dihentikan.")
            return
        print(Fore.YELLOW + f"Serangan DDoS sedang berlangsung ke {target} pada port {port}...")
        time.sleep(1)  # Simulasi jeda antara serangan
    print(Fore.GREEN + f"Serangan DDoS ke {target} pada port {port} selesai.")

def kalkulator(angka1, operator, angka2):
    try:
        angka1 = float(angka1)
        angka2 = float(angka2)
        if operator == '+':
            return angka1 + angka2
        elif operator == '-':
            return angka1 - angka2
        elif operator == '*':
            return angka1 * angka2
        elif operator == '/':
            if angka2 != 0:
                return angka1 / angka2
            else:
                return "Error: Pembagian dengan nol."
        else:
            return "Operator tidak dikenali. Gunakan +, -, *, atau /."
    except ValueError:
        return "Error: Masukkan angka yang valid."

def cekkontol(nama):
    # Menghasilkan persentase acak dari 0 hingga 100
    percent = random.randint(0, 100)
    return f"Kamu {percent}% Eww kontolnya! Hytamm"

def open_url(url):
    # Membuka URL di browser default
    webbrowser.open(url)

def restart_program():
    """Restart the current program."""
    print(Fore.YELLOW + "Restarting the program...")
    os.execv(sys_module.executable, ['python'] + [sys_module.argv[0]])

if __name__ == "__main__":
    clear_terminal()  # Membersihkan layar saat program dijalankan
    loading_animation()
    display_access_message()

    # Mendapatkan informasi untuk log
    ip_address = get_ip_address()
    current_date, current_day = get_current_date_and_day()

    # Meminta password
    password = input(Fore.CYAN + "Masukkan password untuk melanjutkan: ")
    if password != correct_password:
        print(Fore.RED + "Cih pw salah. Wleee")
        sys.exit()  # Menghentikan seluruh program
    else:
        print(Fore.GREEN + "Masuk om pwnya bener hihi")

    # Input command dari pengguna
    while True:
        command = input(Fore.CYAN + "Masukkan perintah: ").strip()

        if command.startswith("track-ip"):
            parts = command.split()
            if len(parts) == 2:
                track_ip(parts[1])
            elif len(parts) == 1:
                print(Fore.RED + "Ex: track-ip 198.168.9.9")
            else:
                print(Fore.RED + "Perintah tidak valid.")
        
        elif command.startswith("dimzai"):
            parts = command.split(maxsplit=1)
            if len(parts) == 2:
                prompt = parts[1]
                response = ai_response(prompt)
                print(Fore.GREEN + response)
            else:
                print(Fore.RED + "Ex: dimzai <Promptnya>")
        
        elif command.startswith("ddos"):
            parts = command.split()
            if len(parts) == 4:
                target = parts[1]
                port = parts[2]
                try:
                    duration = int(parts[3])
                    stop_ddos = False  # Reset flag stop
                    # Jalankan DDoS dalam thread terpisah
                    threading.Thread(target=ddos, args=(target, port, duration)).start()
                except ValueError:
                    print(Fore.RED + "Durasi harus berupa angka.")
            else:
                print(Fore.RED + "Ex: ddos <ip/web> <port> <durasi>")
        
        elif command.startswith("kalkulator"):
            parts = command.split()
            if len(parts) == 4:
                angka1 = parts[1]
                operator = parts[2]
                angka2 = parts[3]
                result = kalkulator(angka1, operator, angka2)
                print(Fore.GREEN + f"Hasil: {result}")
            else:
                print(Fore.RED + "Ex: kalkulator <angka1> <operator> <angka2>")
        
        elif command.startswith("cekkontol"):
            parts = command.split(maxsplit=1)
            if len(parts) == 2:
                nama = parts[1]
                result = cekkontol(nama)
                print(Fore.GREEN + result)
            else:
                print(Fore.RED + "Ex: cekkontol <nama>")
        
        elif command.startswith("open"):
            parts = command.split(maxsplit=1)
            if len(parts) == 2:
                url = parts[1]
                open_url(url)
            else:
                print(Fore.RED + "Ex: open <url>")
        
        elif command == "restart":
            restart_program()  # Restart program
        
        elif command == "stop":
            print(Fore.YELLOW + "Menghentikan program...")
            sys.exit()  # Menghentikan seluruh program
        
        else:
            print(Fore.RED + "Perintah tidak dikenali.")
