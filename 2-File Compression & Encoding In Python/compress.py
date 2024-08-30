import zlib, base64

def comprimir(archivo_entrada, archivo_salida):
    data = open(archivo_entrada, 'r').read()
    data_bytes = bytes(data,'utf-8') #datos convertidos de string a bytes
    compressed_data = base64.b64encode(zlib.compress(data_bytes, 1)) #cambiamos la base de 32 a 64 y comprimimos los datos
    decoded_data = compressed_data.decode('utf-8') #datos convertidos de bytes a string
    compressed_file = open(archivo_salida, 'w')
    compressed_file.write(decoded_data)

def descomprimir(archivo_entrada, archivo_salida):
    data = open(archivo_entrada, 'r').read()
    encoded_data = data.encode('utf-8') #datos convertidos de string a bytes
    decompressed_data = zlib.decompress(base64.b64decode(encoded_data)) #descomprimimos los datos
    decoded_data = decompressed_data.decode('utf-8') #datos convertidos de bytes a string
    decompressed_file = open(archivo_salida, 'w')
    decompressed_file.write(decoded_data)
    decompressed_file.close()

if __name__ == '__main__':
    comprimir('demo.txt', 'compressed.txt')
    
    descomprimir('compressed.txt', 'copia.txt')
    


