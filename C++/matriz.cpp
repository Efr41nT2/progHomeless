// ingresar e imprimir matriz
#include<iostream>

using namespace std;

int main() {
    int matriz[4][4];
    int i, j, filas = 3, columnas = 3, val;
    for(i = 1; i <= filas; i++){
        for(j = 1; j <= columnas; j++){
            cout << "en la posición ["<<i<<"]""["<<j<<"]"<<endl;
            cout << "Ingrese valor: ";
            cin >> val;
            matriz[i][j] = val;
        }
    }
    cout << endl;
    cout << "la matriz queda asi" << endl;
    for(i = 1 ; i <= filas; i++){
        for(j = 1; j <= columnas; j++){
            cout << matriz[i][j];
        }
        cout << endl;
    }
    return 0; 
}
