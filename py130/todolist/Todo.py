class Todo:
    IS_DONE = 'X'
    IS_UNDONE = ' '

    def __init__(self, title, status=False):
        self._title = title
        self._done = status

    @property
    def title(self):
        return self._title

    @property
    def done(self):
        return self._done

    @done.setter
    def done(self, status):
        self._done = status

    def __str__(self):
        marker = Todo.IS_DONE if self.done else Todo.IS_UNDONE

        return f"[{marker}] {self.title}"

    # def __repr__(self):
    #     return f"Todo('{self.title}', '{self.done}')"

    def __eq__(self, other):
        if not isinstance(other, Todo):
            return NotImplemented

        return self.title == other.title and self.done == other.done

    def mark_done(self):
        self.done = True

    def mark_undone(self):
        self.done = False

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

    def add(self, todo):
        if not isinstance(todo, Todo):
            raise TypeError('Only Todo objects can be added to a TodoList')

        self._todos.append(todo)

    def __str__(self):
        if not self._todos:
            return "Nothing to do today!"

        output_lines = [f"---- {self.title} -----"]
        for todo in self._todos:
            output_lines.append(f"{todo}")
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
        if index not in range(0, len(self._todos)):
            raise IndexError('Index does not exist')

        return self._todos[index]

    def mark_done_at(self, index):
        todo = self.todo_at(index)
        todo.done = True

    def mark_undone_at(self, index):
        todo = self.todo_at(index)
        todo.done = False

    def mark_all_done(self):
        # for todo in self._todos:
        #     todo.done = True
        self.each(lambda todo: todo.mark_done())

    def mark_all_undone(self):
        # for todo in self._todos:
        #     todo.done = False
        self.each(lambda todo: todo.mark_undone())

    def all_done(self):
        completed_todos = [todo.done for todo in self._todos]
        return all(completed_todos)

    def remove_at(self, index):
        del self._todos[index]

    def each(self, callback):
        for todo in self._todos:
            callback(todo)

    def select(self, callback):
        new_todo_list = TodoList(self.title)
        
        def choose(todo):
            if callback(todo):
                new_todo_list.add(todo)
        
        self.each(choose)
        return new_todo_list

    def find_by_title(self, title):
        # def match_title(todo):
        #     return todo.title == title

        # target = [todo for todo in self._todos if match_title(todo)]
        # return target[0]
        found = self.select(lambda todo: todo.title == title)
        return found.todo_at(0)

    def done_todos(self):
        # def done(todo):
        #     return todo.done

        # return self.select(done)
        return self.select(lambda todo: todo.done)

    def undone_todos(self):
        # def undone(todo):
        #     return todo.done == False

        # return self.select(undone)
        return self.select(lambda todo: not todo.done)

    def mark_done(self, title):
        if self.find_by_title(title):
            # index = self._todos.index(Todo(title))
            # self.mark_done_at(index)
            found = self.find_by_title(title)
            found.done = True

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

def step_7():
    print('--------------------------------- Step 7')
    todo_list = setup()

    todo_list.mark_done_at(0)
    print(todo_list)
    # ---- Today's Todos -----
    # [X] Buy milk
    # [X] Clean room
    # [ ] Go to gym

    todo_list.mark_done_at(1)
    print(todo_list)
    # ---- Today's Todos -----
    # [X] Buy milk
    # [X] Clean room
    # [ ] Go to gym

    todo_list.mark_done_at(2)
    print(todo_list)
    # ---- Today's Todos -----
    # [X] Buy milk
    # [X] Clean room
    # [X] Go to gym

    try:
        todo_list.mark_done_at(3)
    except IndexError:
        print('Expected IndexError: Got it!')

    todo_list.mark_undone_at(0)
    print(todo_list)
    # ---- Today's Todos -----
    # [ ] Buy milk
    # [X] Clean room
    # [X] Go to gym

    todo_list.mark_undone_at(1)
    print(todo_list)
    # ---- Today's Todos -----
    # [ ] Buy milk
    # [ ] Clean room
    # [X] Go to gym

    todo_list.mark_undone_at(2)
    print(todo_list)
    # ---- Today's Todos -----
    # [ ] Buy milk
    # [ ] Clean room
    # [ ] Go to gym

    try:
        todo_list.mark_undone_at(3)
    except IndexError:
        print('Expected IndexError: Got it!')

step_7()

