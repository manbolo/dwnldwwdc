#!/usr/bin/env python
import sys
import os
import urllib
import argparse
from bs4 import BeautifulSoup


def report(count, block_size, total_size):
    """Report save progression."""
    progress_size = int(count * block_size) / (1024 * 1024)
    percent = int(count * block_size * 100 / total_size)
    sys.stdout.write("\r  {0}%, {1} MB".format(percent, progress_size))
    sys.stdout.flush()


def save(url, dst, force=False):
    """Download a file at url to local folder."""
    if not os.path.isfile(dst) or force:
        # Test if the directory exist or create
        d = os.path.dirname(dst)
        if not os.path.exists(d):
            os.makedirs(d)
        print(u"\nDownloading: {0} to {1}".format(url, dst))
        urllib.urlretrieve(url, dst, report)


def download(folder_dst, pdf, sd, hd):
    """Parse the WWDC html page at https://developer.apple.com/wwdc/videos/.
    The page has been downloaded locally to prevent signin etc... Not the
    better solution, but a pragmatic one."""
    html_src = os.path.abspath(os.path.join(os.path.dirname(__file__), 'wwdc2013.html'))

    try:
        soup = BeautifulSoup(open(html_src, 'r').read())
    except IOError:
        print("No wwdc2013.html here! Download the file from https://raw.github.com/manbolo/dwnldwwdc/master/wwdc2013.html")
        return -1

    for div in soup.find_all('div', 'description active'):
        ul = div.find('ul')
        li = ul.find_all('li')

        title = li[0].text
        session = li[1].text
        p = div.find('p', 'download')
        if not p:
            continue
        a = p.find_all('a')

        if len(a) and hd:
            url = a[0].get('href')
            dst = u"{0}/Videos/{1} - {2} - HD.mov".format(folder_dst, title, session)
            save(url, dst)

        if len(a) > 1 and sd:
            url = a[1].get('href')
            dst = u"{0}/Videos/{1} - {2}.mov".format(folder_dst, title, session)
            save(url, dst)

        if len(a) > 2 and pdf:
            url = a[2].get('href')
            dst = u"{0}/Slides/{1} - {2}.pdf".format(folder_dst, title, session)
            save(url, dst)

    print(u"\nDone!")
    return 0

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("dst", help="destination folder")
    parser.add_argument("--pdf", help="download only PDF", action="store_true", default=False)
    parser.add_argument("--sd", help="download only SD videos", action="store_true", default=False)
    parser.add_argument("--hd", help="download only HD videos", action="store_true", default=False)
    args = parser.parse_args()

    sys.exit(download(folder_dst=args.dst, pdf=args.pdf, sd=args.sd, hd=args.hd))


