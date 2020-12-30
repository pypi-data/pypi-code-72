from symfem import create_element


def all_equal(a, b):
    try:
        for i, j in zip(a, b):
            if not all_equal(i, j):
                return False
        return True
    except TypeError:
        return a == b


def test_lagrange():
    space = create_element("triangle", "Lagrange", 1)
    assert all_equal(
        space.tabulate_basis([[0, 0], [0, 1], [1, 0]]),
        ((1, 0, 0), (0, 0, 1), (0, 1, 0)),
    )


def test_nedelec():
    space = create_element("triangle", "Nedelec", 1)
    assert all_equal(
        space.tabulate_basis([[0, 0], [1, 0], [0, 1]], "xxyyzz"),
        ((0, 0, 1, 0, 1, 0), (0, 0, 1, 1, 0, 1), (-1, 1, 0, 0, 1, 0)),
    )


def test_rt():
    space = create_element("triangle", "Raviart-Thomas", 1)
    assert all_equal(
        space.tabulate_basis([[0, 0], [1, 0], [0, 1]], "xxyyzz"),
        ((0, -1, 0, 0, 0, 1), (-1, 0, -1, 0, 0, 1), (0, -1, 0, -1, 1, 0)),
    )


def test_Q():
    space = create_element("quadrilateral", "Q", 1)
    assert all_equal(
        space.tabulate_basis([[0, 0], [1, 0], [0, 1], [1, 1]]),
        ((1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)),
    )
