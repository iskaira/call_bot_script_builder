import json
import argparse
from jinja2 import Template
from pathlib import Path

REQUIRED_FIELDS = [
    "debtor_name",
    "total_amount",
    "extension_amount",
    "currency",
    "due_date",
    "days_overdue",
    "payment_methods",
    "callback_number",
    "language",
    "company_name",
    "assistant_name",
    "timezone",
]


def validate_input(data: dict):
    missing = [field for field in REQUIRED_FIELDS if field not in data]
    if missing:
        raise ValueError(f"Missing required keys in input JSON: {missing}")


def build_prompt(input_path: str, output_path: str):
    # Read input JSON
    with open(input_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Validate fields
    validate_input(data)

    # Load template
    template_file = Path("system_instruction.md")
    if not template_file.exists():
        raise FileNotFoundError("system_instruction.md not found in project directory.")

    with template_file.open('r', encoding='utf-8') as f:
        template_text = f.read()

    template = Template(template_text)
    rendered = template.render(**data)

    # Save rendered prompt
    output_file = Path(output_path)
    output_file.write_text(rendered, encoding='utf-8')
    print(f"✅ Prompt has been generated and saved to {output_file.resolve()}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Build structured system prompt for debt collection scenario.")
    parser.add_argument("--input", required=True, help="Path to input JSON file")
    parser.add_argument("--output", required=True, help="Path to output Markdown file")
    args = parser.parse_args()

    build_prompt(args.input, args.output)
