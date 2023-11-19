import openai

# Set your OpenAI API key
api_key = ""

openai.api_key = api_key

def generate_video_description(transcript, title, keywords, length=500):
    print(keywords)
    prompt = f'''Create a fun and hooking, but not too intense YouTube video description for a video titled '{title}'. 
    This is the transcript of the video {transcript}. Keywords: {keywords}. 
    Description length should be around {length} characters.'''


    response = openai.ChatCompletion.create(
        model="gpt-4",  # Use the GPT-3.5 Turbo model
       messages = [
           {"role":"assistant","content": "you are to create fun youtube descriptions for videos with the given information"},
           {"role":"assistant","content": "NEVER repeat the same description EVER"},
           {"role":"assistant","content": f"This is an example of what the return response should look like {example}"},
           {"role":"user","content":prompt}
        ],
        max_tokens=length,
        temperature=0.7,
    )

    return response

def extract_summary_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    summaries = []
    current_summary = ""
    for line in lines:
        if line.startswith("Summary:"):
            current_summary = line[len("Summary:"):].strip()
        elif current_summary and line.strip() == "":
            summaries.append(current_summary)
            current_summary = ""
    
    return "\n".join(summaries)

transcript_file_path = "transcription.txt"

transcript = extract_summary_from_file(transcript_file_path)

example = "Are LAN parties still a thing? If not, this portable PC is making me want to make LAN parties a thing again. The KXRORS S500 is 15.9L, which makes it a slightly larger companion to KXRORSs S300 case (8.1L). The added space makes room for some ATX components and larger cooling options while staying small enough to grab by the handle and move around as needed. Follow along as I build an awesomely portable ITX gaming PC. Links below for components."

# Input data
title = "UNREAL Mini Gaming PC - PS5 on Steroids"
keywords = input("What are keywords in the video (seperate with commmas): ").lower()
keywords = keywords.replace(', ', ',')
keywords = keywords.split(',')

# Generate the video description

def generate_and_print_description(transcript, title, keywords, num_times=3):
    for _ in range(num_times):
        video_description = generate_video_description(transcript, title, keywords)
        generated_content = video_description['choices'][0]['message']['content']
        print(generated_content)
        print("-----")  # Just to separate the outputs

generate_and_print_description(transcript, title, keywords, num_times=3)