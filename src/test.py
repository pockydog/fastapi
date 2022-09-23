import requests


class Test:
    _URL = 'http://127.0.0.1:8000/file'

    @classmethod
    def add_info(cls):
        files = {'files': open('/Users/vicky/Desktop/123.jpg', 'rb')}
        payload = {
            'image': files,
            'description': files,
        }
        response = requests.post(url=cls._URL, files=files, json=payload)
        print(response.text)

if __name__ == '__main__':
    Test.add_info()