# Library for handling images

def main():
    data = get('/home/dci-student/Python/shopping_list/pexels-bertellifotografia-573299.jpg')
    print(type(data))

def get(path: str) -> bytes:
    with open(path, 'rb') as file:
        binary_data = file.read()
        return binary_data

def store(file: str, image: bytes) -> None:
    """Store binary data to file
    
    THe image is converted into jpeg and stored in file.jpg

    Args:
        file (str): Name of the file
        image (bytes): variable holding the image as bytes
    """
    with open(file, 'wb') as file:
        output_file_path = f"{file}.jpg"
        file.write(image)

if __name__ == "__main__":
    main()