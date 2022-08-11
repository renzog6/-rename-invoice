import cv2  # opencv-python
import fitz
import base64
import json
from pyzbar.pyzbar import decode

# Convierte la pagina en imagen png y lle el codigo QR
# Devuelve un string en el formato que se quiere renombrar los archivos


def get_name_file(path_file):
    try:        
        # read pdf file
        pdf = fitz.open(path_file)
        # load pdf page using index
        page = pdf.load_page(0)        

        #image_matrix.preScale zoom para detectar QR
        image_matrix = fitz.Matrix(4, 4)  # (fitz.Identity)    
        pix = page.get_pixmap(alpha=False, matrix=image_matrix)
        pix.save('tmp.png')

        #Lee image temporal
        img = cv2.imread("tmp.png")
        #Detecata codigo QR
        qr_code = "none"
        for barcode in decode(img):
            qr_code = barcode.data.decode('ascii')
            #print(qr_code)
        #convierte string del QR en json
        base64_message = qr_code.replace('https://www.afip.gob.ar/fe/qr/?p=', '')
        base64_bytes = base64_message.encode('ascii')
        message_bytes = base64.b64decode(base64_bytes)
        message = message_bytes.decode('ascii')
        #print(message)
        msj_json = json.loads(message)
        # {
        #     "ver":1,
        #     "fecha":"2022-08-08",
        #     "cuit":20218218351,
        #     "ptoVta":3,
        #     "tipoCmp":3,
        #     "nroCmp":25,
        #     "importe":16509.24,
        #     "moneda":"PES","ctz":1,
        #     "tipoDocRec":80,
        #     "nroDocRec":30710703503,
        #     "tipoCodAut":"E",
        #     "codAut":72321962143214
        # }
        #print(msj_json["fecha"])
        #print(type(msj_json["cuit"]))
        tipoCmp = '{:>03d}'.format(msj_json["tipoCmp"])
        ptoVta = '{:>05d}'.format(msj_json["ptoVta"])
        nroCmp = '{:>08d}'.format(msj_json["nroCmp"])
        name_file = str(msj_json["cuit"]) +"_"+tipoCmp +"_"+ ptoVta +"-"+nroCmp+"_"+msj_json["fecha"]
        return name_file
    except:
        #print("An exception occurred")
        return "ERROR"
