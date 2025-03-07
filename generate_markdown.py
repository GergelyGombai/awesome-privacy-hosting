import yaml

# YAML file containing hosting data
yaml_file = "hostings.yml"

# Mapping of cryptocurrencies to Shields.io badge colors and logo names
crypto_badges = {
    "BTC": {"color": "orange", "logo": "bitcoin"},
    "ETH": {"color": "blue", "logo": "ethereum"},
    "XMR": {"color": "darkorange", "logo": "monero"},
    "LTC": {"color": "gray", "logo": "litecoin"},
    "USDT": {"color": "green", "logo": "tether"},
    "altcoins": {"color": "purple", "logo": None},  # Special case for generic altcoins
}

payment_badges = {
    "PayPal": {"color": "blue", "logo": "paypal"},
    "Credit Card": {"color": "green", "logo": "visa"},
    "Bank Transfer": {"color": "purple", "logo": "bank"},
    "AliPay": {"color": "blue", "logo": "alipay"},
}

# Load YAML data
with open(yaml_file, "r") as file:
    data = yaml.safe_load(file)

# Generate Markdown
markdown = """# Awesome Hostings

A curated list of hosting providers that offer DDoS protection / no KYC / DMCA-ignored services.

"""

for host in data["hostings"]:
    name = host["name"]
    url = host["url"]
    description = host["description"]
    logo = host.get("logo", "")
    privacy_policy = host.get("privacy_policy", "")
    terms_of_service = host.get("terms_of_service", "")
    lowendtalk_profile = host.get("lowendtalk_profile", "")
    asn = host["asn"]
    looking_glass = host.get("looking_glass", "")
    dmca_ignored = host.get("dmca_ignored", False)
    ddos_protection = host.get("ddos_protection", False)
    stateful_protection = host.get("stateful_protection", False)
    max_ddos_capacity = host.get("max_ddos_capacity_tbps", None)
    kyc_required = host.get("kyc_required", False)
    hosting_types = ", ".join(host.get("types", []))
    cryptos = host.get("cryptos", [])
    other_payment_methods = host.get("other_payment_methods", [])

    # Generate crypto badges
    crypto_icons = " ".join(
        [f"![{crypto}](https://img.shields.io/badge/{crypto}-{crypto_badges.get(crypto, {'color': 'gray'})['color']}?style=flat{('&logo=' + crypto_badges[crypto]['logo'] + '&logoColor=white') if crypto in crypto_badges and crypto_badges[crypto]['logo'] else ''})"
         for crypto in cryptos]
    )

    # Generate other payment methods badges
    other_payment_methods_icons = " ".join(
        [f"![{payment_method}](https://img.shields.io/badge/{payment_method}-{payment_badges.get(payment_method, {'color': 'gray'})['color']}?style=flat{('&logo=' + payment_badges[payment_method]['logo'] + '&logoColor=white') if payment_method in payment_badges and payment_badges[payment_method]['logo'] else ''})"
         for payment_method in other_payment_methods]
    )

    markdown += f"## [{name}]({url})\n"
    if logo:
        markdown += f"![{name} Logo]({logo})\n\n"
    markdown += f"**Description:** {description}\n\n"
    markdown += f"**Hosting Types:** {hosting_types}\n\n" if hosting_types else ""
    markdown += f"**ASN:** [AS{asn}](https://bgp.tools/as/{asn})\n\n"
    markdown += f"**Looking Glass:** [{looking_glass}]({looking_glass})\n\n" if looking_glass else ""
    markdown += f"**DMCA Ignored:** {'✅ Yes' if dmca_ignored else '❌ No'}\n\n"
    markdown += f"**DDoS Protection:** {'✅ Yes' if ddos_protection else '❌ No'}\n\n"
    markdown += f"**Stateful DDoS Protection:** {'✅ Yes' if stateful_protection else '❌ No'}\n\n"
    markdown += f"**Max DDoS Capacity:** {max_ddos_capacity} Tbps\n\n" if max_ddos_capacity else ""
    markdown += f"**KYC Required:** {'✅ Yes' if kyc_required else '❌ No'}\n\n"
    markdown += f"**Privacy Policy:** [{privacy_policy}]({privacy_policy})\n\n" if privacy_policy else ""
    markdown += f"**Terms of Service:** [{terms_of_service}]({terms_of_service})\n\n" if terms_of_service else ""
    markdown += f"**LowEndTalk Profile:** [{lowendtalk_profile}]({lowendtalk_profile})\n\n" if lowendtalk_profile else ""
    markdown += f"**Accepts:** {crypto_icons} {other_payment_methods_icons}\n\n"

# Save to README.md
with open("README.md", "w") as md_file:
    md_file.write(markdown)

print("✅ README.md updated successfully!")
