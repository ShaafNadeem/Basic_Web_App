while True:
    user_action = input('Type add, show, edit, complete or exit:')
    user_action = user_action.strip()
    match user_action:
        case 'add':
            todo = input('Enter a todo:')+'\n'
            with open ('../code_files/text.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            with open ('../code_files/text.txt', 'w') as file:
                todos = file.writelines(todos)
        case 'show':
            with open ('../code_files/text.txt', 'r') as file:
                todos = file.readlines()
            for index,item in enumerate(todos):
                item = item.strip('\n')
                row = f'{index+1}-{item}'
                print(row)
        case 'edit':
            number = int(input('Number of the todo to ed0it:0'))
            index = number -1
            with open ('../code_files/text.txt', 'r') as file:
                todos = file.readlines()
            
            new_todo = input('Enter new todo:')
            todos[index] = new_todo + '\n'
            
            with open ('../code_files/text.txt', 'w') as file:
                todos = file.writelines(todos)
        case 'complete':
            number = int(input('Number of the todo to complete:'))
            index = number -1

            with open ('../code_files/text.txt', 'r') as file:
                todos = file.readlines()
            
            todo_to_remove = todos[index].strip('\n') 
            todos.pop(index)

            with open ('../code_files/text.txt', 'w') as file:
                todos = file.writelines(todos)

            message = f'{todo_to_remove} is removed from your list.'
            print(message)
        case 'exit':
            break
print('Bye!')