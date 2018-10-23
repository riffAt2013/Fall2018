#include <bits/stdc++.h>
using namespace std;
vector<int> G[100];

int main ()
{
    int vertex, edge;
    cin >> vertex >> edge;

    for(int i = 0 ; i < edge; i++)
    {
        int x, y ;
        cin >> x >> y;
        G[x].push_back(y);
    }

    while(true)
    {
        cout<<"which vertex adjacents you wanna see?\n";
        int n;
        cin>>n;

        for (int i = 0; i<G[n].size(); i++)
        {
            cout<<G[n][i]<<" "<<'\n';
        }
    }
}
