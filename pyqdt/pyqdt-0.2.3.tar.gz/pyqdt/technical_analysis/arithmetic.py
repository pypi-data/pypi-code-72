# -*- coding: utf-8 -*-

import threading
from functools import wraps

import numpy as np
import pandas as pd


class ArithmeticQuoteValue(object):
    def __init__(self, label=None):
        self._label = label

    @property
    def label(self):
        return self._label

    @property
    def value(self):
        return ArithmeticContainer().ref(self._label)

    def _f(self, val):
        return float(val) if val else 0

    def __get__(self, instance, owner):
        print('get')
        return self.value

    def __float__(self):
        return self._f(self.value)

    def __add__(self, other):
        return self.value + self._f(other)

    def __radd__(self, other):
        return self._f(other) + self.value

    def __sub__(self, other):
        return self.value - self._f(other)

    def __rsub__(self, other):
        return self._f(other) - self.value

    def __mul__(self, other):
        return self.value * self._f(other)

    def __rmul__(self, other):
        return self._f(other) * self.value

    def __truediv__(self, other):
        return self.value / self._f(other)

    def __rtruediv__(self, other):
        return self._f(other) / self.value

    def __floordiv__(self, other):
        return self.value / self._f(other)

    def __rfloordiv__(self, other):
        return self._f(other) / self.value

    def __mod__(self, other):
        return self.value % self._f(other)

    def __rmod__(self, other):
        return self._f(other) / self.value

    def __pow__(self, power, modulo=None):
        return pow(self.value, power, modulo)

    def __rpow__(self, other):
        return pow(self._f(other), self.value)

    def __neg__(self):
        return -self.value

    def __pos__(self):
        return self.value

    def __lt__(self, other):
        return self.value < self._f(other)

    def __gt__(self, other):
        return self.value > self._f(other)

    def __le__(self, other):
        return self.value <= self._f(other)

    def __ge__(self, other):
        return self.value >= self._f(other)

    def __eq__(self, other):
        return self.value == self._f(other)

    def __ne__(self, other):
        return self.value != self._f(other)


class ArithmeticContainer(object):
    """计算容器"""
    _threading_local = threading.local()

    def __new__(cls, *args, **kwargs):
        """单例模式-线程隔离"""
        if not hasattr(cls._threading_local, "_instance"):
            cls._threading_local._instance = object.__new__(cls)
        return cls._threading_local._instance

    def __init__(self):
        if not hasattr(self, '_security'):
            self._security = None
        if not hasattr(self, '_operator'):
            self._operator = None
        if not hasattr(self, '_result'):
            self._result = None

    def reset(self, security=None):
        if self._security == security:
            return
        if not security:
            self._security = None
            self._operator = None
            self._result = None
        else:
            # trace('new operator', security)
            self._security = security
            self._result = None
            self._operator = ArithmeticOperator()

    def update(self, data):
        if self._operator:
            self._operator.update(data)

    def __setattr__(self, key, value):
        if key == 'result':
            self._result = value
            return
        self.__dict__[key] = value

    def __getattr__(self, item):
        if item == 'result':
            return self._result

        if item.lower() in ['ref', 'std', 'abs', 'max', 'min', 'sum',
                            'ma', 'ema', 'mema', 'sma', 'hhv', 'llv']:
            if self._operator:
                return getattr(self._operator, item.lower())


