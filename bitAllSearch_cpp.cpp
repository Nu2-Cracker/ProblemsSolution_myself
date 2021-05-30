#include <iostream>
#include <vector>
using namespace std;

//c++でbit全探索

int main(){
  int n=3;

  for (int bit=0; bit < (1<<n); ++bit){
    vector<int>S;
    for (int i=0;i < n; ++i){
      if(bit & (1<<i)){ //列挙にiが含まれるか
        S.push_back(i);
      }
    }
    cout << bit << ": {";
    for (int i=0; i<(int)S.size();++i){
      cout << S[i] << " ";
    }
    cout << "}" << endl;
  }

}