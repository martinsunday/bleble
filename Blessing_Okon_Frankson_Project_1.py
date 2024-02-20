# an empty list that will contain our tasks.
tasks = []


# this function adds a new task to our empty tasks list which we defined above
# it accepts a task info as its argument and creates a dictionary
# containing a task's id, info and completion status
# each task's id is the total number of tasks we previously had + 1.
def add_task(task_info):
    task_id = len(tasks) + 1
    task = {'id': task_id, 'info': task_info, 'status': 'uncompleted'}
    tasks.append(task)
    print('Task added successfully !')


# this function changes the status of a task to completed
# it accepts a task_id as its argument
# because we start counting index from 0
# we have to subtract 1 from the task_id to get its index
# in the tasks list
# because we define each task as a dictionary when we added it in the add_task function
# we can sets its status to completed
# we also use error handling using try and except in case the task index doesnot exist in our task lists
# we can print an error message and prevent our app from crashing
def complete_task(task_id):
    try:
        index = task_id - 1
        tasks[index]['status'] = 'completed'
        print('Task completed successfully !')
    except IndexError:
        print('Invalid task index !')

# this function removes a task from our tasks list
# it accepts a task_id as its argument
# because we start counting index from 0
# we have to subtract 1 from the task id to get its index
# in the tasks list
# we also use error handling using try and except in case the task index doesnot exist in our task lists
# we can print an error message and prevent our app from crashing.


def remove_task(task_id):
    try:
        index = task_id - 1
        tasks.pop(index)
        print('Task removed successfully !')
    except IndexError:
        print('Invalid task index !')

# this function prints all our tasks


def view_tasks():
    if len(tasks) > 0:
        print('All tasks:')

        for task in tasks:
            print('#{} {} ({})'.format(
                task['id'], task['info'], task['status']))
    else:
        print('No tasks yet !')


# our main app begins, here we will use all the fucctions we defined above
# because we use an infinite while loop, our app will remain running
# until we decide to exit.
print('Welcome to my todo list manager app !')

while True:
    print('Enter any of the options to proceed:')
    print('1. Add Task')
    print('2. Complete Task')
    print('3. Remove Task')
    print('4. View Tasks')
    print('5. Exit Application')

    choice = input()

    if choice == '1':
        task_info = input('Enter Task Info: ')
        add_task(task_info)
    elif choice == '2':
        task_id = int(input('Enter the id of the task to complete: '))
        complete_task(task_id)
    elif choice == '3':
        task_id = int(input('Enter the id of the task to remove: '))
        remove_task(task_id)
    elif choice == '4':
        view_tasks()
    elif choice == '5':
        print('Exited successfully !')
        break
    else:
        print('Invalid option selected !')
