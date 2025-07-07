from datetime import datetime

def main():
    now = datetime.now()
    msg_start = f"Pipeline started at {now}\n"
    msg_end = f"Pipeline completed at {datetime.now()}\n"

    print(msg_start.strip())
    print(msg_end.strip())

    # Save logs to file
    with open("log.txt", "a") as log_file:
        log_file.write(msg_start)
        log_file.write(msg_end)
        log_file.write("-" * 50 + "\n")

if __name__ == "__main__":
    main()