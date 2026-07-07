import tiktoken

# Load the tokenizer
encoding = tiktoken.get_encoding("cl100k_base")

def analyze_text(text):
    print("Text:", text)

    # Encode text into token IDs
    token = encoding.encode(text)

    # Decode each token into readable text
    tokens = [encoding.decode([token]) for token in token]

    print("Tokens:", tokens)
    print("Token count:", len(token))
    print("Word count:", len(text.split()))
    print("=" * 60)


# Example 1
analyze_text("AI is transforming software.")

# Example 2
analyze_text("antidisestablishmentarianism")

# Example 3 (English)
analyze_text("Artificial Intelligence is changing the world.")

# Example 4 (Urdu)
analyze_text("مصنوعی ذہانت دنیا کو بدل رہی ہے۔")

