from pants import Ant, Edge, Solver, World
from random import uniform
from math import sqrt, pow
from model.pub import Pub
from pprint import pprint


def evaluate(a: Pub, b: Pub):
    return sqrt(pow(a.location[1] - b.location[1], 2) + pow(a.location[0]-b.location[0], 2))


def create_word(nodes: list):
    return World(nodes, evaluate)


def print_solution(solution, prefix="    -> "):
    print(prefix, solution.distance, "\n",
          prefix, [x.name for x in solution.tour], "\n",
          #prefix, [x for x in solution.path], "\n"
          )


def create_colony(world: World, solver: Solver):
    # simple way first
    return solver.create_colony(world)


def ACO(solver: Solver, colony):
    return solver.aco(colony)


def GUI(world: World, solution):
    import matplotlib.pyplot as plt
    plt.ylabel("northing")
    plt.xlabel("eating")
    for node in world._nodes:
        plt.scatter(node.location[0], node.location[1], marker="o", c="blue")
        plt.annotate(node.name, xy=(
            node.location[0], node.location[1]), xytext=(-20, 20),
            textcoords='offset points', ha='right', va='bottom',
            bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.5),
            arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0')
        )

    # pprint([x.name for x in solution.tour])
    for i, pub in enumerate(solution.tour):
        # print(pub, i)
        if(i == 0):
            plt.plot(pub.location[0], pub.location[1], c="green")

        else:
            plt.plot([solution.tour[i-1].location[0], pub.location[0]],
                     [solution.tour[i-1].location[1], pub.location[1]], c="green")
    mng = plt.get_current_fig_manager()
    mng.window.showMaximized()
    plt.show()


def solve(world: World):
    solver = Solver()
    colony = create_colony(world, solver)
    solution = ACO(solver, colony)
    #solution = solver.solve(world)

    GUI(world, solution)
    # print_solution(solution)
