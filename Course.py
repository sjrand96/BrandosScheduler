class Course:
    """ Course class representing a individual course, will split later into course_instance and general course """

    def __init__(self, name, pk=0, max_size = 10000):
        """ Create a new point at the origin """
        self.pk = pk  # primary key
        self.name = name
        self.time_slot = None
        self.max_size = max_size
        self.assigned_students = []

    def assign_student(self, student):  # currently unused
        self.assigned_students.append(student)

    def display(self):
        print(self.name + " | Track " + str(self.time_slot))