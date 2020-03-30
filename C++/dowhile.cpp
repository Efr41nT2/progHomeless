#include <iostream>

using namespace std;

int main(){
    char resp;
    bool ban = false;
    do{
        cout << "Deseas continuar [Y/N]: ";
        cin >> resp;
        if(tolower(resp) == 'n'){
            ban = false;
        }else{
            if(tolower(resp) == 'y'){
                ban = true;
            }
        }
    }while(ban == false);
    return 0;
}
