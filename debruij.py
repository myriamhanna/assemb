import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_arguments("-i")
    parser.add_arguments("-k")
    parser.add_arguments("-o")
    args = parser.parse_args()


def read_fastq(fpath):
    
    with open(fpath, 'r') as file:
        for line in file:


            yield next(file)




if __name__ == "__main__":
    main()
