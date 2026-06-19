import re
import sys

html_path = r"C:\Users\Vision\.gemini\antigravity\scratch\Aurora-portfolio\index.html"

try:
    with open(html_path, "r", encoding="utf-8") as f:
        html = f.read()
    
    # Check if there is any unclosed tag or mismatched script tag
    script_matches = re.findall(r"<script>.*?</script>", html, re.DOTALL)
    print(f"Found {len(script_matches)} script tags")
    
    # Parse style tags
    style_matches = re.findall(r"<style>.*?</style>", html, re.DOTALL)
    print(f"Found {len(style_matches)} style tags")
    
    # Check JS syntax for any basic error using node (if available)
    # Let's extract the JS and check it
    js_blocks = re.findall(r"<script>(.*?)</script>", html, re.DOTALL)
    for idx, js in enumerate(js_blocks):
        print(f"JS Block {idx}: {len(js)} chars")
        # Check basic syntax
        # Check matching curly braces, parentheses, brackets
        braces = 0
        parens = 0
        brackets = 0
        for pos, char in enumerate(js):
            if char == '{': braces += 1
            elif char == '}': braces -= 1
            elif char == '(': parens += 1
            elif char == ')': parens -= 1
            elif char == '[': brackets += 1
            elif char == ']': brackets -= 1
            
        print(f"  Braces: {braces}, Parens: {parens}, Brackets: {brackets}")
        if braces != 0 or parens != 0 or brackets != 0:
            print("  Mismatched brackets detected!")
            
except Exception as e:
    print(f"Error: {e}")
