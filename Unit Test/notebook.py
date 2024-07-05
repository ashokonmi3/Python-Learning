class Note:
    CATEGORY = 'General'  # Adding the class attribute

    def __init__(self, content):
        self.content = content


class Notebook:
    def __init__(self):
        self.notes = []

    def add_note(self, content):
        self.notes.append(content)

    def search_notes(self, keyword):
        return [note for note in self.notes if keyword.lower() in note.lower()]
