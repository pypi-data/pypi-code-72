#
# Copyright 2014 Quantopian, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import abc
import logbook
from datetime import datetime

import pandas as pd

from six import with_metaclass

from zipline.errors import (
    AccountControlViolation,
    TradingControlViolation,
)
from zipline.utils.input_validation import (
    expect_bounded,
    expect_types,
)


log = logbook.Logger('TradingControl')


class TradingControl(with_metaclass(abc.ABCMeta)):
    """
    Abstract base class representing a fail-safe control on the behavior of any
    algorithm.
    """

    def __init__(self, on_error, **kwargs):
        """
        Track any arguments that should be printed in the error message
        generated by self.fail.
        """
        self.on_error = on_error
        self.__fail_args = kwargs

    @abc.abstractmethod
    def validate(self,
                 asset,
                 amount,
                 portfolio,
                 algo_datetime,
                 algo_current_data):
        """
        Before any order is executed by TradingAlgorithm, this method should be
        called *exactly once* on each registered TradingControl object.

        If the specified asset and amount do not violate this TradingControl's
        restraint given the information in `portfolio`, this method should
        return None and have no externally-visible side-effects.

        If the desired order violates this TradingControl's contraint, this
        method should call self.fail(asset, amount).
        """
        raise NotImplementedError

    def _constraint_msg(self, metadata):
        constraint = repr(self)
        if metadata:
            constraint = "{constraint} (Metadata: {metadata})".format(
                constraint=constraint,
                metadata=metadata
            )
        return constraint

    def handle_violation(self, asset, amount, datetime, metadata=None):
        """
        Handle a TradingControlViolation, either by raising or logging and
        error with information about the failure.

        If dynamic information should be displayed as well, pass it in via
        `metadata`.
        """
        constraint = self._constraint_msg(metadata)

        if self.on_error == 'fail':
            raise TradingControlViolation(
                asset=asset,
                amount=amount,
                datetime=datetime,
                constraint=constraint)
        elif self.on_error == 'log':
            log.error("Order for {amount} shares of {asset} at {dt} "
                      "violates trading constraint {constraint}",
                      amount=amount, asset=asset, dt=datetime,
                      constraint=constraint)

    def __repr__(self):
        return "{name}({attrs})".format(name=self.__class__.__name__,
                                        attrs=self.__fail_args)


class MaxOrderCount(TradingControl):
    """
    TradingControl representing a limit on the number of orders that can be
    placed in a given trading day.
    """

    def __init__(self, on_error, max_count):

        super(MaxOrderCount, self).__init__(on_error, max_count=max_count)
        self.orders_placed = 0
        self.max_count = max_count
        self.current_date = None

    def validate(self,
                 asset,
                 amount,
                 portfolio,
                 algo_datetime,
                 algo_current_data):
        """
        Fail if we've already placed self.max_count orders today.
        """
        algo_date = algo_datetime.date()

        # Reset order count if it's a new day.
        if self.current_date and self.current_date != algo_date:
            self.orders_placed = 0
        self.current_date = algo_date

        if self.orders_placed >= self.max_count:
            self.handle_violation(asset, amount, algo_datetime)
        self.orders_placed += 1


class RestrictedListOrder(TradingControl):
    """TradingControl representing a restricted list of assets that
    cannot be ordered by the algorithm.

    Parameters
    ----------
    restrictions : zipline.finance.asset_restrictions.Restrictions
        Object representing restrictions of a group of assets.
    """

    def __init__(self, on_error, restrictions):
        super(RestrictedListOrder, self).__init__(on_error)
        self.restrictions = restrictions

    def validate(self,
                 asset,
                 amount,
                 portfolio,
                 algo_datetime,
                 algo_current_data):
        """
        Fail if the asset is in the restricted_list.
        """
        if self.restrictions.is_restricted(asset, algo_datetime):
            self.handle_violation(asset, amount, algo_datetime)


