class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if image[sr][sc] == newColor: return image
        q = [(sr,sc)]
        oldColor = image[sr][sc]
        image[sr][sc] = newColor
        m, n = len(image), len(image[0])
        for i, j in q:
            for ii, jj in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                if 0 <= ii < m and 0 <= jj < n and image[ii][jj] == oldColor:
                    image[ii][jj] = newColor
                    q.append((ii,jj))
        return image