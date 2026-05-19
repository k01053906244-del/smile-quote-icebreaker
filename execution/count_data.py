import re

def count_items(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        humor_matches = re.findall(r'\{ category: ".*?", situation: ".*?", guide: ".*?", joke: ".*?" \}', content)
        balance_matches = re.findall(r'\{ a: ".*?", b: ".*?" \}', content)
        
        print(f"File: {file_path}")
        print(f"HumorData items: {len(humor_matches)}")
        print(f"BalanceDB items: {len(balance_matches)}")
    except Exception as e:
        print(f"Error reading {file_path}: {e}")

count_items('index.html')
count_items('resources/index.html')