def step_8():
    print('--------------------------------- Step 8')
    todo_list = setup()

    print(todo_list)
    # ---- Today's Todos -----
    # [ ] Buy milk
    # [X] Clean room
    # [ ] Go to gym

    todo_list.mark_all_done()
    print(todo_list)
    # ---- Today's Todos -----
    # [X] Buy milk
    # [X] Clean room
    # [X] Go to gym

    todo_list.mark_all_undone()
    print(todo_list)
    # ---- Today's Todos -----
    # [ ] Buy milk
    # [ ] Clean room
    # [ ] Go to gym

step_8()

# def step_9():
#     print('--------------------------------- Step 9')
#     todo_list = setup()

#     print(todo_list.all_done())         # False

#     todo_list.mark_all_done()
#     print(todo_list.all_done())         # True

#     todo_list.mark_undone_at(1)
#     print(todo_list.all_done())         # False

#     print(empty_todo_list.all_done())   # True

# step_9()

# def step_10():
#     print('--------------------------------- Step 10')
#     todo_list = setup()

#     print(todo_list)
#     # ---- Today's Todos -----
#     # [ ] Buy milk
#     # [X] Clean room
#     # [ ] Go to gym

#     todo_list.remove_at(1)
#     print(todo_list)
#     # ---- Today's Todos -----
#     # [ ] Buy milk
#     # [ ] Go to gym

#     todo_list.remove_at(1)
#     print(todo_list)
#     # ---- Today's Todos -----
#     # [ ] Buy milk

#     try:
#         todo_list.remove_at(1)
#     except IndexError:
#         print('Expected IndexError: Got it!')

#     todo_list.remove_at(0)
#     print(todo_list)
#     # ---- Today's Todos -----

# step_10()

# def step_11():
#     print('--------------------------------- Step 11')
#     todo_list = setup()

#     todo_list.mark_all_undone()
#     print(todo_list)
#     # ---- Today's Todos -----
#     # [ ] Buy milk
#     # [ ] Clean room
#     # [ ] Go to gym

#     def done_if_y_in_title(todo):
#         if 'y' in todo.title:
#             todo.done = True

#     todo_list.each(done_if_y_in_title)
#     print(todo_list)
#     # ---- Today's Todos -----
#     # [X] Buy milk
#     # [ ] Clean room
#     # [X] Go to gym

#     todo_list.each(lambda todo: print('>>>', todo))
#     # >>> [X] Buy milk
#     # >>> [ ] Clean room
#     # >>> [X] Go to gym

# step_11()

# def step_12():
#     print('--------------------------------- Step 12')
#     todo_list = setup()

#     def y_in_title(todo):
#         return 'y' in todo.title

#     print(todo_list.select(y_in_title))
#     # ---- Today's Todos -----
#     # [ ] Buy milk
#     # [ ] Go to gym

#     print(todo_list.select(lambda todo: todo.done))
#     # ---- Today's Todos -----
#     # [X] Clean room

# step_12()

# def step_13():
#     print('--------------------------------- Step 13')
#     todo_list = setup()

#     todo_list.add(Todo('Clean room'))
#     print(todo_list)
#     # ---- Today's Todos -----
#     # [ ] Buy milk
#     # [X] Clean room
#     # [ ] Go to gym
#     # [ ] Clean room

#     found = todo_list.find_by_title('Go to gym')
#     print(found)
#     # [ ] Go to gym

#     found = todo_list.find_by_title('Clean room')
#     print(found)
#     # [X] Clean room

#     try:
#         todo_list.find_by_title('Feed cat')
#     except IndexError:
#         print('Expected IndexError: Got it!')

# step_13()

# def step_14():
#     print('--------------------------------- Step 14')
#     todo_list = setup()

#     done = todo_list.done_todos()
#     print(done)
#     # ----- Today's Todos -----
#     # [X] Clean room

#     undone = todo_list.undone_todos()
#     print(undone)
#     # ----- Today's Todos -----
#     # [ ] Buy milk
#     # [ ] Go to gym

#     done = empty_todo_list.done_todos()
#     print(done)
#     # ----- Nothing Doing -----

#     undone = empty_todo_list.undone_todos()
#     print(undone)
#     # ----- Nothing Doing -----

# step_14()

# def step_15():
#     print('--------------------------------- Step 15')
#     todo_list = setup()

#     todo_list.mark_done('Go to gym')
#     print(todo_list)
#     # ----- Today's Todos -----
#     # [ ] Buy milk
#     # [X] Clean room
#     # [X] Go to gym

#     try:
#         todo_list.mark_done('Feed cat')
#     except IndexError:
#         print('Expected IndexError: Got it!')

# step_15()