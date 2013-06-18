dwnldwwdc
=========

Download videos and slides from WWDC 2013 <https://developer.apple.com/wwdc/videos/>

Usage
-----

```bash
python dwnldwwdc.py ~/Tmp/ --pdf --sd
```

Download PDF slides and SD videos to the specified folder. Use --hd if you want to download HD videos.
This script uses a local copy of the WWDC Videos page, to not deals with authentication etc...

Prerequisites
-------------

Python 2.7+ and [Beautiful Soup 4](http://www.crummy.com/software/BeautifulSoup/)
To install Beautiful Soup 4, simply type

```bash
pip install beautifulsoup4 
```

 
