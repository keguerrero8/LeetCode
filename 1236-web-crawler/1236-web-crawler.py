# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution(object):
    def crawl(self, startUrl, htmlParser):
        start, end = -1, -1
        for i in range(1, len(startUrl)):
            if startUrl[i] == "/" and startUrl[i-1] == "/":
                start = i + 1
            elif start != -1 and startUrl[i] == "/":
                end = i
                break
        if end == -1:
            end = len(startUrl)
        res = set()
        
        def dfs(url):
            if startUrl[start:end] not in url:
                return
            
            if startUrl[start:end] in url:
                res.add(url)
                
            neighbors = htmlParser.getUrls(url)
            for nei in neighbors:
                if nei in res:
                    continue
                dfs(nei)
              

        dfs(startUrl)
        return list(res)
                
        