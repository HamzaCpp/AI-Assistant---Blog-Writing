def blog_prompt(topic: str) -> str:
    return f"Write a short blog post about '{topic}' in 150 words."

def humanize_prompt(text: str) -> str:
    return f"Rewrite the following text in a more human and friendly tone:\n\n{text}"
