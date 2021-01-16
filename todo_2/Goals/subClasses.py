# sub class
class Task_data:

    def __init__(self, title, complete, created, priority):
        self.title = title
        self.complete = complete
        self.created = created
        self.priority = priority

    def __eq__(self, other):
        title = other.title
        complete = other.complete
        created = other.created
        return Task_data(title, complete, created)
    
    def __lt__(self, other):
        return self.title.upper() < other.title.upper()
    def __le__(self, other):
        return self.title.upper() <= other.title.upper()