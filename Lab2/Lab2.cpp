#include <iostream>
#include <cmath>
using namespace std;


int main() {

    int n;
    cout << "Please enter a positive integer greater than 1: ";
    cin >> n;

    int steps = 0;
    cout << n;

    while (n != 1) {

        if (n % 2 == 0)
            n = n / 2;
        else
            n = 3 * n + 1;

        cout << " -> " << n;
        steps++;
    }

    cout << endl << "Total steps: " << steps << endl << endl;



    cout << "Please enter a number between 10 and 100: ";
    cin >> n;

    while (n < 10 || n > 100) {
        cout << "Invalid input." << endl;
        cout << "Please enter a number between 10 and 100: ";
        cin >> n;
    }

    int fizz = 0;
    int buzz = 0;
    int fizzbuzz = 0;
    
    for (int i = 1; i <= n; i++) {

        if (i % 7 == 0) {
            cout << "(" << i << " is skipped)" << endl;
            continue;
        }

        if (i % 3 == 0 && i % 5 == 0) {
            cout << "FizzBuzz" << endl;
            fizzbuzz++;
        }
        else if (i % 3 == 0) {
            cout << "Fizz" << endl;
            fizz++;
        }
        else if (i % 5 == 0) {
            cout << "Buzz" << endl;
            buzz++;
        }
        else {
            cout << i << endl;
        }
    }

    cout << "--- Summary ---" << endl;
    cout << "Fizz count: " << fizz << endl;
    cout << "Buzz count: " << buzz << endl;
    cout << "FizzBuzz count: " << fizzbuzz << endl << endl;



    cout << "Please enter a number between 3 and 9: ";
    cin >> n;

    for (int i = 1; i < 2*n; i++) {

        int k = n - abs(n - i);

        for (int j = 0; j < k; j++) {
            cout << "*";
        }

        cout << endl;
    }

    return 0;
}
