import matplotlib.pyplot as plt
import numpy as np

def main():
    plt.plot([1, 2, 3, 4], [1,4, 9, 16])
    plt.ylabel('numbers')
    plt.xlabel('domain')
    plt.show()

    t = np.arange(0., 5., 0.2)
    plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
    plt.xlabel('domain')
    plt.ylabel('numbers')
    plt.show()


if __name__ == "__main__":
    main()