class Publication:
    def __init__(self, title: str, author: str):
        self._title = title
        self._author = author

   
    @property
    def title(self) -> str:
        return self._title

    @property
    def author(self) -> str:
        return self._author

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")


class Book(Publication):
    def __init__(self, title: str, author: str, pages: int):
        super().__init__(title, author)
        self.pages = pages  

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, value: int):
        if value <= 0:
            print(" The number of pages must be positive.")
            self._pages = 1 
        else:
            self._pages = value

    def display_info(self):
        super().display_info()
        print(f"Pages: {self.pages}")


class Magazine(Publication):
    def __init__(self, title: str, author: str, issue_number: int):
        super().__init__(title, author)
        self.issue_number = issue_number  

    @property
    def issue_number(self) -> int:
        return self._issue_number

    @issue_number.setter
    def issue_number(self, value: int):
        if value <= 0:
            print(" The issue number must be positive.")
            self._issue_number = 1 
        else:
            self._issue_number = value

    def display_info(self):
        super().display_info()
        print(f"Issue Number: {self.issue_number}")