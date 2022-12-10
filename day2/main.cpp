#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

string help(char c) {
    return c == 'A' ? "rock" : c == 'B' ? "paper" : "scissors";
}

string beats(string s) {
    return s == "rock" ? "paper" : s == "paper" ? "scissors" : "rock";
}

string loses(string s) {
    return s == "rock" ? "scissors" : s == "scissors" ? "paper" : "rock";
}

int points(string s) {
    return s == "rock" ? 1 : s == "paper" ? 2 : 3;
}

int type(char c) {
    return c == 'X' ? 0 : c == 'Y' ? 3 : 6;
}

int main() {
    freopen("main.in", "r", stdin);
    int ans = 0;
    for (int i = 0; i < 2500; ++i) {
        char opp, instruct;
        cin >> opp >> instruct;
        int score = 0;
        if (type(instruct) == 3) score += points(help(opp)) + 3;
        if (type(instruct) == 0) score += points(loses(help(opp))) + 0;
        if (type(instruct) == 6) score += points(beats(help(opp))) + 6;
        ans += score;
    }
    cout << ans << '\n';
    return 0;
}
