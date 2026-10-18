import os,re
def color_check(r,g,b):
    if b>r and b>g:
        return True
    return False
def hex_to_rgb(hex_str):
    if len(hex_str)==3:
        hex_str="".join([char*2 for char in hex_str])
    r=int(hex_str[0:2],16)
    g=int(hex_str[2:4],16)
    b=int(hex_str[4:6],16)
    return r,g,b
def scan_directory_for_illegal_colors():
    hex_pattern=re.compile(r"#?\b([0-9a-fA-F]{6}\b|[0-9a-fA-F]{3}\b)")
    current_dir=os.path.dirname(os.path.realpath(__file__))
    print(f"Scanning directory recursively: {current_dir}\n")
    for root,_,files in os.walk(current_dir):
        for file in files:
            if file==os.path.basename(__file__):
                continue
            file_path=os.path.join(root, file)
            try:
                with open(file_path,"r",encoding="utf-8") as f:
                    for line_num,line in enumerate(f,start=1):
                        matches=hex_pattern.findall(line)
                        for match in matches:
                            if(not line.strip().startswith("#")and match.isdigit()):continue
                            try:
                                r,g,b=hex_to_rgb(match)
                                if color_check(r,g,b):
                                    print(f"[ILLEGAL COLOR] Found {match} (RGB: {r}, {g}, {b}) "f"in {os.path.relpath(file_path, current_dir)} on line {line_num}")
                                    print(f"  Line: {line.strip()}\n")
                            except ValueError:
                                continue
            except (UnicodeDecodeError,PermissionError):
                continue
scan_directory_for_illegal_colors()
