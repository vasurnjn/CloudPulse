def parse_logs(logs):
    parsed_logs=[]
    for line in logs:
                parts=line.split()
                if len(parts)<4:
                    continue
                timestamp=parts[0]+" "+parts[1]
                level=parts[2]
                message=" ".join(parts[3:])
                parsed_logs.append({"timestamp":timestamp,"level":level,"message":message})
    return parsed_logs
