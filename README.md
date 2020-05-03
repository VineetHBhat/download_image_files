# Download Images using Python `requests` module

This program is developed using TDD (Test Driven Development) approach to download images from [unsplash](https://unsplash.com) and save them in a directory defined by `download_dir_path` which is passed to `download_from_url()` method. The program also uses `re` module to use *regular expresssions* to extract URL and image names. Since, multiple images are being downloaded, `download_from_url()` method also implements the use of `concurrent.futures` module to start the downloads on multiple threads.

## Description about various files

1. The URL's for all images are stored in `url_list.txt` file.
1. `download_files.py` defines the `class Download_files` which provides the following methods.
    1. `read_url_file(self, read_file_regex)`: This method reads the file containing the URL's and returns the URL's in the form of a list. You may need to pass a modified `read_file_regex` variable to use this with other URL's.
    1. `extract_image_names(self, url_list, extract_name_regex)`: This method takes a URL list (returned by `read_url_file()`) and returns a list with image names. The image names are extracted from the URL. You may need to pass a modified `extract_name_regex` variable to use this with other URL's.
    1. `download_from_url(self, url_list, image_name_list, download_dir_path)`: This method does the actual task of downloading and saving the images from the web.
    1. `download_files.py` also provides a classmethod named `download_single_image(cls, image, url)` which is used by `download_from_url()`.
1. `test_download_files.py` defines test-cases for all 3 methods defined in `download_files.py`. Three different *instance variabes* have been created to test the 3 methods, but this is not necessary and a single *instance variabe* can also be used.

*This program needs refactoring. I will be working on it from time to time. Meanwhile any suggestion are appreciated.*
