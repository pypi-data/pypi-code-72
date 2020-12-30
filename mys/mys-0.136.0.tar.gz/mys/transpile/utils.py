import re
import textwrap
from ..parser import ast

class CompileError(Exception):

    def __init__(self, message, node):
        self.message = message
        self.lineno = node.lineno
        self.offset = node.col_offset

class InternalError(CompileError):
    pass

SNAKE_CASE_RE = re.compile(r'^(_*[a-z][a-z0-9_]*)$')
UPPER_SNAKE_CASE_RE = re.compile(r'^(_*[A-Z][A-Z0-9_]*)$')
PASCAL_CASE_RE = re.compile(r'^_?[A-Z][a-zA-Z0-9]*$')

BOOL_OPS = {
    ast.And: '&&',
    ast.Or: '||'
}

METHOD_OPERATORS = {
    '__add__': '+',
    '__sub__': '-',
    '__iadd__': '+=',
    '__isub__': '-=',
    '__eq__': '==',
    '__ne__': '!=',
    '__gt__': '>',
    '__ge__': '>=',
    '__lt__': '<',
    '__le__': '<='
}

OPERATORS = {
    ast.Add: '+',
    ast.Sub: '-',
    ast.Mult: '*',
    ast.Div: '/',
    ast.Mod: '%',
    ast.LShift: '<<',
    ast.RShift: '>>',
    ast.BitOr: '|',
    ast.BitXor: '^',
    ast.BitAnd: '&',
    ast.FloorDiv: '/',
    ast.Not: '!',
    ast.Invert: '~',
    ast.UAdd: '+',
    ast.USub: '-',
    ast.Is: '==',
    ast.Eq: '==',
    ast.NotEq: '!=',
    ast.Lt: '<',
    ast.LtE: '<=',
    ast.Gt: '>',
    ast.GtE: '>='
}

PRIMITIVE_TYPES = set([
    'i8',
    'i16',
    'i32',
    'i64',
    'u8',
    'u16',
    'u32',
    'u64',
    'f32',
    'f64',
    'bool',
    'char'
])

INTEGER_TYPES = set(['i8', 'i16', 'i32', 'i64', 'u8', 'u16', 'u32', 'u64'])
NUMBER_TYPES = INTEGER_TYPES | set(['f32', 'f64'])
FOR_LOOP_FUNCS = set(['enumerate', 'range', 'reversed', 'slice', 'zip'])
CPP_RESERVED = set([
    'alignas',
    'alignof',
    'and',
    'and_eq',
    'asm',
    'atomic_cancel',
    'atomic_commit',
    'atomic_noexcept',
    'auto',
    'bitand',
    'bitor',
    'bool',
    'break',
    'case',
    'catch',
    'char',
    'char8_t',
    'char16_t',
    'char32_t',
    'class',
    'compl',
    'concept',
    'const',
    'consteval',
    'constexpr',
    'constinit',
    'const_cast',
    'continue',
    'co_await',
    'co_return',
    'co_yield',
    'decltype',
    'default',
    'delete',
    'do',
    'double',
    'dynamic_cast',
    'else',
    'enum',
    'explicit',
    'export',
    'extern',
    'false',
    'float',
    'for',
    'friend',
    'goto',
    'if',
    'inline',
    'int',
    'long',
    'mutable',
    'namespace',
    'new',
    'noexcept',
    'not',
    'not_eq',
    'nullptr',
    'operator',
    'or',
    'or_eq',
    'private',
    'protected',
    'public',
    'reflexpr',
    'register',
    'reinterpret_cast',
    'requires',
    'return',
    'short',
    'signed',
    'sizeof',
    'static',
    'static_assert',
    'static_cast',
    'struct',
    'switch',
    'synchronized',
    'template',
    'this',
    'thread_local',
    'throw',
    'true',
    'try',
    'typedef',
    'typeid',
    'typename',
    'union',
    'unsigned',
    'using',
    'virtual',
    'void',
    'volatile',
    'wchar_t',
    'while',
    'xor',
    'xor_eq',
])

def make_name(name):
    if name in CPP_RESERVED:
        name = f'__cpp_{name}'

    return name

class Variables:

    def __init__(self):
        self._first_add = True
        self._variables = {}

    def add_branch(self, variables):
        if self._first_add:
            for name, info in variables.items():
                self._variables[name] = info

            self._first_add = False
        else:
            to_remove = []

            for name, info in self._variables.items():
                new_info = variables.get(name)

                if new_info is None or new_info != info:
                    to_remove.append(name)

            for name in to_remove:
                self._variables.pop(name)

    def defined(self):
        return self._variables

def mys_type_to_target_cpp_type(mys_type):
    if is_primitive_type(mys_type):
        return 'auto'
    else:
        return 'const auto&'

def split_dict_mys_type(mys_type):
    key_mys_type = list(mys_type.keys())[0]
    value_mys_type = list(mys_type.values())[0]

    return key_mys_type, value_mys_type

def format_binop(left, right, op_class):
    if op_class == ast.Pow:
        return f'ipow({left}, {right})'
    else:
        op = OPERATORS[op_class]

        return f'({left} {op} {right})'

def make_shared(cpp_type, values):
    return f'std::make_shared<{cpp_type}>({values})'

def shared_list_type(cpp_type):
    return f'SharedList<{cpp_type}>'

def make_shared_list(cpp_type, value):
    return (f'std::make_shared<List<{cpp_type}>>('
            f'std::initializer_list<{cpp_type}>{{{value}}})')

def shared_dict_type(key_cpp_type, value_cpp_type):
    return f'SharedDict<{key_cpp_type}, {value_cpp_type}>'

def make_shared_dict(key_cpp_type, value_cpp_type, items):
    return (f'std::make_shared<Dict<{key_cpp_type}, {value_cpp_type}>>('
            f'std::initializer_list<robin_hood::pair<{key_cpp_type}, '
            f'{value_cpp_type}>>{{{items}}})')

def shared_tuple_type(items):
    return f'SharedTuple<{items}>'

def wrap_not_none(obj, mys_type):
    if is_primitive_type(mys_type):
        return obj
    elif obj == 'this':
        return obj
    elif mys_type == 'string':
        return f'string_not_none({obj})'
    elif mys_type == 'bytes':
        return f'bytes_not_none({obj})'
    else:
        return f'shared_ptr_not_none({obj})'

def compare_is_variable(variable, variable_mys_type):
    if variable != 'nullptr':
        if variable_mys_type == 'string':
            variable = f'{variable}.m_string'
        elif variable_mys_type == 'bytes':
            variable = f'{variable}.m_bytes'

    return variable

def compare_is_variables(left, left_mys_type, right, right_mys_type):
    left = compare_is_variable(left, left_mys_type)
    right = compare_is_variable(right, right_mys_type)

    return left, right

def compare_assert_is_variable(variable):
    if variable[1] == 'string':
        variable = f'{variable[0]}.m_string'
    elif variable[1] == 'bytes':
        variable = f'{variable[0]}.m_bytes'
    else:
        variable = variable[0]

    return variable

def compare_assert_is_variables(variable_1, variable_2):
    variable_1 = compare_assert_is_variable(variable_1)
    variable_2 = compare_assert_is_variable(variable_2)

    return variable_1, variable_2

def is_allowed_dict_key_type(mys_type):
    if is_primitive_type(mys_type):
        return True
    elif mys_type == 'string':
        return True

    return False

def raise_if_self(name, node):
    if name == 'self':
        raise CompileError("it's not allowed to assign to 'self'", node)

def raise_if_wrong_number_of_parameters(actual_nargs,
                                        expected_nargs,
                                        node,
                                        min_args=None):
    if min_args is None:
        min_args = expected_nargs

    if min_args <= actual_nargs <= expected_nargs:
        return

    if expected_nargs == 1:
        raise CompileError(
            f"expected {expected_nargs} parameter, got {actual_nargs}",
            node)
    else:
        raise CompileError(
            f"expected {expected_nargs} parameters, got {actual_nargs}",
            node)

def format_str(value, mys_type):
    if is_primitive_type(mys_type):
        return f'String({value})'
    elif mys_type == 'string':
        return f'string_str({value})'
    elif mys_type == 'bytes':
        return f'bytes_str({value})'
    else:
        none = handle_string("None")

        return f'({value} ? shared_ptr_not_none({value})->__str__() : {none})'

def format_print_arg(arg, context):
    value, mys_type = arg

    if mys_type == 'i8':
        value = f'(int){value}'
    elif mys_type == 'u8':
        value = f'(unsigned){value}'
    elif mys_type == 'string':
        value = f'PrintString({value})'
    elif mys_type == 'char':
        value = f'PrintChar({value})'

    return value

def format_arg(arg, context):
    value, mys_type = arg

    if mys_type == 'i8':
        value = f'(int){value}'
    elif mys_type == 'u8':
        value = f'(unsigned){value}'

    return value

def is_none_value(node):
    if not isinstance(node, ast.Constant):
        return False

    return node.value is None

def is_primitive_type(mys_type):
    if not isinstance(mys_type, str):
        return False

    return mys_type in PRIMITIVE_TYPES

def raise_types_differs(left_mys_type, right_mys_type, node):
    left = format_mys_type(left_mys_type)
    right = format_mys_type(right_mys_type)

    raise CompileError(f"types '{left}' and '{right}' differs", node)

def raise_if_types_differs(left_mys_type, right_mys_type, node):
    if left_mys_type != right_mys_type:
        raise_types_differs(left_mys_type, right_mys_type, node)

def raise_wrong_types(actual_mys_type, expected_mys_type, node):
    if is_primitive_type(expected_mys_type) and actual_mys_type is None:
        raise CompileError(f"'{expected_mys_type}' can't be None", node)
    else:
        actual = format_mys_type(actual_mys_type)
        expected = format_mys_type(expected_mys_type)

        raise CompileError(f"expected a '{expected}', got a '{actual}'", node)

def raise_if_wrong_types(actual_mys_type, expected_mys_type, node, context):
    if actual_mys_type == expected_mys_type:
        return

    if actual_mys_type is None:
        if context.is_class_or_trait_defined(expected_mys_type):
            return
        elif expected_mys_type in ['string', 'bytes']:
            return
        elif isinstance(expected_mys_type, (list, tuple, dict)):
            return

    raise_wrong_types(actual_mys_type, expected_mys_type, node)

def raise_if_not_bool(mys_type, node, context):
    raise_if_wrong_types(mys_type, 'bool', node, context)

def raise_if_wrong_visited_type(context, expected_mys_type, node):
    raise_if_wrong_types(context.mys_type,
                         expected_mys_type,
                         node,
                         context)

def is_snake_case(value):
    return SNAKE_CASE_RE.match(value) is not None

def is_upper_snake_case(value):
    return UPPER_SNAKE_CASE_RE.match(value) is not None

def is_pascal_case(value):
    return PASCAL_CASE_RE.match(value)

def mys_to_cpp_type(mys_type, context):
    if isinstance(mys_type, tuple):
        items = ', '.join([mys_to_cpp_type(item, context) for item in mys_type])

        return shared_tuple_type(items)
    elif isinstance(mys_type, list):
        item = mys_to_cpp_type(mys_type[0], context)

        return shared_list_type(item)
    elif isinstance(mys_type, dict):
        key_mys_type, value_mys_type = split_dict_mys_type(mys_type)
        key = mys_to_cpp_type(key_mys_type, context)
        value = mys_to_cpp_type(value_mys_type, context)

        return shared_dict_type(key, value)
    else:
        if mys_type == 'string':
            return 'String'
        elif mys_type == 'bool':
            return 'Bool'
        elif mys_type == 'char':
            return 'Char'
        elif mys_type == 'bytes':
            return 'Bytes'
        elif context.is_class_or_trait_defined(mys_type):
            return f'std::shared_ptr<{mys_type}>'
        elif context.is_enum_defined(mys_type):
            return context.get_enum_type(mys_type)
        else:
            return mys_type

def mys_to_cpp_type_param(mys_type, context):
    cpp_type = mys_to_cpp_type(mys_type, context)

    if not is_primitive_type(mys_type):
        cpp_type = f'const {cpp_type}&'

    return cpp_type

def mys_to_value_type(mys_type):
    if isinstance(mys_type, tuple):
        return tuple([mys_to_value_type(item) for item in mys_type])
    elif isinstance(mys_type, list):
        return [mys_to_value_type(mys_type[0])]
    elif isinstance(mys_type, dict):
        key_mys_type, value_mys_type = split_dict_mys_type(mys_type)

        return Dict(mys_to_value_type(key_mys_type),
                    mys_to_value_type(value_mys_type))
    else:
        return mys_type

