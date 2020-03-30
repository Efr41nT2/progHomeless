#include <iostream>

using namespace std;

int main() {
    int a;
    cout << "Ingrese número: ";
    cin >> a;

    if(a < 0){
        cout << "el número es negativo" << endl;
    }else{
        if(a == 0){
            cout << "el número es cero" << endl;
        }else{
            cout << "el número es positivo" << endl;
        }
    }
}
