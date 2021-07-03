
// we learn about VARIABLEs
// we learn about DATA TYPES
// we learn about OPERATORS
//we learn about GETTING USER INPUT
// we learn about BUILDING CALCULATOR
// we learn about ARRAYS
// we learn about FUNCTIONS
// we learn about RETURN
// we learn about IF STATEMENTS
// we learn about COMPARISONS


// beginner tutorial


#include <iostream>
#include <cmath>

using namespace std;

int getMax(int num1, int num2){
    int result;

    if (num1 > num2){
        result = num1;
    }
    else{
        result = num2;
    }

    return result;

}


int main(){
/*     string CharacterName = "John";
    int CharacterAge;
    CharacterAge = 35;

    cout<<"The name is "<< CharacterName <<endl;
    cout<< "The age is "<< CharacterAge<<endl;
    cout<< "The guys name "<< CharacterName << " His age is " << CharacterAge <<endl; */

    /* char grade = 'A';
    string phrase = "Giraffe academy";
    int age = 23;
    float number = 23.8;
    double number2 = 23.9999;// better than float
    bool isMAle = true;//small letters */

/*     cout <<"Giraffer academy\n";
    string pharse ="Giraffe academy";

    cout<< pharse.length();
    cout<< pharse[0];
    cout<<pharse[1];
    pharse[0] = 'B';
    cout<<pharse.find("ff")<<endl;
    cout<<pharse.substr(8, 3)<<endl; // from index 8, and find 3 characters

 */


/*     cout<<(345-78)+788*67<<endl;
    int wnum = 6;
    double dnum = 89.99;

    cout<<pow(2, 6)<<endl;
    cout<<sqrt(34.9)<<endl;
    cout<<round(3.4)<<endl;
    cout<<ceil(23.8)<<endl;
    cout<<floor(23.8)<<endl;
    cout<<fmax(3,19)<<endl;
    cout<<fmin(3,19)<<endl;
 */
/*     string name;
    cout<< "enter your name :" ;
    getline(cin, name);

    cout<<"your name is :"<< name << endl; */

/* 
    int num1, num2;

    cout<<"please enter a number: "<<endl;
    cin>>num1;

    cout<<"please enter the second number: "<<endl;
    cin>>num2;

    cout<<num1+num2<<endl;

 */

/*     string color, pluralNoun, celebrity;

    cout<< "enter a color :";
    getline(cin, color);
    cout<< "enter a noun :";
    getline(cin, pluralNoun);
    cout<< "enter a celebrity :";
    getline(cin, celebrity);

    cout<< "roses are "<<color<<endl;
    cout<<pluralNoun<< "are purple"<<endl;
    cout<< "i love "<<celebrity<<endl;


 */
/*     int luckyNumber[10];
    luckyNumber[0] = 7;

    cout<<luckyNumber[0];



 */

/* 
    bool isMale = false;
    bool isTall = true;

    if (isMale && isTall){
        cout<< "You are tall male"; 
    }
    else if(isMale && !isTall)
    {
        cout<<"your not a tall male";
    }
    else if(!isMale && isTall){
        cout<<" you are tall female";
    }
    else{
        cout<<"you are not male and not tall";
    } */






    cout<< getMax(2,5);
    return 0;

}


