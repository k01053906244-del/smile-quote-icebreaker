
import re

def count_entries(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    humor_matches = re.findall(r'\{ category: ".*?\}', content)
    balance_matches = re.findall(r'\{ a: ".*?\}', content)
    
    print(f"File: {file_path}")
    print(f"Humor entries: {len(humor_matches)}")
    print(f"Balance entries: {len(balance_matches)}")

count_entries('index.html')
