#include <iostream>
#include <queue>
#include <algorithm>

#define MAX 26
using namespace std;

string map[MAX];
queue<pair<int, int>> q;
vector<int> result;
int visited[MAX][MAX] = {0,};

int dx[] = {-1, 0, 1, 0};
int dy[] = {0, 1, 0, -1};

int main(void) {
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> map[i];
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (map[i][j] == '1' && visited[i][j] == 0) {
                int count = 0;
                q.push({i, j}); visited[i][j] = 1;

                while (!q.empty()) {
                    int x = q.front().first; int y = q.front().second;
                    q.pop(); count++;

                    for (int d = 0; d < 4; d++) {
                        int nx = x + dx[d]; int ny = y + dy[d];

                        if (0 <= nx && 0 <= ny && nx < n && ny < n && visited[nx][ny]==0 && map[nx][ny]=='1') {
                            q.push({nx, ny});
                            visited[nx][ny] = 1;
                        }
                    }
                }
                result.push_back(count);
            }
        }
    }
    sort(result.begin(), result.end());
    cout << result.size() << "\n";
    for (int i=0; i < result.size(); i++) {
        cout << result[i] << "\n";
    }
}