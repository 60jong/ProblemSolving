package dev._60jong.backtracking.programmers.server_scale_out;

class Solution {
    public int solution(int[] players, int m, int k) {
        int answer = 0;

        int s = 0;

        while (s < 24) {
            int servers = players[s] / m;
            if (servers <= 0) {
                s++;
                continue;
            }

            int e = Math.min(s + k, 24);
            for (int i = s; i < e; i++) {
                players[i] -= servers * m;
            }
            answer += servers;
            s++;
        }

        return answer;
    }
}
