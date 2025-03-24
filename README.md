# Network Attack Tool

Una herramienta educativa para simular y estudiar diferentes tipos de ataques de red en un entorno controlado. Diseñada con fines de investigación y aprendizaje en ciberseguridad.

⚠️ **AVISO LEGAL**: Esta herramienta está diseñada exclusivamente para propósitos educativos y de investigación. Su uso en redes o sistemas sin autorización expresa es ilegal.

## Características

- **SYN Flood**: Simula ataques de denegación de servicio mediante inundación de paquetes SYN
- **ARP Spoofing**: Permite el estudio de ataques de suplantación ARP
- **Ping Flood**: Simula ataques DoS mediante inundación de paquetes ICMP
- Soporte para múltiples hilos
- Sistema de logging integrado
- Interfaz de línea de comandos intuitiva

## Requisitos

- Python 3.8+
- Privilegios de root/administrador
- Bibliotecas requeridas listadas en `requirements.txt`

## Instalación

```bash
# Clonar el repositorio
git clone https://github.com/XlHader/network-attack-tool.git
cd network_attack_tool

# Ejecutar entorno virtual (opcional pero recomendado)
python3 -m venv venv
source venv/bin/activate  

# Instalar dependencias
pip install -r requirements.txt

# Dar permisos de administrador a Python para enviar paquetes de red
sudo setcap cap_net_raw,cap_net_admin=eip $(which python3)
```

## Estructura del Proyecto

```
network_attack_tool/
├── config/             # Configuraciones
├── logs/               # Archivos de registro
├── src/                # Código fuente
│   ├── attacks/        # Implementaciones de ataques
│   ├── core/           # Núcleo de la aplicación
│   ├── utils/          # Utilidades
│   └── __main__.py     # Punto de entrada
├── .gitignore
├── README.md
└── requirements.txt
```

## Uso

### Sintaxis General
```bash
python3 -m src -i TARGET_IP [--arp GATEWAY_IP | --syn | --icmp] -n NUM_PACKETS --threads NUM_THREADS
```

### Parámetros
- `-i, --ip`: IP objetivo
- `-n, --num`: Número de paquetes
- `--threads`: Número de hilos
- `--arp`: Ataque ARP Spoofing (requiere IP del gateway)
- `--syn`: Ataque SYN Flood
- `--icmp`: Ataque Ping Flood

### Ejemplos

1. Ataque ARP Spoofing:
```bash
python3 -m src -i 192.168.0.11 --arp 192.168.0.5 -n 1000 --threads 8
```

2. Ataque SYN Flood:
```bash
python3 -m src -i 192.168.0.11 --syn -n 1000 --threads 8
```

3. Ataque Ping Flood:
```bash
python3 -m src -i 192.168.0.11 --icmp -n 1000 --threads 8
```

## Uso Responsable

Esta herramienta debe utilizarse únicamente en:
- Entornos de laboratorio controlados
- Sistemas con autorización explícita
- Fines educativos y de investigación

## Registro y Monitoreo

Los logs se almacenan en el directorio `logs/` y contienen:
- Timestamp de los eventos
- Tipo de ataque ejecutado
- Resultados y errores
- Métricas de rendimiento

## Descargo de Responsabilidad

El autor no se hace responsable del mal uso de esta herramienta. Los usuarios deben cumplir con todas las leyes y regulaciones aplicables.