class MaxOrderSize(TradingControl):
    """
    TradingControl representing a limit on the magnitude of any single order
    placed with the given asset.  Can be specified by share or by dollar
    value.
    """

    def __init__(self, on_error, asset=None, max_shares=None,
                 max_notional=None):
        super(MaxOrderSize, self).__init__(on_error,
                                           asset=asset,
                                           max_shares=max_shares,
                                           max_notional=max_notional)
        self.asset = asset
        self.max_shares = max_shares
        self.max_notional = max_notional

        if max_shares is None and max_notional is None:
            raise ValueError(
                "Must supply at least one of max_shares and max_notional"
            )

        if max_shares and max_shares < 0:
            raise ValueError(
                "max_shares cannot be negative."
            )

        if max_notional and max_notional < 0:
            raise ValueError(
                "max_notional must be positive."
            )

    def validate(self,
                 asset,
                 amount,
                 portfolio,
                 algo_datetime,
                 algo_current_data):
        """
        Fail if the magnitude of the given order exceeds either self.max_shares
        or self.max_notional.
        """

        if self.asset is not None and self.asset != asset:
            return

        if self.max_shares is not None and abs(amount) > self.max_shares:
            self.handle_violation(asset, amount, algo_datetime)

        current_asset_price = algo_current_data.current(asset, "price")
        order_value = amount * current_asset_price

        too_much_value = (self.max_notional is not None and
                          abs(order_value) > self.max_notional)

        if too_much_value:
            self.handle_violation(asset, amount, algo_datetime)


class MaxPositionSize(TradingControl):
    """
    TradingControl representing a limit on the maximum position size that can
    be held by an algo for a given asset.
    """

    def __init__(self, on_error, asset=None, max_shares=None,
                 max_notional=None):
        super(MaxPositionSize, self).__init__(on_error,
                                              asset=asset,
                                              max_shares=max_shares,
                                              max_notional=max_notional)
        self.asset = asset
        self.max_shares = max_shares
        self.max_notional = max_notional

        if max_shares is None and max_notional is None:
            raise ValueError(
                "Must supply at least one of max_shares and max_notional"
            )

        if max_shares and max_shares < 0:
            raise ValueError(
                "max_shares cannot be negative."
            )

        if max_notional and max_notional < 0:
            raise ValueError(
                "max_notional must be positive."
            )

    def validate(self,
                 asset,
                 amount,
                 portfolio,
                 algo_datetime,
                 algo_current_data):
        """
        Fail if the given order would cause the magnitude of our position to be
        greater in shares than self.max_shares or greater in dollar value than
        self.max_notional.
        """

        if self.asset is not None and self.asset != asset:
            return

        current_share_count = portfolio.positions[asset].amount
        shares_post_order = current_share_count + amount

        too_many_shares = (self.max_shares is not None and
                           abs(shares_post_order) > self.max_shares)
        if too_many_shares:
            self.handle_violation(asset, amount, algo_datetime)

        current_price = algo_current_data.current(asset, "price")
        value_post_order = shares_post_order * current_price

        too_much_value = (self.max_notional is not None and
                          abs(value_post_order) > self.max_notional)

        if too_much_value:
            self.handle_violation(asset, amount, algo_datetime)


class LongOnly(TradingControl):
    """
    TradingControl representing a prohibition against holding short positions.
    """

    def __init__(self, on_error):
        super(LongOnly, self).__init__(on_error)

    def validate(self,
                 asset,
                 amount,
                 portfolio,
                 algo_datetime,
                 algo_current_data):
        """
        Fail if we would hold negative shares of asset after completing this
        order.
        """
        if portfolio.positions[asset].amount + amount < 0:
            self.handle_violation(asset, amount, algo_datetime)


