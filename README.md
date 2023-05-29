# Aplicativo dockerizado para crear dns dinamicos en tus servidores
### Este repositorio te permite implementar en tu servidores el uso de los dns dinámicos, usando [duckdns](https://www.duckdns.org/) como proveedor de servicio. De esta manera este código te permitirá extraer la ip pública dinámica que tienes en el momento para actualizar el servicio de tu proveedor. además está preparado para actualizar varios al mismo tiempo
## Clonar el repositorio
```shell
git clone https://github.com/gbbolivar/worker-update-dynamic-dns.git
```
## Ingresar al repositorio
```shell
cd worker-update-dynamic-dns
```
## Agregar las las configuraciones de tus servicios
cp code/config/config.example.json code/config/config.json
```json
{
    "dns": [
        {
            "url": "https://www.duckdns.org/update?{DOMAIN}&token={TOKEN}&ip={IP-PUBLIC}"
        }
    ],
    "checkIp": "http://checkip.dyndns.org"
}
```
### Debes cambiar las variables {DOMAIN} y {TOKEN} solamente

## Descargar las imagenes
```shell
make build
```
## Activar el contenedor
```shell
make start
```
## Ingresar el contenedor
```shell
make ssh-ba
```
## Ver los logs
```shell
make logs-f
```