from pathlib import Path


business_name = "Example Company"
category = "AI consulting"
location = "Casablanca, Morocco"
website = "https://example.com"

services = [
    "AI audit",
    "Business automation",
    "LLM visibility",
    "SEO, AEO and GEO strategy",
]

target_audience = [
    "SMBs",
    "Consultants",
    "B2B service providers",
    "Local businesses",
]

official_links = {
    "Website": "https://example.com",
    "LinkedIn": "https://linkedin.com/company/example",
    "Contact": "https://example.com/contact",
}

source_pages = [
    "https://example.com/",
    "https://example.com/about",
    "https://example.com/services",
    "https://example.com/contact",
]

suggested_ai_summary = (
    "Example Company helps businesses improve AI visibility, "
    "structure entity information and automate practical workflows."
)


def value_or_default(value):
    return value if value else "Not specified"


def format_list(items):
    if not items:
        return "- Not specified"
    return "\n".join(f"- {item}" for item in items)


def format_links(links):
    if not links:
        return "- Not specified"
    return "\n".join(f"- {label}: {url}" for label, url in links.items())


def article_for(value):
    if not value:
        return "a"
    return "an" if value[0].lower() in "aeiou" else "a"


def generate_llms_txt():
    content = f"""# {value_or_default(business_name)}

## Overview

{value_or_default(business_name)} is {article_for(category)} {value_or_default(category)} business based in {value_or_default(location)}.

## Website

{value_or_default(website)}

## Services

{format_list(services)}

## Target audience

{format_list(target_audience)}

## Official links

{format_links(official_links)}

## Source of truth pages

{format_list(source_pages)}

## Suggested AI summary

{value_or_default(suggested_ai_summary)}

## Important note

This file is intended to summarize public business information in a clear and structured format. It does not guarantee rankings, citations or recommendations in AI-generated answers.
"""

    output_path = Path("llms.txt")
    output_path.write_text(content, encoding="utf-8")
    return output_path


if __name__ == "__main__":
    path = generate_llms_txt()
    print(f"Generated {path}")
