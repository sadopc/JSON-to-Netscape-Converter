import tkinter as tk
from tkinter import scrolledtext, messagebox
import json
import sys # Keep sys for potential future use, though not strictly needed now

def convert_json_to_netscape(json_string):
    """Converts a JSON string of cookies to Netscape format."""
    try:
        cookies_data = json.loads(json_string)
        if not isinstance(cookies_data, list):
            return "Error: Input JSON must be a list of cookies."

        netscape_output = [
            "# Netscape HTTP Cookie File",
            "# http://curl.haxx.se/rfc/cookie_spec.html",
            "# This is a generated file! Do not edit.\n"
        ]

        for cookie in cookies_data:
            if not isinstance(cookie, dict):
                print(f"Warning: Skipping non-dictionary item in list: {cookie}")
                continue # Skip if the item isn't a dictionary

            # Extract fields with defaults
            domain = cookie.get('domain', '')
            host_only = cookie.get('hostOnly', False)
            path = cookie.get('path', '/')
            secure = cookie.get('secure', False)
            expiration_date = cookie.get('expirationDate')
            name = cookie.get('name', '')
            value = cookie.get('value', '')

            # Process expiration date
            if expiration_date is None:
                expires = 0
            else:
                try:
                    expires = int(expiration_date)
                except (ValueError, TypeError):
                    print(f"Warning: Could not parse expirationDate '{expiration_date}' for cookie '{name}'. Using 0.")
                    expires = 0

            # Determine Netscape format fields
            include_subdomains = "FALSE" if host_only else "TRUE"
            domain_output = ('.' + domain) if not host_only and not domain.startswith('.') else domain
            secure_flag = "TRUE" if secure else "FALSE"

            # Format the line
            line = f"{domain_output}\t{include_subdomains}\t{path}\t{secure_flag}\t{expires}\t{name}\t{value}"
            netscape_output.append(line)

        return "\n".join(netscape_output)

    except json.JSONDecodeError:
        return "Error: Invalid JSON format. Please paste valid JSON."
    except Exception as e:
        return f"An unexpected error occurred during conversion: {e}"

def perform_conversion():
    """Gets JSON from input, converts it, and displays in output."""
    json_input = input_text.get("1.0", tk.END).strip()
    if not json_input:
        messagebox.showwarning("Input Empty", "Please paste JSON cookie data into the input box.")
        return

    result = convert_json_to_netscape(json_input)

    output_text.config(state=tk.NORMAL) # Enable writing
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, result)
    output_text.config(state=tk.DISABLED) # Disable writing

    if "Error:" not in result:
         messagebox.showinfo("Success", "Conversion complete!")


def copy_to_clipboard():
    """Copies the content of the output text area to the clipboard."""
    output_content = output_text.get("1.0", tk.END).strip()
    if output_content and "Error:" not in output_content:
        root.clipboard_clear()
        root.clipboard_append(output_content)
        messagebox.showinfo("Copied", "Netscape cookies copied to clipboard!")
    elif "Error:" in output_content:
         messagebox.showwarning("Cannot Copy", "Cannot copy error messages.")
    else:
        messagebox.showwarning("Output Empty", "Nothing to copy.")

# --- GUI Setup ---
root = tk.Tk()
root.title("JSON Cookie to Netscape Converter")

# Input Area
input_label = tk.Label(root, text="Paste JSON Cookies Here:")
input_label.pack(pady=(10, 0))
input_text = scrolledtext.ScrolledText(root, height=10, width=60, wrap=tk.WORD)
input_text.pack(pady=5, padx=10, fill=tk.BOTH, expand=True)

# Convert Button
convert_button = tk.Button(root, text="Convert", command=perform_conversion)
convert_button.pack(pady=5)

# Output Area
output_label = tk.Label(root, text="Netscape Format Output:")
output_label.pack(pady=(10, 0))
output_text = scrolledtext.ScrolledText(root, height=10, width=60, wrap=tk.WORD)
output_text.pack(pady=5, padx=10, fill=tk.BOTH, expand=True)
output_text.config(state=tk.DISABLED) # Make output read-only initially

# Copy Button
copy_button = tk.Button(root, text="Copy Output to Clipboard", command=copy_to_clipboard)
copy_button.pack(pady=10)

# Start the GUI event loop
root.mainloop()
