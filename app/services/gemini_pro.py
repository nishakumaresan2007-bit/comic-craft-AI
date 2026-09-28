import os

def generate_story(prompt: str, genre: str):
    # .env la key iruntha original Gemini use pannum, illa na dummy story return pannum
    # Ippothiku error vara koodathu-nu dummy-a vechirukken
    
    try:
        import google.generativeai as genai
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise Exception("No API Key")
        
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(f"Write a {genre} comic story for: {prompt}. Give 3 panels.")
        return response.text
    except Exception as e:
        # API key illa na ithu return aagum, error varathu
        return f"""
        **Genre:** {genre}
        **Prompt:** {prompt}

        **Panel 1:** A hero wakes up in a strange world.
        **Panel 2:** He finds a mysterious map leading to treasure.
        **Panel 3:** The adventure begins! (Add your Gemini API Key in .env to get real AI story)

        (Note: {str(e)})
        """