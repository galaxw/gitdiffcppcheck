import logging
import os

from diffcppcheck.cppcheck import report

logger = logging.getLogger(__name__)


def test_cppcheck_report():
    cppcheck_report = report.CppcheckReport("diffcppcheck/cppcheck/test/data/cppcheck-report.xml")
    keep_dict = {
        "main.c": [4]
    }
    cppcheck_report.keep_record(keep_dict)
    report_file_path = "cleaned_cppcheck_report.xml"
    cppcheck_report.store(report_file_path)
    import xml.etree.ElementTree as ET
    xml_report = ET.parse(report_file_path)
    xml_report_root = xml_report.getroot()
    errors = [error for error in xml_report_root.iter('error')]
    assert 1 == len(errors)
    logger.error(errors)
    error_file_name = errors[0].find('location').get('file')
    error_line = int(errors[0].find('location').get('line'))
    assert "main.c" == error_file_name
    assert 4 == error_line
