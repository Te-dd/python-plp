class books :
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        return f"{self.title} by {self.author}, published in {self.year}"
    
class storybooks(books):
    def __init__(self, title, author, year, genre):
        super().__init__(title, author, year)
        self.genre = genre

    def read_story(self):
        return f"Reading a {self.genre} story: {self.title} by {self.author}"
    
book1 = books("1984", "George Orwell", 1949)
storybook1 = storybooks("Harry Potter and the Sorcerer's Stone", "J.K. Rowling", 1997, "Fantasy")

print(book1.get_info())
read_story_output = storybook1.read_story()
print(read_story_output)