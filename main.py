import openai
from youtube_transcript_api import YouTubeTranscriptApi

# Put your OpenAI API key here
openai.api_key = "OPEN-AI-API-KEY"

def extract_video_id(video_link):
    video_id = None
    if "watch?v=" in video_link:
        video_id = video_link.split("watch?v=")[-1]
    elif "youtu.be/" in video_link:
        video_id = video_link.split("youtu.be/")[-1]
    return video_id

def extract_subtitles(video_link):
    video_id = extract_video_id(video_link)
    if not video_id:
        print("Invalid video link.")
        return None

    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return transcript
    except Exception as e:
        print(f"Error: {e}")
        return None

video_link = input("Please enter video link: ")

subtitles = extract_subtitles(video_link)

# Initialize an empty list to store the subtitle texts
subtitle_texts = []

if subtitles:
    for subtitle in subtitles:
        subtitle_texts.append(subtitle['text'])  # Append each subtitle text to the list
else:
    print("No subtitles found or an error occurred.")

# Join the subtitle texts into a single string
subtitles_text = ''.join(subtitle_texts)

string = subtitles_text
part_length = len(string) // 4  # integer division to get the length of each part

part1 = string[:part_length]
part2 = string[part_length:2*part_length]
part3 = string[2*part_length:3*part_length]
part4 = string[3*part_length:]


model_engine1 = "text-davinci-003"
prompt1 = f"Here are the subtitles of a YouTube video. Please provide a detailed summary of this text without leaving any point in bullets: {part1}"

completion1 = openai.Completion.create(
    engine= model_engine1,
    prompt=prompt1,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

response1 = completion1.choices[0].text


model_engine2 = "text-davinci-003"
prompt2= f"Here are the subtitles of a YouTube video. Please provide a detailed summary of this text without leaving any point in bullets: {part2}"

completion2 = openai.Completion.create(
    engine= model_engine2,
    prompt=prompt2,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

response2 = completion2.choices[0].text

model_engine3 = "text-davinci-003"
prompt3 = f"Here are the subtitles of a YouTube video. Please provide a detailed summary of this text without leaving any point in bullets: {part3}"

completion3 = openai.Completion.create(
    engine= model_engine3,
    prompt=prompt3,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

response3 = completion3.choices[0].text

model_engine4 = "text-davinci-003"
prompt4 = f"Here are the subtitles of a YouTube video. Please provide a detailed summary of this text without leaving any point in bullets: {part4}"

completion4 = openai.Completion.create(
    engine= model_engine4,
    prompt=prompt4,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

response4 = completion4.choices[0].text


print(response1)
print(response2)
print(response3)
print(response4)
