from datetime import datetime
from email.mime.image import MIMEImage
from pathlib import Path
import os

from num2words import num2words

from app.core.config import TIME_ZONE
import pytz
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class Utilities:

    @staticmethod
    def model_to_dict(model_instance):
        """Convierte un modelo de SQLAlchemy a un diccionario."""
        return {column.name: getattr(model_instance, column.name) for column in model_instance._table_.columns}

    @staticmethod
    def get_current_time():
        tz = pytz.timezone(TIME_ZONE)
        return datetime.now(tz)

    @staticmethod
    def get_number_to_text(number):
        numero = num2words(number, lang='es_CO')
        return numero.upper()

    @staticmethod
    def map_dto_to_entity(entity, dto, exclude_fields=None):
        exclude_fields = exclude_fields or []

        for field in dto._dict_:
            if not field.startswith("_") and field not in exclude_fields:
                setattr(entity, field, getattr(dto, field))

    @staticmethod
    def generate_table_html(form, version):
        headers = ['Formulario', 'Version']

        row_html = f'<tr><td style="text-align: center;">{form}</td><td style="text-align: ' \
                   f'center;">{version}</td></tr>'

        table_html = f'''
            <p>Estimado usuario se creó una nueva versión, encontraras la información adjunta en la siguiente tabla:</p>
            <table style="border-collapse: collapse; width: 100%;">
                <thead>
                    <tr style="background-color: #D2D904;">
                        <th style="padding: 10px; border: 1px solid #0D0D0D; text-align: center;">{headers[0]}</th>
                        <th style="padding: 10px; border: 1px solid #0D0D0D; text-align: center;">{headers[1]}</th>
                    </tr>
                </thead>
                <tbody style="border: 1px solid #0D0D0D;">{row_html}</tbody>
            </table>
            </br>
            </br>

            <img src="cid:imagenuno" alt="PREVEO © copyright" style="display: block; margin-top: 20px;
            width: 950px; height: 300px;">
        '''
        return table_html

    @staticmethod
    def generate_message_html(form, cc_name):
        headers = ['Formulario', 'Centro De Costo']

        row_html = f'<tr><td style="text-align: center;">{form}</td><td style="text-align: ' \
                   f'center;">{cc_name}</td></tr>'

        table_html = f'''
                <p>Estimado usuario se guardo un nuevo formato, encontraras la información adjunta en la siguiente tabla:</p>
                <table style="border-collapse: collapse; width: 100%;">
                    <thead>
                        <tr style="background-color: #D2D904;">
                            <th style="padding: 10px; border: 1px solid #0D0D0D; text-align: center;">{headers[0]}</th>
                            <th style="padding: 10px; border: 1px solid #0D0D0D; text-align: center;">{headers[1]}</th>
                        </tr>
                    </thead>
                    <tbody style="border: 1px solid #0D0D0D;">{row_html}</tbody>
                </table>
                </br>
                </br>

                <img src="cid:imagenuno" alt="PREVEO © copyright" style="display: block; margin-top: 20px;
                width: 950px; height: 300px;">
            '''
        return table_html

    @staticmethod
    def send_email(receiver, affair, message):
        remitter = 'krivas@progracol.com'
        password = 'Kenneth2022*'
        smtp = 'smtp.gmail.com'
        port = 587
        ssltls = 'SI'

        smtp_server = smtp
        port = port
        remitter = remitter
        password = password

        mensaje_mime = MIMEMultipart()
        mensaje_mime['From'] = remitter
        mensaje_mime['To'] = receiver
        mensaje_mime['Subject'] = affair

        mensaje_mime.attach(MIMEText(message, 'html'))

        directory_base = "app"
        sub_directory = "utils"
        name_file = "PREVEO.jpg"

        complete_path = os.path.join(Path.cwd(), directory_base, sub_directory, name_file)
        fp = open(complete_path, 'rb')
        img = MIMEImage(fp.read())
        fp.close()

        img.add_header('Content-ID', '<imagenuno>')
        mensaje_mime.attach(img)

        receivers = receiver.split(',')

        try:
            with smtplib.SMTP(smtp_server, port) as server:
                server.ehlo()
                if ssltls == "SI":
                    server.starttls()
                server.login(remitter, password)
                server.sendmail(remitter, receivers, mensaje_mime.as_string())

        except Exception as e:
            print('Error al enviar el correo:', str(e))


class ResponseMessages:
    DELETED = "Eliminado con exito"
    UPDATED = "Actualizado con exito"
    CREATED = "Creado con exito"
    SUCCESS_QUERY = "consultado con exito"
    FAILURE = "consulta fallida"


class Constants:
    DRAFT = "DRAFT"