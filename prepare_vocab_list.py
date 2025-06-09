import json
import csv
from romkan import to_roma, to_hiragana, to_katakana

# Load the JSON file
input_file = "vocab/vocab.json"  # Replace with the path to your JSON file
output_file = "vocab/vocabulary.csv"

# Read the JSON data
with open(input_file, "r", encoding="utf-8") as file:
    data = json.load(file)



# Extract the "learnedLexems" array
learned_lexems = data.get("learnedLexemes", [])
print("learned_lexems:", learned_lexems)

# Open the CSV file for writing
with open(output_file, "w", encoding="utf-8", newline="") as csvfile:
    csv_writer = csv.writer(csvfile)
    
    # Write the header row
    csv_writer.writerow(["text", "romanji", "hiragana", "katakana", "translation"])
    
    # Iterate through the learnedLexems array
    for lexem in learned_lexems:
        text = lexem.get("text", "")
        print("text:", text)
        translations = lexem.get("translations", [])
        
        # Convert text to romanji, hiragana, and katakana
        romanji = to_roma(text)
        hiragana = to_hiragana(text)
        katakana = to_katakana(text)
        
        # Join translations with a semicolon
        translation = ";".join(translations)
        
        # Write the row to the CSV file
        csv_writer.writerow([text, romanji, hiragana, katakana, translation])

print(f"Vocabulary CSV file has been created: {output_file}")