import json
import logging
import os

def perform_comp_check(results, compliance_file, log_file, target):
    
    logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file),
        ]
    )


    json_file = 'utils/comp.json'
    try:
        with open(json_file, 'r') as file:
            compliance_data = json.load(file)
    except Exception as e:
        print(e)

    cat_map = {
        "Symmetric algorithms" : "symmetric",
        "Hash functions": "hash",
        "Digital signatures": "signature",
        "Libraries": "libraries"
    }

    found_noncompliant = {}
    try:
        for file_path, positive in results.items():
            for category, algorithms in positive.items():
                mapped_category = cat_map.get(category)
                if mapped_category and mapped_category in compliance_data:
                    for algorithm, patterns in algorithms.items():
                        for entry in compliance_data[mapped_category]["noncompliant"]:
                            if entry["algorithm"].lower() == algorithm.lower():
                                if algorithm not in found_noncompliant:
                                    found_noncompliant[algorithm] = {
                                        "files": set(),
                                        "reason": entry["reason"],
                                        "compliance": entry["compliance"]
                                    }
                                found_noncompliant[algorithm]["files"].add(file_path)
        logging.info(f"Compliance check processed successfully.")
    except Exception as e:
            print(f"Something failed --> {e}")
            logging.info("Compliance check failed.")
   
    trgt_dir = os.path.normpath(target)
    src_code = os.path.basename(target)

    with open(compliance_file, 'w') as f:
        for algorithm, details in found_noncompliant.items():
            reasons = details["reason"]
            recs = details["compliance"]
            if isinstance(reasons, list):
                reason_str = "\n     - ".join(reasons)
            else:
                reason_str = reasons
            if isinstance(recs, list):
                rec_str = "\n     - ".join(recs)
            else:
                rec_str = recs
            compliance_remediation = details["compliance"]
            f.write("***\n\n")
            f.write(f"NONCOMPLIANT CRYPTOGRAPHIC MATERIAL: {algorithm}\n")
            f.write(f"   - REASON: {reason_str}\n")
            f.write(f"   - COMPLIANCE RECOMMENDATION: {rec_str}\n")
            f.write(f"   - AFFECTED FILES:\n")
            for file_path in details["files"]:
                relative_path = os.path.relpath(file_path, start=trgt_dir)
                f.write(f"         - {relative_path}\n")
                

            f.write("\n***")
            f.write("\n\n")
