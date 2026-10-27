import threading
from flask import Flask, jsonify, render_template
from scapy.all import IP, sniff

app = Flask(__name__)

# Store captured packets in memory
captured_packets = []
MAX_PACKETS = 50  # Keep latest 50 packets


def process_packet(packet):
    if packet.haslayer(IP):
        proto_map = {1: 'ICMP', 6: 'TCP', 17: 'UDP'}
        proto_num = packet[IP].proto
        proto_name = proto_map.get(proto_num, f'Other ({proto_num})')

        packet_info = {
            'src': packet[IP].src,
            'dst': packet[IP].dst,
            'protocol': proto_name,
            'length': len(packet),
        }

        captured_packets.insert(0, packet_info)
        if len(captured_packets) > MAX_PACKETS:
            captured_packets.pop()


def start_sniffing():
    # Sniff packets continuously in background
    sniff(prn=process_packet, store=False)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/packets')
def get_packets():
    return jsonify(captured_packets)


if __name__ == '__main__':
    # Run packet sniffer in a background thread
    sniffer_thread = threading.Thread(target=start_sniffing, daemon=True)
    sniffer_thread.start()

    print('Starting Web Server at http://127.0.0.1:5000')
    app.run(debug=True, port=5000, use_reloader=False)
