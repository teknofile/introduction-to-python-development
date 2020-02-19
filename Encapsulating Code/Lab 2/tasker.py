def print_todo(todo):
    """
    print_todo takes in a todo dictionary and prints it out
    with by separating the `name` from the `body` using a colon (:).

    >>> todo = {'name': 'Example 1', 'body': 'This is a test task', 'points': '3'}
    >>> print_todo(todo)
    Example 1: This is a test task
    >>>
    """
    print(f"{todo['name']}: {todo['body']}")

def take_first(todos):
    """
    take_first receives a list of todos and removes the first todo
    and returns that todo and the remaining todos in a touple

    >>> todos = [{'name': 'Example 1', 'body': 'This is a test task', 'points': '3'},
    ... {'name': 'Task 2', 'body': 'Yet another example task', 'points': '2'}]
    >>> todo, todos = take_first(todos)
    >>> todo
    {'name': 'Example 1', 'body': 'This is a test task', 'points': '3'}
    >>> todos
    [{'name': 'Task 2', 'body': 'Yet another example task', 'points': '2'}]
    >>> todos = []
    >>> take_first(todos)
    (None, [])
    """
    if todos:
        todo = todos.pop(0)
        return (todo, todos)
    else:
        return (None, todos)

def sum_points(todos):
    """
    sum_points receives two todo dictionaries and returns sum of their `point` values.

    >>> todos = [{'name': 'Example 1', 'body': 'This is a test task', 'points': '3'},
    ... {'name': 'Task 2', 'body': 'Yet another example task', 'points': '2'},
    ... {'name': 'Task 3', 'body': 'Third task', 'points': '5'}]
    >>> sum_points(todos)
    10
    """
    total_points = 0
    for theTodo in todos:
        total_points += int(theTodo['points'])

    return total_points
