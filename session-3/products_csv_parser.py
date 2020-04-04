import csv
import argparse
    
parser = argparse.ArgumentParser(description='Products file CSV Reader and Writer')
parser.add_argument('--file-input', type=str, required=True,
                    help='Input csv file to be read (format: "filename.csv")')
parser.add_argument('--file-output', type=str, required=True,
                    help='Final csv file with categorized products.(format: "filename.csv")')
args = parser.parse_args()


with open(args.file_input, newline='') as f:
    reader = csv.reader(f)
    categorized =[row for row in reader if row[25]!=""]
    #     for row in reader:
    #         if row[25] != None:
    #             categorized.append(row)
    #         else:
    #             continue   

with open(args.file_output, 'w', newline='') as f:
    writer = csv.writer(f)
    for row in categorized:
        writer.writerows([row])