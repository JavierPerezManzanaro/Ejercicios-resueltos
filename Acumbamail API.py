
"""
url a generar: https://acumbamail.com/api/1/(nombreFuncion)/

createTemplate(string auth_token,string template_name,string html_content,number id,string custom_category,string subject,dict bee_json)


Mensaje de acumba:

https://acumbamail.com/api/1/addSubscriber/?auth_token=XXXXXXXXXXXX&list_id=XXX&merge_fields[email]=test@test.com&merge_fields[nombre]=test

https://acumbamail.com/api/1/send/?auth_token=XXXXXXXXXXXX&messages = [{"subject":"asunto","from_email":"a@a.com","to_email":"b@b.com","template_id":"123" } ]

https://acumbamail.com/api/1/createCampaign/?auth_token=XXXXX&name=XXXXXX&from_name=my_name&from_email=XXXXXX&subject=XXXXX&lists[0]=XXXX

(si se usa postman, campos grandes como content deben ir en el Body, como form-data)


"""




"""



Códigos de estado
200: La consulta ha ido bien
201: Los datos se han modificado correctamente
400: Petición incorrecta: algún argumento ha sido incorrecto
401: No autorizado, el proceso de autenticación ha sido incorrecto
429: Demasiadas peticiones a una función en un periodo de tiempo
500: Se ha producido algún error en el servidor. Infórmanos para que lo arreglemos
"""


import requests
import json
import datos_de_acceso
from pprint import pprint






def api_create_template(template_name, html_content):
    """Crea una campaña en acumbamail. Solo pedimos los argumentos que cambian de una plantilla a otra.
    https://acumbamail.com/apidoc/function/createTemplate/

    Args:
        template_name (_type_): _description_
        html_content (_type_): _description_
    """

    # URL de la API
    api_url = "https://acumbamail.com/api/1/createTemplate/"

    # Parámetros de la solicitud
    params = {
        "auth_token": datos_de_acceso.TOKEN_ACUMBAMAIL,
        "template_name": template_name,
        "html_content": html_content
    }

    try:
        # Realizar la solicitud POST a la API
        response = requests.post(api_url, data=params)
        print_response(response)
        # Verificar el estado de la respuesta
        if response.status_code == 200:
            print("Solicitud exitosa")
            # Puedes imprimir o manejar la respuesta de la API aquí
        else:
            print(f"Error en la solicitud. Código de estado: {response.status_code}")
    except Exception as e:
        print(f"Error al realizar la solicitud: {str(e)}")


def createCampaign(name, subject, html_content, date_send):
    """Crea y manda (a no ser que la fecha sea diferente) una campaña. Solo se pide los argumentos que cambian de una campaña a otra.
    Una vez creada la campaña se lanza automaticamente a no ser que se ponga una date_send.
    https://acumbamail.com/apidoc/function/createCampaign/

    Esta es la ayuda que manda Acumbamail: https://acumbamail.com/api/1/createCampaign/?auth_token=XXXXX&name=XXXXXX&from_name=my_name&from_email=XXXXXX&subject=XXXXX&lists[0]=XXXX

    Args:
        name (string): Nombre de la campaña (no es público)
        subject (string): El asunto de la campaña
        html_content (string): El html que contendrá la campaña
        date_send (date): (Opcional) Fecha de comienzo del envío. Sólo para envíos programados. (YYYY-MM-DD HH:MM)

    Args que son comunes y no se piden:
        auth_token (string): Tu token de autenticación de cliente
        from_name (string): Nombre del remitente de la campaña
        listas (dict): Los identificadores de las listas a las que se enviará la campaña, o de los segmentos a los que se quiera enviar precedidos de s. No se puede enviar a más de un segmento de una misma lista, ni a un segmento y a una lista a la que pertenezca
        from_email (string): El email desde el que se enviará la campaña, se puede usar Nombre <email@dominio.com>
        tracking_urls (integer):   (Opcional) Sustituir enlaces para seguimiento de clicks. Por defecto=1
        complete_json (integer):    Para que devuelva un json completo con formato completo. Por defecto=0
    """
    api_url = "https://acumbamail.com/api/1/createCampaign/"
    # Parámetros de la solicitud
    params = {
                "auth_token": datos_de_acceso.TOKEN_ACUMBAMAIL,
                "name": name, #"prueba",
                "from_name": "Suscripciones",
                "from_email": "suscripciones@axoncomunicacion.net",
                "subject": subject,
                "content": html_content,
                "date_send": date_send

    }
    # añadimos las listas necesarias
    params_combinado = params | datos_de_acceso.DICCIONARIO_DE_LISTAS
    try:
        # Realizar la solicitud POST a la API
        response = requests.post(api_url, data=params_combinado)
        pprint(params)
        print_response(response)
        # Verificar el estado de la respuesta
        if response.status_code == 200:
            print("Solicitud exitosa")
            # Puedes imprimir o manejar la respuesta de la API aquí
            respuesta = json.loads(response.text)
            print('Campaña: ' + str(respuesta['id']))
        else:
            print(f"Error en la solicitud. Código de estado: {response.status_code}")
    except Exception as e:
        print(f"Error al realizar la solicitud: {str(e)}")


def print_response(response):
    print(f"{response.text=}")
    pprint(response.json())
    print(f"{response.status_code=}")
    print(f"{response.headers=}")


# * Creación de plantilla
# Guardamos el archivo que esta en la web (después de su edición en Dreamweaver)
# html_content = requests.get(datos_de_acceso.RUTA_PLANTILAS + archivo)
# if html_content.status_code != 200:
#     logging.warning('❌ Cuidado: Error al leer la plantilla de la web. Sigue de forma manual.')
#     os.system(ALERTA)
#     sys.exit()
# html_content = html_content.text.replace('<img src="', '<img src="https://axoncomunicacion.net/masivos/axon_news/')
# * Creamos la plantilla en Acumbamail
# api_create_template(str(boletin), html_content)


# * Creación de campaña
createCampaign(name='Prueba3', subject='Asunto', html_content='código html', date_send='2023-12-30 23:00')
