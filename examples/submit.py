"""Submit and poll a spicy-catalog image endpoint through Muapi.

Usage:
    export MUAPI_API_KEY="your-api-key"
    python examples/submit.py seedream5-t2i
    python examples/submit.py seedream45-edit
"""

import os
import sys
import time

import requests

BASE = "https://api.muapi.ai/api/v1"
TERMINAL = {"completed", "succeeded", "success", "failed", "error", "cancelled"}

T2I_PROMPT = "A cinematic editorial portrait with dramatic red lighting and intricate styling"
EDIT_PROMPT = "Change the jacket to a glossy black leather jacket while preserving the pose and lighting"
SOURCE = "https://example.com/source.jpg"  # replace with a public image URL

JOBS = {
    "seedream5-t2i": ("bytedance-seedream-5.0-pro",
                      {"prompt": T2I_PROMPT, "aspect_ratio": "2:3", "resolution": "2K"}),
    "seedream5-edit": ("bytedance-seedream-5.0-pro-edit",
                       {"prompt": EDIT_PROMPT, "images_list": [SOURCE], "resolution": "2K"}),
    "seedream45-t2i": ("bytedance-seedream-v4.5",
                       {"prompt": T2I_PROMPT, "aspect_ratio": "2:3", "quality": "high"}),
    "seedream45-edit": ("bytedance-seedream-v4.5-edit",
                        {"prompt": EDIT_PROMPT, "images_list": [SOURCE], "quality": "high"}),
    "qwen3-t2i": ("qwen3-text-to-image",
                  {"prompt": T2I_PROMPT, "aspect_ratio": "2:3", "resolution": "2k"}),
    "qwen3-edit": ("qwen3-image-to-image",
                   {"prompt": EDIT_PROMPT, "images_list": [SOURCE], "resolution": "2k"}),
    "qwen2-t2i": ("qwen-image-2.0",
                  {"prompt": T2I_PROMPT, "aspect_ratio": "3:4"}),
    "qwen2-edit": ("qwen-image-2.0-edit",
                   {"prompt": EDIT_PROMPT, "images_list": [SOURCE]}),
    "wan27-t2i": ("wan2.7-text-to-image",
                  {"prompt": T2I_PROMPT, "aspect_ratio": "2:3"}),
    "wan27-edit": ("wan2.7-image-edit",
                   {"prompt": EDIT_PROMPT, "images_list": [SOURCE]}),
    "grok-t2i": ("grok-imagine-text-to-image",
                 {"prompt": T2I_PROMPT, "aspect_ratio": "2:3"}),
    "grok2-t2i": ("grok-imagine-image-2",
                  {"prompt": T2I_PROMPT, "aspect_ratio": "2:3"}),
    "z-image-turbo": ("z-image-turbo",
                      {"prompt": T2I_PROMPT, "width": 1024, "height": 1024}),
}


def main():
    api_key = os.environ.get("MUAPI_API_KEY")
    if not api_key:
        sys.exit("Set MUAPI_API_KEY first.")
    if len(sys.argv) != 2 or sys.argv[1] not in JOBS:
        sys.exit("Usage: python examples/submit.py {" + "|".join(JOBS) + "}")

    endpoint, payload = JOBS[sys.argv[1]]
    headers = {"x-api-key": api_key, "Content-Type": "application/json"}

    resp = requests.post(f"{BASE}/{endpoint}", headers=headers, json=payload, timeout=60)
    resp.raise_for_status()
    request_id = resp.json()["request_id"]
    print(f"Submitted {endpoint}: request_id={request_id}")

    for _ in range(120):
        result = requests.get(f"{BASE}/predictions/{request_id}/result", headers=headers, timeout=60)
        result.raise_for_status()
        body = result.json()
        status = str(body.get("status", "")).lower()
        print(f"status={status}")
        if status in TERMINAL:
            print(body)
            return
        time.sleep(3)
    sys.exit("Timed out waiting for the result; poll the request_id again later.")


if __name__ == "__main__":
    main()
