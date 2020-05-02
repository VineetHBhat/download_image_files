import unittest
import download_files

class Test_download_files(unittest.TestCase):

    def setUp(self):
        self.readUrlFile = download_files.Download_files()
        self.extractName = download_files.Download_files()
        self.downloadUrl = download_files.Download_files()


    def test_read_url_file(self):
        test_list = ['https://unsplash.com/photos/tgDyb7H40-c/download?force=true',
                      'https://unsplash.com/photos/LZ-eqwE0NJA/download?force=true',
                      'https://unsplash.com/photos/SW9cs-yTjCE/download?force=true',
                      'https://unsplash.com/photos/g00cmIe0XN0/download?force=true',
                      'https://unsplash.com/photos/LkatwszbYjA/download?force=true',
                      'https://unsplash.com/photos/2S4Z6OQbyjE/download?force=true']

        self.assertEqual(self.readUrlFile.read_url_file("url_list.txt"), test_list)


    def test_extract_image_names(self):

        image_name_list = ['tgDyb7H40-c-unsplash.jpg',
                            'LZ-eqwE0NJA-unsplash.jpg',
                            'SW9cs-yTjCE-unsplash.jpg',
                            'g00cmIe0XN0-unsplash.jpg',
                            'LkatwszbYjA-unsplash.jpg',
                            '2S4Z6OQbyjE-unsplash.jpg']

        url_list = self.extractName.read_url_file("url_list.txt")

        self.assertListEqual(self.extractName.extract_image_names(url_list), image_name_list)


    def test_download_from_url(self):

        downloaded_images = ['download_dir/tgDyb7H40-c-unsplash.jpg',
                            'download_dir/LZ-eqwE0NJA-unsplash.jpg',
                            'download_dir/SW9cs-yTjCE-unsplash.jpg',
                            'download_dir/g00cmIe0XN0-unsplash.jpg',
                            'download_dir/LkatwszbYjA-unsplash.jpg',
                            'download_dir/2S4Z6OQbyjE-unsplash.jpg']

        urls = self.downloadUrl.read_url_file("url_list.txt")
        images = self.downloadUrl.extract_image_names(urls)

        self.assertEqual(self.downloadUrl.download_from_url(urls, images),downloaded_images)

if __name__ == "__main__":
    unittest.main()
