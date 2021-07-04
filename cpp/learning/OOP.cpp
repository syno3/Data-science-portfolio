// We learn about CONSTRUCT FUNCTIONS
// we learn about OBJECT FUNCTIONS
// we learn about GETTERS AND SETTERS

# include <iostream>

using namespace std;

class Book{
    public: 
        string title;
        string author;
        int pages;

        Book(string aTitle, string aAuthor, int aPages){
            title = aTitle;
            author = aAuthor;
            pages = aPages;
        }

        bool hasMany(){
            if (pages > 30){
                return true;
            }else{
                return false;
            }

        }

};

int main (){
    Book book1("Lord of the rings", "JKrwolings", 67);

    cout<< book1.hasMany();

    return 0;
}