class AssetDateBounds(TradingControl):
    """
    TradingControl representing a prohibition against ordering an asset before
    its start_date, or after its end_date.
    """

    def __init__(self, on_error):
        super(AssetDateBounds, self).__init__(on_error)

    def validate(self,
                 asset,
                 amount,
                 portfolio,
                 algo_datetime,
                 algo_current_data):
        """
        Fail if the algo has passed this Asset's end_date, or before the
        Asset's start date.
        """
        # If the order is for 0 shares, then silently pass through.
        if amount == 0:
            return

        normalized_algo_dt = pd.Timestamp(algo_datetime).normalize()

        # Fail if the algo is before this Asset's start_date
        if asset.start_date:
            normalized_start = pd.Timestamp(asset.start_date).normalize()
            if normalized_algo_dt < normalized_start:
                metadata = {
                    'asset_start_date': normalized_start
                }
                self.handle_violation(
                    asset, amount, algo_datetime, metadata=metadata)
        # Fail if the algo has passed this Asset's end_date
        if asset.end_date:
            normalized_end = pd.Timestamp(asset.end_date).normalize()
            if normalized_algo_dt > normalized_end:
                metadata = {
                    'asset_end_date': normalized_end
                }
                self.handle_violation(
                    asset, amount, algo_datetime, metadata=metadata)


class AccountControl(with_metaclass(abc.ABCMeta)):
    """
    Abstract base class representing a fail-safe control on the behavior of any
    algorithm.
    """

    def __init__(self, **kwargs):
        """
        Track any arguments that should be printed in the error message
        generated by self.fail.
        """
        self.__fail_args = kwargs

    @abc.abstractmethod
    def validate(self,
                 _portfolio,
                 _account,
                 _algo_datetime,
                 _algo_current_data):
        """
        On each call to handle data by TradingAlgorithm, this method should be
        called *exactly once* on each registered AccountControl object.

        If the check does not violate this AccountControl's restraint given
        the information in `portfolio` and `account`, this method should
        return None and have no externally-visible side-effects.

        If the desired order violates this AccountControl's contraint, this
        method should call self.fail().
        """
        raise NotImplementedError

    def fail(self):
        """
        Raise an AccountControlViolation with information about the failure.
        """
        raise AccountControlViolation(constraint=repr(self))

    def __repr__(self):
        return "{name}({attrs})".format(name=self.__class__.__name__,
                                        attrs=self.__fail_args)


class MaxLeverage(AccountControl):
    """
    AccountControl representing a limit on the maximum leverage allowed
    by the algorithm.
    """

    def __init__(self, max_leverage):
        """
        max_leverage is the gross leverage in decimal form. For example,
        2, limits an algorithm to trading at most double the account value.
        """
        super(MaxLeverage, self).__init__(max_leverage=max_leverage)
        self.max_leverage = max_leverage

        if max_leverage is None:
            raise ValueError(
                "Must supply max_leverage"
            )

        if max_leverage < 0:
            raise ValueError(
                "max_leverage must be positive"
            )

    def validate(self,
                 _portfolio,
                 _account,
                 _algo_datetime,
                 _algo_current_data):
        """
        Fail if the leverage is greater than the allowed leverage.
        """
        if _account.leverage > self.max_leverage:
            self.fail()


class MinLeverage(AccountControl):
    """AccountControl representing a limit on the minimum leverage allowed
    by the algorithm after a threshold period of time.

    Parameters
    ----------
    min_leverage : float
        The gross leverage in decimal form.
    deadline : datetime
        The date the min leverage must be achieved by.

    For example, min_leverage=2 limits an algorithm to trading at minimum
    double the account value by the deadline date.
    """

    @expect_types(
        __funcname='MinLeverage',
        min_leverage=(int, float),
        deadline=datetime
    )
    @expect_bounded(__funcname='MinLeverage', min_leverage=(0, None))
    def __init__(self, min_leverage, deadline):
        super(MinLeverage, self).__init__(min_leverage=min_leverage,
                                          deadline=deadline)
        self.min_leverage = min_leverage
        self.deadline = deadline

    def validate(self,
                 _portfolio,
                 account,
                 algo_datetime,
                 _algo_current_data):
        """
        Make validation checks if we are after the deadline.
        Fail if the leverage is less than the min leverage.
        """
        if (algo_datetime > self.deadline and
                account.leverage < self.min_leverage):
            self.fail()
