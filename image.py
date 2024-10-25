# Library for handling images

def main():
    data = get('/home/dci-student/Python/shopping_list/pexels-bertellifotografia-573299.jpg')
    print(type(data))

def get(path: str) -> bytes:
    with open(path, 'rb') as file:
        binary_data = file.read()
        return binary_data

def store(image: bytes) -> None:
    

if __name__ == "__main__":
    main()