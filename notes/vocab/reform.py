# coding 'utf-8'

max_length = 0

def process_line(raw_line):
    stripped = raw_line.strip()
    return stripped 

def check_len(line):
    if len(line) > max_length: 
        max_length = len(line)
    return line
        
 
def read_three_lines_at_a_time(sourcefile_path):
    try:
        with open(sourcefile_path) as sourcefile:
            while True:
                idx = process_line(next(sourcefile))
                ko = check_len(process_line(next(sourcefile)))
                en = process_line(next(sourcefile))
                print idx, ko, en
    except StopIteration:
        pass

def main():
    sourcefile = 'freq'
    vocab_file = read_three_lines_at_a_time(sourcefile)

if __name__ == '__main__':
    main()

    

