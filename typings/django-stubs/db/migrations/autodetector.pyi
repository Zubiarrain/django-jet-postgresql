from collections.abc import Callable, Iterable
from typing import Any

from django.db.migrations.graph import MigrationGraph
from django.db.migrations.migration import Migration
from django.db.migrations.operations.base import Operation
from django.db.migrations.questioner import MigrationQuestioner
from django.db.migrations.state import ProjectState
from django.db.models.fields import Field

class MigrationAutodetector:
    from_state: ProjectState
    to_state: ProjectState
    questioner: MigrationQuestioner
    existing_apps: set[Any]
    def __init__(
        self, from_state: ProjectState, to_state: ProjectState, questioner: MigrationQuestioner | None = ...
    ) -> None: ...
    def changes(
        self,
        graph: MigrationGraph,
        trim_to_apps: set[str] | None = ...,
        convert_apps: set[str] | None = ...,
        migration_name: str | None = ...,
    ) -> dict[str, list[Migration]]: ...
    def deep_deconstruct(self, obj: Any) -> Any: ...
    def only_relation_agnostic_fields(
        self, fields: dict[str, Field]
    ) -> list[tuple[str, list[Any], dict[str, Callable | int | str]]]: ...
    def check_dependency(self, operation: Operation, dependency: tuple[str, str, str | None, bool | str]) -> bool: ...
    def add_operation(
        self,
        app_label: str,
        operation: Operation,
        dependencies: Iterable[tuple[str, str, str | None, bool | str]] | None = ...,
        beginning: bool = ...,
    ) -> None: ...
    def swappable_first_key(self, item: tuple[str, str]) -> tuple[str, str]: ...
    renamed_models: Any
    renamed_models_rel: Any
    def generate_renamed_models(self) -> None: ...
    def generate_created_models(self) -> None: ...
    def generate_created_proxies(self) -> None: ...
    def generate_deleted_models(self) -> None: ...
    def generate_deleted_proxies(self) -> None: ...
    renamed_fields: Any
    def generate_renamed_fields(self) -> None: ...
    def generate_added_fields(self) -> None: ...
    def generate_removed_fields(self) -> None: ...
    def generate_altered_fields(self) -> None: ...
    def create_altered_indexes(self) -> None: ...
    def generate_added_indexes(self) -> None: ...
    def generate_removed_indexes(self) -> None: ...
    def generate_altered_unique_together(self) -> None: ...
    def generate_altered_index_together(self) -> None: ...
    def generate_altered_db_table(self) -> None: ...
    def generate_altered_options(self) -> None: ...
    def generate_altered_order_with_respect_to(self) -> None: ...
    def generate_altered_managers(self) -> None: ...
    def arrange_for_graph(
        self, changes: dict[str, list[Migration]], graph: MigrationGraph, migration_name: str | None = ...
    ) -> dict[str, list[Migration]]: ...
    @classmethod
    def parse_number(cls, name: str) -> int: ...