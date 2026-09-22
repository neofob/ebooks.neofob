#!/usr/bin/env python3

import os
import argparse
import sys

def split_file(filename, num_parts=4, output_dir='splits'):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split by double newline to get paragraphs
    paragraphs = content.split('\n\n')

    total_paras = len(paragraphs)
    print(f"Total paragraphs found: {total_paras}")

    paras_per_part = total_paras // num_parts
    extra_paras = total_paras % num_parts

    # Get base name without extension for output files
    base_name = os.path.splitext(os.path.basename(filename))[0]

    start = 0
    for i in range(num_parts):
        end = start + paras_per_part + (1 if i < extra_paras else 0)
        part_content = '\n\n'.join(paragraphs[start:end])

        output_filename = f"{base_name}-part{i+1}.txt"
        with open(os.path.join(output_dir, output_filename), 'w', encoding='utf-8') as f_out:
            f_out.write(part_content)

        num_in_part = end - start
        start = end
        print(f"Saved {output_filename} with {num_in_part} paragraphs.")

def count_paragraphs(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    paragraphs = content.split('\n\n')
    print(f"Total paragraphs in {filename}: {len(paragraphs)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Split a chapter file into multiple parts based on paragraphs.")
    parser.add_argument("filename", help="The input file to split or count.")
    parser.add_argument("-n", "--num-parts", type=int, default=4, help="Number of parts to split into (default: 4).")
    parser.add_argument("-c", "--count", action="store_true", help="Only count paragraphs and exit.")

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(0)

    args = parser.parse_args()

    if args.count:
        count_paragraphs(args.filename)
    else:
        split_file(args.filename, args.num_parts)
