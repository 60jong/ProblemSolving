import java.util.*;
import java.io.*;

public class Main {
    static int N, M, P, C, D;
    static int Rr, Rc;

    static List<List<Integer>> grid;

    static int[] RdirR = {-1, -1, 0, 1, 1,  1,  0, -1};
    static int[] RdirC = {0,   1, 1, 1, 0, -1, -1, -1};

    static Santa[] santaLocations;
    static int[] scores;
    static int retired = 0;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        // Grid
        N = Integer.parseInt(st.nextToken());
        grid = new ArrayList<>(N + 1);
        for (int n = 0; n <= N; n++) {
            grid.add(new ArrayList<>(Collections.nCopies(N + 1, 0)));
        }

        M = Integer.parseInt(st.nextToken());
        P = Integer.parseInt(st.nextToken());
        santaLocations = new Santa[P + 1];
        scores = new int[P + 1];

        C = Integer.parseInt(st.nextToken());
        D = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine(), " ");
        Rr = Integer.parseInt(st.nextToken());
        Rc = Integer.parseInt(st.nextToken());
        setGridValue(Rr, Rc, -1);

        // Santa
        for (int p = 0; p < P; p++) {
            st = new StringTokenizer(br.readLine(), " ");
            int Si = Integer.parseInt(st.nextToken());
            int Sr = Integer.parseInt(st.nextToken());
            int Sc = Integer.parseInt(st.nextToken());

            setGridValue(Sr, Sc, Si);
            santaLocations[Si] = new Santa(Si, Sr, Sc);
        }

        for (int m = 1; m <= M; m++) {
            // Move Rudolf
            int dir = findShortestRDir();
            setGridValue(Rr, Rc, 0);
            Rr += RdirR[dir];
            Rc += RdirC[dir];

            int colSid = getGridValue(Rr, Rc);
            setGridValue(Rr, Rc, -1);

            // Collision
            if (colSid > 0) {
                collidSanta(C, dir, colSid, m);
            }

            // Move Santa
            for (int si = 1; si < santaLocations.length; si++) {
                Santa s = santaLocations[si];

                if (!s.alive || s.moveTurn > m) continue;

                int distance = (int) Math.pow(Rr - s.r, 2) + (int) Math.pow(Rc - s.c, 2);
                int dirS = 8;
                for (int i = 0; i < 8; i += 2) {
                    int nr = s.r + RdirR[i];
                    int nc = s.c + RdirC[i];

                    if (!isInGrid(nr, nc) || getGridValue(nr, nc) > 0) continue; // another santa

                    int dist = (int) Math.pow(Rr - nr, 2) + (int) Math.pow(Rc - nc, 2);
                    if (dist < distance) {
                        dirS = i;
                        distance = dist;
                    }
                }

                if (dirS > 7) continue;

                int nextSr = s.r + RdirR[dirS];
                int nextSc = s.c + RdirC[dirS];
                if (Rr == nextSr && Rc == nextSc) {
                    setGridValue(s.r, s.c, 0);
                    collidSanta(D, (dirS + 4) % 8, s.id, m); // jump to reverse direction
                } else {
                    setGridValue(s.r, s.c, 0);
                    setGridValue(nextSr, nextSc, s.id);

                    santaLocations[s.id].r = nextSr;
                    santaLocations[s.id].c = nextSc;
                }
            }

            if (retired >= P) {
                break;
            }

            // Give safe score
            for (int si = 1; si < santaLocations.length; si++) {
                Santa s = santaLocations[si];
                if (s.alive) {
                    scores[si] += 1;
                }
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 1; i < scores.length; i++) {
            sb.append(scores[i]);
            sb.append(" ");
        }
        System.out.println(sb.toString().trim());
    }

    public static void collidSanta(int w, int dir, int colSid, int turn) {
        // Get Score
        scores[colSid] += w;
        santaLocations[colSid].moveTurn = turn + 2;

        // Jump
        int Lr = Rr + w * RdirR[dir];
        int Lc = Rc + w * RdirC[dir];

        int tempSid = colSid;
        while (true) {
            if (isInGrid(Lr, Lc)) {
                if (getGridValue(Lr, Lc) > 0) {
                    tempSid = getGridValue(Lr, Lc);
                    setGridValue(Lr, Lc, colSid);
                    santaLocations[colSid].r = Lr;
                    santaLocations[colSid].c = Lc;
                    colSid = tempSid;
                } else {
                    setGridValue(Lr, Lc, colSid);
                    santaLocations[colSid].r = Lr;
                    santaLocations[colSid].c = Lc;
                    break;
                }
                Lr += RdirR[dir];
                Lc += RdirC[dir];
            } else {
                santaLocations[colSid].alive = false;
                retired += 1;
                break;
            }
        }
    }

    public static int getGridValue(int r, int c) {
        return grid.get(r).get(c);
    }

    public static int setGridValue(int r, int c, int v) {
        return grid.get(r).set(c, v);
    }

    public static int findShortestRDir() {
        int dist = 1000000000;
        Santa targetSanta = null;

        for (Santa s : santaLocations) {
            if (s == null || !s.alive) continue;

            int distance = (int) Math.pow(Rr - s.r, 2) + (int) Math.pow(Rc - s.c, 2);
            if (dist >= distance) {
                if (dist == distance) {
                    if (targetSanta.r <= s.r) {
                        if (targetSanta.r == s.r) {
                            if (targetSanta.c < s.c) {
                                targetSanta = s;
                            }
                            continue;
                        }
                        targetSanta = s;
                    }
                    continue;
                }

                dist = distance;
                targetSanta = s;
            }
        }

        int dr = targetSanta.r - Rr;
        int dc = targetSanta.c - Rc;

        if (dr == 0) {
            if (dc > 0) {
                return 2;
            } else {
                return 6;
            }
        } else if (dr > 0) {
            if (dc == 0) {
                return 4;
            } else if (dc > 0) {
                return 3;
            } else {
                return 5;
            }
        } else {
            if (dc == 0) {
                return 0;
            } else if (dc > 0) {
                return 1;
            } else {
                return 7;
            }
        }
    }

    public static boolean isInGrid(int r, int c) {
        return (r >= 1) && (r <= N) && (c >= 1) && (c <= N);
    }

    public static class Santa {
        int id;
        int r;
        int c;
        boolean alive;
        int moveTurn;

        public Santa(int id, int r, int c) {
            this.id = id;
            this.r = r;
            this.c = c;
            this.alive = true;
            this.moveTurn = 1;
        }
    }
}