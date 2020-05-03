import unittest
import download_files


class Test_download_files(unittest.TestCase):

    def setUp(self):
        #######################################################################
        #            Following variables should be modified for               #
        #                     some other url_txt_file                         #
        #######################################################################
        url_txt_file = "url_list.txt"
        self.read_file_regex = r'https.+true'
        self.extract_name_regex = r'(?<=/)[^/]+(?=/download)'
        self.download_dir_path = 'download_dir'

        self.test_list = [
            'https://unsplash.com/photos/tgDyb7H40-c/download?force=true',
            'https://unsplash.com/photos/LZ-eqwE0NJA/download?force=true',
            'https://unsplash.com/photos/SW9cs-yTjCE/download?force=true',
            'https://unsplash.com/photos/g00cmIe0XN0/download?force=true',
            'https://unsplash.com/photos/LkatwszbYjA/download?force=true',
            'https://unsplash.com/photos/2S4Z6OQbyjE/download?force=true'
        ]
        self.image_name_list = ['tgDyb7H40-c-unsplash.jpg',
                                'LZ-eqwE0NJA-unsplash.jpg',
                                'SW9cs-yTjCE-unsplash.jpg',
                                'g00cmIe0XN0-unsplash.jpg',
                                'LkatwszbYjA-unsplash.jpg',
                                '2S4Z6OQbyjE-unsplash.jpg']
        self.downloaded_images = ['download_dir/tgDyb7H40-c-unsplash.jpg',
                                  'download_dir/LZ-eqwE0NJA-unsplash.jpg',
                                  'download_dir/SW9cs-yTjCE-unsplash.jpg',
                                  'download_dir/g00cmIe0XN0-unsplash.jpg',
                                  'download_dir/LkatwszbYjA-unsplash.jpg',
                                  'download_dir/2S4Z6OQbyjE-unsplash.jpg']
        #######################################################################

        self.readUrlFile = download_files.Download_files(url_txt_file)
        self.extractName = download_files.Download_files(url_txt_file)
        self.downloadUrl = download_files.Download_files(url_txt_file)

        #######################################################################

    def test_read_url_file(self):

        self.assertEqual(self.readUrlFile.read_url_file(self.read_file_regex),
                         self.test_list)

    def test_extract_image_names(self):

        url_list = self.extractName.read_url_file(self.read_file_regex)

        self.assertListEqual(self.extractName.extract_image_names(
            url_list, self.extract_name_regex), self.image_name_list)

    def test_download_from_url(self):

        urls = self.downloadUrl.read_url_file(self.read_file_regex)
        images = self.downloadUrl.extract_image_names(urls,
                                                      self.extract_name_regex)

        self.assertEqual(self.downloadUrl.download_from_url(
            urls, images, self.download_dir_path), self.downloaded_images)


if __name__ == "__main__":
    unittest.main()
