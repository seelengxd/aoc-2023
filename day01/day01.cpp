#include "/Users/seelengxd/stdc++.h"

int main()
{
    string s;
    int ans = 0;
    string digits[] = {"zero",
                       "one",
                       "two",
                       "three",
                       "four",
                       "five",
                       "six",
                       "seven",
                       "eight",
                       "nine"};
    while (cin >> s)
    {
        // Your loop body
        vector<int> v;
        string curr = "";
        for (char c : s)
        {
            if ('0' <= c && c <= '9')
            {
                v.push_back(c - '0');
                curr = "";
            }
            else
            {
                curr.push_back(c);
                for (int i = 0; i < 10; i++)
                {
                    string digit = digits[i];
                    if (curr.find(digit) != string::npos)
                    {
                        v.push_back(i);
                        if (!curr.empty())
                        {
                            curr = "";
                            curr.push_back(c);
                        }
                        break;
                    }
                }
            }
        }
        ans += v[0] * 10 + v[v.size() - 1];
    }
    cout << ans;
}