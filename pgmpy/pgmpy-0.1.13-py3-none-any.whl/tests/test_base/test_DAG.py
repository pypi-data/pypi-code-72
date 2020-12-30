#!/usr/bin/env python3

import unittest

from pgmpy.base import DAG, PDAG
import pgmpy.tests.help_functions as hf
import networkx as nx


class TestDAGCreation(unittest.TestCase):
    def setUp(self):
        self.graph = DAG()

    def test_class_init_without_data(self):
        self.assertIsInstance(self.graph, DAG)

    def test_class_init_with_data_string(self):
        self.graph = DAG([("a", "b"), ("b", "c")])
        self.assertListEqual(sorted(self.graph.nodes()), ["a", "b", "c"])
        self.assertListEqual(
            hf.recursive_sorted(self.graph.edges()), [["a", "b"], ["b", "c"]]
        )

    def test_add_node_string(self):
        self.graph.add_node("a")
        self.assertListEqual(list(self.graph.nodes()), ["a"])

    def test_add_node_nonstring(self):
        self.graph.add_node(1)

    def test_add_nodes_from_string(self):
        self.graph.add_nodes_from(["a", "b", "c", "d"])
        self.assertListEqual(sorted(self.graph.nodes()), ["a", "b", "c", "d"])

    def test_add_nodes_from_non_string(self):
        self.graph.add_nodes_from([1, 2, 3, 4])

    def test_add_node_weight(self):
        self.graph.add_node("weighted_a", 0.3)
        self.assertEqual(self.graph.nodes["weighted_a"]["weight"], 0.3)

    def test_add_nodes_from_weight(self):
        self.graph.add_nodes_from(["weighted_b", "weighted_c"], [0.5, 0.6])
        self.assertEqual(self.graph.nodes["weighted_b"]["weight"], 0.5)
        self.assertEqual(self.graph.nodes["weighted_c"]["weight"], 0.6)

        self.graph.add_nodes_from(["e", "f"])
        self.assertEqual(self.graph.nodes["e"]["weight"], None)
        self.assertEqual(self.graph.nodes["f"]["weight"], None)

    def test_add_edge_string(self):
        self.graph.add_edge("d", "e")
        self.assertListEqual(sorted(self.graph.nodes()), ["d", "e"])
        self.assertListEqual(list(self.graph.edges()), [("d", "e")])
        self.graph.add_nodes_from(["a", "b", "c"])
        self.graph.add_edge("a", "b")
        self.assertListEqual(
            hf.recursive_sorted(self.graph.edges()), [["a", "b"], ["d", "e"]]
        )

    def test_add_edge_nonstring(self):
        self.graph.add_edge(1, 2)

    def test_add_edges_from_string(self):
        self.graph.add_edges_from([("a", "b"), ("b", "c")])
        self.assertListEqual(sorted(self.graph.nodes()), ["a", "b", "c"])
        self.assertListEqual(
            hf.recursive_sorted(self.graph.edges()), [["a", "b"], ["b", "c"]]
        )
        self.graph.add_nodes_from(["d", "e", "f"])
        self.graph.add_edges_from([("d", "e"), ("e", "f")])
        self.assertListEqual(sorted(self.graph.nodes()), ["a", "b", "c", "d", "e", "f"])
        self.assertListEqual(
            hf.recursive_sorted(self.graph.edges()),
            hf.recursive_sorted([("a", "b"), ("b", "c"), ("d", "e"), ("e", "f")]),
        )

    def test_add_edges_from_nonstring(self):
        self.graph.add_edges_from([(1, 2), (2, 3)])

    def test_add_edge_weight(self):
        self.graph.add_edge("a", "b", weight=0.3)
        if nx.__version__.startswith("1"):
            self.assertEqual(self.graph.edge["a"]["b"]["weight"], 0.3)
        else:
            self.assertEqual(self.graph.adj["a"]["b"]["weight"], 0.3)

    def test_add_edges_from_weight(self):
        self.graph.add_edges_from([("b", "c"), ("c", "d")], weights=[0.5, 0.6])
        if nx.__version__.startswith("1"):
            self.assertEqual(self.graph.edge["b"]["c"]["weight"], 0.5)
            self.assertEqual(self.graph.edge["c"]["d"]["weight"], 0.6)

            self.graph.add_edges_from([("e", "f")])
            self.assertEqual(self.graph.edge["e"]["f"]["weight"], None)
        else:
            self.assertEqual(self.graph.adj["b"]["c"]["weight"], 0.5)
            self.assertEqual(self.graph.adj["c"]["d"]["weight"], 0.6)

            self.graph.add_edges_from([("e", "f")])
            self.assertEqual(self.graph.adj["e"]["f"]["weight"], None)

    def test_update_node_parents_bm_constructor(self):
        self.graph = DAG([("a", "b"), ("b", "c")])
        self.assertListEqual(list(self.graph.predecessors("a")), [])
        self.assertListEqual(list(self.graph.predecessors("b")), ["a"])
        self.assertListEqual(list(self.graph.predecessors("c")), ["b"])

    def test_update_node_parents(self):
        self.graph.add_nodes_from(["a", "b", "c"])
        self.graph.add_edges_from([("a", "b"), ("b", "c")])
        self.assertListEqual(list(self.graph.predecessors("a")), [])
        self.assertListEqual(list(self.graph.predecessors("b")), ["a"])
        self.assertListEqual(list(self.graph.predecessors("c")), ["b"])

    def test_get_leaves(self):
        self.graph.add_edges_from(
            [("A", "B"), ("B", "C"), ("B", "D"), ("D", "E"), ("D", "F"), ("A", "G")]
        )
        self.assertEqual(sorted(self.graph.get_leaves()), sorted(["C", "G", "E", "F"]))

    def test_get_roots(self):
        self.graph.add_edges_from(
            [("A", "B"), ("B", "C"), ("B", "D"), ("D", "E"), ("D", "F"), ("A", "G")]
        )
        self.assertEqual(["A"], self.graph.get_roots())
        self.graph.add_edge("H", "G")
        self.assertEqual(sorted(["A", "H"]), sorted(self.graph.get_roots()))

    def test_init_with_cycle(self):
        self.assertRaises(ValueError, DAG, [("a", "a")])
        self.assertRaises(ValueError, DAG, [("a", "b"), ("b", "a")])
        self.assertRaises(ValueError, DAG, [("a", "b"), ("b", "c"), ("c", "a")])

    def test_get_ancestral_graph(self):
        dag = DAG([("A", "C"), ("B", "C"), ("D", "A"), ("D", "B")])
        anc_dag = dag.get_ancestral_graph(["A", "B"])
        self.assertEqual(set(anc_dag.edges()), set([("D", "A"), ("D", "B")]))
        self.assertRaises(ValueError, dag.get_ancestral_graph, ["A", "gibber"])

    def tearDown(self):
        del self.graph


