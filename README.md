# Image Steganography using OpenCV and Python

This project demonstrates how to encode and decode secret messages within images using steganography. The implementation is done using Python and OpenCV.

## Description

Steganography is the practice of hiding a secret message within another file, such as an image. This project uses the least significant bit (LSB) technique to encode and decode messages.

### Features
- Encode a secret message within an image.
- Decode the secret message from an encoded image.

## Requirements

- Python 3.x
- OpenCV
- NumPy

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/osmancanaksoy/image-steganography.git
    ```

2. Navigate to the project directory:

    ```bash
    cd image-steganography
    ```

## Usage

1. Place the input image (`input_image.png`) in the project directory.

2. Run the script:

    ```bash
    python image_in_text.py
    ```

3. Enter the secret message when prompted.

4. The encoded image will be saved as `encoded_image.png`.

5. To decode the message, run the script again and it will extract and display the hidden message.

## Code Overview

### `to_binary(data)`

Converts data to its binary representation.

### `encode(image_name, secret_message)`

Encodes the secret message into the image.

### `decode(image_name)`

Decodes the secret message from the image.

## Example

### Encoding

1. Input image: `ktu_logo.png`
2. Secret message: `Hello, World!`

```bash
python image_in_text.py
```

### Decoding

```bash
python image_in_text.py
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

