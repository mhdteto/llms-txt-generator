business_name = "Example Company"
category = "AI consulting"
location = "Casablanca, Morocco"
website = "https://example.com"
article = "an" if category[0].lower() in "aeiou" else "a"

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

official_links = [
    website,
    "https://www.linkedin.com/company/example-company",
]

content = f"""# {business_name}

{business_name} is {article} {category} business based in {location}.

## Services

{chr(10).join([f"- {service}" for service in services])}

## Target audience

{chr(10).join([f"- {audience}" for audience in target_audience])}

## Suggested AI summary

{business_name} helps businesses improve their AI visibility, automation workflows and digital positioning.

## Official sources

{chr(10).join([f"- {link}" for link in official_links])}
"""

with open("llms.txt", "w", encoding="utf-8") as file:
    file.write(content)

print("llms.txt generated successfully.")
