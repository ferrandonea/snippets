''' Relacionado con monkey_patching.ipynb'''
import requests

def get_data() -> dict:
    r = requests.get('https://jsonplaceholder.typicode.com/todos/1')
    data: dict = r.json()
    return data

if __name__ == "__main__":
    print (get_data())
    print (type(get_data()))