# Copyright (c) 2015 Universidade Federal Fluminense (UFF)
# This file is part of PyPosAST.
# Please, consult the license terms in the LICENSE file.

from __future__ import (absolute_import, division)

import ast

from .utils import get_nodes, NodeTestCase, only_python2, only_python3


class TestMod(NodeTestCase):

    def test_module(self):
        code = ("#bla\n"
                "")
        nodes = get_nodes(code, ast.Module)
        self.assertPosition(nodes[0], (0, 0), (0, 0), (0, 0))
        self.assertNoBeforeInnerAfter(nodes[0])

    def test_module2(self):
        code = ("#bla\n"
                "a")
        nodes = get_nodes(code, ast.Module)
        self.assertPosition(nodes[0], (2, 0), (2, 1), (2, 1))
        self.assertNoBeforeInnerAfter(nodes[0])

    def test_interactive(self):
        code = ("a")
        nodes = get_nodes(code, ast.Interactive, mode='single')
        self.assertPosition(nodes[0], (1, 0), (1, 1), (1, 1))
        self.assertNoBeforeInnerAfter(nodes[0])

    def test_expression(self):
        code = ("a")
        nodes = get_nodes(code, ast.Expression, mode='eval')
        self.assertPosition(nodes[0], (1, 0), (1, 1), (1, 1))
        self.assertNoBeforeInnerAfter(nodes[0])
