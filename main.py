from LazyGrad.Tensor import Tensor
from LazyGrad.Matrix import Matrix, Kernel
from LazyGrad.Vector import Vector

def main():
    # t1 = Tensor([1, 2])
    # t2 = Tensor([3, 4])
    # t3 = Tensor([5])

    v1 = Vector([1, 2, 3])
    v2 = Vector([4, 5, 6])
    v3 = Vector([7, 8, 9])

    m1 = Matrix(10, 10, [list(range(10)) for _ in range(10)])
    m2 = Matrix(10, 10, [[1 for _ in range(10)] for _ in range(10)])
    k1 = Kernel(3, [[1, 1, 1], [1, 1, 1], [1, 1, 1]])
    sob_kernel = Kernel(3, [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])

    print(sob_kernel)
    print(m1.convolve(sob_kernel))
    print(m2.convolve(k1))

    # print(t1)
    # print(t2)
    # print(t3)
    # print(t1*t2)


if __name__ == "__main__":
    main()