def format_mys_type(mys_type):
    if isinstance(mys_type, tuple):
        if len(mys_type) == 1:
            items = f'{format_mys_type(mys_type[0])}, '
        else:
            items = ', '.join([format_mys_type(item) for item in mys_type])

        return f'({items})'
    elif isinstance(mys_type, list):
        item = format_mys_type(mys_type[0])

        return f'[{item}]'
    elif isinstance(mys_type, dict):
        key_mys_type, value_mys_type = split_dict_mys_type(mys_type)
        key = format_mys_type(key_mys_type)
        value = format_mys_type(value_mys_type)

        return f'{{{key}: {value}}}'
    else:
        return str(mys_type)

def format_value_type(value_type):
    if isinstance(value_type, tuple):
        if len(value_type) == 1:
            items = f'{format_value_type(value_type[0])}, '
        else:
            items = ', '.join([format_value_type(item) for item in value_type])

        return f'({items})'
    elif isinstance(value_type, list):
        if len(value_type) == 1:
            return f'[{format_value_type(value_type[0])}]'
        else:
            return '/'.join([format_value_type(item) for item in value_type])
    elif isinstance(value_type, dict):
        key_value_type, value_value_type = split_dict_value_type(value_type)
        key = format_value_type(key_value_type)
        value = format_value_type(value_value_type)

        return f'{{{key}: {value}}}'
    else:
        return value_type

class TypeVisitor(ast.NodeVisitor):

    def visit_Name(self, node):
        return node.id

    def visit_List(self, node):
        nitems = len(node.elts)

        if nitems != 1:
            raise CompileError(f"expected 1 type in list, got {nitems}", node)

        return [self.visit(elem) for elem in node.elts]

    def visit_Tuple(self, node):
        return tuple([self.visit(elem) for elem in node.elts])

    def visit_Dict(self, node):
        return {node.keys[0].id: self.visit(node.values[0])}

def intersection_of(type_1, type_2, node):
    """Find the intersection of given visited types.

    """

    if type_1 is None:
        if is_primitive_type(type_2):
            raise CompileError(f"'{type_2}' can't be None", node)
        else:
            return type_2, type_2
    elif type_2 is None:
        if is_primitive_type(type_1):
            raise CompileError(f"'{type_1}' can't be None", node)
        else:
            return type_1, type_1
    elif type_1 == type_2:
       return type_1, type_2
    elif isinstance(type_1, str) and isinstance(type_2, str):
        raise_if_types_differs(type_1, type_2, node)
    elif isinstance(type_1, tuple) and isinstance(type_2, tuple):
        if len(type_1) != len(type_2):
            return None, None
        else:
            new_type_1 = []
            new_type_2 = []

            for item_type_1, item_type_2 in zip(type_1, type_2):
                item_type_1, item_type_2 = intersection_of(item_type_1,
                                                           item_type_2,
                                                           node)

                if item_type_1 is None or item_type_2 is None:
                    return None, None

                new_type_1.append(item_type_1)
                new_type_2.append(item_type_2)

            return tuple(new_type_1), tuple(new_type_2)
    elif isinstance(type_1, Dict) and isinstance(type_2, Dict):
        key_value_type_1, key_value_type_2 = intersection_of(type_1.key_type,
                                                             type_2.key_type,
                                                             node)
        value_value_type_1, value_value_type_2 = intersection_of(type_1.value_type,
                                                                 type_2.value_type,
                                                                 node)

        return (Dict(key_value_type_1, value_value_type_1),
                Dict(key_value_type_2, value_value_type_2))
    elif isinstance(type_1, str):
        if not isinstance(type_2, list):
            return None, None
        elif type_1 not in type_2:
            type_1 = format_value_type(type_1)
            type_2 = format_value_type(type_2)

            raise CompileError(f"can't convert '{type_1}' to '{type_2}'", node)
        else:
            return type_1, type_1
    elif isinstance(type_2, str):
        if not isinstance(type_1, list):
            return None, None
        elif type_2 not in type_1:
            type_1 = format_value_type(type_1)
            type_2 = format_value_type(type_2)

            raise CompileError(f"can't convert '{type_1}' to '{type_2}'", node)
        else:
            return type_2, type_2
    elif isinstance(type_1, list) and isinstance(type_2, list):
        if len(type_1) == 0 and len(type_2) == 0:
            return [], []
        elif len(type_1) == 1 and len(type_2) == 1:
            item_type_1, item_type_2 = intersection_of(type_1[0], type_2[0], node)

            return [item_type_1], [item_type_2]
        elif len(type_1) == 1 and len(type_2) == 0:
            return type_1, type_1
        elif len(type_2) == 1 and len(type_1) == 0:
            return type_2, type_2
        elif len(type_1) == 1 and len(type_2) > 1:
            type_1 = format_value_type(type_1)
            type_2 = format_value_type(type_2)

            raise CompileError(f"can't convert '{type_1}' to '{type_2}'", node)
        elif len(type_2) == 1 and len(type_1) > 1:
            type_1 = format_value_type(type_1)
            type_2 = format_value_type(type_2)

            raise CompileError(f"can't convert '{type_1}' to '{type_2}'", node)
        else:
            new_type_1 = []
            new_type_2 = []

            for item_type_1 in type_1:
                for item_type_2 in type_2:
                    if isinstance(item_type_1, str) and isinstance(item_type_2, str):
                        if item_type_1 != item_type_2:
                            continue
                    else:
                        item_type_1, item_type_2 = intersection_of(item_type_1,
                                                                   item_type_2,
                                                                   node)

                        if item_type_1 is None or item_type_2 is None:
                            continue

                    new_type_1.append(item_type_1)
                    new_type_2.append(item_type_2)

            if len(new_type_1) == 0:
                type_1 = format_value_type(type_1)
                type_2 = format_value_type(type_2)

                raise CompileError(f"can't convert '{type_1}' to '{type_2}'", node)
            elif len(new_type_1) == 1:
                return new_type_1[0], new_type_2[0]
            else:
                return new_type_1, new_type_2
    else:
        raise InternalError("specialize types", node)

def reduce_type(value_type):
    if isinstance(value_type, list):
        if len(value_type) == 0:
            return ['bool']
        elif len(value_type) == 1:
            return [reduce_type(value_type[0])]
        else:
            return reduce_type(value_type[0])
    elif isinstance(value_type, tuple):
        values = []

        for item in value_type:
            values.append(reduce_type(item))

        return tuple(values)
    elif isinstance(value_type, str):
        return value_type
    elif isinstance(value_type, Dict):
        return {reduce_type(value_type.key_type): reduce_type(value_type.value_type)}

class Dict:

    def __init__(self, key_type, value_type):
        self.key_type = key_type
        self.value_type = value_type

    def __str__(self):
        return f'Dict({self.key_type}, {self.value_type})'

class ValueTypeVisitor(ast.NodeVisitor):

    def __init__(self, source_lines, context):
        self.source_lines = source_lines
        self.context = context
        self.factor = 1

    def visit_BoolOp(self, node):
        return 'bool'

    def visit_JoinedStr(self, node):
        return 'string'

    def visit_BinOp(self, node):
        left_value_type = self.visit(node.left)
        right_value_type = self.visit(node.right)

        return intersection_of(left_value_type, right_value_type, node)[0]

    def visit_Subscript(self, node):
        value_type = self.visit(node.value)

        if isinstance(value_type, list):
            value_type = value_type[0]
        elif isinstance(value_type, tuple):
            index = make_integer_literal('i64', node.slice)
            value_type = value_type[int(index)]
        elif isinstance(value_type, Dict):
            value_type = value_type.value_type
        elif value_type == 'string':
            value_type = 'char'
        elif value_type == 'bytes':
            value_type = 'u8'
        else:
            raise

        return value_type

    def visit_IfExp(self, node):
        return self.visit(node.body)

    def visit_Attribute(self, node):
        name = node.attr

        if isinstance(node.value, ast.Name):
            value = node.value.id

            if self.context.is_enum_defined(value):
                value_type = value
            elif self.context.is_variable_defined(value):
                value_type = self.context.get_variable_type(value)
            else:
                raise InternalError("attribute", node)
        else:
            value_type = self.visit(node.value)

        if self.context.is_class_defined(value_type):
            member = self.context.get_class(value_type).members[name]
            value_type = member.type

        if isinstance(value_type, dict):
            value_type = Dict(list(value_type.keys())[0],
                              list(value_type.values())[0])

        return value_type

    def visit_UnaryOp(self, node):
        if isinstance(node.op, ast.USub):
            factor = -1
        else:
            factor = 1

        self.factor *= factor

        try:
            value = self.visit(node.operand)
        except CompileError as e:
            e.lineno = node.lineno
            e.offset = node.col_offset

            raise e

        self.factor *= factor

        return value

    def visit_Constant(self, node):
        if isinstance(node.value, bool):
            return 'bool'
        elif isinstance(node.value, int):
            types = ['i64', 'i32', 'i16', 'i8']

            if self.factor == 1:
                types += ['u64', 'u32', 'u16', 'u8']

            return types
        elif isinstance(node.value, float):
            return ['f64', 'f32']
        elif isinstance(node.value, str):
            if is_string(node, self.source_lines):
                return 'string'
            else:
                return 'char'
        elif isinstance(node.value, bytes):
            return 'bytes'
        elif node.value is None:
            return None
        else:
            raise

    def visit_Name(self, node):
        name = node.id

        if name == '__unique_id__':
            return 'i64'
        elif name == '__line__':
            return 'u64'
        elif name == '__name__':
            return 'string'
        elif name == '__file__':
            return 'string'
        else:
            if not self.context.is_variable_defined(name):
                raise CompileError(f"undefined variable '{name}'", node)

            value_type = self.context.get_variable_type(name)

            if isinstance(value_type, dict):
                value_type = Dict(list(value_type.keys())[0],
                                  list(value_type.values())[0])

            return value_type

    def visit_List(self, node):
        if len(node.elts) == 0:
            return []

        item_type = self.visit(node.elts[0])

        for item in node.elts[1:]:
            item_type, _ = intersection_of(item_type, self.visit(item), item)

        return [item_type]

    def visit_Tuple(self, node):
        return tuple([self.visit(elem) for elem in node.elts])

    def visit_Dict(self, node):
        if len(node.keys) > 0:
            return Dict(self.visit(node.keys[0]), self.visit(node.values[0]))
        else:
            return Dict(None, None)

    def visit_call_function(self, name, node):
        function = self.context.get_functions(name)[0]

        return mys_to_value_type(function.returns)

    def visit_call_class(self, mys_type, node):
        return mys_type

    def visit_call_enum(self, mys_type, node):
        return mys_type

    def visit_call_builtin(self, name, node):
        if name in NUMBER_TYPES:
            return name
        elif name == 'len':
            return 'u64'
        elif name == 'str':
            return 'string'
        elif name == 'char':
            return 'char'
        elif name == 'list':
            value_type = self.visit(node.args[0])

            if isinstance(value_type, Dict):
                return [(value_type.key_type, value_type.value_type)]
            else:
                raise InternalError(f"list('{value_type}') not supported", node)
        elif name in ['min', 'max', 'sum']:
            value_type = self.visit(node.args[0])

            if isinstance(value_type, list):
                return value_type[0]
            else:
                return value_type
        elif name == 'abs':
            return self.visit(node.args[0])
        elif name == 'range':
            # ???
            return self.visit(node.args[0])
        elif name == 'enumerate':
            # ???
            return [('i64', self.visit(node.args[0]))]
        elif name == 'zip':
            # ???
            return [self.visit(node.args[0])]
        elif name == 'slice':
            # ???
            return [self.visit(node.args[0])]
        elif name == 'reversed':
            # ???
            return [self.visit(node.args[0])]
        elif name == 'input':
            return 'string'
        else:
            raise InternalError(f"builtin '{name}' not supported", node)

    def visit_call_method_list(self, name, node):
        raise InternalError(f"dict method '{name}' not supported", node)

    def visit_call_method_dict(self, name, value_type, node):
        if name in ['get', 'pop']:
            return value_type.value_type
        elif name == 'keys':
            return [value_type.key_type]
        elif name == 'values':
            return [value_type.value_type]
        else:
            raise InternalError(f"dict method '{name}' not supported", node)

    def visit_call_method_string(self, name, node):
        if name == 'to_utf8':
            return 'bytes'
        elif name == 'join':
            return 'string'
        else:
            raise InternalError(f"string method '{name}' not supported", node)

    def visit_call_method_class(self, name, value_type, node):
        definitions = self.context.get_class(value_type)

        if name in definitions.methods:
            method = definitions.methods[name][0]
            method = self.context.get_class(value_type).methods[name][0]
            returns = method.returns
        else:
            raise CompileError(
                f"class '{value_type}' has no method '{name}'",
                node)

        if isinstance(returns, dict):
            returns = Dict(list(returns.keys())[0], list(returns.values())[0])

        return returns

    def visit_call_method_trait(self, name, value_type, node):
        method = self.context.get_trait(value_type).methods[name][0]
        returns = method.returns

        if isinstance(returns, dict):
            returns = Dict(list(returns.keys())[0], list(returns.values())[0])

        return returns

    def visit_call_method(self, node):
        name = node.func.attr
        value_type = self.visit(node.func.value)

        if isinstance(value_type, list):
            return self.visit_call_method_list(name, node.func)
        elif isinstance(value_type, Dict):
            return self.visit_call_method_dict(name, value_type, node.func)
        elif value_type == 'string':
            return self.visit_call_method_string(name, node.func)
        elif value_type == 'bytes':
            raise CompileError('bytes method not implemented', node.func)
        elif self.context.is_class_defined(value_type):
            return self.visit_call_method_class(name, value_type, node.func)
        elif self.context.is_trait_defined(value_type):
            return self.visit_call_method_trait(name, value_type, node)
        else:
            raise CompileError("None has no methods", node.func)

    def visit_Call(self, node):
        if isinstance(node.func, ast.Name):
            name = node.func.id

            if self.context.is_function_defined(node.func.id):
                return self.visit_call_function(name, node)
            elif self.context.is_class_defined(name):
                return self.visit_call_class(name, node)
            elif self.context.is_enum_defined(name):
                return self.visit_call_enum(name, node)
            elif node.func.id in BUILTIN_CALLS:
                return self.visit_call_builtin(name, node)
            else:
                if is_snake_case(name):
                    raise CompileError(f"undefined function '{name}'", node)
                else:
                    raise CompileError(f"undefined class '{name}'", node)
        elif isinstance(node.func, ast.Attribute):
            return self.visit_call_method(node)
        elif isinstance(node.func, ast.Lambda):
            raise CompileError('lambda functions are not supported', node.func)
        else:
            raise CompileError("not callable", node.func)

