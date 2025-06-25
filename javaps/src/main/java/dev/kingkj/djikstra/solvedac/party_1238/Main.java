package dev.kingkj.djikstra.solvedac.party_1238;

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        // setup //
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] line = br.readLine().split(" ");

        int N = Integer.parseInt(line[0]);
        int M = Integer.parseInt(line[1]);
        int X = Integer.parseInt(line[2]);

        List<List<Pair>> graph = new ArrayList<>();
        List<List<Pair>> reverseGraph = new ArrayList<>();
        for (int i = 0; i < N + 1; i++) {
            graph.add(new ArrayList<>());
            reverseGraph.add(new ArrayList<>());
        }

        for (int i = 0; i < M; i++) {
            line = br.readLine().split(" ");

            int from = Integer.parseInt(line[0]);
            int to = Integer.parseInt(line[1]);
            int cost = Integer.parseInt(line[2]);

            graph.get(from).add(new Pair(to, cost));
            reverseGraph.get(to).add(new Pair(from, cost));
        }

        // solution //

        // N -> X
        int INF = 1_000_000_000; // billion
        int[] dist1 = new int[N + 1];
        Arrays.fill(dist1, INF);

        PriorityQueue<Pair> pq = new PriorityQueue<>();
        pq.offer(new Pair(X, 0)); // start : X
        dist1[X] = 0;

        while (!pq.isEmpty()) {
            Pair pair = pq.poll();

            int ct = pair.t;
            int cc = pair.c;

            for (Pair p : graph.get(ct)) {
                if (dist1[p.t] > cc + p.c) {
                    dist1[p.t] = cc + p.c;
                    pq.offer(new  Pair(p.t, dist1[p.t]));
                }
            }
        }
        // X -> N
        int[] dist2 = new int[N + 1];
        Arrays.fill(dist2, INF);

        pq.offer(new Pair(X, 0));
        dist2[X] = 0;

        while (!pq.isEmpty()) {
            Pair pair = pq.poll();

            int ct = pair.t;
            int cc = pair.c;

            for (Pair p : reverseGraph.get(ct)) {
                if (dist2[p.t] > cc + p.c) {
                    dist2[p.t] = cc + p.c;
                    pq.offer(new  Pair(p.t, dist2[p.t]));
                }
            }
        }

        int result = 0;
        for (int i = 1; i < N + 1; i++) {
            if (result < dist1[i] + dist2[i]) {
                result = dist1[i] + dist2[i];
            }
        }


        // result //
        System.out.println(result);
    }

    public static class Pair implements Comparable<Pair> {
        int t;
        int c;

        public Pair(int t, int c) {
            this.t = t;
            this.c = c;
        }

        @Override
        public int compareTo(Pair o) {
            return o.c - this.c;
        }
    }
}
