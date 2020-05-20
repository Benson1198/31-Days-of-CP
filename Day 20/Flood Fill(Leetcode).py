class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        rows = len(image)
        cols = len(image[0]) 
        
        match = image[sr][sc]
        image[sr][sc] = newColor
        
        visited = {(sr,sc):True}
        queue = [(sr,sc)]
        
        while len(queue) != 0:
            x,y = queue.pop()
            
            if x-1>=0 and image[x-1][y]==match and (x-1,y) not in visited:
                image[x-1][y] = newColor
                queue.append((x-1,y))
                visited[(x-1,y)] = True
                
            if x+1<rows and image[x+1][y]==match and (x+1,y) not in visited:
                image[x+1][y] = newColor
                queue.append((x+1,y))
                visited[(x+1,y)] = True
                
            if y-1>=0 and image[x][y-1]==match and (x,y-1) not in visited:
                image[x][y-1] = newColor
                queue.append((x,y-1))
                visited[(x,y-1)] = True
                
            if y+1<cols and image[x][y+1]==match and (x,y+1) not in visited:
                image[x][y+1] = newColor
                queue.append((x,y+1))
                visited[(x,y+1)] = True
                
        return image