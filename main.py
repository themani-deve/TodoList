import sqlite3
import os

todo_list = []
choice = ''


def show_operation():
    print('1.Add Tasks')
    print('2.Show Tasks')


def main():
    while True:
        show_operation()
        choice = input('Chose a Task: ')

        if int(choice) == 1:
            add_task()
        elif int(choice) == 2:
            show_tasks()


def add_task():
    title = input('Enter a Title For Task: ')
    description = input('Enter a Description For Task: ')
    status = False

    confirm = input('Accept This Task(Yes / No): ')
    lower_confirm = confirm.lower()

    if lower_confirm == 'yes':
        todo_list.append(
            {'title': title, 'description': description, 'status': status, }
        )

        with sqlite3.connect('sqlite3.db') as connection:
            cursor = connection.cursor()
            insert_query = 'INSERT INTO todolist (title, description) values (?, ?)'
            data = (todo_list[0]['title'], todo_list[0]['description'])
            cursor.execute(insert_query, data)

        todo_list.clear()

        print('Task Added To Todo List!')
        print('------------------------')
    elif lower_confirm == 'no':
        print('Task Not Add Into Todo List.')
        print('------------------------')


def show_tasks():
    with sqlite3.connect('sqlite3.db') as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM todolist')
        tasks = cursor.fetchall()

    print('-------------------------------')
    print('Your Tasks:')
    print('-------------------------------')
    for task in tasks:
        print(f'Task id: {task[0]}')
        print(f'Task Title: {task[1]}')
        print(f'Task Description: {task[2]}')
        if task[3] == 0:
            print('Task Status: Not Completed!')
        else:
            print('Task Status: Completed!')
        print('-------------------------------')


main()
