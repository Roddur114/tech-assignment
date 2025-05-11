from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq()

def summarize_text(text):
    completion = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant that summarizes text into 5 to 10 concise sentences while preserving key ideas and context.Return only the summary without any prefix like 'Here is a summary of the text in 7 sentences:'"
            },
            {
                "role": "user",
                "content": f"Please summarize the following text in 5 to 10 sentences:\n\n{text}\n\n return only the summarization."
            }
        ],
        temperature=1,
        max_completion_tokens=1024,
        top_p=1,
        stream=True,
        stop=None,
    )

    response = ""
    for chunk in completion:
        content = chunk.choices[0].delta.content
        if content:
            response += content
    return response
