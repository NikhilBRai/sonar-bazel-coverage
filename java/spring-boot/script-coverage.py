import subprocess
import re
import os

def get_git_diff_lines(commit_id, folder_path):
    """
    Get the lines that were changed in the specified commit and folder path using git diff.
    Returns a dictionary where the keys are file paths and the values are sets of line numbers.
    """
    command = ['git', 'diff', commit_id, '--unified=0', '--', folder_path]
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

    if result.returncode != 0:
        raise Exception(f"Error getting git diff: {result.stderr}")

    diff_lines = result.stdout
    changes = {}
    filename = ""
    changes_set = set()
    prev_line_num = None
    line_num = 1

    for line in diff_lines.splitlines():
        if line.startswith('diff --git'):
            if filename and changes_set and filename.endswith('.java'):
                changes[filename] = list(changes_set)
            filename = re.sub(r'^a/', '', line.split()[2])
            changes_set = set()
        elif line.startswith('@@ '):
            match = re.search(r'\+(\d+)', line)
            if match:
                line_num = int(match.group(1))
        elif line.startswith('+') and not (line.startswith('+++') or line.startswith('---')):
            if changes_set:
                if line_num != prev_line_num:
                    changes_set.add(line_num)
            else:
                changes_set.add(line_num)
            prev_line_num = line_num
            line_num += 1

    if filename and changes_set and filename.endswith('.java'):
        changes[filename] = list(changes_set)

    return changes


def parse_lcov_report(lcov_report_path):
    """
    Parse the LCOV report and return a dictionary with the file paths as keys and the coverage data as values.
    Each file will have a dictionary with DA, FN, FNDA, FNF, FNH as keys.
    """
    if not os.path.exists(lcov_report_path):
        raise FileNotFoundError(f"LCOV report not found at path: {lcov_report_path}")

    coverage_data = {}
    current_file = None
    coverage_record = None

    with open(lcov_report_path, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith('SF:'):
                current_file = line[3:]
                coverage_record = {'DA': [], 'LH': 0, 'LF': 0}
                coverage_data[current_file] = coverage_record
            elif line.startswith('DA:'):
                parts = line[3:].split(',')
                line_number = int(parts[0])
                coverage_hits = int(parts[1])
                coverage_record['DA'].append((line_number, coverage_hits))
            elif line.startswith('LH:'):
                coverage_record['LH'] = int(line[3:])
            elif line.startswith('LF:'):
                coverage_record['LF'] = int(line[3:])
    return coverage_data


def filter_lcov_by_git_diff(git_diff_changes, coverage_data):
    """
    Filter the LCOV report coverage data to only include the lines that were changed/added in the git diff.
    """
    filtered_coverage = {}

    for file, changed_lines in git_diff_changes.items():
        print("Changed Line=", changed_lines)
        for cd in coverage_data.keys():
            if cd in file:
                data = coverage_data[cd]
                print("Data=",data)
                filtered_da = [(line, hits) for line, hits in data['DA'] if line in changed_lines]

                # Calculate LH and LF based on filtered DA
                filtered_lh = len(filtered_da)
                filtered_lf = len(set(line for line, _ in filtered_da))

                if filtered_da:
                    filtered_coverage[cd] = {
                        'DA': filtered_da,
                        'LH': filtered_lh,
                        'LF': filtered_lf
                    }

    return filtered_coverage


def save_filtered_lcov_report(filtered_coverage, output_path):
    """
    Save the filtered LCOV data back into the LCOV format.
    """
    with open(output_path, 'w') as f:
        for file, data in filtered_coverage.items():
            f.write(f'SF:{file}\n')

            # Write DA (line coverage)
            for line, hits in data['DA']:
                f.write(f'DA:{line},{hits}\n')

            # Write LH and LF
            f.write(f'LH:{data["LH"]}\n')
            f.write(f'LF:{data["LF"]}\n')

            f.write('end_of_record\n')


def main(commit_id, folder_path, lcov_report_path, output_lcov_path):
    # Step 1: Get the git diff changes
    git_diff_changes = get_git_diff_lines(commit_id, folder_path)
    print("Diff Changes=", git_diff_changes)

    # Step 2: Parse the LCOV report
    coverage_data = parse_lcov_report(lcov_report_path)

    #print("Coverage Date", coverage_data)

    # Step 3: Filter LCOV data based on git diff
    filtered_coverage = filter_lcov_by_git_diff(git_diff_changes, coverage_data)

    # Step 4: Save the filtered LCOV report
    save_filtered_lcov_report(filtered_coverage, output_lcov_path)
    print(f"Filtered LCOV report saved to: {output_lcov_path}")


if __name__ == '__main__':
    # Replace with your commit_id, folder_path, lcov_report_path, and output_lcov_path
    commit_id = '6464cc4a6130b7da39dd8a70c82defb28282719a'
    folder_path = '/Users/nikhil.rai/personal-projects/sonar-bazel-coverage/java/spring-boot/src/main/java/com/bmuschko'
    lcov_report_path = '/Users/nikhil.rai/personal-projects/sonar-bazel-coverage/java/spring-boot/bazel-out/_coverage/_coverage_report.dat'
    output_lcov_path = '/Users/nikhil.rai/personal-projects/sonar-bazel-coverage/java/spring-boot/bazel-out/_coverage/filtered_coverage_report.dat'

    main(commit_id, folder_path, lcov_report_path, output_lcov_path)
