#                         MAIN FUNCTION                              #
# ------------------------------------------------------------------ #

import argparse
import os

from scanner.automaton import ac_setup
from scanner.scan_directory import *
from utils.results import *
from utils.compliance_check import *
from utils.rec import *
from crypto.algo_to_search import *


def main():

    parser = argparse.ArgumentParser(description="CryptoScan -- A secure development and auditing tool for conducting a cryptographic inventory and FIPS compliance check")
    
    parser.add_argument('source', type=str, help='directory of target source code')
    
    parser.add_argument('-s', '--scan', action='store_true', help='run an inventory scan with output sent to a text file')
    parser.add_argument('-c', '--compliance', action='store_true', help='run a FIPS 140-2/FIPS 140-3 compliance check')
    parser.add_argument('-r', '--recommend', action='store_true', help='run a list of recommended changes for cryptographic materials')

    sys_args = parser.parse_args()

    if sys_args.scan or sys_args.compliance or sys_args.recommend:

        code_directory = sys_args.source

        try:

            automaton = ac_setup(ALGORITHMS)
            print("\nScanning target source code...\n")

            results = directory_analysis(code_directory, automaton)

            source_name = os.path.basename(os.path.normpath(sys_args.source))

            log_file = f"tests/logs/{source_name}_cryptoscan.log"
            output_file = f"tests/{source_name}_cryptoscan.txt"
            compliance_file = f"tests/{source_name}_compliance.txt"
            recommend_file = f"tests/{source_name}_recommendations.txt"
            
            if sys_args.scan:
                print("Building cryptographic inventory...")
                with open(output_file, 'w') as f:
                    for file_path, positive in results.items():
                        result_string = output(file_path, positive, log_file, code_directory)
                        f.write(result_string)
                print(f"Results written to {output_file}\n")    

            if sys_args.compliance:
                print("Running FIPS compliance check for detected cryptographic materials...")
                try:
                    for file_path, positive in results.items():
                        perform_comp_check(results, compliance_file, log_file, code_directory)
                except Exception as e:
                    print(f"Something went wrong --> {e}")    
                print(f"Compliance results written to: {compliance_file}\n")

            if sys_args.recommend:
                print("Building a recommendation list for crypto detected...")
                try:
                    for file_path, positive in results.items():
                        perform_recommendation(results, recommend_file, log_file, code_directory)
                except Exception as e:
                    print(f"Failed to build list of recommendations --> {e}")
                print(f"Recommendation list written to: {recommend_file}")

        except Exception as e:
            print(f"Directory not found!!!\n ---> {e}")
    else:
        print("Run --help for usage information.")


if __name__ == '__main__':
    main()