#include <iostream>
using namespace std;


void swapValues(int* p1, int* p2) {
    int temp = *p1;
    *p1 = *p2;
    *p2 = temp;
}



void printArray(int* arr, int size) {
    for (int i = 0; i < size; i++) {
        cout << *(arr + i) << " ";
    }
    cout << endl;
}



int findSum(int* arr, int size) {
    int sum = 0;
    for (int i = 0; i < size; i++) {
        sum += *(arr + i);
    }
    return sum;
}



void shiftRight(int* arr, int size) {
    int last = *(arr + size - 1);

    for (int i = size - 1; i > 0; i--) {
        *(arr + i) = *(arr + i - 1);
    }

    *arr = last;
}



int* createArray(int size) {
    int* arr = new int[size];
    return arr;
}



void deleteArray(int* arr) {
    delete[] arr;
}

int main() {

    int size = 5;

    int* arr = createArray(size);

    cout << "Enter 5 numbers: ";
    for (int i = 0; i < size; i++) {
        cin >> *(arr + i);
    }

    cout << "Array: ";
    printArray(arr, size);

    
    cout << "Sum: " << findSum(arr, size) << endl;


    shiftRight(arr, size);
    cout << "After shifting right: ";
    printArray(arr, size);

    
    swapValues(arr, arr + 1);
    cout << "After swapping first two: ";
    printArray(arr, size);

  
    deleteArray(arr);

    return 0;
}
