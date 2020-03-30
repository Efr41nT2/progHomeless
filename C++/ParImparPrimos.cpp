#include <iostream>

using namespace std;

int main(){
    int divisor = 1, divisores = 0, num = 0;
    cout << "Ingrese número: ";
    cin >> num;
    do{
        if(num % divisor == 0){
            divisores++;
        }
        divisor++;
    }while(divisor <= num);
    if(num % 2 == 0){
        cout << "el número " << num << " es par" << endl;
    }else{
        cout << "el número " << num << " es impar" << endl;
    }
    if(divisores == 2){
        cout << "el número " << num << " es primo" << endl;
    }else{
        cout << "el número " << num << " no es primo" << endl;
    }
    return 0;
}