class TestDAGMoralization(unittest.TestCase):
    def setUp(self):
        self.graph = DAG()
        self.graph.add_edges_from([("diff", "grade"), ("intel", "grade")])

    def test_get_parents(self):
        self.assertListEqual(sorted(self.graph.get_parents("grade")), ["diff", "intel"])

    def test_moralize(self):
        moral_graph = self.graph.moralize()
        self.assertListEqual(
            hf.recursive_sorted(moral_graph.edges()),
            [["diff", "grade"], ["diff", "intel"], ["grade", "intel"]],
        )

    def test_moralize_disconnected(self):
        graph_copy = self.graph.copy()
        graph_copy.add_node("disconnected")
        moral_graph = graph_copy.moralize()
        self.assertListEqual(
            hf.recursive_sorted(moral_graph.edges()),
            [["diff", "grade"], ["diff", "intel"], ["grade", "intel"]],
        )
        self.assertEqual(
            sorted(moral_graph.nodes()), ["diff", "disconnected", "grade", "intel"]
        )

    def test_get_children(self):
        self.assertListEqual(sorted(self.graph.get_children("diff")), ["grade"])

    def tearDown(self):
        del self.graph


class TestDoOperator(unittest.TestCase):
    def setUp(self):
        self.graph = DAG()
        self.graph.add_edges_from([("X", "A"), ("A", "Y"), ("A", "B")])

    def test_do(self):
        dag_do_x = self.graph.do("A")
        self.assertEqual(set(dag_do_x.nodes()), set(self.graph.nodes()))
        self.assertEqual(sorted(list(dag_do_x.edges())), [("A", "B"), ("A", "Y")])


