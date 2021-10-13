#Wilson Nugrah
#2301858976

# Tugas membuat Client dan server dengan socket TCP yang memiliki fitur chat

# Client

# Memasukkan modul libraries socket dan threading
import socket
import threading

# sesuai dengan function di TCPServer yang telah dibuat,
# pertama-tama saya akan meminta kode nickname yaitu "nick" sesuai yang ada di server
nickname = input("Input your nickname: ")

# Setelah itu kita hubungkan client dengan socket dan menggunakan TCP Sockstream agar bisa berkomunikasi 2 arah
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 65534))

# Membuat function untuk selalu menerima pesan dari server dengan menggunakan endless loop
def receive():
    while True:
        try:
            # Menerima pesan yang diberikan server
            # Jika nick mengirimkan nickname dalam bentuk ascii dan akan didecode sesuai dengan function dibawah
            message = client.recv(1024).decode('ascii')
            if message == 'nick':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            # Function berikut terjadi apabila koneksi mengalami error sehingga akan menampilkan pesan error
            # setelah itu akan mematikan client dan terminate function
            print("An error occured!")
            client.close()
            break

# Function selanjutnya yaitu function untuk mengirimkan pesan yang ingin ditulis kepada server dengan endless loop yang artinya server akan selalu menerima pesan client
def write():
    while True:
        message = f'{nickname} : {input("")}'
        client.send(message.encode('ascii'))

# Selanjutnya saya jalankan threading untuk receive dan write yang telah kita buat
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()


# Penjelasan demonstrasi saya jelaskan dinotepad yang akan saya sertakan difile zip tugas ini

# Link Referensi : https://anokick.blogspot.com/2017/04/membuat-aplikasi-chatting-client-server.html
#                  https://www.neuralnine.com/tcp-chat-in-python/
#                  Powerpoint Session 1