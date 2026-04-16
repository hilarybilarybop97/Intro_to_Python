class Todo:
    IS_DONE = 'X'
    IS_UNDONE = ' '

    def __init__(self, task, status=False):
        self._task = task
        self._done = status

    @property
    def task(self):
        return self._task

    @property
    def done(self):
        return self._done

    @done.setter
    def done(self, status):
        self._done = status

    def __str__(self):
        marker = Todo.IS_DONE if self.done else Todo.IS_UNDONE

        return f"[{marker}] {self.task}"

    def __repr__(self):
        return f"Todo('{self.task}', '{self.done}')"

    def __eq__(self, other):
        if not isinstance(other, Todo):
            return NotImplemented

        return self.task == other.task and self.done == other.done

# def test_todo():
#     todo1 = Todo('Buy milk')
#     todo2 = Todo('Clean room')
#     todo3 = Todo('Go to gym')
#     todo4 = Todo('Clean room')

#     print(todo1)                  # [ ] Buy milk
#     print(todo2)                  # [ ] Clean room
#     print(todo3)                  # [ ] Go to gym
#     print(todo4)                  # [ ] Clean room

#     print(todo2 == todo4)         # True
#     print(todo1 == todo2)         # False
#     print(todo4.done)             # False

#     todo1.done = True
#     todo4.done = True
#     print(todo4.done)             # True

#     print(todo1)                  # [X] Buy milk
#     print(todo2)                  # [ ] Clean room
#     print(todo3)                  # [ ] Go to gym
#     print(todo4)                  # [X] Clean room

#     print(todo2 == todo4)         # False

#     todo4.done = False
#     print(todo4.done)             # False
#     print(todo4)                  # [ ] Clean room

# test_todo()

class TodoList:
    def __init__(self, title):
        self._title = title
        self._todos = []

    @property
    def title(self):
        return self._title

    def add(self, task):
        if not isinstance(task, Todo):
            raise TypeError('Only Todo objects can be added to a TodoList')

        self._todos.append(task)

    def __str__(self):
        if not self._todos:
            return "Nothing to do today!"

        output_lines = [f"---- {self.title} -----"]
        for task in self._todos:
            output_lines.append(f"{task}")
        return "\n".join(output_lines)

    def __len__(self):
        return len(self._todos)

    def first(self):
        if not self._todos:
            raise IndexError('TodoList is empty')

        return self._todos[0]

    def last(self):
        if not self._todos:
            raise IndexError('TodoList is empty')

        return self._todos[-1]

    def to_list(self):
        return self._todos[::]

    def todo_at(self, index):
        if self._todos.find(index) == -1:
            raise IndexError('Index does not exist')

        return self._todos[index]

empty_todo_list = TodoList('Nothing Doing')

def setup():
    todo1 = Todo('Buy milk')
    todo2 = Todo('Clean room')
    todo3 = Todo('Go to gym')

    todo2.done = True

    todo_list = TodoList("Today's Todos")
    todo_list.add(todo1)
    todo_list.add(todo2)
    todo_list.add(todo3)

    return todo_list

def step_1():
    print('--------------------------------- Step 1')
    todo_list = setup()

    # setup() uses `todo_list.add` to add 3 todos

    try:
        todo_list.add(1)
    except TypeError:
        print('TypeError detected')    # TypeError detected

    for todo in todo_list._todos:
        print(todo)

step_1()

def step_2():
    print('--------------------------------- Step 2')
    todo_list = setup()

    print(todo_list)
    # ---- Today's Todos -----
    # [ ] Buy milk
    # [X] Clean room
    # [ ] Go to gym

step_2()

def step_3():
    print('--------------------------------- Step 3')
    todo_list = setup()

    print(len(todo_list))              # 3
    print(len(empty_todo_list))        # 0

step_3()

def step_4():
    print('--------------------------------- Step 4')
    todo_list = setup()

    print(todo_list.first())           # [ ] Buy milk
    print(todo_list.last())            # [ ] Go to gym

    try:
        empty_todo_list.first()
    except IndexError:
        print('Expected IndexError: Got it!')

    try:
        empty_todo_list.last()
    except IndexError:
        print('Expected IndexError: Got it!')

step_4()

def step_5():
    print('--------------------------------- Step 5')
    todo_list = setup()

    print(empty_todo_list.to_list())    # []

    todos = todo_list.to_list()
    print(type(todos).__name__)         # list

    for todo in todos:
        print(todo)                     # [ ] Buy milk
                                        # [X] Clean room
                                        # [ ] Go to gym

step_5()

def step_6():
    print('--------------------------------- Step 6')
    todo_list = setup()

    print(todo_list.todo_at(0))        # [ ] Buy milk
    print(todo_list.todo_at(1))        # [X] Clean room
    print(todo_list.todo_at(2))        # [ ] Go to gym

    try:
        todo_list.todo_at(3)
    except IndexError:
        print('Expected IndexError: Got it!')

    # Ensure we have a reference
    print(todo_list.todo_at(1) is todo_list.todo_at(1))  # True

step_6()