class ArithmeticOperator(object):
    def __init__(self):
        self._data = pd.DataFrame()
        self._stats = []
        self._index = 0

    def _fetch_stat(self):
        if self._index <= len(self._stats):
            self._stats.append(ArithmeticStatistics())
        # print('current stats [%d]' % (self._index))
        stat = self._stats[self._index]
        self._index += 1
        return stat

    def update(self, data):
        self._data = self._data.append(data[['open', 'close', 'high', 'low', 'volume', 'money']])
        self._index = 0

    def ref(self, x, n=0):
        label = None
        if type(x) is ArithmeticQuoteValue:
            label = x.label
        elif type(x) is str:
            label = x
        if label:
            if n >= len(self._data):
                n = -1
            r = self._data.iloc[-n - 1][label]
            if label == 'volume':
                r = r / 100
            return r
        else:
            stat = self._fetch_stat()
            # print('ref', x, n)
            return stat.ref(x, n)

    def abs(self, x):
        return abs(float(x))

    def max(self, *args):
        return max(args)

    def min(self, *args):
        return min(args)

    def __getattr__(self, item):
        if item in ['open', 'close', 'high', 'low', 'volume', 'money']:
            return self.ref(item)
        elif item in ['std', 'sum', 'ma', 'ema', 'mema', 'sma', 'hhv', 'llv']:
            stat = self._fetch_stat()
            return getattr(stat, item)


class ArithmeticStatistics(object):
    def __init__(self):
        self._data = []
        self._result = None

    @staticmethod
    def _val(x):
        return x.value if type(x) is ArithmeticQuoteValue else x

    @property
    def result(self):
        return self._result

    def _update(self, x, n):
        self._data.append(x)
        while 0 < n < len(self._data):
            self._data.pop(0)
        # print(self._data)

    def ref(self, x, n):
        x = self._val(x)
        self._update(x, n + 1)
        self._result = self._data[-n - 1] if len(self._data) > n else self._data[0]
        return self._result

    '''
    def max(self, x):
        self.hhv(x, 0)

    def min(self, x):
        self.llv(x, 0)
    '''

    def std(self, x, n):
        x = self._val(x)
        self._update(x, n)
        self._result = float(np.std(self._data[-n:]))
        return self._result

    def sum(self, x, n=0):
        x = self._val(x)
        self._update(x, n)
        self._result = float(np.sum(self._data[-n:]))
        return self._result

    def ma(self, x, n):
        x = self._val(x)
        self._update(x, n)
        self._result = float(np.mean(self._data[-n:])) if len(self._data) >= n else None
        return self._result

    def ema(self, x, n):
        x = self._val(x)
        return self.sma(x, n + 1, 2)

    def mema(self, x, n):
        x = self._val(x)
        return self.sma(x, n, 1)

    def sma(self, x, n, m):
        x = self._val(x)
        self._result = (m * x + (n - m) * self._result) / n if self._result else x
        return self._result

    def hhv(self, x, n):
        x = self._val(x)
        self._update(x, n)
        self._result = float(np.max(self._data[-n:]))
        return self._result

    def llv(self, x, n):
        x = self._val(x)
        self._update(x, n)
        self._result = float(np.min(self._data[-n:]))
        return self._result


def arithmetic_wrapper(func):
    @wraps(func)
    def _wrapper(*args, **kwargs):
        if args and type(args[0]) is pd.Series:
            data = args[0]
            arith = ArithmeticContainer()
            arith.reset(data['code'])
            arith.update(data)
            if data['paused'] == 1:
                return arith.result
            if 'X' in kwargs:
                kwargs['X'] = eval(kwargs['X'].upper())

            try:
                arith.result = func(*args[1:], **kwargs)
            except (TypeError, ZeroDivisionError):
                returns = arithmetic_returns(func.__code__)
                if type(returns) is list:
                    arith.result = tuple([np.nan for i in range(len(returns))])
                else:
                    arith.result = np.nan
            return arith.result
        else:
            return func(*args, **kwargs)

    return _wrapper


def arithmetic_reset():
    ArithmeticContainer().reset()


def arithmetic_returns(func_code):
    result = None
    if len(func_code.co_consts) > 0:
        for x in func_code.co_consts[0].splitlines():
            p = x.find('=')
            if p >= 0 and x[0:p].strip() == 'RETURNS':
                y = x[p + 1:].strip()
                if len(y) > 2 and y[0] == '(' and y[-1] == ')':
                    result = [z.strip() for z in y[1:-1].split(',') if z.strip()]
                else:
                    result = y.strip()
    return result


