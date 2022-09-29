# diffcppcheck tool

It is used to clean cppcheck report xml file, Remove records which is not changed in a specified range(a git diff log)

##
git diff code from
https://github.com/nathforge/gitdiffparser


## Usage

root@toolchain01:/home/wei.xiong/gerrit/gitdiffcppcheck# bazel run //diffcppcheck:diffcppcheck -- --help
usage: main.py [-h] [--git-diff-file GIT_DIFF_FILE] [--input-report INPUT_REPORT] [--output-report OUTPUT_REPORT] [--log-level {CRITCAL,ERROR,WARNING,INFO,DEBUG}]
               [--log-config-file LOG_CONFIG_FILE] [--error-log-root-dir ERROR_LOG_ROOT_DIR]

optional arguments:
  -h, --help            show this help message and exit
  --git-diff-file GIT_DIFF_FILE
                        git diff file path
  --input-report INPUT_REPORT
                        cppcheck report input file
  --output-report OUTPUT_REPORT
                        cppcheck report output file
  --log-level {CRITCAL,ERROR,WARNING,INFO,DEBUG}
                        level of messages to catch/display; level of messages to catch/display
  --log-config-file LOG_CONFIG_FILE
                        logging configuration file
  --error-log-root-dir ERROR_LOG_ROOT_DIR
                        the path to store error log for every case, one case will be one log file
