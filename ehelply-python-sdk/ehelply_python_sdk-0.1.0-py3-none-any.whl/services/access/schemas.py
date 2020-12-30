from ehelply_python_sdk.services.service_schemas import *


class SearchTypeItem(BaseModel):
    uuid: str
    name: str
    slug: str
    summary: str
    created_at: str


class CreateType(BaseModel):
    name: str
    summary: str


class CreateTypeResponse(HTTPResponse):
    uuid: str
    partition_identifier: str
    name: str
    slug: str
    summary: str
    created_at: str


class CreateNode(BaseModel):
    name: str
    node: str
    summary: str


class CreateNodeResponse(HTTPResponse):
    uuid: str
    name: str
    node: str
    type_uuid: str
    summary: str
    created_at: str


class CreateGroup(BaseModel):
    name: str
    summary: str
    entity_identifiers: List[str] = []
    default: bool = False


class CreateGroupResponse(HTTPResponse):
    uuid: str
    partition_identifier: str
    name: str
    summary: str
    created_at: str
    default: bool


class CreateRole(BaseModel):
    name: str
    summary: str


class CreateRoleResponse(HTTPResponse):
    uuid: str
    partition_identifier: str
    name: str
    summary: str
    created_at: str


class AttachKeyToEntityResponse(HTTPResponse):
    entity_key_uuid: str
    key_uuid: str


class MakeRGTResponse(MessageResponse):
    group_uuid: str
    target_identifier: str
    role_uuid: str
