from spyne import Application, rpc, ServiceBase, Integer, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication


class MiServicio(ServiceBase):
    @rpc(Unicode, _returns=Unicode)
    def obtener_saludo(ctx, nombre):
        return f"Hola, {nombre}! Bienvenido a tu primer servicio SOAP con Python - Mateo Carrasco."
    
    @rpc(Integer, Integer, _returns=Integer)
    def sumar(ctx, a, b):
        return a + b

# Configurar el servicio
soap_app = Application(
    [MiServicio],
    'mi.soap.servicio',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)

# Configurar el servidor WSGI
wsgi_app = WsgiApplication(soap_app)

if __name__ == "__main__":
    from wsgiref.simple_server import make_server

    # Ejecutar el servidor en el puerto 8000
    server = make_server('0.0.0.0', 8000, wsgi_app)
    print("Servicio SOAP ejecutándose en http://localhost:8000")
    server.serve_forever()


def generar_wsdl(app, nombre_archivo):
    with open(nombre_archivo, "w") as wsdl_file:
        wsdl_file.write(app.wsdl())
    print(f"WSDL generado: {nombre_archivo}")

if __name__ == "__main__":
    generar_wsdl(soap_app, "mi_servicio.wsdl")
    server = make_server('0.0.0.0', 8000, wsgi_app)
    print("Servicio SOAP ejecutándose en http://localhost:8000")
    server.serve_forever()
