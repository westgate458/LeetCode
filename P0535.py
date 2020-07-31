class Codec:
	# (26+26+10)-based number
    def __init__(self):
        self.map = {}
        self.chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        self.ID = 0
        
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        shortUrl = ''
        ID = self.ID
        while ID:
            ID, p = divmod(ID, 62)
            shortUrl += self.chars[p]
        self.map[shortUrl] = longUrl
        self.ID += 1
        return 'http://tinyurl.com/' + shortUrl
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.map[shortUrl.split('/')[-1]]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))