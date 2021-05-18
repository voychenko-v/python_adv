from .task_1 import string_rename
import pytest


@pytest.mark.parametrize('fun_on, fun_off', [('One', 'Один'), ('Two', 'Два'), ('Three', 'Три')])
def test_hw3(fun_on, fun_off):
    tmp_res = string_rename(fun_on)
    assert tmp_res == fun_off
