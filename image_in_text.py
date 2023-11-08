import cv2 as cv
import numpy as np

def to_binary(data):
    if isinstance(data, str):
        return ''.join([ format(ord(i), "08b") for i in data ])
    elif isinstance(data, bytes):
        return ''.join([ format(i, "08b") for i in data ])
    elif isinstance(data, np.ndarray):
        return [ format(i, "08b") for i in data ]
    elif isinstance(data, int) or isinstance(data, np.uint8):
        return format(data, "08b")
    else:
        raise TypeError("Desteklenmeyen tür.")
    
def encode(image_name, secret_message):

    image = cv.imread(image_name, cv.COLOR_BGR2RGB)

    #kodlanacak maksimum bayt sayısını hesaplama
    n_bytes = image.shape[0] * image.shape[1] * 3 // 8
    print("Kodlanacak maksimum bayt sayısı:", n_bytes)

    if len(secret_message) > n_bytes:
        raise ValueError("Yetersiz bayt, daha büyük görüntü veya mesaj kullanın.")

    print("Mesaj Kodlanıyor...")

    secret_message += "*****"
    message_index = 0

    binary_secret_message = to_binary(secret_message)

    message_len = len(binary_secret_message)

    for col in range(image.shape[0]):
        for row in range(image.shape[1]):
            pixel = image[col,row]

            r = to_binary(pixel[0])
            g = to_binary(pixel[1])
            b = to_binary(pixel[2])

            if message_index < message_len:
                # least significant red pixel bit
                pixel[0] = int(r[:-1] + binary_secret_message[message_index], 2)
                message_index += 1
            if message_index < message_len:
                # least significant green pixel bit
                pixel[1] = int(g[:-1] + binary_secret_message[message_index], 2)
                message_index += 1
            if message_index < message_len:
                # least significant blue pixel bit
                pixel[2] = int(b[:-1] + binary_secret_message[message_index], 2)
                message_index += 1
            # eğer mesaj kodlanmışsa döngüden çık
            if message_index >= message_len:
                break

    print("Mesaj Kodlandı...")

    return image

def decode(image_name):
    print("Mesaj Çözülüyor...")

    image = cv.imread(image_name)
    binary_data = ""

    for col in range(image.shape[0]):
        for row in range(image.shape[1]):
            pixel = image[col, row]

            r = to_binary(pixel[0])
            g = to_binary(pixel[1])
            b = to_binary(pixel[2])

            #anlamsız biti diziye ekle
            binary_data += r[-1]
            binary_data += g[-1]
            binary_data += b[-1]

    # 8 bit aralıklara bölerek tüm byteları diziye koy
    all_bytes = []
    for i in range(0, len(binary_data), 8):
        byte = binary_data[i: i+8]
        all_bytes.append(byte)

    decoded_message = ""

    #byteları gez mesajı çıkar
    for byte in all_bytes:
        decoded_message += chr(int(byte, 2))
        if decoded_message[-5: ] == "*****":
            break

    print("Mesaj Çözüldü...")

    return decoded_message[:-5]    

if __name__ == "__main__":

    input_image = "ktu_logo.png"
    output_image = "gizlenmis.png"

    secret_message = input("Lütfen Gizlenecek Mesajı Giriniz: ")
    encoded_image = encode(image_name=input_image, secret_message=secret_message)    
    cv.imwrite(output_image, encoded_image)

    decoded_data = decode(output_image)
    print("Gizlenen Mesaj: " + decoded_data)

