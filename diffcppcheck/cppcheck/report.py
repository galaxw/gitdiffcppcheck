from typing import Dict
from typing import List
import logging
import xml.etree.ElementTree as ET

logger = logging.getLogger(__name__)

class CppcheckReport():

    def __init__(self, report_file_path: str):
        self._report_xml = ET.parse(report_file_path)

    def keep_record(self, condition: Dict[str, List[int]]):
        xml_root = self._report_xml.getroot()
        node_tobe_removed = []
        for error_node in xml_root.iter('error'):
            location_node = error_node.find('location')
            if location_node is None:
                continue
            error_file_name = location_node.get('file')
            error_line = int(location_node.get('line'))
            if error_file_name not in condition:
                node_tobe_removed.append(error_node)
                continue
            if error_line not in condition[error_file_name]:
                logger.debug("Remove record %s: %s", error_file_name, error_line)
                node_tobe_removed.append(error_node)
                continue
        for node in node_tobe_removed:
            xml_root.find('errors').remove(node)

    def store(self, report_file_path: str):
        self._report_xml.write(report_file_path)
