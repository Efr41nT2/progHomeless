#include <iostream>

using namespace std;

int main() {
    char resp;
    bool ban = false;
    while(ban == false){
        cout << "Deseas continuar[Y/N]: ";
        cin >> resp;
        if(resp == 'Y' || resp == 'y'){
            ban = false;
        }else{
            if(resp == 'N' || resp == 'n'){
                ban = true;
            }
        }
    }
    return 0;
}
