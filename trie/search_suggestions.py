# https://leetcode.com/problems/search-suggestions-system
class Solution:
    def suggestedProducts(self, products: list[str], searchWord: str) -> list[list[str]]:
        products = sorted(products)
        suggested_products = []
        for i in range(len(searchWord)):
            products = [p for p in products if len(p) > i and p[i] == searchWord[i]]
            suggested_products.append(products[0:3])
        return suggested_products
        
