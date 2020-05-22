from unittest.mock import Mock

import pytest

from knb.errors import NotFoundError, PermissionDeniedError, StorageError
from knb.use_cases.update_note import IGateway, UseCase, Input, Output
from knb.utils import factory


def test_update_my_note():
    gateway: IGateway = Mock()
    note = factory.create_note()
    gateway.save_note.return_value = note, "1"
    uc = UseCase(gateway)
    input = Input(user_id="1", note_id="1", new_note=note)
    output: Output = uc(input)
    assert output.note == note


def test_forbidden_note():
    gateway: IGateway = Mock()

    gateway.get_note.side_effect = NotFoundError(type="", id="")
    uc = UseCase(gateway)
    note = factory.create_note()

    input = Input(user_id="1", note_id="1", new_note=note)
    output: Output = uc(input)
    assert output.note is None
    assert PermissionDeniedError() in output.errors


def test_error():
    gateway: IGateway = Mock()
    gateway.get_note.side_effect = StorageError()
    uc = UseCase(gateway)
    note = factory.create_note()

    input = Input(user_id="1", note_id="1", new_note=note)
    output: Output = uc(input)
    assert output.errors
