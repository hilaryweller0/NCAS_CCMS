"""
This python file imports data from a URL. Optional second command line argument: directory name in which to save the file. Run in terminal window as: python download_url.py <URL> <OPTIONAL directory_name>
Author: Amber te Winkel
Date: 23-08-2025
"""


import sys
import os
import urllib.request as ur


def main():
    # Put command line arguments in variables
    url = sys.argv[1]
    cwd = os.getcwd()
    filename = url.split('/')[-1]

    # Create the directory inside the present working directory if it doesn't exist yet (to check the present working directory: run 'pwd' in the terminal or print out the cwd variable above)
    dirname = '' # an empty string
    if len(sys.argv) > 2:
        dirname = sys.argv[2]
        if not os.path.exists(f'{cwd}/{dirname}'):
            os.mkdir(dirname)
    filepath = cwd + '/' + dirname + '/' + filename
    
    # Download and save data (CAREFUL: this will overwrite existing files)
    ur.urlretrieve(url, filepath)
    print(f'URL data saved to {filepath}')


if __name__ == "__main__":
    main()