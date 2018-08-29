from Course import Course
from Student import Student
import random
import copy


class Schedule:
    """ A potential order of classes """

    def __init__(self, students=[], courses=[], num_slots=3):
        self.students = students
        self.courses = courses
        self.num_slots = num_slots
        self.best_fitness = 0
        self.generation = 0

    def random_start(self):
        """Assign random slots to each course in the list"""

        # assign random slots
        for c in self.courses:
            c.time_slot = random.randint(0,self.num_slots-1)

        # print initial fitness
        self.best_fitness = self.get_fitness()
        self.display()

    def get_fitness(self):
        fitness = 0

        # for each student
        for s in self.students:
            occupied_slots = []
            # add points to fitness for classes they want that do not overlap
            for c in s.class_list:
                if c.time_slot not in occupied_slots:
                    # note that i did this score not using number of unique values to allow for use of occupied slots
                    # in student class when we later want people to be able to block of times
                    fitness += 1
                    occupied_slots.append(c.time_slot)
        return fitness

    def rand_mutate(self):
        # print("before: ")
        # for c in self.courses: c.display()
        # self.display()

        # randomly select one course and randomly change it's time
        course_to_change = self.courses[random.randint(0,self.num_slots-1)]
        new_val = random.randint(0,self.num_slots-1)
        course_to_change.time_slot = new_val

        #print("Charged " + course_to_change.name + " to slot " + str(new_val))
        # print("after:")
        # for c in self.courses: c.display()
        # self.display()

    def display(self):
        print("Generation %d | Score %d" % (self.generation, self.get_fitness()))

    def display_final(self):
        # print("Name  =  Time Slot")
        # for c in self.courses:
        #     print(c.name + "  =  " + str(c.time_slot))
        for s in self.students:
            s.display(consise=True)
