/*  
Author: Syed Faysel Ahammad Rajo
handle: syedrajo20
*/

#include<bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    queue<int> q;

    q.push(23);
    q.push(10);
    q.front();
    cout<<q.front()<<endl;
    cout<<q.back()<<endl;
    q.pop();
    cout<<q.front()<<endl;
    return 0;
}