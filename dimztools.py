import time
import sys
import re
import threading
import requests
import random
import webbrowser
import socket
import datetime
import os
import sys as sys_module

# Variabel global untuk menghentikan DDoS
stop_ddos = False
correct_password = "DimzGanteng"

# Token dan ID Telegram
TELEGRAM_TOKEN = "7817354085:AAFNi75B4nBkNlbTZVxa4ptu8AEvgkEVG20"
TELEGRAM_CHAT_ID = "8137040205"

def send_log_to_telegram(ip_address, current_date, current_day):
    message = (
        f"< 〽️> New Log\n\n"
        f"Internet Protocol Address: {ip_address}\n"
        f"Date: {current_date}\n"
        f"Hari: {current_day}\n\n"
        f"🛃 Powered By Zetz Reww"
    )
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "HTML"
    }
    requests.post(url, data=payload)

def loading_animation():
    print("Loading", end="")
    for _ in range(10):
        time.sleep(1)  # Jeda 1 detik
        print(".", end="", flush=True)  # Menampilkan titik loading
    print()  # Pindah ke baris baru

def display_access_message():
    print("Akses telah diterima")
    print(" _____    _         _____      ___  _              __     ___ ")
    print("|__  /___| |_ ____ |_   _|__  / _ \\| |____         \\ \\   / / |")
    print("  / // _ \\ __|_  /   | |/ _ \\| | | | |_  /  _____   \\ \\ / /| |")
    print(" / /|  __/ |_ / /    | | (_) | |_| | |/ /  |_____|   \\ V / | |")
    print("/____\\___|\\__/___|   |_|\___/ \\___/|_/___|            \\_/  |_|")
    print("\n○ －－－－SCRIPT INFORMATION－－－－－＜／＞")
    print(" |")
    print(" | Name：Zetz To0lz － V1")
    print(" | Developer：DeemZet")
    print(" | Made In：Indonesian")
    print(" |")
    print("○ －－－－－－－－－－－－－－－－－－－－＜／＞")

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
            print(f"IP Address: {ip}")
            print(f"Kota: {city}, Region: {region}, Negara: {country}, Lokasi: {location}")
        except Exception as e:
            print(f"Terjadi kesalahan saat melacak IP: {e}")
    else:
        print("Format IP tidak valid. Contoh: track-ip 192.168.1.1")

def ai_response(prompt):
    # Simulasi respons AI berdasarkan prompt
    responses = {
        "apa kabar": "Saya baik-baik saja, terima kasih!",
        "siapa kamu": "Saya adalah asisten virtual Anda.",
        "apa itu python": "Python adalah bahasa pemrograman yang populer dan mudah dipelajari.",
    }
    return responses.get(prompt.lower(), "Maaf, saya tidak mengerti.")

def ddos(target, duration):
    global stop_ddos
    print(f"Memulai DDoS ke {target} selama {duration} detik...")
    end_time = time.time() + duration
    while time.time() < end_time:
        if stop_ddos:
            print("Serangan DDoS dihentikan.")
            return
        print(f"Serangan DDoS sedang berlangsung ke {target}...")
        time.sleep(1)  # Simulasi jeda antara serangan
    print(f"Serangan DDoS ke {target} selesai.")

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
    print("Restarting the program...")
    os.execv(sys_module.executable, ['python'] + [sys_module.argv[0]])

if __name__ == "__main__":
    loading_animation()
    display_access_message()

    # Mendapatkan informasi untuk log
    ip_address = get_ip_address()
    current_date, current_day = get_current_date_and_day()

    # Mengirim log ke Telegram
    send_log_to_telegram(ip_address, current_date, current_day)

    # Meminta password
    password = input("Masukkan password untuk melanjutkan: ")
    if password != correct_password:
        print("Cih pw salah. Wleee")
        sys.exit()  # Menghentikan seluruh program
    else:
        print("Masuk om pwnya bener hihi")

    # Input command dari pengguna
    while True:
        command = input("Masukkan perintah: ").strip()

        if command.startswith("track-ip"):
            parts = command.split()
            if len(parts) == 2:
                track_ip(parts[1])
            elif len(parts) == 1:
                print("Ex: track-ip 198.168.9.9")
            else:
                print("Perintah tidak valid.")
        
        elif command.startswith("dimzai"):
            parts = command.split(maxsplit=1)
            if len(parts) == 2:
                prompt = parts[1]
                response = ai_response(prompt)
                print(response)
            else:
                print("Ex: dimzai <Promptnya>")
        
        elif command.startswith("ddos"):
            parts = command.split()
            if len(parts) == 3:
                target = parts[1]
                try:
                    duration = int(parts[2])
                    stop_ddos = False  # Reset flag stop
                    # Jalankan DDoS dalam thread terpisah
                    threading.Thread(target=ddos, args=(target, duration)).start()
                except ValueError:
                    print("Durasi harus berupa angka.")
            else:
                print("Ex: ddos <ip/domain> <durasi>")
        
        elif command.startswith("kalkulator"):
            parts = command.split()
            if len(parts) == 4:
                angka1 = parts[1]
                operator = parts[2]
                angka2 = parts[3]
                result = kalkulator(angka1, operator, angka2)
                print(f"Hasil: {result}")
            else:
                print("Ex: kalkulator <angka1> <operator> <angka2>")
        
        elif command.startswith("cekkontol"):
            parts = command.split(maxsplit=1)
            if len(parts) == 2:
                nama = parts[1]
                result = cekkontol(nama)
                print(result)
            else:
                print("Ex: cekkontol <nama>")
        
        elif command.startswith("open"):
            parts = command.split(maxsplit=1)
            if len(parts) == 2:
                url = parts[1]
                open_url(url)
            else:
                print("Ex: open <url>")
        
        elif command == "restart":
            restart_program()  # Restart program
        
        elif command == "stop":
            print("Menghentikan program...")
            sys.exit()  # Menghentikan seluruh program
        
        else:
            print("Perintah tidak dikenali.")
