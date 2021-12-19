from os import path, makedirs, sep
import os

import requests
import sys
import zipfile
import tarfile

class Loader:

    def __init__(self, url, target_folder, extraction_target=None, skip_unzip=False):
        """
            zip_folder_path doit terminer par un separateur ('/' ou '\')
        """
        self.url = url
        self.folder_path = target_folder
        
        # recuperation du nom du zip
        self.file = self.folder_path + url.split('/')[-1]
        self.extraction_target = extraction_target

        self.skip_unzip = skip_unzip

    def ensure_data_loaded(self):
        '''
        Ensure if data are already loaded. Download if missing.
        '''

        if not path.exists(self.file):
            if Loader.__ask("Télécharger le fichier [y]/n ? "):
                try:
                    self.__download_data()
                except requests.exceptions.ConnectionError as e:
                    os.rmdir(self.file)
                    raise e
        else:
            print('Le fichier existe déjà')

        if self.skip_unzip:
            return

        if not Loader.__ask("Dé-zipper le fichier [y]/n ? "):
            return

        Loader.extract_data(self.extraction_target, self.file)

        print('\nLes fichiers sont correctement extractés')

    def __ask(input_text) -> bool:
        user_input = ""
        user_input = input(input_text)
        while user_input not in ["n", "N", "y", "Y", ""]:
            user_input = input(input_text)

        if user_input in ["y", "Y", ""]:
            return True

    @staticmethod
    def __test_folder(folder):
        if path.exists(folder) == False:
            try:
                makedirs(folder)
            except OSError:
                print(f"Creation of the directory {folder} failed")
                exit(1)
            else:
                print(f"Successfully created the directory {folder}")

    def __download_data(self):
        '''
        Download the data from internet
        '''
        Loader.__test_folder(self.folder_path)

        try:
            print('Downloading data')
            with open(self.file, "wb") as f:
                response = requests.get(self.url, stream=True)
                total_length = response.headers.get('content-length')

                if total_length is None: # no content length header
                    f.write(response.content)
                else:
                    dl = 0
                    total_length = int(total_length)
                
                    for data in response.iter_content(chunk_size=4096):
                        dl += len(data)
                        f.write(data)
                        done = int(50 * dl / total_length)
                        sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50-done)) )    
                        sys.stdout.flush()
        except Exception as e:
            os.remove(self.file)
            raise Exception(e)

    @staticmethod
    def extract_data(extraction_target, file):
        '''
        Extract the zip file to the hard disk
        '''
        Loader.__test_folder(extraction_target)

        # print(self.file)
        
        if file.endswith(".zip"):
            with zipfile.ZipFile(file, 'r') as compressed_file:
                compressed_file.extractall(extraction_target)
        elif file.endswith(".tar.gz"):
            with tarfile.TarFile.open(file, 'r:gz') as compressed_file:
                compressed_file.extractall(extraction_target)

        print('Extracted', len(os.listdir(extraction_target)), "files in '" + extraction_target + "'")

if __name__ == "__main__":
    loader = Loader(
        "https://stdatalake010.blob.core.windows.net/public/cifar-100.zip",
        '../datas/ZIP/',
        '../datas/RAW/'
    )
    loader.ensure_data_loaded()
    