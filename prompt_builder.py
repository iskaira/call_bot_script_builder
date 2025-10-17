import json
import argparse
from jinja2 import Template
from pathlib import Path


def build_prompt(input_path: str, output_path: str):
    # Read input JSON
    with open(input_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Load template (for simplicity, template is embedded in this file)
    with open('system_instruction.md', 'r', encoding='utf-8') as f:
        template_text = f.read()

    template = Template(template_text)
    rendered = template.render(**data)

    # Save the rendered prompt
    output_file = Path(output_path)
    output_file.write_text(rendered, encoding='utf-8')
    print(f"✅ Prompt has been generated and saved to {output_file.resolve()}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Build structured system prompt for debt collection scenario.")
    parser.add_argument("--input", required=True, help="Path to input JSON file")
    parser.add_argument("--output", required=True, help="Path to output Markdown file")
    args = parser.parse_args()

    build_prompt(args.input, args.output)