OPEN = ArithmeticQuoteValue('open')
CLOSE = ArithmeticQuoteValue('close')
HIGH = ArithmeticQuoteValue('high')
LOW = ArithmeticQuoteValue('low')
VOL = ArithmeticQuoteValue('volume')
MONEY = ArithmeticQuoteValue('money')


def IF(C, T, F):
    return float(T) if C else float(F)


def ABS(X):
    """绝对值"""
    return ArithmeticContainer().abs(X)


def MAX(*args):
    """最大值"""
    return ArithmeticContainer().max(*args)


def MIN(*args):
    """最小值"""
    return ArithmeticContainer().min(*args)


@arithmetic_wrapper
def SUM(X=CLOSE, N=5):
    """汇总

    输入:
        X: 数值或行情类型 [OPEN， CLOSE, HIGH, LOW, VOL, MONEY]
        N: 统计天数

    输出：
        前N周期的汇总数值

    """
    return ArithmeticContainer().sum(X, N)


@arithmetic_wrapper
def STD(X=CLOSE, N=0):
    """标准差

    输入:
        X: 数值或行情类型 [OPEN， CLOSE, HIGH, LOW, VOL, MONEY]
        N: 统计天数

    输出:
        前N周期的标准差

    """
    return ArithmeticContainer().std(X, N)


@arithmetic_wrapper
def REF(X=CLOSE, N=0):
    """获取参考数据

    输入:
        X: 数值或行情类型 [OPEN， CLOSE, HIGH, LOW, VOL, MONEY]
        N: 统计天数

    输出:
        前N周期的行情数值

    """
    return ArithmeticContainer().ref(X, N)


@arithmetic_wrapper
def HHV(X=HIGH, N=5):
    """最大值

    输入:
        X: 数值或行情类型 [OPEN， CLOSE, HIGH, LOW, VOL, MONEY]
        N: 统计天数

    输出:
        前N周期的最大值

    """
    return ArithmeticContainer().hhv(X, N)


@arithmetic_wrapper
def LLV(X=LOW, N=5):
    """最小值

    输入:
        X: 数值或行情类型 [OPEN， CLOSE, HIGH, LOW, VOL, MONEY]
        N: 统计天数

    输出:
        前N周期的最小值

    """
    return ArithmeticContainer().llv(X, N)


@arithmetic_wrapper
def MA(X=CLOSE, N=5):
    """均线

    公式：
        MA1: MA(CLOSE, N)
    输入：
        N: 统计的天数
    输出：
        MA: 移动平均

    """
    return ArithmeticContainer().ma(X, N)


@arithmetic_wrapper
def EMA(X=CLOSE, N=30):
    """指数移动平均

    公式：
        若Y=EMA(X,N)，则 Y = (2 * X + (N - 1) * Y') / (N + 1), 其中Y'表示上一周期Y值。
    输入：
        N: 统计的天数
    输出：
        EMA：指数移动平均
    """
    return ArithmeticContainer().ema(X, N)


@arithmetic_wrapper
def MEMA(X=CLOSE, N=5):
    """平滑移动平均

    公式：
        若Y=MEMA(X,N)，则 Y = (X + (N - 1) * Y') / N, 其中Y'表示上一周期Y值。
    输入：
        N: 统计的天数
    输出：
        MEMA：指数移动平均
    """
    return ArithmeticContainer().mema(X, N)


@arithmetic_wrapper
def SMA(X=CLOSE, N=7, M=1):
    """简单移动平均

    公式：
        计算SMA(X,N,M)， 即X的N日移动平均，M为权重。
        若Y=SMA(X,N,M) 则 Y = (M * X + (N - M) * Y') / N, 其中Y'表示上一周期Y值,N必须大于M。
    输入：
        N：统计的天数 N
        M：权重 M
    输出：
        SMA: 简单移动平均
    """
    return ArithmeticContainer().sma(X, N, M)
