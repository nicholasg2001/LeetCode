class Solution:
    def isPathCrossing(self, path: str) -> bool:
        d=[[0,0]]
        x,y=0,0
        for i in path:
            if(i=="N"):
                y+=1
            elif(i=="E"):
                x+=1
            elif(i=="S"):
                y-=1
            else:
                x-=1
            if [x,y] in d:
                return True
            d.append([x,y])
            
        return False
        