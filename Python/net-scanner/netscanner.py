import pygeoip
import socket
from ports import getcommonports


def geo(_file, _ip):
    geoDb = pygeoip.GeoIP(_file)
    ip_dictionary_values = geoDb.record_by_addr(_ip)
    ip_list_values = ip_dictionary_values.items()
    print("***********************")
    print("***** GEOLOCATION *****")
    print("***********************")
    for value in ip_list_values:
        print(str(value[0]) + ": " + str(value[1]))


def hosts(_ip):
    print("\n*********************")
    print("******* HOST ********")
    print("**********************")
    try:
        hosts_values = socket.gethostbyaddr(_ip)
        print(hosts_values[0])
    except:
        print("No host associate")


def portscan(_host, _port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.001)
        result = sock.connect_ex((_host, _port))
        sock.close()
    except:
        pass
    return result


def ports(_ip):
    ''' This function search open ports '''
    common_ports = getcommonports()
    print("\n*******************")
    print("***    Ports    ***")
    print("*******************")
    for value in common_ports:
        if not portscan(_ip, value):
            print(str(value) + ': ' + str(common_ports[value]))


def main(_ip):
    geo('GeoIp/GeoLiteCity.dat', _ip)
    hosts(_ip)
    ports(_ip)


if __name__ == "__main__":
    print("Escaner de dispositivos internet: ")
    # pass ip to scan
    main('8.8.8.8')
