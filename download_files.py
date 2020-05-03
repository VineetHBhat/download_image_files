import requests
import concurrent.futures
import re

class Download_files:
    '''
    This class provides methods to read a list of urls from a file and then
    download those files using the urls.
    '''

    ###########################################################################

    def read_url_file(self, url_file):
        '''
        This method reads the file containing the urls and return the urls in
        the form of a list. You may need to modify the %reg_exp% variable.
        '''

        self.url_file = url_file
        reg_exp = r'https.+true'
        self.url_list = []

        with open(self.url_file, 'r') as url_f:
            urls = url_f.read()

        pattern = re.compile(reg_exp)
        matches = pattern.finditer(urls)

        for match in matches:
            self.url_list.append(match.group())

        return self.url_list

    ###########################################################################

    def extract_image_names(self, url_list):
        '''
        This method takes a url list and returns a list with image names. The
        image names are extracted from the url. You may need to modify the
        %reg_exp% variable.
        '''

        url_list_str = ""
        reg_exp = r'(?<=/)[^/]+(?=/download)'
        self.extracted_image_name = []

        pattern = re.compile(reg_exp)
        matches = pattern.finditer(url_list_str.join(url_list))

        for match in matches:
            self.extracted_image_name.append(f'{match.group()}-unsplash.jpg')

        return self.extracted_image_name

    ###########################################################################

    def download_from_url(self, urls, images):
        '''
        This method does the actual task of downloading and saving the images
        from the web.
        '''

        download_dir_path = 'download_dir'
        self.downloaded_images = []

        with concurrent.futures.ThreadPoolExecutor() as executor:

            futures = [executor.submit(Download_files.download_single_image, image, url)\
                            for (image, url) in zip(images, urls)]

            for (future,image) in zip(concurrent.futures.as_completed(futures),images):

                try:
                    response = future.result()
                    response.raise_for_status()

                except Exception:
                    print("###################################################")
                    print("An exception was generated while downloading {image}.\nDetails:\n{Exception}")
                    print("###################################################")

                else:
                    print("===================================================")
                    print(f'Downloaded [{image}]')

                    with open(f'{download_dir_path}/{image}', 'wb') as byte_img:
                        byte_img.write(response.content)

                    print(f'Saved in {download_dir_path}/')
                    print("===================================================")

                    self.downloaded_images.append(f'{download_dir_path}/{image}')

        print("All downloads have completed.")
        return self.downloaded_images

    ###########################################################################

    @classmethod
    def download_single_image(cls, image, url):
        print(f'Downloading [{image}] from <{url}>')
        cls.response = requests.get(url)
        return cls.response

    ###########################################################################
