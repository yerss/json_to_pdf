import json
import requests

from generate_pdf import generate

biin = '111140019207'


def main():
    url = f'http://192.168.2.107/counterparty/detail/{biin}/pdf'
    response = requests.get(url)
    if response.status_code == 200:
        content = response.content
        data = json.loads(content)
        generate(data)


if __name__ == '__main__':
    main()
