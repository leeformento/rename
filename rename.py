import os
import urllib.request
from bs4 import BeautifulSoup

def make_soup(url):
    thepage= urllib.request.urlopen(url)
    soupdata = BeautifulSoup(thepage, "html.parser")
    return soupdata

os.chdir('/Users/Lee/Desktop/New Fabrics/Schumacher/Bleeker_Blach')

for f in os.listdir():
    file_name, file_ext = os.path.splitext(f)

    f_color, f_sku = file_name.split('_')
    print('{}-{}{}'.format(f_color, f_sku, file_ext))

