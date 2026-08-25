msgs=["INFO", "DEBUG", "WARNING", "ERROR", "INFO", "CRITICAL", "WARNING"]

for msg in msgs:
    if msg=="INFO":
        continue
    elif msg=="CRITICAL":
        print("Breaking the loop as message is CRITICAL")
        break
    elif msg=="WARNING" or msg=="ERROR":
        print(f"ALERT : {msg}")
