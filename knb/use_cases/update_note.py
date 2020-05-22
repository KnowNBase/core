import typing as t
from abc import ABCMeta
from dataclasses import dataclass, field

from knb.errors import BaseError, StorageError, NotFoundError, PermissionDeniedError
from knb.models import Note
from knb.use_cases import AbstractUseCase
from knb.use_cases.specs import Spec, AuthorSpec, FieldValueMatchSpec


@dataclass
class Input:
    user_id: str
    note_id: str
    new_note: Note


@dataclass
class Output:
    note: t.Optional[Note] = None
    errors: t.List[BaseError] = field(default_factory=list)

    def is_valid(self):
        return self.note is not None


class IGateway(metaclass=ABCMeta):
    def get_note(self, spec: Spec) -> Note:
        """"""

    def save_note(self, old_id: str, note: Note) -> t.Tuple[Note, str]:
        """"""


@dataclass(eq=False)
class UseCase(AbstractUseCase[Input, Output]):
    gateway: IGateway

    def _exec(self, input: Input) -> Output:
        # check that user own note
        spec: Spec = AuthorSpec(author_id=input.user_id)
        spec = spec.and_spec(FieldValueMatchSpec(id=input.note_id))
        try:
            self.gateway.get_note(spec)
            note, _ = self.gateway.save_note(input.note_id, input.new_note)
            return Output(note=note)
        except NotFoundError:
            error = PermissionDeniedError()
            return self._error_response(error)

    def _error_response(self, error: BaseError) -> Output:
        return Output(errors=[error])
