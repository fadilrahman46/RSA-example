import base64
from PIL import Image
from io import BytesIO

with open("C:/Users/User/Downloads/Kampus-II-UNS-di-Caruban.jpg", "rb") as image_file:
    data = base64.b64encode(image_file.read())

print(data)
        
with open("D:/UNS/UNS MADIUN/Sistem Keamanan Data/Materi_Praktikum/RSA/encode_image_asli2.txt", "w") as file:
    file.write(str(data))

im = Image.open(BytesIO(base64.b64decode(data)))
im.save('D:/UNS/UNS MADIUN/Sistem Keamanan Data/Materi_Praktikum/RSA/image1.png', 'PNG')