""" This program downloads all images and converts them into one format.
"""

import os
import requests
import cairosvg
from PIL import Image
from pathlib import Path

from bs4 import BeautifulSoup


site = 'http://www.softformance.com'
out_folder = 'downloaded_images/'
out_path = Path.home() / out_folder


def get_response(site):
    """ Get a response from the site.
    """

    try:
        response = requests.get(site)
    except requests.exceptions.ConnectionError:
        print('Site name is incorrect!')
    else:
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup


def list_urls(soup):
    """ Form a list of links to the images from the site page.
    """

    img_tags = soup.find_all('img')
    urls = [img['src'] for img in img_tags]
    return urls


def file_name(file):
    """ Write a file as a png file.
    """

    return file.split('.')[0] + '.png'


def remove_file(path):
    """ Delete the file in the specified path.
    """

    os.remove(path)


def convert_svg_format(file):
    """ Convert svg images to png format
    """

    filename = file_name(file)
    outpath = os.path.join(out_path, file)
    outpath2 = os.path.join(out_path, filename)

    try:
        cairosvg.svg2png(url=outpath, write_to=outpath2)
    except TypeError:
        print("The file '{}' cann't convert to png format".format(file))
    else:
        remove_file(out_path / file)


def convert_other_format(file):
    """ Convert images (other than svg format) to png format.
    """

    im = Image.open(out_path / file)
    filename = file_name(file)

    if file.find('.') == -1:
        filename = file + '.png'

    im.save(out_path / filename, 'PNG')
    remove_file(out_path / file)


def convert_format(out_path):
    """ Convert all images to png format.
    """

    for file in os.listdir(out_path):
        if file[-3:] == 'png':
            continue
        if file[-3:] == 'svg':
            convert_svg_format(file)
            continue

        convert_other_format(file)
    print('All images from site "{}" were downloaded to the folder "{}"'
          ' and converted to png format.'.format(site, out_path))


def write_content(urls):
    """ Write url content to a folder.
    """

    for url in urls:
        filename = url.split('/')[-1]
        outpath = os.path.join(out_path, filename)

        if not out_path.exists():
            out_path.mkdir(parents=True)

        with open(outpath, 'wb') as f:

            if 'http' not in url:
                url = '{}/{}'.format(site, url)

            try:
                response = requests.get(url)
            except requests.exceptions.ConnectionError:
                print('Image url "{}"" is incorrect!'.format(url))
                continue
            else:
                f.write(response.content)


def list_section_links(soup):
    """ Form a list of links to all sections of the site.
    """

    site_menu = soup.find('ul', attrs={'id': 'menu-main'})

    if site_menu:
        site_sections = site_menu.find_all('a')
        if site_sections:
            url_sections = [a['href'] for a in site_sections]

    return url_sections


def main(site):
    """ Main entry point.
    """

    soup = get_response(site)
    if soup:
        urls = list_urls(soup)
        if urls:
            write_content(urls)

        url_sections = list_section_links(soup)
        if url_sections:
            for url_section in url_sections:
                soup = get_response(url_section)
                if soup:
                    urls = list_urls(soup)
                    if urls:
                        write_content(urls)

    if out_path.exists():
        convert_format(out_path)


if __name__ == '__main__':
    main(site)
