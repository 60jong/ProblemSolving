package dev._60jong.backtracking.programmers.holzzak_tree;

import java.io.*;
import java.util.*;

class Solution {
    public int[] solution(int[] nodes, int[][] edges) {
        /* edge 정리 */
        int maxNodeNum = 0;
        Map<Integer, List<Integer>> nodeChildren = new HashMap<>();

        for (int n : nodes) { // O(V)
            nodeChildren.put(n, new ArrayList<>());
            maxNodeNum = Math.max(n, maxNodeNum);
        }

        for (int[] edge : edges) { // O(E)
            int a = edge[0];
            int b = edge[1];

            nodeChildren.get(a).add(b);
            nodeChildren.get(b).add(a);
        }

        /* tree 그룹 분리 */
        List<List<Integer>> treeGroup = new ArrayList<>();
        List<Count> counts = new ArrayList<>();

        boolean[] vis = new boolean[maxNodeNum + 1];

        for (int i = 1; i <= maxNodeNum; i++) {
            if (vis[i]) continue;
            if (!nodeChildren.containsKey(i)) continue;

            List<Integer> treeElements = new ArrayList<>();

            Queue<Integer> q = new LinkedList<>();
            treeElements.add(i);
            q.add(i);
            vis[i] = true;

            Count count = new Count();

            while (!q.isEmpty()) {
                int cur = q.poll();

                count(count, cur, nodeChildren);

                for (int next : nodeChildren.get(cur)) {
                    if (!vis[next]) {
                        q.add(next);
                        vis[next] = true;
                        treeElements.add(next);
                    }
                }
            }

            treeGroup.add(treeElements);
            counts.add(count);
        }

        /* Tree group 마다 하나씩 root 설정 */
        int nCount = 0;
        int rCount = 0;

        for (int i = 0; i < treeGroup.size(); i++) {
            List<Integer> group = treeGroup.get(i);
            Count cnt = counts.get(i);

            boolean nEnable = false;
            boolean rEnable = false;

            for (int n : group) {
                if (nEnable && rEnable) {
                    break;
                }

                int[] cntTemp = {cnt.odd, cnt.even, cnt.rOdd, cnt.rEven};

                int idx = findTypeIdx(n, nodeChildren);
                cntTemp[idx] -= 1;

                int temp = cntTemp[0];
                cntTemp[0] = cntTemp[2];
                cntTemp[2] = temp;

                temp = cntTemp[1];
                cntTemp[1] = cntTemp[3];
                cntTemp[3] = temp;

                cntTemp[idx] += 1;

                if (cntTemp[0] == 0 && cntTemp[1] == 0) {
                    rEnable = true;
                }

                if (cntTemp[2] == 0 && cntTemp[3] == 0) {
                    nEnable = true;
                }
            }

            if (nEnable) nCount++;
            if (rEnable) rCount++;
        }


        return new int[] {nCount, rCount};
    }

    public int findTypeIdx(int n, Map<Integer, List<Integer>> nc) {
        boolean isEven = n % 2 == 0;
        boolean isCEven = nc.get(n).size() % 2 == 0;

        if (isEven) {
            if (isCEven) {
                return 1;
            } else {
                return 3;
            }
        } else {
            if (isCEven) {
                return 2;
            } else {
                return 0;
            }
        }
    }

    public void count(Count cnt, int cur, Map<Integer, List<Integer>> nc) {
        boolean isEven = cur % 2 == 0;
        boolean isCEven = nc.get(cur).size() % 2 == 0;

        if (isEven) {
            if (isCEven) {
                cnt.even++;
            } else {
                cnt.rEven++;
            }
        } else {
            if (isCEven) {
                cnt.rOdd++;
            } else {
                cnt.odd++;
            }
        }
    }

    public static class Count {
        int odd;
        int even;
        int rOdd;
        int rEven;

        public String toString() {
            return String.format("{odd : %d, even : %d, rOdd : %d, rEven : %d}", odd, even, rOdd, rEven);
        }
    }
}
