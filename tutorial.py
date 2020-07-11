class Tutorial():
    def __init__(self, title, url, url_image):
        self.title = title
        self.url = url
        self.url_image = url_image

    def get_tutorial(self):
        return 'https://realpython.com/' + self.url