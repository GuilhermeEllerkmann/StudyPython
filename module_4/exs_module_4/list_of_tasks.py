import os
import json

list_of_tasks = []
list_of_erased_tasks = []

def listar(list):
    if not list:
        return print('Nothing to list\n')
    
    for i in list:
        print(f'{i}\n')

def undo(lista1, lista2):
    if not lista1:
        return print('Nothing to undo\n')
    
    last_item = lista1.pop()
    lista2.append(last_item)
    
def redo(lista1, lista2):
    if not lista2:
        return print('Nothing to redo\n')
    
    newest_redo_item = lista2.pop()
    lista1.append(newest_redo_item)

def add(task, list_of_tasks):
    task = task.strip()
    if not task:
        return print('You did not type any tasks')
    
    list_of_tasks.append(task)
        
def finish(list):
    base_dir = os.path.dirname(__file__)
    save_to = os.path.join(base_dir, 'tasks.json')
    with open(save_to, 'w') as arquivo:
        json.dump(list, arquivo, indent=2)
    
    print('An archive with your tasks was created,')

while True:

    print('Commands: list, undo, redo, finish\n')
    user_choice = str(input('Type an task or an command:'))

    if user_choice.lower() == 'clear':
        os.system('clear')
    elif user_choice.lower() == 'list':
        listar(list_of_tasks)
    elif user_choice.lower() == 'undo':
      undo(list_of_tasks, list_of_erased_tasks)
    elif user_choice.lower() == 'redo':
       redo(list_of_tasks, list_of_erased_tasks)
    elif user_choice.lower() not in ('clear', 'list', 'undo', 'redo', 'finish'):
        add(user_choice, list_of_tasks)
    elif user_choice.lower() == 'finish':
        finish(list_of_tasks)
