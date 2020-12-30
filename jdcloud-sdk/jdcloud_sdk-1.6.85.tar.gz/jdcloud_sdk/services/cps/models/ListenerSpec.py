# coding=utf8

# Copyright 2018 JDCLOUD.COM
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
#
# NOTE: This class is auto generated by the jdcloud code generator program.


class ListenerSpec(object):

    def __init__(self, loadBalancerId, protocol, port, algorithm, stickySession, name, healthCheck, realIp=None, description=None, healthCheckTimeout=None, healthCheckInterval=None, healthyThreshold=None, unhealthyThreshold=None, serverGroupId=None):
        """
        :param loadBalancerId:  负载均衡实例ID
        :param protocol:  协议, 如TCP
        :param port:  端口1-65535
        :param algorithm:  调度算法，取值wrr（加权轮询）|wlc（加权最小连接数）|conhash（源IP）)
        :param stickySession:  是否开启会话保持，取值on|off
        :param realIp: (Optional) 是否获取真实ip，取值on|off
        :param name:  名称
        :param description: (Optional) 描述
        :param healthCheck:  是否开启健康检查，取值on|off
        :param healthCheckTimeout: (Optional) 健康检查响应的最大超时时间，单位s
        :param healthCheckInterval: (Optional) 健康检查响应的最大间隔时间，单位s
        :param healthyThreshold: (Optional) 健康检查结果为success的阈值
        :param unhealthyThreshold: (Optional) 健康检查结果为fail的阈值
        :param serverGroupId: (Optional) 服务器组id
        """

        self.loadBalancerId = loadBalancerId
        self.protocol = protocol
        self.port = port
        self.algorithm = algorithm
        self.stickySession = stickySession
        self.realIp = realIp
        self.name = name
        self.description = description
        self.healthCheck = healthCheck
        self.healthCheckTimeout = healthCheckTimeout
        self.healthCheckInterval = healthCheckInterval
        self.healthyThreshold = healthyThreshold
        self.unhealthyThreshold = unhealthyThreshold
        self.serverGroupId = serverGroupId
