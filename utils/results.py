#                      CENTRAL OUTPUT OPERATIONS                      #
# ------------------------------------------------------------------- #
import logging
import os

SYMM = 'Symmetric algorithms'
MODE = 'Modes of operation'


def detector(algorithms, category):
    op_line = [f"   {category}:\n"]
    op_line.extend(f"    - {algorithm}\n" for algorithm in algorithms.keys())
    result = ''
    
    return ''.join(op_line)


def output(file_path, positive, log_file, target):
    
    logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file),
        ]
    )
    
    rel_path = os.path.relpath(file_path, start=target)
    has_symmetric = False
    op_lines = []

    for category, algorithms in positive.items():
        if algorithms:
            if category == SYMM:
                has_symmetric = True
                
            if not op_lines:
                op_lines.append(f"\nLocation: {rel_path}\n")
            
            if category != MODE:
                op_lines.append(detector(algorithms, category))

        """ I was getting duplicates for the modes of operation, as in for each location
        where modes of operation were found, it would print them twice. After a lot of trial
        and error, this was the avenue I took for getting rid of this duplicate. Probably not
        the most elegant, but it works!"""        

        if has_symmetric and MODE in positive and positive[MODE]:
            op_lines.append(detector(positive[MODE], MODE))
            positive[MODE] = None
            logging.info("Modes of operation processed without duplicate instances.")
    
    return ''.join(op_lines)
