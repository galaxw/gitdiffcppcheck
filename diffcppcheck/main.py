"""
git diff files with cppcheck tool
"""
import argparse
import logging
from typing import Any
from typing import Dict
from typing import Generator
from typing import List

from diffcppcheck.diff import get_diff_info
from diffcppcheck.cppcheck import report

logger = logging.getLogger(__name__)

def get_args() -> argparse.Namespace:
    """Parse commandline."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--git-diff-file',
        type=str,
        dest='git_diff_file',
        help='git diff file path',
    )
    parser.add_argument(
        '--input-report',
        type=str,
        dest='input_report',
        help='cppcheck report input file',
    )
    parser.add_argument(
        '--output-report',
        type=str,
        dest='output_report',
        help='cppcheck report output file',
    )
    parser.add_argument(
        '--log-level',
        choices=['CRITCAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG'],
        default='WARNING',
        help='level of messages to catch/display; level of messages to catch/display',
    )
    parser.add_argument(
        '--log-config-file',
        type=str,
        help='logging configuration file',
    )
    parser.add_argument(
        '--error-log-root-dir',
        type=str,
        dest='error_log_root_dir',
        default='/tmp',
        help='the path to store error log for every case, one case will be one log file',
    )
    args = parser.parse_args()
    return args


def main(args: Any = None) -> None:
    """git diff cppcheck main function"""
    if args is None:
        args = get_args()

    if args.log_config_file:
        import logging.config
        logging.config.fileConfig(args.log_config_file)
    else:
        import logging
        logging.getLogger().setLevel(level=args.log_level)
    diff_info = get_diff_info(args.git_diff_file)
    logger.info("Changed content:")
    for file_name, changed_lines in diff_info.items():
        logger.info("file name: %s: %s", file_name, str(changed_lines))
    cppcheck_report = report.CppcheckReport(args.input_report)
    cppcheck_report.keep_record(diff_info)
    cppcheck_report.store(args.output_report)


if __name__ == '__main__':
    main()
