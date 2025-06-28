package dev._60jong.backtracking.programmers.complete_criminal;

class Solution {
    int[][] infos;
    int N;
    int M;
    boolean[][][] vis;
    int minA = Integer.MAX_VALUE;
    public int solution(int[][] info, int n, int m) {
        infos=info;
        N=n;
        M=m;
        vis=new boolean[info.length][121][121];
        dfs(0,0,0);

        if(minA == Integer.MAX_VALUE) return -1;
        return minA;
    }

    public void dfs(int i, int a, int b) {
        if (a>=N || b>=M) return;
        if (i==infos.length) {
            minA=Math.min(a, minA);
            return;
        }


        if (vis[i][a][b]) {
            return;
        }
        vis[i][a][b] = true;
        dfs(i+1, a+infos[i][0], b);
        dfs(i+1,a,b+infos[i][1]);
    }
}
