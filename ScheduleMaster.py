from Course import Course
from Student import Student
from Schedule import Schedule
import random
import copy


def main():

    # assign random names to courses and students
    with open('/home/spencer/PycharmProjects/BrandosScheduler/course_names.txt') as c_names:
        all_class_names = [line.strip() for line in c_names]
    with open('/home/spencer/PycharmProjects/BrandosScheduler/student_names.txt') as s_names:
        all_student_names = [line.strip() for line in s_names]

    courses = []
    num_courses = 80
    class_names = random.sample(all_class_names,num_courses)
    for i in range(num_courses): courses.append(Course(class_names[i], pk=i))

    students = []
    num_students = 400
    student_names = random.sample(all_student_names, num_students)
    for i in range(num_students):
        name = student_names[i]
        cList = random.sample(courses,8)
        students.append(Student(i,cList,name))

    # make an initial schedule with random tracks
    starter = Schedule(students=students, courses=courses,num_slots=8)
    starter.random_start()
    starter.get_fitness()

    # make initial parent the starter schedule
    parent = starter

    # loop for this many random change attempts
    for i in range(1000):

        # make the child a copy of the parent, randomly change one of it's class times
        child = copy.deepcopy(parent)
        child.rand_mutate()

        # if the score improvees as a result of this, update the parent and generation
        if child.get_fitness() > parent.get_fitness():
            parent = copy.deepcopy(child)
            parent.best_fitness = parent.get_fitness()
            parent.generation+=1
            parent.display()

    parent.display_final()


if __name__ == '__main__':
    main()