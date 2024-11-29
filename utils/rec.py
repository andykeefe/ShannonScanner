import json
import logging
import os


def perform_recommendation(results, rec_file, log_file, target):
    logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file),
        ]
    )

    json_file = 'utils/rec.json'
    try:
        with open(json_file, 'r') as file:
            rec_data = json.load(file)
    except Exception as e:
        print(e)

    cat_map = {
        "Symmetric algorithms" : "symmetric",
        "Hash functions": "hash",
        "Modes of operation": "modes",
        "Digital signatures": "signature",
        "Libraries": "libraries"
    }

    found_nonrecommend = {}

    try:
        for file_path, positive in results.items():
            for category, algorithms in positive.items():
                mapped_category = cat_map.get(category)
                if mapped_category and mapped_category in rec_data:
                    for algorithm, patterns in algorithms.items():
                        for entry in rec_data[mapped_category]["nonrecommended"]:
                            if algorithm == entry["algorithm"]:
                                if algorithm not in found_nonrecommend:
                                    found_nonrecommend[algorithm] = {
                                        "files": set(),
                                        "reason": entry["reason"],
                                        "recommended": entry["recommended"],
                                        "rec_reason": entry["rec_reason"],
                                        "references": entry["references"],         
                                    }
                                found_nonrecommend[algorithm]["files"].add(file_path)
        logging.info("Recommendation made successfully.")
    except Exception as e:
        print(f"Recommendation failed --> {e}")
        logging.info("Recommendation failed.")

    trgt_dir = os.path.normpath(target)

    with open(rec_file, 'w') as f:
        for algorithm, details in found_nonrecommend.items():
            reasons = details["reason"]
            if isinstance(reasons, list):
                reason_str = "\n     - ".join(reasons)
            else:
                reason_str = reasons
            
            recommendations = details["recommended"]
            if isinstance(recommendations, list):
                recommend_str = "\n    - ".join(recommendations)
            else:
                recommend_str = recommendations

            rec_rsn = details["rec_reason"]
            if isinstance(rec_rsn, list):
                rsn_str = "\n    - ".join(rec_rsn)
            else:
                rsn_str = rec_rsn

            ref_str = details["references"]
            if isinstance(ref_str, list):
                ref_list = "\n    - ".join(ref_str)
            else:
                ref_list = ref_str

            f.write(f"NONRECOMMENDED CRYPTOGRAPHIC MATERIAL: {algorithm}\n")
            f.write(f"  - Why {algorithm} should not be used: {reason_str}\n")
            f.write(f"  - RECOMMENDATION: {recommend_str}\n")
            f.write(f"  - RECOMMENDATION REASONING: {rsn_str}\n")
            f.write(f'  - REFERENCE: \n    - {ref_list}\n')
            f.write(f"  - AFFECTED FILES:\n")
            for file_path in details["files"]:
                relative_path = os.path.relpath(file_path, start=trgt_dir)
                f.write(f"     - {relative_path}\n")
            f.write("\n\n")



