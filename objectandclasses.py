class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = str(name)
        self.age = int(age)
        self.tracks = list(tracks)
        self.score = float(score)

    def change_name(self, add_name):
        self.add_name = add_name
        print('My name is',add_name)

    def change_age(self, add_age):
        self.add_age = add_age
        print('My age is', add_age)

    def add_tracks(self, add_tracks):
        self.add_tracks = add_tracks
        self.tracks.append(track)

    def get_score(self):
        print(self.score)


Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_tracks("UI/UX")
print(Bob.get_score())
print(Bob.tracks)