class TestPDAG(unittest.TestCase):
    def setUp(self):
        self.pdag_mix = PDAG(
            directed_ebunch=[("A", "C"), ("D", "C")],
            undirected_ebunch=[("B", "A"), ("B", "D")],
        )
        self.pdag_dir = PDAG(
            directed_ebunch=[("A", "B"), ("D", "B"), ("A", "C"), ("D", "C")]
        )
        self.pdag_undir = PDAG(
            undirected_ebunch=[("A", "C"), ("D", "C"), ("B", "A"), ("B", "D")]
        )

    def test_init_normal(self):
        # Mix directed and undirected
        directed_edges = [("A", "C"), ("D", "C")]
        undirected_edges = [("B", "A"), ("B", "D")]
        pdag = PDAG(directed_ebunch=directed_edges, undirected_ebunch=undirected_edges)
        expected_edges = {
            ("A", "C"),
            ("D", "C"),
            ("A", "B"),
            ("B", "A"),
            ("B", "D"),
            ("D", "B"),
        }
        self.assertEqual(set(pdag.edges()), expected_edges)
        self.assertEqual(set(pdag.nodes()), {"A", "B", "C", "D"})
        self.assertEqual(pdag.directed_edges, set(directed_edges))
        self.assertEqual(pdag.undirected_edges, set(undirected_edges))

        # Only undirected
        undirected_edges = [("A", "C"), ("D", "C"), ("B", "A"), ("B", "D")]
        pdag = PDAG(undirected_ebunch=undirected_edges)
        expected_edges = {
            ("A", "C"),
            ("C", "A"),
            ("D", "C"),
            ("C", "D"),
            ("B", "A"),
            ("A", "B"),
            ("B", "D"),
            ("D", "B"),
        }
        self.assertEqual(set(pdag.edges()), expected_edges)
        self.assertEqual(set(pdag.nodes()), {"A", "B", "C", "D"})
        self.assertEqual(pdag.directed_edges, set())
        self.assertEqual(pdag.undirected_edges, set(undirected_edges))

        # Only directed
        directed_edges = [("A", "B"), ("D", "B"), ("A", "C"), ("D", "C")]
        pdag = PDAG(directed_ebunch=directed_edges)
        self.assertEqual(set(pdag.edges()), set(directed_edges))
        self.assertEqual(set(pdag.nodes()), {"A", "B", "C", "D"})
        self.assertEqual(pdag.directed_edges, set(directed_edges))
        self.assertEqual(pdag.undirected_edges, set())

        # TODO: Fix the cycle issue.
        # Test cycle
        # directed_edges = [('A', 'C')]
        # undirected_edges = [('A', 'B'), ('B', 'D'), ('D', 'C')]
        # self.assertRaises(ValueError, PDAG, directed_ebunch=directed_edges, undirected_ebunch=undirected_edges)

    def test_copy(self):
        pdag_copy = self.pdag_mix.copy()
        expected_edges = {
            ("A", "C"),
            ("D", "C"),
            ("A", "B"),
            ("B", "A"),
            ("B", "D"),
            ("D", "B"),
        }
        expected_dir = [("A", "C"), ("D", "C")]
        expected_undir = [("B", "A"), ("B", "D")]
        self.assertEqual(set(pdag_copy.edges()), expected_edges)
        self.assertEqual(set(pdag_copy.nodes()), {"A", "B", "C", "D"})
        self.assertEqual(pdag_copy.directed_edges, set([("A", "C"), ("D", "C")]))
        self.assertEqual(pdag_copy.undirected_edges, set([("B", "A"), ("B", "D")]))

    def test_pdag_to_dag(self):
        # PDAG no: 1  Possibility of creating a v-structure
        pdag = PDAG(
            directed_ebunch=[("A", "B"), ("C", "B")],
            undirected_ebunch=[("C", "D"), ("D", "A")],
        )
        dag = pdag.to_dag()
        self.assertTrue(("A", "B") in dag.edges())
        self.assertTrue(("C", "B") in dag.edges())
        self.assertFalse((("A", "D") in dag.edges()) and (("C", "D") in dag.edges()))
        self.assertTrue(len(dag.edges()) == 4)

        # PDAG no: 2  No possibility of creation of v-structure.
        pdag = PDAG(
            directed_ebunch=[("B", "C"), ("A", "C")], undirected_ebunch=[("A", "D")]
        )
        dag = pdag.to_dag()
        self.assertTrue(("B", "C") in dag.edges())
        self.assertTrue(("A", "C") in dag.edges())
        self.assertTrue((("A", "D") in dag.edges()) or (("D", "A") in dag.edges()))

        # PDAG no: 3  Already existing v-structure, possiblity to add another
        pdag = PDAG(
            directed_ebunch=[("B", "C"), ("A", "C")], undirected_ebunch=[("C", "D")]
        )
        dag = pdag.to_dag()
        expected_edges = {("B", "C"), ("C", "D"), ("A", "C")}
        self.assertEqual(expected_edges, set(dag.edges()))
