import time

from urllib.request import urlopen

class WebPage:
    def __init__(self, url):
        self.url = url
        self._content = None

    @property
    def content(self):
        if not self._content:
            print("Retrieving New Page...")
            self._content = urlopen(self.url).read()
        return self._content

if __name__ in '__main__':
    wp = WebPage('https://github.com/dsysoev')
    print('run content')
    start = time.time()
    _ = wp.content
    print('elapsed time: {:.4f} sec'.format(time.time() - start))
    print('run content again')
    start = time.time()
    _ = wp.content
    print('elapsed time: {:.4f} sec'.format(time.time() - start))
