
//https://www.hackerrank.com/challenges/staircase/problem
#include <bits/stdc++.h>
using namespace std;

void printStar (int n)
{
    for (int i=0; i<n; i++)
        cout<<'#';
}

void putWhitespace (int n)
{
  for (int i= 0; i<n; i++)
    cout<<' ';
}

int main()
{
    int n; cin>>n;

    for (int i = 1; i<=n; i++)
       {
          putWhitespace (n-i);
          printStar (i);
          cout<<'\n';
       }
}       

