from ipaddress import IPv4Address, IPv4Network
import random
from typing import Optional
from scapy.all import srp 
from scapy.layers.l2 import ARP, Ether

def generate_random_ip(network: str = "192.168.1.0/24") -> str:
    """Genera una dirección IP aleatoria dentro de una red."""
    net = IPv4Network(network)
    random_ip = IPv4Address(
        random.randint(
            int(net.network_address) + 1,
            int(net.broadcast_address) - 1
        )
    )
    return str(random_ip)


def validate_ip_range(ip_range: str) -> bool:
    """Valida un rango de direcciones IP."""
    try:
        IPv4Network(ip_range)
        return True
    except ValueError:
        return False


def get_network_info(ip: str, mask: Optional[str] = None) -> dict:
    """Obtiene información de una red."""
    try:
        if mask:
            network = IPv4Network(f"{ip}/{mask}", strict=False)
        else:
            network = IPv4Network(ip, strict=False)

        return {
            "network_address": str(network.network_address),
            "broadcast_address": str(network.broadcast_address),
            "netmask": str(network.netmask),
            "num_addresses": network.num_addresses,
            "is_private": network.is_private
        }
    except ValueError as e:
        raise ValueError(f"IP o máscara inválida: {e}")

def get_mac_address(ip):
	"""
    Obtiene la dirección MAC de una IP en la red local.
	"""
	ans, _ = srp(Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(pdst=ip), timeout=3, verbose=0)
	if ans:
		return ans[0][1].src