import requests
from pprint import pprint
  
class YaDrive:

    def __init__(self, token, default_cloud_path):
          self.token = token
          self.default_cloud_path = default_cloud_path
    
    def get_headers(self):
        return {
            'Accept' : 'application/json',
            'Authorization' : f'OAuth {self.token}'
        }

    def get_files_list(self, path_to_cloud=None):
        if path_to_cloud is None:
            path_to_cloud = self.default_cloud_path    
        files_url = 'https://cloud-api.yandex.net/v1/disk/resources/'
        headers = self.get_headers()
        parametrs = {
            'path' :  path_to_cloud,
            'limit' : 1000
        }
        response = requests.get(files_url, headers=headers, params=parametrs)
        files = [file['name'] for file in response.json()['_embedded']['items']]
        print(files)

    def upload(self, filename, path_to_cloud = None, path_to_folder = ''):
        if '\\' in filename:
            path_to_folder = filename[: filename.rfind('\\') + 1]   
            filename = filename[filename.rfind('\\') + 1 :]    
        if path_to_cloud is None:
            path_to_cloud = self.default_cloud_path          
        url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": path_to_cloud + filename, "overwrite": "true"}
        link =  requests.get(url, headers=headers, params=params).json().get('href', None)
        if link is None:
            print('Unable to get upload link')
        else:  
            response = requests.put(link, data=open(path_to_folder + filename, 'rb'))
            if response.status_code == 201:
                print(f'Upload {filename} is Success')
            else:
                print('Upload is falled')


if __name__ == '__main__':
    token = ''
    disck = YaDrive(token, '/test_app/')
    disck.upload('E:\\RP.txt')
    disck.get_files_list()













