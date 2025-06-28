package dev._60jong.backtracking.programmers.kakao_select_dice;

import java.util.*;


public class Solution {
    private static List<List<Integer>> combinations = new ArrayList<>();

    private static int n;
    private static int hn;

    private static int[][] records;
    private static int[][] dices;

    private static int maxWins = 0;
    private static int maxCombIdx = 0;

    public int[] solution(int[][] dice) {
        dices = dice;
        n = dice.length;
        hn = n / 2;

        // combination
        for (int i = 0; i <= hn; i++) {
            List<Integer> comb = new ArrayList<>();
            comb.add(i);

            getCombinations(comb, hn - 1);
        }
        records = new int[combinations.size()][501];

        // calculate sums
        for (int j = 0; j < combinations.size(); j++) {
            calculateSum(j, hn, 0);
        }

        // count wins - two pointers
        for (int k = 0; k < combinations.size() / 2; k++) {
            int[] r1 = records[k];
            int[] r2 = records[combinations.size() - 1 - k];

            // 1 -> 2
            int p1 = 0;
            int p2 = 0;

            int wins = 0;
            int temp = 0;
            while (p1 < 501) {

                while (r1[p1] <= 0) {
                    if (p1 >= 500) {
                        break;
                    }
                    p1++;
                }

                while (p2 < p1) {
                    temp += r2[p2];
                    p2++;
                }

                wins += r1[p1] * temp;
                p1++;

                if (p1 >= 500) {
                    break;
                }
            }

            if (wins > maxWins) {
                maxWins = wins;
                maxCombIdx = k;
            }

            // 2 -> 1
            p1 = 0;
            p2 = 0;
            wins = 0;
            temp = 0;

            while (p2 < 501) {
                while (r2[p2] <= 0) {
                    if (p2 >= 500) {
                        break;
                    }
                    p2++;
                }

                while (p1 < p2) {
                    temp += r1[p1];
                    p1++;
                }

                wins += r2[p2] * temp;
                p2++;

                if (p2 >= 500) {
                    break;
                }
            }
            if (wins > maxWins) {
                maxWins = wins;
                maxCombIdx = combinations.size() - 1 - k;
            }
        }


        int[] answer = new int[hn];
        for (int i = 0; i < hn; i++) {
            answer[i] = combinations.get(maxCombIdx).get(i) + 1;
        }

        return answer;
    }

    public void getCombinations(List<Integer> comb, int count) {
        // base condition
        if (count == 0) {
            combinations.add(List.copyOf(comb));
            return;
        }

        int lastNum = comb.get(comb.size() - 1);
        for (int i = lastNum + 1; i <= n - count; i++) {
            comb.add(i);

            getCombinations(comb, count - 1);

            comb.remove(comb.size() - 1);
        }
    }

    public void calculateSum(int recordIdx, int count, int sum) {
        if (count == 0) {
            records[recordIdx][sum] += 1;
            return;
        }

        int idx = hn - count; // 조합 내부 인덱스 - 주사위 번호

        for (int di : dices[combinations.get(recordIdx).get(idx)]) {
            calculateSum(recordIdx, count - 1, sum + di);
        }
    }
}