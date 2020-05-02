# Download Images using Python `requests` module

This program is developed using TDD (Test Driven Development) approach to download images from [unsplash](https://unsplash.com). The program also uses `re` module to extract URL and image names. Since, multiple images are being downloaded, `download_from_url` method also implements the use of `concurrent.futures` module to start the downloads on multiple threads.

## Description about various files

1. The URL's for all images are store in `url_list.txt` file.
2. `download_files.py` defines the `class Download_files` which provides the following method.
⋅⋅1. `read_url_file(self, url_file)`: This method reads the file containing the urls and return the urls in the form of a list. You may need to modify the %reg_exp% variable.
⋅⋅2. `extract_image_names(self, url_list)`: This method takes a url list and returns a list with image names. The image names are extracted from the url. You may need to modify the %reg_exp% variable.
⋅⋅3. `download_from_url(self, urls, images)`: This method does the actual task of downloading and saving the images from the web.
⋅⋅4. `download_files.py` also provides a classmethod named `download_single_image(cls, image, url)` which is used by `download_from_url(self, urls, images)`.
3. `test_download_files.py` defines test-cases for all 3 methods defined in `download_files.py`. Three different *instance variabes* have been created to test the 3 methods, but this is not necessary and a single *instance variabe* can also be used.