class UnpackVisitor(ast.NodeVisitor):

    def visit_Name(self, node):
        return (node.id, node)

    def visit_Tuple(self, node):
        return (tuple([self.visit(elem) for elem in node.elts]), node)

class IntegerLiteralVisitor(ast.NodeVisitor):

    def visit_BinOp(self, node):
        return self.visit(node.left) and self.visit(node.right)

    def visit_UnaryOp(self, node):
        return self.visit(node.operand)

    def visit_Constant(self, node):
        if isinstance(node.value, bool):
            return False
        else:
            return isinstance(node.value, int)

    def generic_visit(self, node):
        return False

def is_integer_literal(node):
    return IntegerLiteralVisitor().visit(node)

def is_float_literal(node):
    if isinstance(node, ast.Constant):
        return isinstance(node.value, float)

    return False

class MakeIntegerLiteralVisitor(ast.NodeVisitor):

    def __init__(self, type_name):
        self.type_name = type_name
        self.factor = 1

    def visit_BinOp(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        op_class = type(node.op)

        return format_binop(left, right, op_class)

    def visit_UnaryOp(self, node):
        if isinstance(node.op, ast.USub):
            factor = -1
        else:
            factor = 1

        self.factor *= factor

        try:
            value = self.visit(node.operand)
        except CompileError as e:
            e.lineno = node.lineno
            e.offset = node.col_offset

            raise e

        self.factor *= factor

        return value

    def visit_Constant(self, node):
        value = node.value * self.factor

        if self.type_name == 'u8':
            if 0 <= value <= 0xff:
                return str(value)
        elif self.type_name == 'u16':
            if 0 <= value <= 0xffff:
                return str(value)
        elif self.type_name == 'u32':
            if 0 <= value <= 0xffffffff:
                return str(value)
        elif self.type_name == 'u64':
            if 0 <= value <= 0xffffffffffffffff:
                return f'{value}ull'
        elif self.type_name == 'i8':
            if -0x80 <= value <= 0x7f:
                return str(value)
        elif self.type_name == 'i16':
            if -0x8000 <= value <= 0x7fff:
                return str(value)
        elif self.type_name == 'i32':
            if -0x80000000 <= value <= 0x7fffffff:
                return str(value)
        elif self.type_name == 'i64':
            if -0x8000000000000000 <= value <= 0x7fffffffffffffff:
                return str(value)
        elif self.type_name is None:
            raise CompileError("integers can't be None", node)

        else:
            mys_type = format_mys_type(self.type_name)

            raise CompileError(f"can't convert integer to '{mys_type}'", node)

        raise CompileError(
            f"integer literal out of range for '{self.type_name}'",
            node)

def make_integer_literal(type_name, node):
    return MakeIntegerLiteralVisitor(type_name).visit(node)

def make_float_literal(type_name, node):
    if type_name == 'f32':
        return str(node.value)
    elif type_name == 'f64':
        return str(node.value)
    elif type_name is None:
        raise CompileError("floats can't be None", node)
    else:
        mys_type = format_mys_type(type_name)

        raise CompileError(f"can't convert float to '{mys_type}'", node)

    raise CompileError(f"float literal out of range for '{type_name}'", node)

BUILTIN_CALLS = set(
    list(INTEGER_TYPES) + [
        'print',
        'char',
        'list',
        'input',
        'assert_eq',
        'TypeError',
        'ValueError',
        'GeneralError',
        'SystemExitError',
        'str',
        'min',
        'max',
        'len',
        'abs',
        'f32',
        'f64',
        'enumerate',
        'range',
        'reversed',
        'slice',
        'sum',
        'zip'
    ])

class Range:

    def __init__(self, target, target_node, begin, end, step, mys_type):
        self.target = target
        self.target_node = target_node
        self.begin = begin
        self.end = end
        self.step = step
        self.mys_type = mys_type

class Enumerate:

    def __init__(self, target, target_node, initial, mys_type):
        self.target = target
        self.target_node = target_node
        self.initial = initial
        self.mys_type = mys_type

class Slice:

    def __init__(self, begin, end, step):
        self.begin = begin
        self.end = end
        self.step = step

class OpenSlice:

    def __init__(self, begin):
        self.begin = begin

class Reversed:
    pass

class Zip:

    def __init__(self, children):
        self.children = children

class Data:

    def __init__(self, target, target_node, value, mys_type):
        self.target = target
        self.target_node = target_node
        self.value = value
        self.mys_type = mys_type

class Context:

    def __init__(self, module_levels=''):
        self.name = '.'.join(module_levels)
        self._stack = [[]]
        self._variables = {}
        self._classes = {}
        self._traits = {}
        self._functions = {}
        self._enums = {}
        self.return_mys_type = None
        self.mys_type = None
        self.unique_count = 0
        self.constants = {}

    def unique_number(self):
        self.unique_count += 1

        return self.unique_count

    def unique(self, name):
        return f'__{name}_{self.unique_number()}'

    def define_variable(self, name, info, node):
        if self.is_variable_defined(name):
            raise CompileError(f"redefining variable '{name}'", node)

        if self.is_function_defined(name):
            raise CompileError(f"'{name}' is a function", node)

        if not is_snake_case(name):
            raise CompileError("local variable names must be snake case", node)

        self._variables[name] = info
        self._stack[-1].append(name)

    def define_global_variable(self, name, info, node):
        if self.is_variable_defined(name):
            raise CompileError(f"redefining variable '{name}'", node)

        self._variables[name] = info
        self._stack[-1].append(name)

    def is_variable_defined(self, name):
        if not isinstance(name, str):
            return False

        return name in self._variables

    def get_variable_type(self, name):
        return self._variables[name]

    def define_class(self, name, definitions):
        self._classes[name] = definitions

    def is_class_defined(self, name):
        if not isinstance(name, str):
            return False

        return name in self._classes

    def get_class(self, name):
        return self._classes[name]

    def define_trait(self, name, definitions):
        self._traits[name] = definitions

    def is_trait_defined(self, name):
        if not isinstance(name, str):
            return False

        return name in self._traits

    def get_trait(self, name):
        return self._traits[name]

    def define_function(self, name, definitions):
        self._functions[name] = definitions

    def is_function_defined(self, name):
        if not isinstance(name, str):
            return False

        return name in self._functions

    def get_functions(self, name):
        return self._functions[name]

    def define_enum(self, name, type_):
        self._enums[name] = type_

    def is_enum_defined(self, name):
        if not isinstance(name, str):
            return False

        return name in self._enums

    def get_enum_type(self, name):
        return self._enums[name]

    def is_class_or_trait_defined(self, name):
        if self.is_class_defined(name):
            return True
        elif self.is_trait_defined(name):
            return True

        return False

    def is_type_defined(self, mys_type):
        if isinstance(mys_type, tuple):
            for item_mys_type in mys_type:
                if not self.is_type_defined(item_mys_type):
                    return False
        elif isinstance(mys_type, list):
            for item_mys_type in mys_type:
                if not self.is_type_defined(item_mys_type):
                    return False
        elif isinstance(mys_type, dict):
            key_mys_type, value_mys_type = split_dict_mys_type(mys_type)

            if not self.is_type_defined(key_mys_type):
                return False

            if not self.is_type_defined(value_mys_type):
                return False
        elif self.is_class_or_trait_defined(mys_type):
            return True
        elif self.is_enum_defined(mys_type):
            return True
        elif is_primitive_type(mys_type):
            return True
        elif mys_type == 'string':
            return True
        elif mys_type == 'bytes':
            return True
        else:
            return False

        return True

    def push(self):
        self._stack.append([])

    def pop(self):
        result = {}

        for name in self._stack[-1]:
            result[name] = self._variables.pop(name)

        self._stack.pop()

        return result

def make_relative_import_absolute(module_levels, module, node):
    prefix = '.'.join(module_levels[0:-node.level])

    if not prefix:
        raise CompileError('relative import is outside package', node)

    if module is None:
        module = prefix
    else:
        module = f'{prefix}.{module}'

    return module

def is_relative_import(node):
    return node.level > 0

def get_import_from_info(node, module_levels):
    module = node.module

    if is_relative_import(node):
        module = make_relative_import_absolute(module_levels, module, node)

    if '.' not in module:
        module += '.lib'

    if len(node.names) != 1:
        raise CompileError(f'only one import is allowed, found {len(node.names)}',
                           node)

    name = node.names[0]

    if name.asname:
        asname = name.asname
    else:
        asname = name.name

    return module, name, asname

def return_type_string(node, source_lines, context, filename):
    if node is None:
        return 'void'
    else:
        return CppTypeVisitor(source_lines, context, filename).visit(node)

def params_string(function_name,
                  args,
                  source_lines,
                  context,
                  filename=''):
    params = ', '.join([
        ParamVisitor(source_lines, context, filename).visit(arg)
        for arg in args
    ])

    if not params:
        params = 'void'

    return params

def indent_lines(lines):
    return ['    ' + line for line in lines if line]

def indent(string):
    return '\n'.join(indent_lines(string.splitlines()))

def dedent(string):
    return '\n'.join([line[4:] for line in string.splitlines() if line])

def is_ascii(value):
    return len(value) == len(value.encode('utf-8'))

def handle_string(value):
    if value.startswith('mys-embedded-c++'):
        return '\n'.join([
            '/* mys-embedded-c++ start */\n',
            textwrap.dedent(value[16:]).strip(),
            '\n/* mys-embedded-c++ stop */'])
    elif is_ascii(value):
        value = value.encode("unicode_escape").decode('utf-8')
        value = value.replace('"', '\\"')

        return f'String("{value}")'
    else:
        values = []

        for ch in value:
            values.append(f'Char({ord(ch)})')

        value = ', '.join(values)

        return f'String({{{value}}})'

def is_string(node, source_lines):
    line = source_lines[node.lineno - 1]

    return line[node.col_offset] != "'"

def is_docstring(node, source_lines):
    if not isinstance(node, ast.Constant):
        return False

    if not isinstance(node.value, str):
        return False

    if not is_string(node, source_lines):
        return False

    return not node.value.startswith('mys-embedded-c++')

def has_docstring(node, source_lines):
    first = node.body[0]

    if isinstance(first, ast.Expr):
        return is_docstring(first.value, source_lines)

    return False

def find_item_with_length(items):
    for item in items:
        if isinstance(item, (Slice, OpenSlice, Reversed)):
            pass
        elif isinstance(item, Zip):
            return find_item_with_length(item.children[0])
        else:
            return item

class BaseVisitor(ast.NodeVisitor):

    def __init__(self, source_lines, context, filename):
        self.source_lines = source_lines
        self.context = context
        self.filename = filename
        self.constants = []

    def unique_number(self):
        return self.context.unique_number()

    def unique(self, name):
        return self.context.unique(name)

    def return_type_string(self, node):
        return return_type_string(node,
                                  self.source_lines,
                                  self.context,
                                  self.filename)

    def mys_to_cpp_type(self, mys_type):
        return mys_to_cpp_type(mys_type, self.context)

    def visit_Name(self, node):
        name = node.id

        if name == '__unique_id__':
            self.context.mys_type = 'i64'

            return str(self.unique_number())
        elif name == '__line__':
            self.context.mys_type = 'u64'

            return str(node.lineno)
        elif name == '__name__':
            self.context.mys_type = 'string'

            return handle_string(self.context.name)
        elif name == '__file__':
            self.context.mys_type = 'string'

            return handle_string(self.filename)
        else:
            if not self.context.is_variable_defined(name):
                raise CompileError(f"undefined variable '{name}'", node)

            self.context.mys_type = self.context.get_variable_type(name)

            if name == 'self':
                return 'shared_from_this()'
            else:
                return make_name(name)

    def find_print_kwargs(self, node):
        end = ' << std::endl'
        flush = None

        for keyword in node.keywords:
            if keyword.arg == 'end':
                value = self.visit(keyword.value)
                end = f' << PrintString({value})'
            elif keyword.arg == 'flush':
                flush = self.visit(keyword.value)
            else:
                raise CompileError(
                    f"invalid keyword argument '{keyword.arg}' to print(), only "
                    "'end' and 'flush' are allowed",
                    node)

        return end, flush

    def handle_print(self, node):
        args = []

        for arg in node.args:
            if is_integer_literal(arg):
                args.append((make_integer_literal('i64', arg), 'i64'))
                self.context.mys_type = 'i64'
            else:
                args.append((self.visit(arg), self.context.mys_type))

                if self.context.mys_type is None:
                    raise CompileError("None can't be printed", arg)

        end, flush = self.find_print_kwargs(node)
        code = 'std::cout'

        if len(args) == 1:
            code += f' << {format_print_arg(args[0], self.context)}'
        elif len(args) != 0:
            first = format_print_arg(args[0], self.context)
            args = ' << " " << '.join([format_print_arg(arg, self.context)
                                       for arg in args[1:]])
            code += f' << {first} << " " << {args}'

        code += end

        if flush:
            code += ';\n'
            code += f'if ({flush}) {{\n'
            code += f'    std::cout << std::flush;\n'
            code += '}'

        self.context.mys_type = None

        return code

    def visit_values_of_same_type(self, value_nodes):
        items = []
        mys_type = None

        for value_node in value_nodes:
            if is_integer_literal(value_node):
                items.append(('integer', value_node))
            elif is_float_literal(value_node):
                items.append(('float', value_node))
            else:
                value = self.visit(value_node)
                items.append((self.context.mys_type, value))

                if mys_type is None:
                    mys_type = self.context.mys_type

        if mys_type is None:
            if items[0][0] == 'integer':
                mys_type = 'i64'
            else:
                mys_type = 'f64'

        values = []

        for i, (item_mys_type, value_node) in enumerate(items):
            if item_mys_type in ['integer', 'float']:
                value = self.visit_value_check_type(value_node, mys_type)
            else:
                raise_if_wrong_types(item_mys_type,
                                     mys_type,
                                     value_nodes[i],
                                     self.context)
                value = value_node

            values.append(value)

        self.context.mys_type = mys_type

        return values

    def handle_min_max(self, node, name):
        nargs = len(node.args)

        if nargs == 0:
            raise CompileError("expected at least one parameter", node)
        elif nargs == 1:
            values = [self.visit(node.args[0])]

            if not isinstance(self.context.mys_type, list):
                raise CompileError('expected a list', node.args[0])

            self.context.mys_type = self.context.mys_type[0]
        else:
            values = self.visit_values_of_same_type(node.args)

        items = ', '.join(values)

        return f'{name}({items})'

    def handle_sum(self, node):
        nargs = len(node.args)

        if nargs != 1:
            raise CompileError("expected one parameter", node)

        values = self.visit(node.args[0])
        if not isinstance(self.context.mys_type, list):
            raise CompileError('expected a list', node.args[0])

        self.context.mys_type = self.context.mys_type[0]

        return f'sum({values})'

    def handle_len(self, node):
        raise_if_wrong_number_of_parameters(len(node.args), 1, node)
        value = self.visit(node.args[0])
        mys_type = self.context.mys_type
        self.context.mys_type = 'u64'

        if mys_type == 'string':
            if value.startswith('"'):
                return f'strlen({value})'
            else:
                return f'{value}.__len__()'
        elif mys_type == 'bytes':
            return f'{value}.__len__()'
        else:
            return f'shared_ptr_not_none({value})->__len__()'

    def handle_str(self, node):
        raise_if_wrong_number_of_parameters(len(node.args), 1, node)
        value = self.visit(node.args[0])
        mys_type = self.context.mys_type
        self.context.mys_type = 'string'

        return format_str(value, mys_type)

    def handle_list(self, node):
        raise_if_wrong_number_of_parameters(len(node.args), 1, node)
        value = self.visit(node.args[0])
        mys_type = self.context.mys_type

        if isinstance(mys_type, dict):
            key_mys_type, value_mys_type = list(mys_type.items())[0]
            self.context.mys_type = [(key_mys_type, value_mys_type)]
            key_cpp_type = self.mys_to_cpp_type(key_mys_type)
            value_cpp_type = self.mys_to_cpp_type(value_mys_type)

            return (f'create_list_from_dict<{key_cpp_type}, {value_cpp_type}>('
                    f'{value})')
        else:
            raise CompileError("not supported", node)

    def handle_char(self, node):
        raise_if_wrong_number_of_parameters(len(node.args), 1, node)
        value = self.visit_value_check_type(node.args[0], 'i32')
        self.context.mys_type = 'char'

        return f'Char({value})'

    def handle_input(self, node):
        raise_if_wrong_number_of_parameters(len(node.args), 1, node)
        prompt = self.visit_value_check_type(node.args[0], 'string')
        self.context.mys_type = 'string'

        return f'input({prompt})'

    def visit_cpp_type(self, node):
        return CppTypeVisitor(self.source_lines,
                              self.context,
                              self.filename).visit(node)

    def visit_call_params_keywords(self, function, node):
        keyword_args = {}
        params_names = [name for (name, _), _ in function.args]

        if node.keywords:
            for keyword in node.keywords:
                if keyword.arg not in params_names:
                    raise CompileError(f"invalid parameter '{keyword.arg}'",
                                       keyword)

                if keyword.arg in keyword_args:
                    raise CompileError(
                        f"parameter '{keyword.arg}' given more than once",
                        keyword)

                keyword_args[keyword.arg] = keyword.value

        return keyword_args

    def visit_call_params(self, function, node):
        min_args = len([default for _, default in function.args if default is None])
        raise_if_wrong_number_of_parameters(len(node.args) + len(node.keywords),
                                            len(function.args),
                                            node.func,
                                            min_args)

        keyword_args = self.visit_call_params_keywords(function, node)
        call_args = node.args[:]

        for ((param_name, _), default) in function.args[len(call_args):]:
            value = keyword_args.get(param_name)

            if value is None:
                value = default

            call_args.append(value)

        return [
            self.visit_value_check_type(arg, mys_type)
            for ((_, mys_type), _), arg in zip(function.args, call_args)
        ]

    def visit_call_function(self, name, node):
        functions = self.context.get_functions(name)

        if len(functions) != 1:
            raise CompileError("overloaded functions are not yet supported",
                               node.func)

        function = functions[0]
        args = self.visit_call_params(function, node)
        self.context.mys_type = function.returns

        return f'{name}({", ".join(args)})'

    def visit_call_class(self, mys_type, node):
        cls = self.context.get_class(mys_type)
        args = []

        if '__init__' in cls.methods:
            function = cls.methods['__init__'][0]
            args = self.visit_call_params(function, node)
        else:
            # ToDo: This __init__ method should be added when
            # extracting definitions. The code below should be
            # removed.
            public_members = [
                member
                for member in cls.members.values()
                if not member.name.startswith('_')
            ]
            raise_if_wrong_number_of_parameters(len(node.args),
                                                len(public_members),
                                                node.func)

            for member, arg in zip(public_members, node.args):
                args.append(self.visit_value_check_type(arg, member.type))

        args = ', '.join(args)
        self.context.mys_type = mys_type

        return make_shared(mys_type, args)

    def visit_call_enum(self, mys_type, node):
        raise_if_wrong_number_of_parameters(len(node.args), 1, node)
        cpp_type = self.context.get_enum_type(mys_type)
        value = self.visit_value_check_type(node.args[0], cpp_type)
        self.context.mys_type = mys_type

        return f'enum_{mys_type}_from_value({value})'

    def visit_call_builtin(self, name, node):
        if name == 'print':
            code = self.handle_print(node)
        elif name in ['min', 'max']:
            code = self.handle_min_max(node, name)
        elif name == 'sum':
            code = self.handle_sum(node)
        elif name == 'len':
            code = self.handle_len(node)
        elif name == 'str':
            code = self.handle_str(node)
        elif name == 'list':
            code = self.handle_list(node)
        elif name == 'char':
            code = self.handle_char(node)
        elif name in FOR_LOOP_FUNCS:
            raise CompileError(f"function can only be used in for-loops", node)
        elif name == 'input':
            code = self.handle_input(node)
        else:
            args = []

            for arg in node.args:
                if is_integer_literal(arg):
                    args.append((make_integer_literal('i64', arg), 'i64'))
                    self.context.mys_type = 'i64'
                else:
                    args.append((self.visit(arg), self.context.mys_type))

            args = ', '.join([value for value, _ in args])

            if name in INTEGER_TYPES:
                if self.context.mys_type == 'string':
                    args += '.__int__()'

                mys_type = name
            elif name in ['f32', 'f64']:
                mys_type = name
            elif name == 'abs':
                mys_type = self.context.mys_type
            else:
                mys_type = None

            code = f'{name}({args})'
            self.context.mys_type = mys_type

        return code

    def visit_call_method_list(self, name, args, node):
        if name == 'append':
            raise_if_wrong_number_of_parameters(len(args), 1, node)
            self.context.mys_type = None
        elif name in ['sort', 'reverse']:
            raise_if_wrong_number_of_parameters(len(args), 0, node)
            self.context.mys_type = None
        else:
            raise CompileError('list method not implemented', node)

    def visit_call_method_dict(self, name, mys_type, args, node):
        if name == 'keys':
            raise_if_wrong_number_of_parameters(len(args), 0, node)
            self.context.mys_type = list(mys_type.keys())
        elif name == 'values':
            raise_if_wrong_number_of_parameters(len(args), 0, node)
            self.context.mys_type = list(mys_type.values())
        elif name == 'get':
            raise_if_wrong_number_of_parameters(len(args), 2, node)
            self.context.mys_type = list(mys_type.values())[0]
        elif name == 'pop':
            raise_if_wrong_number_of_parameters(len(args), 2, node)
            self.context.mys_type = list(mys_type.values())[0]
        elif name == 'clear':
            raise_if_wrong_number_of_parameters(len(args), 0, node)
            self.context.mys_type = None
        elif name == 'update':
            raise_if_wrong_number_of_parameters(len(args), 1, node)
            self.context.mys_type = None
        else:
            raise CompileError('dict method not implemented', node)

    def visit_call_method_string(self, name, args, node):
        if name == 'to_utf8':
            raise_if_wrong_number_of_parameters(len(args), 0, node)
            self.context.mys_type = 'bytes'
        elif name in ['upper', 'lower']:
            raise_if_wrong_number_of_parameters(len(args), 0, node)
            self.context.mys_type = None
        elif name == 'starts_with':
            raise_if_wrong_number_of_parameters(len(args), 1, node)
            self.context.mys_type = 'bool'
        elif name == 'join':
            raise_if_wrong_number_of_parameters(len(args), 1, node)
            self.context.mys_type = 'string'
        else:
            raise CompileError('string method not implemented', node)

        return '.'

    def visit_call_method_class(self, name, mys_type, value, node):
        definitions = self.context.get_class(mys_type)

        if name in definitions.methods:
            method = definitions.methods[name][0]
            args = self.visit_call_params(method, node)
            self.context.mys_type = method.returns
        else:
            raise CompileError(
                f"class '{mys_type}' has no method '{name}'",
                node)

        if value == 'shared_from_this()':
            value = 'this'
        elif name.startswith('_'):
            raise CompileError(f"class '{mys_type}' method '{name}' is private",
                               node)

        return value, args

    def visit_call_method_trait(self, name, mys_type, node):
        definitions = self.context.get_trait(mys_type)

        if name in definitions.methods:
            method = definitions.methods[name][0]
            args = self.visit_call_params(method, node)
            self.context.mys_type = method.returns
        else:
            raise CompileError(
                f"trait '{mys_type}' has no function '{name}'",
                node)

        return args

    def visit_call_method(self, node):
        name = node.func.attr
        args = []

        for arg in node.args:
            if is_integer_literal(arg):
                args.append(make_integer_literal('i64', arg))
                self.context.mys_type = 'i64'
            else:
                args.append(self.visit(arg))

        value = self.visit(node.func.value)
        mys_type = self.context.mys_type
        op = '->'

        if isinstance(mys_type, list):
            self.visit_call_method_list(name, args, node.func)
        elif isinstance(mys_type, dict):
            self.visit_call_method_dict(name, mys_type, args, node.func)
        elif mys_type == 'string':
            op = self.visit_call_method_string(name, args, node.func)
        elif mys_type == 'bytes':
            raise CompileError('bytes method not implemented', node.func)
        elif self.context.is_class_defined(mys_type):
            value, args = self.visit_call_method_class(name, mys_type, value, node)
        elif self.context.is_trait_defined(mys_type):
            args = self.visit_call_method_trait(name, mys_type, node)
        else:
            mys_type = format_mys_type(mys_type)

            raise CompileError(f"'{mys_type}' not defined", node.func)

        value = wrap_not_none(value, mys_type)
        args = ', '.join(args)

        return f'{value}{op}{name}({args})'

    def visit_Call(self, node):
        if isinstance(node.func, ast.Name):
            name = node.func.id

            if self.context.is_function_defined(node.func.id):
                return self.visit_call_function(name, node)
            elif self.context.is_class_defined(name):
                return self.visit_call_class(name, node)
            elif self.context.is_enum_defined(name):
                return self.visit_call_enum(name, node)
            elif node.func.id in BUILTIN_CALLS:
                return self.visit_call_builtin(name, node)
            else:
                if is_snake_case(name):
                    raise CompileError(f"undefined function '{name}'", node)
                else:
                    raise CompileError(f"undefined class '{name}'", node)
        elif isinstance(node.func, ast.Attribute):
            return self.visit_call_method(node)
        elif isinstance(node.func, ast.Lambda):
            raise CompileError('lambda functions are not supported', node.func)
        else:
            raise CompileError("not callable", node.func)

    def visit_Constant(self, node):
        if isinstance(node.value, str):
            if is_string(node, self.source_lines):
                self.context.mys_type = 'string'

                return handle_string(node.value)
            else:
                self.context.mys_type = 'char'

                if node.value:
                    try:
                        value = ord(node.value)
                    except TypeError:
                        raise CompileError("bad character literal", node)
                else:
                    value = -1

                return f"Char({value})"
        elif isinstance(node.value, bool):
            self.context.mys_type = 'bool'

            return f'Bool({str(node.value).lower()})'
        elif isinstance(node.value, float):
            self.context.mys_type = 'f64'

            return str(node.value)
        elif isinstance(node.value, int):
            self.context.mys_type = 'i64'

            return str(node.value)
        elif node.value is None:
            self.context.mys_type = None

            return 'nullptr'
        elif isinstance(node.value, bytes):
            self.context.mys_type = 'bytes'
            values = ', '.join([str(v) for v in node.value])

            return f'Bytes({{{values}}})'
        else:
            raise InternalError("constant node", node)

    def visit_Expr(self, node):
        return self.visit(node.value) + ';'

    def visit_BinOp(self, node):
        left_value_type = ValueTypeVisitor(self.source_lines,
                                           self.context).visit(node.left)
        right_value_type = ValueTypeVisitor(self.source_lines,
                                            self.context).visit(node.right)
        left_value_type, right_value_type = intersection_of(
            left_value_type,
            right_value_type,
            node)
        left_value_type = reduce_type(left_value_type)
        right_value_type = reduce_type(right_value_type)
        left = self.visit_value_check_type(node.left, left_value_type)
        right = self.visit_value_check_type(node.right, right_value_type)

        return format_binop(left, right, type(node.op))

    def visit_UnaryOp(self, node):
        operand = self.visit(node.operand)
        op = OPERATORS[type(node.op)]

        if isinstance(node.op, ast.Not):
            raise_if_not_bool(self.context.mys_type, node.operand, self.context)
        elif isinstance(node.op, (ast.UAdd, ast.USub)):
            if self.context.mys_type not in NUMBER_TYPES:
                raise CompileError(f"unary '{op}' can only operate on numbers",
                                   node)

        return f'{op}({operand})'

    def visit_AugAssign(self, node):
        lval = self.visit(node.target)
        lval = wrap_not_none(lval, self.context.mys_type)
        op = OPERATORS[type(node.op)]
        rval = self.visit(node.value)

        return f'{lval} {op}= {rval};'

    def visit_Tuple(self, node):
        items = []
        mys_types = []

        for item in node.elts:
            items.append(self.visit(item))
            mys_types.append(self.context.mys_type)

        self.context.mys_type = tuple(mys_types)
        cpp_type = self.mys_to_cpp_type(self.context.mys_type)
        items = ', '.join(items)

        return make_shared(cpp_type[6:], items)

    def visit_List(self, node):
        items = []
        item_mys_type = None

        for item in node.elts:
            items.append(self.visit(item))

            if item_mys_type is None:
                item_mys_type = self.context.mys_type

        if item_mys_type is None:
            self.context.mys_type = None
        else:
            self.context.mys_type = [item_mys_type]

        value = ", ".join(items)
        item_cpp_type = self.mys_to_cpp_type(item_mys_type)

        return make_shared_list(item_cpp_type, value)

    def visit_Dict(self, node):
        key_mys_type = None
        keys = []

        for key_node in node.keys:
            keys.append(self.visit(key_node))

            if key_mys_type is not None:
                raise_if_wrong_visited_type(self.context, key_mys_type, key_node)

            if key_mys_type is None:
                key_mys_type = self.context.mys_type

        value_mys_type = None
        values = []

        for value_node in node.values:
            value = self.visit(value_node)
            values.append(value)

            if value_mys_type is not None:
                raise_if_wrong_visited_type(self.context, value_mys_type, value_node)

            if value_mys_type is None:
                value_mys_type = self.context.mys_type

        self.context.mys_type = {key_mys_type: value_mys_type}

        key_cpp_type = self.mys_to_cpp_type(key_mys_type)
        value_cpp_type = self.mys_to_cpp_type(value_mys_type)
        items = ', '.join([f'{{{key}, {value}}}' for key, value in zip(keys, values)])

        return make_shared_dict(key_cpp_type, value_cpp_type, items)

    def visit_for_list(self, node, value, mys_type):
        item_mys_type = mys_type[0]
        items = self.unique('items')
        i = self.unique('i')
        target_type = mys_type_to_target_cpp_type(item_mys_type)

        if isinstance(node.target, ast.Tuple):
            target = []

            for j, item in enumerate(node.target.elts):
                name = item.id

                if not name.startswith('_'):
                    self.context.define_variable(name, item_mys_type[j], item)
                    target.append(
                        f'    {target_type} {make_name(name)} = '
                        f'std::get<{j}>('
                        f'shared_ptr_not_none({items}->get({i}))->m_tuple);')

            target = '\n'.join(target)
        else:
            name = node.target.id

            if not name.startswith('_'):
                self.context.define_variable(name, item_mys_type, node.target)

            target = f'    {target_type} {name} = {items}->get({i});'

        body = indent('\n'.join([
            self.visit(item)
            for item in node.body
        ]))

        return [
            f'const auto& {items} = {value};',
            f'for (auto {i} = 0; {i} < {items}->__len__(); {i}++) {{',
            target,
            body,
            '}'
        ]

    def visit_for_dict(self, node, dvalue, mys_type):
        key_mys_type, value_mys_type = split_dict_mys_type(mys_type)
        items = self.unique('items')
        i = self.unique('i')

        if (not isinstance(node.target, ast.Tuple)
            or len(node.target.elts) != 2):
            raise CompileError(
                "iteration over dict must be done on key/value tuple",
                node.target)

        key = node.target.elts[0]
        key_name = key.id
        self.context.define_variable(key_name, key_mys_type, key)

        value = node.target.elts[1]
        value_name = value.id
        self.context.define_variable(value_name, value_mys_type, value)

        body = indent('\n'.join([
            self.visit(item)
            for item in node.body
        ]))

        return [
            f'const auto& {items} = {dvalue};',
            f'for (const auto& {i} : {items}->m_map) {{',
            f'    const auto& {make_name(key_name)} = {i}.first;',
            f'    const auto& {make_name(value_name)} = {i}.second;',
            body,
            '}'
        ]

    def visit_for_string(self, node, value, mys_type):
        items = self.unique('items')
        i = self.unique('i')
        name = node.target.id

        if not name.startswith('_'):
            self.context.define_variable(name, 'char', node.target)

        target = f'    auto {name} = {items}.get({i});'
        body = indent('\n'.join([
            self.visit(item)
            for item in node.body
        ]))

        return [
            f'const auto& {items} = {value};',
            f'for (auto {i} = 0; {i} < {items}.__len__(); {i}++) {{',
            target,
            body,
            '}'
        ]

    def visit_iter_parameter(self, node, expected_mys_type=None):
        value = self.visit(node)
        mys_type = self.context.mys_type

        if mys_type not in INTEGER_TYPES:
            mys_type = format_mys_type(mys_type)

            raise CompileError(
                f"parameter type must be an integer, not '{mys_type}'",
                node)

        if expected_mys_type is not None and mys_type != expected_mys_type:
            raise_types_differs(mys_type, expected_mys_type, node)

        return value, mys_type

    def visit_for_call_range(self,
                             items,
                             target_value,
                             target_node,
                             iter_node,
                             nargs):
        if nargs == 1:
            begin = 0
            end, mys_type = self.visit_iter_parameter(iter_node.args[0])
            step = 1
        elif nargs == 2:
            begin, mys_type = self.visit_iter_parameter(iter_node.args[0])
            end, _ = self.visit_iter_parameter(iter_node.args[1], mys_type)
            step = 1
        elif nargs == 3:
            begin, mys_type = self.visit_iter_parameter(iter_node.args[0])
            end, _ = self.visit_iter_parameter(iter_node.args[1], mys_type)
            step, _ = self.visit_iter_parameter(iter_node.args[2], mys_type)
        else:
            raise CompileError(f"expected 1 to 3 parameters, got {nargs}",
                               iter_node)

        items.append(Range(target_value, target_node, begin, end, step, mys_type))

    def visit_enumerate_parameter(self, node):
        value = self.visit(node)
        mys_type = self.context.mys_type

        if mys_type not in INTEGER_TYPES:
            raise CompileError(f"initial value must be an integer, not '{mys_type}'",
                               node)

        return value, mys_type

    def visit_for_call_enumerate(self,
                                 items,
                                 target_value,
                                 target_node,
                                 iter_node,
                                 nargs):
        actual_count = len(target_value)

        if actual_count != 2:
            raise CompileError(
                f"can only unpack enumerate into two variables, got {actual_count}",
                target_node)

        if nargs == 1:
            self.visit_for_call(items,
                                target_value[1],
                                iter_node.args[0])
            items.append(Enumerate(target_value[0][0], target_node, 0, 'i64'))
        elif nargs == 2:
            self.visit_for_call(items,
                                target_value[1],
                                iter_node.args[0])
            initial, mys_type = self.visit_enumerate_parameter(
                iter_node.args[1])
            items.append(Enumerate(target_value[0][0],
                                   target_node,
                                   initial,
                                   mys_type))
        else:
            raise CompileError(f"expected 1 or 2 parameters, got {nargs}",
                               iter_node)

    def visit_for_call_slice(self, items, target, iter_node, nargs):
        self.visit_for_call(items, target, iter_node.args[0]),

        if nargs == 2:
            end, _ = self.visit_iter_parameter(iter_node.args[1])
            items.append(OpenSlice(end))
        elif nargs == 3:
            begin, mys_type = self.visit_iter_parameter(iter_node.args[1])
            end, _ = self.visit_iter_parameter(iter_node.args[2], mys_type)
            items.append(Slice(begin, end, 1))
        elif nargs == 4:
            begin, mys_type = self.visit_iter_parameter(iter_node.args[1])
            end, _ = self.visit_iter_parameter(iter_node.args[2], mys_type)
            step, _ = self.visit_iter_parameter(iter_node.args[3], mys_type)
            items.append(Slice(begin, end, step))
        else:
            raise CompileError(f"expected 2 to 4 parameters, got {nargs}",
                               iter_node)

    def visit_for_call_zip(self, items, target_value, target_node, iter_node, nargs):
        if len(target_value) != nargs:
            raise CompileError(
                f"can't unpack {nargs} values into {len(target_value)}",
                target_node)

        children = []

        for value, arg in zip(target_value, iter_node.args):
            items_2 = []
            self.visit_for_call(items_2, value, arg)
            children.append(items_2)

        items.append(Zip(children))

    def visit_for_call_reversed(self, items, target, iter_node, nargs):
        raise_if_wrong_number_of_parameters(nargs, 1, iter_node)
        self.visit_for_call(items, target, iter_node.args[0]),
        items.append(Reversed())

    def visit_for_call_data(self, items, target_value, target_node, iter_node):
        iter_value = self.visit(iter_node)

        if self.context.mys_type == 'string':
            mys_type = 'char'
        else:
            mys_type = self.context.mys_type[0]

        items.append(Data(target_value, target_node, iter_value, mys_type))

    def visit_for_call(self, items, target, iter_node):
        target_value, target_node = target

        if isinstance(iter_node, ast.Call):
            if isinstance(iter_node.func, ast.Name):
                function_name = iter_node.func.id
                nargs = len(iter_node.args)

                if function_name == 'range':
                    self.visit_for_call_range(items,
                                              target_value,
                                              target_node,
                                              iter_node,
                                              nargs)
                elif function_name == 'slice':
                    self.visit_for_call_slice(items, target, iter_node, nargs)
                elif function_name == 'enumerate':
                    self.visit_for_call_enumerate(items,
                                                  target_value,
                                                  target_node,
                                                  iter_node,
                                                  nargs)
                elif function_name == 'zip':
                    self.visit_for_call_zip(items,
                                            target_value,
                                            target_node,
                                            iter_node,
                                            nargs)
                elif function_name == 'reversed':
                    self.visit_for_call_reversed(items, target, iter_node, nargs)
                else:
                    self.visit_for_call_data(items,
                                             target_value,
                                             target_node,
                                             iter_node)
            else:
                self.visit_for_call_data(items, target_value, target_node, iter_node)
        else:
            self.visit_for_call_data(items, target_value, target_node, iter_node)

    def visit_for_items_init(self, items):
        code = []

        for i, item in enumerate(items):
            if isinstance(item, Data):
                if item.mys_type == 'char':
                    op = '.'
                else:
                    op = '->'

                name = self.unique('data')
                code.append(f'const auto& {name}_object = {item.value};')
                code.append(f'auto {name} = Data({name}_object{op}__len__());')
            elif isinstance(item, Enumerate):
                name = self.unique('enumerate')
                prev_name = find_item_with_length(items).name
                code.append(f'auto {name} = Enumerate(i64({item.initial}),'
                            f' i64({prev_name}.length()));')
            elif isinstance(item, Range):
                name = self.unique('range')
                code.append(f'auto {name} = Range(i64({item.begin}), '
                            f'i64({item.end}), i64({item.step}));')
            elif isinstance(item, Slice):
                name = self.unique('slice')
                code.append(f'auto {name} = Slice(i64({item.begin}), i64({item.end}),'
                            f' i64({item.step}), i64({items[0].name}.length()));')

                for item_2 in items[:i]:
                    if not isinstance(item_2, (Slice, OpenSlice)):
                        code.append(f'{item_2.name}.slice({name});')
            elif isinstance(item, OpenSlice):
                name = self.unique('slice')
                code.append(f'auto {name} = OpenSlice(i64({item.begin}));')

                for item_2 in items[:i]:
                    if not isinstance(item_2, (Slice, OpenSlice, Zip, Reversed)):
                        code.append(f'{item_2.name}.slice({name});')
            elif isinstance(item, Reversed):
                for item_2 in items[:i]:
                    if not isinstance(item_2, (Slice, OpenSlice)):
                        code.append(f'{item_2.name}.reversed();')
            elif isinstance(item, Zip):
                names = []

                for items_2 in item.children:
                    code += self.visit_for_items_init(items_2)
                    names.append(find_item_with_length(items_2).name)

                first_child_name = names[0]
                name = self.unique('zip')
                code.append(f'auto {name} = {first_child_name}.length();')

                for child_name in names[1:]:
                    code.append(f'if ({name} != {child_name}.length()) {{')
                    code.append(
                        f'    throw ValueError("can\'t zip different lengths");')
                    code.append('}')
            else:
                raise RuntimeError()

            item.name = name

        return code

    def visit_for_items_iter(self, items):
        code = []

        for item in items:
            if isinstance(item, (Slice, OpenSlice, Reversed)):
                pass
            elif isinstance(item, Zip):
                for items_2 in item.children:
                    code += self.visit_for_items_iter(items_2)
            else:
                code.append(f'{item.name}.iter();')

        return code

    def visit_for_items_len_item(self, items):
        for item in items:
            if isinstance(item, (Slice, OpenSlice, Reversed)):
                pass
            elif isinstance(item, Zip):
                for items_2 in item.children:
                    return self.visit_for_items_len_item(items_2)
            else:
                return item

    def visit_for_items_body(self, items):
        code = []

        for item in items[::-1]:
            if isinstance(item, Data):
                if isinstance(item.target, tuple):
                    for i, ((target, _), mys_type) in enumerate(zip(item.target,
                                                                    item.mys_type)):
                        target_type = mys_type_to_target_cpp_type(mys_type)
                        code.append(f'    {target_type} {make_name(target)} = '
                                    f'std::get<{i}>({item.name}_object->get('
                                    f'{item.name}.next())->m_tuple);')
                else:
                    target_type = mys_type_to_target_cpp_type(item.mys_type)

                    if item.mys_type == 'char':
                        op = '.'
                    else:
                        op = '->'

                    code.append(
                        f'    {target_type} {make_name(item.target)} = '
                        f'{item.name}_object{op}get({item.name}.next());')
            elif isinstance(item, (Slice, OpenSlice, Reversed)):
                continue
            elif isinstance(item, Zip):
                for items_2 in item.children:
                    code += self.visit_for_items_body(items_2)

                continue
            else:
                target_type = mys_type_to_target_cpp_type(item.mys_type)
                code.append(
                    f'    {target_type} {make_name(item.target)} = '
                    f'{item.name}.next();')

            if isinstance(item.target, tuple):
                for (target, node), mys_type in zip(item.target, item.mys_type):
                    if not target.startswith('_'):
                        self.context.define_variable(target, mys_type, node)
            else:
                if not item.target.startswith('_'):
                    self.context.define_variable(item.target,
                                                 item.mys_type,
                                                 item.target_node)

        return code

    def visit_For(self, node):
        self.context.push()

        if isinstance(node.iter, ast.Call):
            target = UnpackVisitor().visit(node.target)
            items = []
            self.visit_for_call(items, target, node.iter)
            code = self.visit_for_items_init(items)
            length = self.unique('len')
            item = self.visit_for_items_len_item(items)
            code.append(f'auto {length} = {item.name}.length();')
            code += self.visit_for_items_iter(items)
            i = self.unique('i')
            code.append(f'for (auto {i} = 0; {i} < {length}; {i}++) {{')
            code += self.visit_for_items_body(items)
            code += [
                indent(self.visit(item))
                for item in node.body
            ]
            code.append('}')
        else:
            value = self.visit(node.iter)
            mys_type = self.context.mys_type

            if isinstance(mys_type, list):
                code = self.visit_for_list(node, value, mys_type)
            elif isinstance(mys_type, dict):
                code = self.visit_for_dict(node, value, mys_type)
            elif isinstance(mys_type, tuple):
                raise CompileError('iteration over tuples not allowed',
                                   node.iter)
            elif mys_type == 'string':
                code = self.visit_for_string(node, value, mys_type)
            else:
                raise CompileError(f'iteration over {mys_type} not supported',
                                   node.iter)

        self.context.pop()

        return '\n'.join(code)

    def visit_attribute_class(self, name, mys_type, value, node):
        definitions = self.context.get_class(mys_type)

        if name in definitions.members:
            self.context.mys_type = definitions.members[name].type
        else:
            raise CompileError(
                f"class '{mys_type}' has no member '{name}'",
                node)

        if value == 'self':
            value = 'this'
        elif name.startswith('_'):
            raise CompileError(f"class '{mys_type}' member '{name}' is private",
                               node)

        return value

    def visit_Attribute(self, node):
        name = node.attr

        if isinstance(node.value, ast.Name):
            value = node.value.id

            if self.context.is_enum_defined(value):
                enum_type = self.context.get_enum_type(value)
                self.context.mys_type = value

                return f'({enum_type}){value}::{name}'
            elif self.context.is_variable_defined(value):
                mys_type = self.context.get_variable_type(value)
            else:
                raise InternalError("attribute", node)
        else:
            value = self.visit(node.value)
            mys_type = self.context.mys_type

        if self.context.is_class_defined(mys_type):
            value = self.visit_attribute_class(name, mys_type, value, node)
        else:
            raise CompileError(f"'{mys_type}' has no member '{name}'", node)

        value = wrap_not_none(value, mys_type)

        return f'{value}->{make_name(node.attr)}'

    def create_constant(self, cpp_type, value):
        if value == 'nullptr':
            return value
        elif is_primitive_type(cpp_type):
            return value

        constant = self.context.constants.get(value)

        if constant is None:
            variable = self.unique('constant')
            self.context.constants[value] = (
                variable,
                f'static const {cpp_type} {variable} = {value};')
        else:
            variable = constant[0]

        return variable

    def visit_compare(self, node):
        if len(node.comparators) != 1:
            raise CompileError("can only compare two values", node)

        left_value_type = ValueTypeVisitor(self.source_lines,
                                           self.context).visit(node.left)
        right_value_type = ValueTypeVisitor(self.source_lines,
                                            self.context).visit(node.comparators[0])

        if isinstance(node.ops[0], (ast.In, ast.NotIn)):
            if isinstance(right_value_type, Dict):
                left_value_type, right_key_value_type = intersection_of(
                    left_value_type,
                    right_value_type.key_type,
                    node)
                right_value_type = Dict(right_key_value_type,
                                        right_value_type.value_type)
            elif isinstance(right_value_type, list) and len(right_value_type) == 1:
                left_value_type, right_value_type = intersection_of(
                    left_value_type,
                    right_value_type[0],
                    node)
                right_value_type = [right_value_type]
            else:
                raise CompileError("not an iterable", node.comparators[0])
        else:
            if not isinstance(node.ops[0], (ast.Is, ast.IsNot)):
                if left_value_type is None or right_value_type is None:
                    raise CompileError("use 'is' and 'is not' to compare to None",
                                       node)

            left_value_type, right_value_type = intersection_of(
                    left_value_type,
                    right_value_type,
                    node)

        left_value_type = reduce_type(left_value_type)
        right_value_type = reduce_type(right_value_type)

        left_value = self.visit_value_check_type(node.left, left_value_type)
        right_value = self.visit_value_check_type(node.comparators[0],
                                                  right_value_type)

        if is_constant(node.left):
            left_value = self.create_constant(
                mys_to_cpp_type(left_value_type, self.context),
                left_value)

        if is_constant(node.comparators[0]):
            right_value = self.create_constant(
                mys_to_cpp_type(right_value_type, self.context),
                right_value)

        items = [
            (left_value_type, left_value),
            (right_value_type, right_value)
        ]

        return items, [type(op) for op in node.ops]

    def visit_Compare(self, node):
        items, ops = self.visit_compare(node)
        left_mys_type, left = items[0]
        right_mys_type, right = items[1]
        op_class = ops[0]
        self.context.mys_type = 'bool'

        if op_class == ast.In:
            return f'Bool(contains({left}, {right}))'
        elif op_class == ast.NotIn:
            return f'Bool(!contains({left}, {right}))'
        elif op_class == ast.Is:
            left, right = compare_is_variables(left,
                                               left_mys_type,
                                               right,
                                               right_mys_type)

            return f'Bool(is({left}, {right}))'
        elif op_class == ast.IsNot:
            left, right = compare_is_variables(left,
                                               left_mys_type,
                                               right,
                                               right_mys_type)

            return f'Bool(!is({left}, {right}))'
        else:
            if left_mys_type != right_mys_type:
                raise CompileError(
                    f"can't compare '{left_mys_type}' and '{right_mys_type}'",
                    node)

            return f'Bool({left} {OPERATORS[op_class]} {right})'

    def variables_code(self, variables, node):
        before = []
        per_branch = []
        after = []

        for name, info in variables.defined().items():
            self.context.define_variable(name, info, node)
            variable_name = self.unique(name)
            cpp_type = mys_to_cpp_type(info, self.context)
            before.append(f'{cpp_type} {variable_name};')
            per_branch.append(f'    {variable_name} = {make_name(name)};')
            after.append(f'auto {make_name(name)} = {variable_name};')

        return (before, per_branch, after)

    def visit_If(self, node):
        variables = Variables()
        cond = self.visit(node.test)
        raise_if_not_bool(self.context.mys_type, node.test, self.context)
        self.context.push()
        body = indent('\n'.join([
            self.visit(item)
            for item in node.body
        ]))
        variables.add_branch(self.context.pop())
        self.context.push()
        orelse = indent('\n'.join([
            self.visit(item)
            for item in node.orelse
        ]))
        variables.add_branch(self.context.pop())

        code, per_branch, after = self.variables_code(variables, node)
        code += [f'if ({cond}) {{', body] + per_branch

        if orelse:
            code += [
                '} else {',
                orelse
            ] + per_branch + [
                '}'
            ]
        else:
            code += ['}']

        code += after

        return '\n'.join(code)

    def visit_return_none(self, node):
        if self.context.return_mys_type is not None:
            raise CompileError("return value missing", node)

        self.context.mys_type = None

        return 'return;'

    def visit_return_value(self, node):
        if self.context.return_mys_type is None:
            raise CompileError("function does not return any value", node.value)

        value = self.visit_value_check_type(node.value,
                                            self.context.return_mys_type)
        raise_if_wrong_visited_type(self.context,
                                    self.context.return_mys_type,
                                    node.value)

        return f'return {value};'

    def visit_Return(self, node):
        if node.value is None:
            return self.visit_return_none(node)
        else:
            return self.visit_return_value(node)

    def visit_Try(self, node):
        variables = Variables()
        self.context.push()
        body = indent('\n'.join([self.visit(item) for item in node.body]))
        variables.add_branch(self.context.pop())
        success_variable = self.unique('success')
        self.context.push()
        or_else_body = '\n'.join([self.visit(item) for item in node.orelse])
        or_else_variables = self.context.pop()

        if or_else_body:
            body += '\n'
            body += indent(f'{success_variable} = true;')
            variables.add_branch(or_else_variables)

        self.context.push()
        finalbody = indent(
            '\n'.join([self.visit(item) for item in node.finalbody]))
        finalbody_variables = self.context.pop()
        handlers = []

        for handler in node.handlers:
            if handler.type is None:
                exception = 'std::exception'
            else:
                exception = handler.type.id

            self.context.push()

            if handler.name is not None:
                raise CompileError("except ... as ... not implemented", handler.name)

            handlers.append('\n'.join([
                f'}} catch ({exception}& e) {{',
                indent('\n'.join([self.visit(item) for item in handler.body]))
            ]))
            variables.add_branch(self.context.pop())

        before, per_branch, after = self.variables_code(variables, node)
        code = '\n'.join(before)

        if code:
            code += '\n'

        if handlers:
            if per_branch:
                after_handler = '\n' + '\n'.join(per_branch)
            else:
                after_handler = ''

            code += '\n'.join([
                'try {',
                body
            ] + per_branch + [
                '\n'.join([handler + after_handler for handler in handlers]),
                '}'
            ])

            if or_else_body:
                code = f'bool {success_variable} = false;\n' + code
                code += '\n'.join([
                    f'\nif ({success_variable}) {{',
                    indent(or_else_body)
                ] + per_branch + [
                    '}\n'
                ])
        else:
            code = '\n'.join([dedent(body)] + per_branch)

        if finalbody:
            code = '\n'.join([
                'try {',
                indent(code),
                finalbody,
                '} catch (...) {',
                finalbody,
                indent('throw;'),
                '}'
            ])

        if after:
            code += '\n'
            code += '\n'.join(after)

        return code

    def visit_Raise(self, node):
        if node.exc is None:
            return 'throw;'
        else:
            exception = self.visit(node.exc)

            return f'throw {exception};'

    def visit_inferred_type_assign(self, node, target):
        value_type = ValueTypeVisitor(self.source_lines,
                                      self.context).visit(node.value)

        if value_type is None:
            raise CompileError("can't infer type from None", node)
        elif isinstance(value_type, Dict):
            if value_type.key_type is None:
                raise CompileError("can't infer type from empty dict", node)
        elif value_type == []:
            raise CompileError("can't infer type from empty list", node)

        value_type = reduce_type(value_type)
        value = self.visit_value_check_type(node.value, value_type)
        cpp_type = 'auto'
        self.context.define_variable(target, self.context.mys_type, node)

        return f'{cpp_type} {make_name(target)} = {value};'

    def visit_assign_tuple_unpack(self, node, target):
        value = self.visit(node.value)
        mys_type = self.context.mys_type

        if not isinstance(mys_type, tuple):
            raise CompileError('only tuples can be unpacked', node.value)

        value_nargs = len(mys_type)
        target_nargs = len(target.elts)

        if value_nargs != target_nargs:
            raise CompileError(
                f'expected {target_nargs} values to unpack, got {value_nargs}',
                node)

        temp = self.unique('tuple')
        lines = [f'auto {temp} = {value};']

        for i, item in enumerate(target.elts):
            if isinstance(item, ast.Name):
                target = item.id

                if self.context.is_variable_defined(target):
                    raise_if_self(target, node)
                    target_mys_type = self.context.get_variable_type(target)
                    raise_if_wrong_types(mys_type[i],
                                         target_mys_type,
                                         item,
                                         self.context)
                else:
                    self.context.define_variable(target, mys_type[i], item)
                    target = f'const auto& {target}'
            else:
                target = self.visit(item)

            lines.append(f'{target} = std::get<{i}>({temp}->m_tuple);')

        return '\n'.join(lines)

    def visit_assign_variable(self, node, target):
        target = target.id

        if self.context.is_variable_defined(target):
            raise_if_self(target, node)
            target_mys_type = self.context.get_variable_type(target)
            value = self.visit_value_check_type(node.value, target_mys_type)
            raise_if_wrong_visited_type(self.context,
                                        target_mys_type,
                                        node.value)

            code = f'{target} = {value};'
        else:
            code = self.visit_inferred_type_assign(node, target)

        return code

    def visit_assign_other(self, node, target):
        target = self.visit(target)
        target_mys_type = self.context.mys_type
        value = self.visit_value_check_type(node.value, target_mys_type)
        raise_if_wrong_visited_type(self.context,
                                    target_mys_type,
                                    node.value)

        return f'{target} = {value};'

    def visit_Assign(self, node):
        target = node.targets[0]

        if isinstance(target, ast.Tuple):
            return self.visit_assign_tuple_unpack(node, target)
        elif isinstance(target, ast.Name):
            return self.visit_assign_variable(node, target)
        else:
            return self.visit_assign_other(node, target)

    def visit_subscript_tuple(self, node, value, mys_type):
        if not is_integer_literal(node.slice):
            raise CompileError(
                "tuple indexes must be compile time known integers",
                node.slice)

        index = make_integer_literal('i64', node.slice)

        try:
            index = int(index)
        except ValueError:
            raise CompileError(
                "tuple indexes must be compile time known integers",
                node.slice)

        if not (0 <= index < len(mys_type)):
            raise CompileError("tuple index out of range", node.slice)

        self.context.mys_type = mys_type[index]

        return f'std::get<{index}>({value}->m_tuple)'

    def visit_subscript_dict(self, node, value, mys_type):
        key_mys_type, value_mys_type = split_dict_mys_type(mys_type)
        key = self.visit_value_check_type(node.slice, key_mys_type)
        self.context.mys_type = value_mys_type

        return f'(*{value})[{key}]'

    def visit_subscript_list(self, node, value, mys_type):
        index = self.visit(node.slice)
        self.context.mys_type = mys_type[0]

        return f'{value}->get({index})'

    def visit_subscript_string(self, node, value):
        index = self.visit(node.slice)
        self.context.mys_type = 'char'

        return f'{value}.get({index})'

    def visit_subscript_bytes(self, node, value):
        index = self.visit(node.slice)
        self.context.mys_type = 'u8'

        return f'{value}[{index}]'

    def visit_Subscript(self, node):
        value = self.visit(node.value)
        mys_type = self.context.mys_type
        value = wrap_not_none(value, mys_type)

        if isinstance(mys_type, tuple):
            return self.visit_subscript_tuple(node, value, mys_type)
        elif isinstance(mys_type, dict):
            return self.visit_subscript_dict(node, value, mys_type)
        elif isinstance(mys_type, list):
            return self.visit_subscript_list(node, value, mys_type)
        elif mys_type == 'string':
            return self.visit_subscript_string(node, value)
        elif mys_type == 'bytes':
            return self.visit_subscript_bytes(node, value)
        else:
            raise CompileError("subscript of this type is not yet implemented",
                               node)

    def visit_value_check_type_tuple(self, node, mys_type):
        if not isinstance(mys_type, tuple):
            mys_type = format_mys_type(mys_type)

            raise CompileError(f"can't convert tuple to '{mys_type}'", node)

        values = []
        types = []

        for i, item in enumerate(node.elts):
            values.append(self.visit_value_check_type(item, mys_type[i]))
            types.append(self.context.mys_type)

        raise_if_wrong_types(tuple(types), mys_type, node, self.context)
        self.context.mys_type = mys_type
        cpp_type = self.mys_to_cpp_type(mys_type)
        values = ", ".join(values)

        return make_shared(cpp_type[6:], values)

    def visit_value_check_type_list(self, node, mys_type):
        if not isinstance(mys_type, list):
            mys_type = format_mys_type(mys_type)

            raise CompileError(f"can't convert list to '{mys_type}'", node)

        values = []
        item_mys_type = mys_type[0]

        for item in node.elts:
            values.append(self.visit_value_check_type(item, item_mys_type))

        self.context.mys_type = mys_type
        value = ", ".join(values)
        item_cpp_type = self.mys_to_cpp_type(item_mys_type)

        return make_shared_list(item_cpp_type, value)

    def visit_value_check_type_dict(self, node, mys_type):
        if not isinstance(mys_type, dict):
            mys_type = format_mys_type(mys_type)

            raise CompileError(f"can't convert dict to '{mys_type}'", node)

        key_mys_type, value_mys_type = split_dict_mys_type(mys_type)

        if not is_allowed_dict_key_type(key_mys_type):
            raise CompileError("invalid key type", node)

        keys = []
        values = []

        for key, value in zip(node.keys, node.values):
            keys.append(self.visit_value_check_type(key, key_mys_type))
            values.append(self.visit_value_check_type(value, value_mys_type))

        self.context.mys_type = mys_type
        items = ", ".join([f'{{{key}, {value}}}' for key, value in zip(keys, values)])
        key_cpp_type = self.mys_to_cpp_type(key_mys_type)
        value_cpp_type = self.mys_to_cpp_type(value_mys_type)

        return make_shared_dict(key_cpp_type, value_cpp_type, items)

    def visit_value_check_type_other(self, node, mys_type):
        value = self.visit(node)

        if self.context.is_trait_defined(mys_type):
            if self.context.is_class_defined(self.context.mys_type):
                definitions = self.context.get_class(self.context.mys_type)

                if mys_type not in definitions.implements:
                    trait_type = format_mys_type(mys_type)
                    class_type = self.context.mys_type

                    raise CompileError(
                        f"'{class_type}' does not implement trait '{trait_type}'",
                        node)
        elif self.context.is_enum_defined(mys_type):
            pass
        else:
            raise_if_wrong_visited_type(self.context, mys_type, node)

        return value

    def visit_value_check_type(self, node, mys_type):
        if is_integer_literal(node):
            value = make_integer_literal(mys_type, node)
            self.context.mys_type = mys_type
        elif is_float_literal(node):
            value = make_float_literal(mys_type, node)
            self.context.mys_type = mys_type
        elif isinstance(node, ast.Constant):
            value = self.visit(node)

            if self.context.mys_type is None:
                if not is_primitive_type(mys_type):
                    self.context.mys_type = mys_type

            raise_if_wrong_visited_type(self.context, mys_type, node)
        elif isinstance(node, ast.Tuple):
            value = self.visit_value_check_type_tuple(node, mys_type)
        elif isinstance(node, ast.List):
            value = self.visit_value_check_type_list(node, mys_type)
        elif isinstance(node, ast.Dict):
            value = self.visit_value_check_type_dict(node, mys_type)
        else:
            value = self.visit_value_check_type_other(node, mys_type)

        return value

    def visit_ann_assign(self, node):
        target = node.target.id

        if node.value is None:
            raise CompileError("variables must be initialized when declared", node)

        mys_type = TypeVisitor().visit(node.annotation)

        if not self.context.is_type_defined(mys_type):
            mys_type = format_mys_type(mys_type)

            raise CompileError(f"undefined type '{mys_type}'", node.annotation)

        code = self.visit_value_check_type(node.value, mys_type)
        cpp_type = self.mys_to_cpp_type(mys_type)
        code = f'{cpp_type} {make_name(target)} = {code};'

        return target, mys_type, code

    def visit_AnnAssign(self, node):
        target, mys_type, code = self.visit_ann_assign(node)
        self.context.define_variable(target, mys_type, node.target)

        return code

    def visit_While(self, node):
        condition = self.visit(node.test)
        raise_if_not_bool(self.context.mys_type, node.test, self.context)
        self.context.push()
        body = indent('\n'.join([self.visit(item) for item in node.body]))
        self.context.pop()

        return '\n'.join([
            f'while ({condition}) {{',
            body,
            '}'
        ])

    def visit_Pass(self, node):
        return ''

    def visit_Break(self, node):
        return 'break;'

    def visit_Continue(self, node):
        return 'continue;'

    def visit_Assert(self, node):
        prepare = []

        if isinstance(node.test, ast.Compare):
            items, ops = self.visit_compare(node.test)
            variables = []

            for mys_type, value in items:
                if mys_type is None:
                    variables.append(('nullptr', mys_type))
                else:
                    variable = self.unique('var')
                    cpp_type = self.mys_to_cpp_type(mys_type)
                    prepare.append(f'const {cpp_type} {variable} = {value};')
                    variables.append((variable, mys_type))

            conds = []
            messages = []

            for i, op_class in enumerate(ops):
                if op_class == ast.In:
                    conds.append(
                        f'contains({variables[i][0]}, {variables[i + 1][0]})')
                    messages.append(
                        f'{format_print_arg(variables[i], self.context)} << " in "')
                elif op_class == ast.NotIn:
                    conds.append(
                        f'!contains({variables[i][0]}, {variables[i + 1][0]})')
                    messages.append(
                        f'{format_print_arg(variables[i], self.context)} << " not in "')
                elif op_class == ast.Is:
                    variable_1, variable_2 = compare_assert_is_variables(
                        variables[i],
                        variables[i + 1])
                    conds.append(f'is({variable_1}, {variable_2})')
                    messages.append(
                        f'{format_print_arg(variables[i], self.context)} << " is "')
                elif op_class == ast.IsNot:
                    variable_1, variable_2 = compare_assert_is_variables(
                        variables[i],
                        variables[i + 1])
                    conds.append(f'!is({variable_1}, {variable_2})')
                    messages.append(
                        f'{format_print_arg(variables[i], self.context)} << " is not "')
                else:
                    op = OPERATORS[op_class]
                    conds.append(f'({variables[i][0]} {op} {variables[i + 1][0]})')
                    messages.append(
                        f'{format_print_arg(variables[i], self.context)} << " {op} "')

            messages.append(f'{format_print_arg(variables[-1], self.context)}')
            cond = ' && '.join(conds)
            message = ' << '.join(messages)
        else:
            message = '"todo"'
            cond = self.visit(node.test)

        filename = self.filename
        line = node.lineno

        return '\n'.join([
            '#if defined(MYS_TEST) || !defined(NDEBUG)'
        ] + prepare + [
            f'if (!({cond})) {{',
            f'    std::cout << "{filename}:{line}: assert " << {message} << '
            '" is not true" << std::endl;',
            f'    throw AssertionError("todo is not true");',
            '}',
            '#endif'
        ])

    def visit_With(self, node):
        items = '\n'.join([
            self.visit(item) + ';'
            for item in node.items
        ])
        body = indent('\n'.join([self.visit(item) for item in node.body]))

        return '\n'.join([
            '{',
            indent(items),
            body,
            '}'
        ])

    def visit_withitem(self, node):
        expr = self.visit(node.context_expr)
        var = self.visit(node.optional_vars)

        return f'auto {var} = {expr}'

    def visit_Lambda(self, node):
        raise CompileError('lambda functions are not supported', node)

    def visit_Import(self, node):
        raise CompileError('imports are only allowed on module level', node)

    def visit_ImportFrom(self, node):
        raise CompileError('imports are only allowed on module level', node)

    def visit_ClassDef(self, node):
        raise CompileError('class definitions are only allowed on module level',
                           node)

    def visit_JoinedStr(self, node):
        if node.values:
            return ' + '.join([
                self.visit(value)
                for value in node.values
            ])
        else:
            return '""'

    def visit_FormattedValue(self, node):
        value = self.visit(node.value)
        value = format_arg((value, self.context.mys_type), self.context)
        value = format_str(value, self.context.mys_type)
        self.context.mys_type = 'string'

        return value

    def visit_BoolOp(self, node):
        values = []

        for value in node.values:
            values.append(self.visit(value))

            if self.context.mys_type is None:
                raise CompileError(f"None is not a 'bool'", value)
            else:
                raise_if_not_bool(self.context.mys_type, value, self.context)

        op = BOOL_OPS[type(node.op)]

        return '((' + f') {op} ('.join(values) + '))'

    def visit_trait_match(self, subject_variable, node):
        cases = []

        for case in node.cases:
            if case.guard is not None:
                raise CompileError("guards are not supported", case.guard)

            casted = self.unique('casted')

            if isinstance(case.pattern, ast.Call):
                class_name = case.pattern.func.id
                cases.append(
                    f'const auto& {casted} = '
                    f'std::dynamic_pointer_cast<{class_name}>({subject_variable});\n'
                    f'if ({casted}) {{\n' +
                    indent('\n'.join([self.visit(item) for item in case.body])) +
                    '\n}')
            elif isinstance(case.pattern, ast.MatchAs):
                if isinstance(case.pattern.pattern, ast.Call):
                    class_name = case.pattern.pattern.func.id
                    self.context.push()
                    self.context.define_variable(case.pattern.name, class_name, case)
                    cases.append(
                        f'const auto& {casted} = '
                        f'std::dynamic_pointer_cast<{class_name}>({subject_variable});\n'
                        f'if ({casted}) {{\n'
                        f'    const auto& {case.pattern.name} = '
                        f'std::move({casted});\n' +
                        indent('\n'.join([self.visit(item) for item in case.body])) +
                        '\n}')
                    self.context.pop()
                else:
                    raise CompileError('trait match patterns must be classes',
                                       case.pattern)
            elif isinstance(case.pattern, ast.Name):
                if case.pattern.id == '_':
                    cases.append('\n'.join([self.visit(item) for item in case.body]))
                else:
                    raise CompileError('trait match patterns must be classes',
                                       case.pattern)
            else:
                raise CompileError('trait match patterns must be classes',
                                   case.pattern)

        body = ''

        for case in cases[1:][::-1]:
            body = ' else {\n' + indent(case + body) + '\n}'

        return cases[0] + body

    def visit_other_match(self, subject_variable, subject_mys_type, node):
        cases = []

        for case in node.cases:
            if case.guard is not None:
                raise CompileError("guards are not supported", case.guard)

            if isinstance(case.pattern, ast.Name):
                if case.pattern.id != '_':
                    raise CompileError("can't match variables", case.pattern)

                pattern = '_'
            else:
                pattern = self.visit_value_check_type(case.pattern, subject_mys_type)

                if subject_mys_type == 'string':
                    pattern = self.create_constant('String', pattern)

            body = indent('\n'.join([self.visit(item) for item in case.body]))

            if pattern == '_':
                cases.append(f'{{\n' + body + '\n}')
            else:
                cases.append(f'if ({subject_variable} == {pattern}) {{\n' + body + '\n}')

        return ' else '.join(cases)

    def visit_Match(self, node):
        subject_variable = self.unique('subject')
        code = f'const auto& {subject_variable} = {self.visit(node.subject)};\n'
        subject_mys_type = self.context.mys_type

        if self.context.is_trait_defined(subject_mys_type):
            code += self.visit_trait_match(subject_variable, node)
        elif self.context.is_class_defined(subject_mys_type):
            raise CompileError("matching classes if not supported", node.subject)
        else:
            code += self.visit_other_match(subject_variable, subject_mys_type, node)

        return code

    def visit_IfExp(self, node):
        test = self.visit(node.test)
        raise_if_not_bool(self.context.mys_type, node.test, self.context)
        body = self.visit(node.body)
        body_type = self.context.mys_type
        orelse = self.visit(node.orelse)
        orelse_type = self.context.mys_type
        raise_if_wrong_types(orelse_type, body_type, node.orelse, self.context)

        return f'(({test}) ? ({body}) : ({orelse}))'

    def visit_ListComp(self, node):
        raise CompileError("list comprehension is not implemented", node)

    def visit_Slice(self, node):
        raise CompileError("slices are not implemented", node)

    def generic_visit(self, node):
        raise InternalError("unhandled node", node)

class CppTypeVisitor(BaseVisitor):

    def visit_Name(self, node):
        cpp_type = node.id

        if cpp_type == 'string':
            return 'String'
        elif self.context.is_class_or_trait_defined(cpp_type):
            return f'std::shared_ptr<{cpp_type}>'
        elif self.context.is_enum_defined(cpp_type):
            return self.context.get_enum_type(cpp_type)
        elif cpp_type == 'bool':
            return 'Bool'
        elif cpp_type == 'char':
            return 'Char'
        elif cpp_type == 'bytes':
            return 'Bytes'
        else:
            return cpp_type

    def visit_List(self, node):
        item_cpp_type = self.visit(node.elts[0])

        return shared_list_type(item_cpp_type)

    def visit_Tuple(self, node):
        items = ', '.join([self.visit(elem) for elem in node.elts])

        return shared_tuple_type(items)

    def visit_Dict(self, node):
        key_cpp_type = self.visit(node.keys[0])
        value_cpp_type = self.visit(node.values[0])

        return shared_dict_type(key_cpp_type, value_cpp_type)

class ParamVisitor(BaseVisitor):

    def visit_arg(self, node):
        param_name = node.arg
        self.context.define_variable(param_name,
                                     TypeVisitor().visit(node.annotation),
                                     node)
        cpp_type = self.visit_cpp_type(node.annotation)

        if isinstance(node.annotation, ast.Name):
            param_type = node.annotation.id

            if (param_type == 'string'
                or self.context.is_class_or_trait_defined(param_type)):
                cpp_type = f'const {cpp_type}&'

            return f'{cpp_type} {make_name(param_name)}'
        else:
            return f'const {cpp_type}& {make_name(param_name)}'

class BodyCheckVisitor(ast.NodeVisitor):

    def visit_Expr(self, node):
        if isinstance(node.value, ast.Name):
            raise CompileError("bare name", node)
        elif isinstance(node.value, ast.Compare):
            raise CompileError("bare comparision", node)
        elif isinstance(node.value, ast.BinOp):
            raise CompileError("bare binary operation", node)
        elif isinstance(node.value, ast.UnaryOp):
            raise CompileError("bare unary operation", node)
        elif isinstance(node.value, ast.Constant):
            if isinstance(node.value.value, str):
                # ToDo: embedded C++
                pass
            elif isinstance(node.value.value, int):
                raise CompileError("bare integer", node)
            if isinstance(node.value.value, float):
                raise CompileError("bare float", node)

class ConstantVisitor(ast.NodeVisitor):

    def __init__(self):
        self.is_constant = True

    def visit_Constant(self, node):
        pass

    def visit_UnaryOp(self, node):
        self.visit(node.operand)

    def visit_List(self, node):
        for item in node.elts:
            self.visit(item)

    def visit_Tuple(self, node):
        for item in node.elts:
            self.visit(item)

    def visit_Dict(self, node):
        for item in node.keys:
            self.visit(item)

        for item in node.values:
            self.visit(item)

    def generic_visit(self, node):
        self.is_constant = False

def is_constant(node):
    visitor = ConstantVisitor()
    visitor.visit(node)

    return visitor.is_constant
