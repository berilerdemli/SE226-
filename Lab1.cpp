#include <iostream>
#include <string>
#include <cmath>

using namespace std;

int main() {

    string name;
    string studentID;

    cout<< "What is your name? ";
    cin>> name;

    cout<< "What is your student ID? ";
    cin>> studentID;

    cout<< "Hello " << name << " ("<< studentID <<")" << endl;



    int totalSeconds;

    cout<< "Enter total seconds: ";
    cin>> totalSeconds;

    int hours=totalSeconds / 3600;
    int minutes=(totalSeconds % 3600) / 60;
    int seconds=totalSeconds % 60;

    cout<< hours << " hours, "
        << minutes << " minutes, "
        << seconds << " seconds." << endl;


    
    double x1, y1, x2, y2;

    cout<< "Enter x1 and y1: ";
    cin>> x1 >> y1;

    cout<< "Enter x2 and y2: ";
    cin>> x2 >> y2;

    double distance=sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2));

    cout<<"Distance = " << distance << endl;


   
    cout<< "\n*******" << endl;
    cout<< " *****" << endl;
    cout<< "  ***" << endl;
    cout<< "   *" << endl;

    return 0;
}
