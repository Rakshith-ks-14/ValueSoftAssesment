class PageNotLoadedException(Exception):
    def __init__(self, msg):
        self.msg = f"<ERROR>- {msg}"


class CheckboxNotSelectedException(Exception):
    def __init__(self, msg):
        self.msg = f"<ERROR>- {msg}"


class InvalidResponseException(Exception):
    def __init__(self, msg):
        self.msg = f"<ERROR>- {msg}"