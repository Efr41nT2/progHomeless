// llenar e imprimir un array
#include <iostream>
using namespace std;

int lista[10];
int n, result=0;

int main() {
    for ( n=1 ; n<11 ; ++n ){
        lista[n] = n;
        cout << lista[n] << endl;
    }
    return 0;
}
