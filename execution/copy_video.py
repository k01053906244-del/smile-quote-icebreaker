import os
import shutil

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    src = os.path.join(base_dir, 'resources', '솔이 뼈다구.mp4')
    dst = os.path.join(base_dir, '솔이_뼈다구.mp4')
    
    print(f"Source file: {src}")
    print(f"Destination file: {dst}")
    
    if not os.path.exists(src):
        print(f"Error: Source file does not exist at {src}")
        return
        
    try:
        shutil.copy2(src, dst)
        print("Success: Video file copied successfully.")
        
        # Verify the copied file size
        size = os.path.getsize(dst)
        print(f"Copied file size: {size} bytes")
    except Exception as e:
        print(f"Error occurred during copy: {e}")

if __name__ == '__main__':
    main()
