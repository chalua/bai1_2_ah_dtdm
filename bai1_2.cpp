#include <iostream>
#include <math.h>
using namespace std;
bool soChinhPhuong(int n){
    if((int)sqrt(n)*(int)sqrt(n)==n)return true;
    else return false;
}
void demSoChinhPhuong(int n){
    int dem = 0;
    for(int i = 1;i<=n;i++){
        if(soChinhPhuong(i)==true){
            dem++;
        }
    }
    cout << "co " << dem << " so chinh phuong: ";
}
int main(void){
    // Your code here!
    //bài 1
    // for(int i =10;i<=100;i++){
    //     if(i%7==0){
    //         cout << i << " ";
    //     }   
    // }
    //bài 2
    int n;
    cout << "nhập số nguyên n: ";
    cin >> n;
    cout << n <<"\n";
    demSoChinhPhuong(n);
    cout << "\n";
    for(int i = 1;i<=n;i++){
        if(soChinhPhuong(i)==true){
            cout << i << " ";
        }
    }
}
