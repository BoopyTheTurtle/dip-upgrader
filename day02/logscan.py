level_dict = {}
skipped = 0 

VALID_LEVELS = ("INFO", "WARN", "ERROR", "DEBUG") 

def parse_line(line):
    parts = line.split(maxsplit=4) 
    if len(parts) < 5: 
        raise ValueError("too few fields: " + repr(line))
    if parts[2] not in VALID_LEVELS: 
        raise ValueError("unknown level: " + repr(line))
    timestamp = parts[0] + " " + parts[1]
    log_dict = { 
        "timestamp": timestamp,
        "level": parts[2],
        "source": parts[3],
        "message": parts[4].strip()
    }
    return log_dict 

with open("app.log") as f:
    for line in f: 
        try: 
            log_dict = parse_line(line) 
            level = log_dict["level"]
            level_dict[level] = level_dict.get(level, 0) + 1
            
        except ValueError as e: 
            print(e)
            skipped += 1
    print(level_dict)
    print("skipped:", skipped)