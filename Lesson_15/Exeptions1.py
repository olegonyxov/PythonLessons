class AirportNotFoundError(BaseException):
    pass


class CountryNonFoundError(BaseException):
    pass


class MultipleOptionsError(BaseException):
    pass


class NoOptionsFoundError(BaseException):
    pass


class IATACodeError(BaseException):
    pass
