from .aggregator import aggregator


def get_diff_info(diff_file_path: str):
    diff_dict = {}
    with open(diff_file_path, 'r') as diff_file:
        infos = aggregator(line_parser.parse_lines(diff_file))
        for info in infos:
            if info is None:
                # Ignore None element
                continue
            if info['is_binary']:
                # Ignore binary file
                continue
            line_numbers = diff_dict.get(info['to']['file'], [])
            for chunk in info['chunks']:
                line_numbers += [line_info['to_line_number'] for line_info in chunk['lines'] if line_info['action'] == 'add']
            diff_dict[info['to']['file']] = line_numbers

    return diff_dict


def get_diff_info1(diff_file_path: str):
    diff_list = []
    with open(diff_file_path, 'r') as diff_file:
        infos = aggregator(line_parser.parse_lines(diff_file))
        for info in infos:
            if info is None:
                # Ignore None element
                continue
            diff_list.append(info)

    return {'diff': diff_list}
