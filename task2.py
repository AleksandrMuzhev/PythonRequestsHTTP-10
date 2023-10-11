import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_upload_link(self, file_path: str):
        """Метод получает ссылку для загрузки файла file_path на яндекс диск"""
        headers = {
            'Authorization': f'OAuth {self.token}'
        }

        file_name = file_path.split('/')[-1]

        response = requests.get(
            f'https://cloud-api.yandex.net:443/v1/disk/resources/upload?path={file_name}',
            headers=headers
        )

        if response.status_code == 200:
            return response.json()['href']
        else:
            return None

    def upload(self, file_path: str):
        """Метод загружает файл file_path на яндекс диск"""
        headers = {
            'Authorization': f'OAuth {self.token}'
        }

        file_name = file_path.split('/')[-1]

        upload_url = self.get_upload_link(file_path)

        if upload_url is not None:
            with open(file_path, 'rb') as file:
                file_content = file.read()

        response = requests.put(
            upload_url,
            headers=headers,
            data=file_content
        )

        if response.status_code == 201:
            return 'Файл успешно загружен на Яндекс.диск'
        else:
            return f'Произошла ошибка при загрузке файла: {response.content.decode()}'


if __name__ == '__main__':
    uploader = YaUploader('y0_Ag12345678DkAADLWwAAAADgh0PnyIs_RfTiRdKEZj1cxm3LXBt6RRw')
    result = uploader.upload('D:/Python/Для pyqo10task2.docx')
    print(result)
