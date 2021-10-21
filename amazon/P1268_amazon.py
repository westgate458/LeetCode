class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:                
        d = defaultdict(list)
        for product in sorted(products):
            for i in range(len(product)):
                d[product[:i+1]].append(product)                
        res = []
        for i in range(len(searchWord)):
            res.append(d[searchWord[:i+1]][:3])        
        return(res)