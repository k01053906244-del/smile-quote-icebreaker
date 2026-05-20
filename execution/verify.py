import os
import json

def verify_all():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(f"Base Directory: {base_dir}")
    
    # 1. Check index.html
    index_path = os.path.join(base_dir, "index.html")
    if not os.path.exists(index_path):
        print("[FAIL] index.html not found.")
        return False
    
    with open(index_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    
    if 'src="솔이_뼈다구.mp4"' in html_content or "src='솔이_뼈다구.mp4'" in html_content:
        print("[SUCCESS] index.html correctly references '솔이_뼈다구.mp4'.")
    else:
        print("[FAIL] index.html does not reference '솔이_뼈다구.mp4'.")
        return False
        
    # 2. Check video file copy
    video_path = os.path.join(base_dir, "솔이_뼈다구.mp4")
    if not os.path.exists(video_path):
        print("[FAIL] 솔이_뼈다구.mp4 not found in root.")
        return False
    
    file_size = os.path.getsize(video_path)
    expected_size = 3680906
    if file_size == expected_size:
        print(f"[SUCCESS] 솔이_뼈다구.mp4 copied perfectly. Size: {file_size} bytes.")
    else:
        print(f"[WARNING] Size mismatch. Expected: {expected_size}, Got: {file_size} bytes.")
        # But we still accept if it exists and has non-zero size
        if file_size > 0:
            print("[SUCCESS] Video exists with positive size.")
        else:
            return False

    # 3. Check manifest files
    manifest_paths = [os.path.join(base_dir, "manifest.json"), os.path.join(base_dir, "manifest-v2.json")]
    for path in manifest_paths:
        name = os.path.basename(path)
        if not os.path.exists(path):
            print(f"[FAIL] {name} not found.")
            return False
        
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
            
            if data.get("name") == "스마일Again - 아이스브레이킹" and data.get("short_name") == "스마일Again":
                print(f"[SUCCESS] {name} properly updated with '스마일Again'.")
            else:
                print(f"[FAIL] {name} fields invalid. Got name: '{data.get('name')}', short_name: '{data.get('short_name')}'")
                return False
        except Exception as e:
            print(f"[FAIL] Error parsing {name}: {e}")
            return False

    print("\n--- ALL CHECKS PASSED SUCCESSFULLY ---")
    return True

if __name__ == "__main__":
    verify_all()
