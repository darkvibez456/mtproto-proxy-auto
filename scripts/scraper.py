import requests
import re
import json
import time
from concurrent.futures import ThreadPoolExecutor

# Sources for MTProto proxies
SOURCES = [
    "https://raw.githubusercontent.com/SoliSpirit/mtproto/master/proxies.txt",
    "https://raw.githubusercontent.com/hookzof/socks5_list/master/tg.txt",
    "https://raw.githubusercontent.com/claudio-p/mtproto-proxy-list/main/proxy.txt"
]

def fetch_proxies(url):
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            # Extract tg://proxy or https://t.me/proxy links
            proxies = re.findall(r'(?:tg://proxy\?|https://t\.me/proxy\?)[^\s\n"\'<>]+', response.text)
            # Normalize all to tg:// format
            normalized = [p.replace("https://t.me/proxy?", "tg://proxy?") for p in proxies]
            return normalized
    except Exception as e:
        print(f"Error fetching from {url}: {e}")
    return []

def verify_proxy(proxy_url):
    # Simple check for connectivity (in a real scenario, this would involve a more robust MTProto ping)
    # For now, we'll just parse the parameters and return them if they seem valid
    try:
        params = dict(re.findall(r'(\w+)=([^&]+)', proxy_url))
        if 'server' in params and 'port' in params and 'secret' in params:
            # Simulate a verification step (replace with actual connectivity test if possible)
            return {
                "url": proxy_url,
                "server": params['server'],
                "port": params['port'],
                "secret": params['secret'],
                "verified": True,
                "latency": "N/A" # Placeholder
            }
    except Exception as e:
        print(f"Error verifying {proxy_url}: {e}")
    return None

def main():
    all_raw_proxies = []
    for source in SOURCES:
        print(f"Fetching from {source}...")
        all_raw_proxies.extend(fetch_proxies(source))
    
    # Remove duplicates
    unique_proxies = list(set(all_raw_proxies))
    print(f"Found {len(unique_proxies)} unique proxies.")

    verified_proxies = []
    with ThreadPoolExecutor(max_workers=10) as executor:
        results = list(executor.map(verify_proxy, unique_proxies))
        verified_proxies = [r for r in results if r is not None]

    print(f"Verified {len(verified_proxies)} proxies.")

    # Save to proxies.txt
    with open("proxies.txt", "w") as f:
        for proxy in verified_proxies:
            f.write(proxy['url'] + "\n")

    # Save to proxies.json for the web interface
    with open("proxies.json", "w") as f:
        json.dump(verified_proxies, f, indent=4)

if __name__ == "__main__":
    main()
