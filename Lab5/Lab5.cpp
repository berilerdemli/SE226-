#include <iostream>
using namespace std;

double alternatingSum(int n) {
    if (n == 1)
        return 1;

    if (n % 2 == 0)
        return alternatingSum(n - 1) - (1.0 / n);
    else
        return alternatingSum(n - 1) + (1.0 / n);
}

int main() {
    int n;
    cout << "n gir: ";
    cin >> n;

    cout << "Sonuc: " << alternatingSum(n) << endl;

    return 0;
}
