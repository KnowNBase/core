from dataclasses import dataclass


class Spec:
    def and_spec(self, other: "Spec") -> "Spec":
        return AndSpec(self, other)

    def or_spec(self, other: "Spec") -> "Spec":
        return OrSpec(self, other)


@dataclass
class OrSpec(Spec):
    left: Spec
    right: Spec


@dataclass
class AndSpec(Spec):
    left: Spec
    right: Spec


@dataclass
class PageSpec(Spec):
    page: int
    items_per_page: int


@dataclass
class AuthorSpec(Spec):
    author_id: str


class FieldValueMatchSpec(Spec):
    def __init__(self, **kwargs):
        kws = list(kwargs.items())
        assert len(kws) > 0
        self.field_name, self.field_value = kws[0]
