from datetime import datetime

def convert_to_srt(data, words_per_subtitle=15):
    subtitles = []
    index = 1

    for line in data:
        timing, text = line.split("] ")
        start, end = timing[1:].split(" -> ")

        # Add hours if missing
        if len(start.split(':')) < 3:
            start = '00:' + start
        if len(end.split(':')) < 3:
            end = '00:' + end

        # Split text into chunks of words_per_subtitle words
        words = text.strip().split()
        for i in range(0, len(words), words_per_subtitle):
            chunk = words[i:i+words_per_subtitle]
            chunk_text = ' '.join(chunk)

            # Adjust timing based on the number of words
            start_time = datetime.strptime(start, '%H:%M:%S.%f')
            end_time = datetime.strptime(end, '%H:%M:%S.%f')
            duration = (end_time - start_time) / len(words)
            chunk_start = start_time + duration * i
            chunk_end = chunk_start + duration * len(chunk)

            subtitle = f"{index}\n{chunk_start.strftime('%H:%M:%S.%f')[:-3]} --> {chunk_end.strftime('%H:%M:%S.%f')[:-3]}\n{chunk_text}\n\n"
            subtitles.append(subtitle)

            index += 1

    return subtitles

def write_srt(subtitles, output_file):
    with open(output_file, 'w') as file:
        file.writelines(subtitles)

def read_subtitle_file(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

data = read_subtitle_file('subtitle.txt')
subtitles = convert_to_srt(data)
write_srt(subtitles, "output.srt")
def write_srt(subtitles, output_file):
    with open(output_file, 'w') as file:
        file.writelines(subtitles)

def read_subtitle_file(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

data = read_subtitle_file('subtitle.txt')
subtitles = convert_to_srt(data)
write_srt(subtitles, "output.srt")