import json 
import sys 

level_dict = {}
skipped = 0 
errors = []

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
try: 
    with open("app.log") as f:
        for line in f: 
            try: 
                log_dict = parse_line(line) 
                level = log_dict["level"]
                level_dict[level] = level_dict.get(level, 0) + 1
                if level == "ERROR": 
                    errors.append(log_dict["message"])
                
            except ValueError as e: 
                print(e)
                skipped += 1
        print(level_dict)
        print(errors)
        print("skipped:", skipped)

except FileNotFoundError as e:
    print (e, file=sys.stderr) 
    sys.exit(1)

to_json = { 
    "counts": level_dict,
    "skipped": skipped,
    "errors": errors
}

with open ("report.json", "w") as fp: 
    json.dump(to_json, fp, indent=2)
