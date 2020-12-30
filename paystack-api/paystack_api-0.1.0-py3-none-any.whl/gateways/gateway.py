from paystack.exceptions.invalid_parameter import InvalidParameters


class BaseGateway:
    gateway_path = ""

    def __init__(self, gateway):
        self.gateway = gateway
        self.config = gateway.config

    def post(self, url, params=None):
        if params is None:
            params = {}
        res = self.config.http().post(url, params)
        print(res)
        return res

    def get(self, url, query_params=None):
        if query_params is None:
            query_params = {}

        res = self.config.http().get(url, params=query_params)
        print(res)
        return res

    def put(self, url, params=None):
        if params is None:
            params = {}
        res = self.config.http().put(url, params)
        print(res)
        return res

    def delete(self, url):
        res = self.config.http().delete(url)
        print(res)
        return res

    def validate(self, fields, required=None):
        fields = dict(**fields)
        if required is None:
            required = []
        if len(fields) == 0:
            raise InvalidParameters("empty body cant be sent")
        for field in required:
            if field == "source":
                if "source" not in fields:
                    fields["source"] = "balance"
            if field not in fields:
                raise InvalidParameters(f"{field} is required")
            if fields[field] == "":
                raise InvalidParameters(f"{field} is required")
        return fields
