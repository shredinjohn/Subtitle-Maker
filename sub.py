import re

def convert_to_srt(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    srt_format = ""
    for i, line in enumerate(lines):
        # Extract the timestamps and text using regex
        match = re.match(r'\[(\d+:\d+\.\d+) -> (\d+:\d+\.\d+)\]  (.*)', line)
        if match:
            start_time, end_time, text = match.groups()

            # Add hours to the timestamps and replace '.' with ','
            start_time = "00:" + start_time.replace('.', ',')
            end_time = "00:" + end_time.replace('.', ',')

            srt_format += f"{i+1}\n"
            srt_format += f"{start_time} --> {end_time}\n"
            srt_format += f"{text}\n\n"

    # Remove trailing empty lines
    srt_format = srt_format.rstrip('\n')

    with open('output.srt', 'w') as file:
        file.write(srt_format)

convert_to_srt('data.txt')