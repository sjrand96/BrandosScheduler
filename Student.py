class Student:
    """ Student class representing a individual student """

    def __init__(self, id, class_list, name="john doe"):
        self.id = id
        self.class_list = class_list
        self.name = name

    def display(self, consise=False):
        print("---------------")

        slots = [s.time_slot for s in self.class_list]
        unique = len(set(slots))
        total = len(slots)
        print(self.name + " got %d out of %d desired" % (unique, total))

        if not consise:
                print("Wants to take following classes:")
                for c in self.class_list:
                    c.display()
