class EBook:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = 1
        self.is_open = False

    def open_book(self):
        self.is_open = True

    def close_book(self):
        self.is_open = False

    def next_page(self):
        if self.is_open:
            if self.current_page < self.pages:
                self.current_page += 1
            else:
                print("You are already on the last page.")
        else:
            print("The book is closed. Open it to read.")

    def previous_page(self):
        if self.is_open:
            if self.current_page > 1:
                self.current_page -= 1
            else:
                print("You are on the first page.")
        else:
            print("The book is closed. Open it to read.")

    def display_status(self):
        status = "Open" if self.is_open else "Closed"
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Total Pages: {self.pages}")
        print(f"Current Page: {self.current_page}")
        print(f"Status: {status}")
        print("-" * 20)