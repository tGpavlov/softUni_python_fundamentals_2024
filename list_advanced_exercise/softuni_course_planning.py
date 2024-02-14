def add(lesson_title):
    if lesson_title not in schedule_of_lessons:
        schedule_of_lessons.append(lesson_title)


def insert(lesson_title, index_of_element):
    if lesson_title not in schedule_of_lessons:
        schedule_of_lessons.insert(index_of_element, lesson_title)


def remove(lesson_title):
    if lesson_title in schedule_of_lessons:
        schedule_of_lessons.remove(lesson_title)
        if lesson_title + '-Exercise' in schedule_of_lessons:
            schedule_of_lessons.remove(lesson_title + '-Exercise')


def swap(index_of_element_1, index_of_element_2):
    schedule_of_lessons[index_of_element_1], schedule_of_lessons[index_of_element_2] \
        = schedule_of_lessons[index_of_element_2], schedule_of_lessons[index_of_element_1]


def remove_and_add_exercise(lesson_exercise, insert_index):
    schedule_of_lessons.remove(lesson_exercise)
    schedule_of_lessons.insert(insert_index, lesson_exercise)


def exercise(lesson_title):
    if lesson_title in schedule_of_lessons and lesson_title + '-Exercise' not in schedule_of_lessons:
        index_of_element = schedule_of_lessons.index(lesson_title)
        schedule_of_lessons.insert(index_of_element + 1, f'{lesson_title}-Exercise')
    elif lesson_title not in schedule_of_lessons and lesson_title + '-Exercise' not in schedule_of_lessons:
        schedule_of_lessons.append(lesson_title)
        schedule_of_lessons.append(f'{lesson_title}-Exercise')


schedule_of_lessons = input().split(', ')
command = input()

while not command == 'course start':
    command = command.split(':')

    if command[0] == 'Add':
        add(command[1])
    elif command[0] == 'Insert':
        insert(command[1], int(command[2]))
    elif command[0] == 'Remove':
        remove(command[1])
    elif command[0] == 'Swap':
        lesson_1 = command[1]
        lesson_2 = command[2]
        if lesson_1 in schedule_of_lessons and lesson_2 in schedule_of_lessons:
            lesson_index_1 = schedule_of_lessons.index(command[1])
            lesson_index_2 = schedule_of_lessons.index(command[2])
            exercise_1 = command[1] + '-Exercise'
            exercise_2 = command[2] + '-Exercise'
            if exercise_1 in schedule_of_lessons and exercise_2 in schedule_of_lessons:
                swap(lesson_index_1, lesson_index_2)
                remove_and_add_exercise(exercise_1, lesson_index_2 + 1)
                remove_and_add_exercise(exercise_2, lesson_index_1 + 1)
            elif exercise_1 in schedule_of_lessons and lesson_2 in schedule_of_lessons:
                swap(lesson_index_1, lesson_index_2)
                remove_and_add_exercise(exercise_1, lesson_index_2 + 1)
            elif exercise_2 in schedule_of_lessons and lesson_1 in schedule_of_lessons:
                swap(lesson_index_1, lesson_index_2)
                remove_and_add_exercise(exercise_2, lesson_index_1 + 1)
            else:
                swap(lesson_index_1, lesson_index_2)
    elif command[0] == 'Exercise':
        exercise(command[1])

    command = input()

for index, element in enumerate(schedule_of_lessons):
    print(f'{index + 1}.{element}')
