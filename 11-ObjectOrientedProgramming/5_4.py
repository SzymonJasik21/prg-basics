from ebook import EBook

my_ebook = EBook("Pan Tadeusz", "Adam Mickiewicz", 400)

my_ebook.open_book()

my_ebook.display_status()

my_ebook.next_page()
my_ebook.next_page()
my_ebook.next_page()

my_ebook.display_status()

my_ebook.close_book()

my_ebook.next_page()