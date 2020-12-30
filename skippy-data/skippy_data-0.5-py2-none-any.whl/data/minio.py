import os
import logging
from collections import defaultdict
from typing import List, Dict

from kubernetes import client, config
from minio import Minio
from minio.error import ResponseError

from skippy.data import utils
from skippy.data.priorities import get_best_node
from skippy.data.utils import get_bucket_urn, get_file_name_urn

_CONSUME_LABEL = 'data.consume'
__PRODUCE_LABEL = 'data.produce'


def list_minio_pods_node(node: str) -> List[str]:
    logging.debug('list minio pods...')
    # Load the configuration when running inside the cluster (by reading envs set by k8s)
    #config.load_kube_config()
    logging.debug('Loading in-cluster config...')
    config.load_incluster_config()
    api = client.CoreV1Api()
    # field selectors are a string, you need to parse the fields from the pods here
    app = 'minio'
    field_selector = 'spec.nodeName=' + node if node else None
    ret = api.list_namespaced_pod(watch=False, namespace="default", label_selector="app=" + app,
                                  field_selector=field_selector)
    for i in ret.items:
        for c in filter(lambda co: co.name == app, i.spec.containers):
            return ['{}:{}'.format(i.status.pod_ip, p.container_port) for p in c.ports]


def has_pod_file(urn: str, minio_addr: str) -> bool:
    try:
        if has_pod_bucket(get_bucket_urn(urn), minio_addr):
            stat = minio_client(minio_addr).stat_object(get_bucket_urn(urn), get_file_name_urn(urn))
            return stat.size > 0
        else:
            return False
    except ResponseError as err:
        logging.warning('MinioClientException: %s', err.message)
        return False


def has_pod_bucket(bucket: str, minio_addr: str) -> bool:
    try:
        return minio_client(minio_addr).bucket_exists(bucket)
    except ResponseError as err:
        logging.error('MinioClientException: %s', err.message)
        return False


def minio_client(minio_addr: str) -> Minio:
    minio_ac = os.environ.get('MINIO_AC', None)
    minio_sc = os.environ.get('MINIO_SC', None)
    client = Minio(minio_addr,
                   access_key=minio_ac,
                   secret_key=minio_sc,
                   secure=False)
    return client


def download_files(urns: str):
    logging.info('download files from urn(s)  %s' % urns)
    data_artifact = defaultdict(list)
    urn_paths = utils.get_urn_from_path(_CONSUME_LABEL, urns)
    for urn in urn_paths:
        data_file = download_file(urn)
        data_artifact[urn].append(data_file)
    return data_artifact


def download_file(urn: str) -> str:
    logging.info('download file from urn  %s' % urn)
    # what is the best pod
    # where do we make this decisison
    # find the best pod to download
    best_storage = get_best_node(urn)
    for minio_addr in list_minio_pods_node(best_storage):
        if has_pod_file(urn, minio_addr):
            client = minio_client(minio_addr)
            response = client.get_object(get_bucket_urn(urn), get_file_name_urn(urn))
            content = str(response.read().decode('utf-8'))
            logging.debug('file content: %s' % content)
            return content


def upload_file(content: str, urn: str) -> None:
    logging.info('upload urn  %s' % urn)
    urn = utils.get_urn_from_path(__PRODUCE_LABEL, urn)[0]
    best_none = get_best_node(urn)
    _wfile_name = get_file_name_urn(urn)
    text_file = open(_wfile_name, "wt")
    text_file.write(content)
    text_file.close()
    try:
        with open(_wfile_name, 'rb') as file_data:
            for minio_addr in list_minio_pods_node(best_none):
                if has_pod_bucket(get_bucket_urn(urn), minio_addr):
                    client = minio_client(minio_addr)
                    file_stat = os.stat(_wfile_name)
                    client.put_object(get_bucket_urn(urn), _wfile_name, file_data, file_stat.st_size,
                                      content_type='application/json')
                    break
    except ResponseError as e:
        logging.error('MinioClientException: %s', e.message)
