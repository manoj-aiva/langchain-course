from dotenv import load_dotenv
import os
load_dotenv()

def main():
    print("Langchain")
    print(os.environ.get("OPEN_AI_KEY"))

if __name__== "__main__":
    main()