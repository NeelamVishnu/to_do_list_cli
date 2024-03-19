class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({'task': task, 'completed': False})
        print(f'Task "{task}" added.')

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            deleted_task = self.tasks.pop(index)
            print(f'Task "{deleted_task["task"]}" deleted.')
        else:
            print('Invalid task index.')

    def mark_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]['completed'] = True
            print(f'Task "{self.tasks[index]["task"]}" marked as completed.')
        else:
            print('Invalid task index.')

    def display_tasks(self):
        print('Todo List:')
        for index, task in enumerate(self.tasks):
            status = '✔' if task['completed'] else '❌'
            print(f'{index + 1}. [{status}] {task["task"]}')


def main():
    todo_list = TodoList()

    while True:
        print('\nMenu:')
        print('1. Add Task')
        print('2. Delete Task')
        print('3. Mark Task as Completed')
        print('4. Display Tasks')
        print('5. Exit')

        choice = input('Enter your choice: ')

        if choice == '1':
            task = input('Enter task: ')
            todo_list.add_task(task)
        elif choice == '2':
            index = int(input('Enter index of task to delete: ')) - 1
            todo_list.delete_task(index)
        elif choice == '3':
            index = int(input('Enter index of task to mark as completed: ')) - 1
            todo_list.mark_completed(index)
        elif choice == '4':
            todo_list.display_tasks()
        elif choice == '5':
            print('Exiting...')
            break
        else:
            print('Invalid choice. Please try again.')


if __name__ == "__main__":
    main()
