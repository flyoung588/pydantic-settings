from __future__ import annotations

import pytest
from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Value(BaseModel):
    name: str
    count: int


class AliasedValue(BaseModel):
    name: str = Field(validation_alias='label')
    count: int


@pytest.mark.parametrize('key', ['other', 'name', 'count'])
def test_model_valued_dict_key(monkeypatch, key):
    class Settings(BaseSettings):
        model_config = SettingsConfigDict(env_prefix='PROBE_', env_nested_delimiter='__')
        values: dict[str, Value]

    monkeypatch.setenv(f'PROBE_VALUES__{key.upper()}', '{"name":"ok","count":7}')
    assert Settings().values == {key: Value(name='ok', count=7)}


@pytest.mark.parametrize('key', ['other', 'name', 'label', 'count'])
def test_aliased_model_valued_dict_key(monkeypatch, key):
    class Settings(BaseSettings):
        model_config = SettingsConfigDict(env_prefix='PROBE_', env_nested_delimiter='__')
        values: dict[str, AliasedValue]

    monkeypatch.setenv(f'PROBE_VALUES__{key.upper()}', '{"label":"ok","count":7}')
    assert Settings().values == {key: AliasedValue(label='ok', count=7)}
