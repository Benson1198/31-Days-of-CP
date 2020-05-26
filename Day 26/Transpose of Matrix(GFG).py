def transpose( mat,n):
    
    for i in range(n):
        for j in range(i+1,n):
            mat[i][j],mat[j][i]=mat[j][i],mat[i][j]

			
def main():
    T=int(input())
    while(T>0):
        n=int(input())
        mat=[[0 for j in range(n)] for i in range(n)]
        line1=[int(x) for x in input().strip().split()]
        
       
        k=0
        for i in range(n):
            for j in range (n):
                mat[i][j]=line1[k]
                k+=1
       
        k=0
       
        transpose(mat,n)
        for i in range(n):
            for j in range(n):
                print(mat[i][j],end=" ")
        print()
            
        
        T-=1

if __name__=="__main__":
    main()
