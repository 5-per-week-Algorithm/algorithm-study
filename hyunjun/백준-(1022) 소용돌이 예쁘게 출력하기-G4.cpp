#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

int getNum(int, int);

int result[100][100];

int main(void) {
    int r1, c1, r2, c2;
    cin >> r1 >> c1 >> r2 >> c2;

    int maxNum = -1;

    for (int r = r1; r <= r2; ++r) {
        for (int c = c1; c <= c2; ++c) {
            int num = getNum(r, c);
            result[r - r1][c - c1] = num;

            if (num > maxNum) {
                maxNum = num;
            }
        }
    }

    int len = log10(maxNum) + 1;

    for (int r = r1; r <= r2; ++r) {
        for (int c = c1; c <= c2; ++c) {
            cout << setw(len) << result[r - r1][c - c1] << ' ';
        }
        
        cout << '\n';
    }
}

int getNum(int r, int c) {
    int roundIdx = max(abs(r), abs(c));
    int countInLine = (roundIdx * 2) + 1;
    int last = countInLine * countInLine;
    int first = (1 + 2 * (roundIdx - 1)) * (1 + 2 * (roundIdx - 1)) + 1;

    if (r == 0 && c == 0) {
        return 1;
    }
    
    if (r == roundIdx) {
        int lf = first + 3 * (countInLine - 2) - 1 - (roundIdx - 1) * 2;
        return lf + (countInLine + c + roundIdx);
    } else if (c == -roundIdx) {
        int lf = first + 2 * (countInLine - 2) - 2 - (roundIdx - 1) * 2;
        return lf + (countInLine + r + roundIdx);
    } else if (r == -roundIdx) {
        int lf = first + countInLine - 2 - 1;
        return lf + (countInLine - c - roundIdx);
    } else {
        return first + (roundIdx - 1 - r);
    }
}