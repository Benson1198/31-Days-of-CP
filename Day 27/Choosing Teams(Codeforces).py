def solve(n,k,par):
    par = sorted(par)
    teams = 0
    for i in range(0,n,3):
        if(i+1<n and i+2<n):
            pl1 = par[i]+k
            pl2 = par[i+1]+k
            pl3 = par[i+2]+k
            if(pl1<=5 and pl2<=5 and pl3<=5):
                teams+=1

    print(teams)

n,k = [int(y) for y in input().split()]
par = [int(y) for y in input().split()]
solve(n,k,par)