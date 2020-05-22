import typing as t
from abc import ABCMeta
from dataclasses import dataclass, field

from knb.errors import BaseError
from knb.use_cases import AbstractUseCase


@dataclass
class Input:
    pass


@dataclass
class Output:
    errors: t.List[BaseError] = field(default_factory=list)


class IGateway(metaclass=ABCMeta):
    pass


@dataclass(eq=False)
class UseCase(AbstractUseCase[Input, Output]):
    gateway: IGateway

    def _exec(self, input: Input) -> Output:
        pass

    def _error_response(self, error: BaseError) -> Output:
        return Output(errors=[error])
