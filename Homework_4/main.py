class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0


class Queue:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0


class Matrix:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.data = [[0] * m for _ in range(n)]

    def get(self, i, j):
        if 0 <= i < self.n and 0 <= j < self.m:
            return self.data[i][j]
        else:
            return None

    def set(self, i, j, value):
        if 0 <= i < self.n and 0 <= j < self.m:
            self.data[i][j] = value

    def transpose(self):
        transposed = [[0] * self.n for _ in range(self.m)]
        for i in range(self.n):
            for j in range(self.m):
                transposed[j][i] = self.data[i][j]
        return transposed

    def matrix_multiply(self, other_matrix):
        if self.m != other_matrix.n:
            return None
        result = [[0] * other_matrix.m for _ in range(self.n)]
        for i in range(self.n):
            for j in range(other_matrix.m):
                for k in range(self.m):
                    result[i][j] += self.data[i][k] * other_matrix.data[k][j]
        return result

    def apply_transform(self, transform_func):
        for i in range(self.n):
            for j in range(self.m):
                self.data[i][j] = transform_func(self.data[i][j])


# Utilizare Stack
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())
print(stack.peek())

# Utilizare Queue
queue = Queue()
queue.push("apple")
queue.push("banana")
queue.push("cherry")
print(queue.pop())
print(queue.peek())

# Utilizare Matrix
matrix = Matrix(3, 3)
matrix.set(0, 0, 1)
matrix.set(0, 1, 2)
matrix.set(0, 2, 3)
matrix.set(1, 0, 4)
matrix.set(1, 1, 5)
matrix.set(1, 2, 6)
matrix.set(2, 0, 7)
matrix.set(2, 1, 8)
matrix.set(2, 2, 9)

print(matrix.get(1, 1))

# Transpusa matricei
transposed_matrix = Matrix(matrix.m, matrix.n)
transposed_matrix.data = matrix.transpose()
print(transposed_matrix.data)

# Înmulțirea a două matrici
matrix2 = Matrix(3, 2)
matrix2.set(0, 0, 1)
matrix2.set(0, 1, 2)
matrix2.set(1, 0, 3)
matrix2.set(1, 1, 4)
matrix2.set(2, 0, 5)
matrix2.set(2, 1, 6)

result_matrix = Matrix(matrix.n, matrix2.m)
result_matrix.data = matrix.matrix_multiply(matrix2)
print(result_matrix.data)

# Aplicarea unei transformări asupra matricei
matrix.apply_transform(lambda x: x * 2)
print(matrix.data)
