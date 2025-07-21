import socket
import time
import os

# === Настройки сервера ===
UDP_IP = "192.168.137.1"
UDP_PORT = 3000
AUDIO_FILE = "output.ima.wav"
SEND_WAV_HEADER = True  # <<< ВКЛ / ВЫКЛ заголовок WAV

# === Инициализация сокета ===
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', UDP_PORT))

# === Отправка аудиофайла по запросу ESP ===
def send_audio_file():
    if not os.path.exists(AUDIO_FILE):
        print(f"Error: File '{AUDIO_FILE}' not found.")
        return

    with open(AUDIO_FILE, "rb") as f:
        if not SEND_WAV_HEADER:
            f.seek(44)  # Пропустить заголовок WAV (обычно 44 байта)

        print("Waiting for requests...")

        while True:
            data, addr = sock.recvfrom(1024)

            if data == b'\xFF\xFF':
                packet = f.read(1024)
                if not packet:
                    print("End of file. Transmission complete.")
                    break
                sock.sendto(packet, addr)
                print(f"Sent {len(packet)} bytes to {addr}")
            else:
                print(f"Ignored unknown packet from {addr}: {data}")

            # time.sleep(0.01)

    print("Closing socket.")
    sock.close()

# === Точка входа ===
if __name__ == "__main__":
    print(f"Starting server on {UDP_IP}:{UDP_PORT}, WAV header: {'ON' if SEND_WAV_HEADER else 'OFF'}")
    send_audio_file()
