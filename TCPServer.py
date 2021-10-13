#Wilson Nugrah
#2301858976

# Tugas membuat Client dan server dengan socket TCP yang memiliki fitur chat

#Server

# memasukkan modul library socket dan threading
import socket
import threading

# membuat host dengan ip address 127.0.0.1 sebagai localhost
# membuat port dengan angka bebas yang belum digunakan
host = '127.0.0.1'
port = 65534

# membuat socket dengan koneksi TCP dengan menggunakan sockstream
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# membuat koneksi server agar terikat dengan host dan port yang sudah dibuat
server.bind((host, port))
server.listen()

# membuat list client yang ingin dihubungkan
clients = []
nicknames = []

# membuat function untuk mengirimkan chat keseluruh client yang terhubung
def chat(message):
    for client in clients:
        client.send(message)

# membuat function yang akan mengenali setiap client yang akan connect dengan server
# function selanjutnya yaitu jika client mengirimkan balasan ataupun chat
# maka seluruh client yang terkoneksi ke server dapat melihat chat tersebut
# jika client mengalami koneksi yang error atau terputus maka akan dihilangkan dan ditutup koneksinya
# Saya namai function ini handling karena berfungsi untuk menanggapi feedback dari client
def handling(client):
    while True:
        try:
            # mengirimkan chat
            message = client.recv(1024)
            chat(message)
        except:
            # menghapus dan menutup client yang terputus koneksinya
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            chat(f'{nickname} left!'.encode('ascii'))
            nicknames.remove(nickname)
            break

# Function terakhir untuk menggabungkan seluruh function yang telah saya buat
def receive():
    while True:
        # Membuat endless loop untuk menerima semua client yang ingin connect dengan server
        # lakukan print untuk memberitahu bahwa client tersebut telah terhubung dengan menunjukkan address client
        client, address = server.accept()
        print(f"Connected with {str(address)}")

        # Client yang ingin terhubung harus memberikan nickname terlebih dahulu yang direquest dalam bentuk ascii
        # Client akan memberikan nickname sesuai dengan yang direquest server
        client.send('nick'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        # Server akan melakukan print bahwa client dengan nickname tersebut telah terhubung dengan server
        # Server akan memberikan chat broadcast kepada seluruh client yang sedang terhubung bahwa ada client baru yang terhubung
        print("Nickname is {}".format(nickname))
        chat(f"{nickname} joined!".encode('ascii'))
        client.send('Connected to the server!'.encode('ascii'))

        # Mulai melakukan koneksi dengan client menggunakan thread
        thread = threading.Thread(target=handling, args=(client,))
        thread.start()

# function ini saya buat untuk memastikan bahwa server berhasil mendengar dan tidak error
print("Server mendengar dan berhasil jalan")
receive()

#Penjelasan demonstrasi saya jelaskan dinotepad yang akan saya sertakan difile zip tugas ini

# Link Referensi : https://anokick.blogspot.com/2017/04/membuat-aplikasi-chatting-client-server.html
#                  https://www.neuralnine.com/tcp-chat-in-python/
#                  Powerpoint Session 1