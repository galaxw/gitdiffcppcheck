import logging
import os

from diffcppcheck.diff import get_diff_info

logger = logging.getLogger(__name__)


def test_git_diff():
    diff_info = get_diff_info("diffcppcheck/diff/test/data/git.diff")
    expected_info = {
        "Lib/test/test_dbm_gnu.py": [121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134],
        "Lib/test/test_dbm_ndbm.py": [136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149],
        "Lib/test/test_unittest/testmock/testpatch.py": [1926],
        "Misc/NEWS.d/next/Library/2022-09-08-20-12-48.gh-issue-46412.r_cfTh.rst": [1],
        "Misc/NEWS.d/next/Tests/2022-09-08-18-31-26.gh-issue-96624.5cANM1.rst": [1],
        "Modules/_dbmmodule.c": [133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 450],
        "Modules/_gdbmmodule.c": [165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 601],
    }
    from unittest import TestCase
    acase = TestCase()
    for file_name in expected_info:
        acase.assertEqual(expected_info[file_name], diff_info[file_name], "changed lines should be the same")
