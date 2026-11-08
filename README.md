# Spicy AI Image Generator API Examples with Muapi

Compare the image models listed in Muapi's spicy AI image generator catalog — Seedream 5.0 Pro and 4.5, Qwen Image 3.0 and 2.0, Wan 2.7 Image, Grok Imagine and Z-Image Turbo — across text-to-image and image-to-image (editing), all behind one API key and one request format. This guide covers Muapi endpoints only; it does not document the upstream providers' direct APIs. Moderation behavior varies by model and can change, so test your own prompts, and remember you remain responsible for complying with Muapi's [terms](https://muapi.ai/terms) and applicable law.

## Related Projects

- [MuAPI](https://muapi.ai) — Unified API for image, video, and audio generation across hundreds of AI models.
- [Spicy AI Video Generator API](https://github.com/Anil-matcha/Spicy-AI-Video-Generator-API) — the video-side companion to this guide.
- [Awesome Uncensored AI Image Models](https://github.com/Anil-matcha/awesome-uncensored-ai-image-models) — catalog of uncensored image models.
- [Seedream 5 Pro API](https://github.com/Anil-matcha/Seedream-5-Pro-API) — Seedream 5.0 Pro examples.
- [Qwen Image API](https://github.com/Anil-matcha/Qwen-Image-API) — Qwen image generation and editing comparisons.
- [Grok Imagine Image 2 API](https://github.com/Anil-matcha/Grok-Imagine-Image-2-API) — Grok Imagine Image 2 examples.
- [AI Image Editing API](https://github.com/Anil-matcha/AI-Image-Editing-API) — image-editing endpoints compared.
- [AI Character Consistency API](https://github.com/Anil-matcha/AI-Character-Consistency-API) — keeping a character consistent across images.

## Overview

- [Spicy AI Image Generator landing page](https://muapi.ai/ai-spicy-image-generator)
- [Muapi API documentation](https://muapi.ai/docs/api-reference)
- [Image generation docs](https://muapi.ai/docs/image-generation)
- [Create or manage an API key](https://muapi.ai/access-keys)

Requests go to `https://api.muapi.ai/api/v1/{endpoint}` with an `x-api-key` header. A submission returns a `request_id`; poll `GET /api/v1/predictions/{request_id}/result` until the task is completed. Generated image URLs are returned in the result.

## Endpoint comparison

| Model family | Workflow | Muapi endpoint | Resolution / quality | Listed price |
|---|---|---|---|---|
| Seedream 5.0 Pro | Text-to-image | `bytedance-seedream-5.0-pro` | 1K, 2K | $0.045–$0.09 / image |
| Seedream 5.0 Pro | Image-to-image | `bytedance-seedream-5.0-pro-edit` | 1K, 2K | $0.045–$0.09 / image |
| Seedream 4.5 | Text-to-image | `bytedance-seedream-v4.5` | basic, high | $0.05 / image |
| Seedream 4.5 | Image-to-image | `bytedance-seedream-v4.5-edit` | basic, high | $0.05 / image |
| Qwen Image 3.0 | Text-to-image | `qwen3-text-to-image` | 1k, 2k | $0.03–$0.05 / image |
| Qwen Image 3.0 Pro | Text-to-image | `qwen3-pro-text-to-image` | 1k, 2k | pay per generation |
| Qwen Image 3.0 | Image-to-image | `qwen3-image-to-image` | 1k, 2k | pay per generation |
| Qwen Image 3.0 Pro | Image-to-image | `qwen3-pro-image-to-image` | 1k, 2k | pay per generation |
| Qwen Image 2.0 | Text-to-image | `qwen-image-2.0` | native | $0.04 / request |
| Qwen Image 2.0 | Image-to-image | `qwen-image-2.0-edit` | native | $0.04 / request |
| Qwen Image 2.0 Pro | Text-to-image | `qwen-image-2.0-pro` | native | $0.09 / request |
| Qwen Image 2.0 Pro | Image-to-image | `qwen-image-2.0-pro-edit` | native | $0.09 / request |
| Wan 2.7 Image | Text-to-image | `wan2.7-text-to-image` | up to 2K | $0.05 / image |
| Wan 2.7 Image | Image-to-image | `wan2.7-image-edit` | up to 2K | $0.05 / image |
| Grok Imagine | Text-to-image | `grok-imagine-text-to-image` | native | $0.05 / call |
| Grok Imagine | Text-to-image (quality) | `grok-imagine-text-to-image-quality` | high fidelity | $0.05 / call |
| Grok Imagine Image 2 | Text-to-image | `grok-imagine-image-2` | native | $0.05 / call |
| Grok Imagine Image 2 | Image-to-image | `grok-imagine-image-2-edit` | native | $0.05 / call |
| Z-Image Turbo | Text-to-image | `z-image-turbo` | width × height | pay per generation |

Prices are Muapi catalog values as listed on the landing page at the time of writing, not upstream provider rates, and can change. Confirm the current price on the endpoint's playground page before estimating production cost.

## Request schemas

Required fields are marked with `*`. All values below come from Muapi's endpoint schemas.

| Endpoint group | Fields |
|---|---|
| Seedream 5.0 Pro text-to-image | `prompt`*, `aspect_ratio` (`1:1`, `16:9`, `9:16`, `4:3`, `3:4`, `2:3`, `3:2`; default `1:1`), `resolution` (`1K`/`2K`; default `1K`) |
| Seedream 5.0 Pro edit | `prompt`*, `images_list`* (up to 10 URLs), `aspect_ratio`, `resolution` |
| Seedream 4.5 text-to-image / edit | `prompt`*, `images_list`* (edit only, up to 10), `aspect_ratio` (adds `21:9`), `quality` (`basic`/`high`) |
| Qwen Image 3.0 / 3.0 Pro | `prompt`*, `images_list`* (image-to-image only, up to 3), `resolution` (`1k`/`2k`), `aspect_ratio` (`1:1`, `3:2`, `2:3`, `4:3`, `3:4`, `16:9`, `9:16`, `21:9`), `output_format` (`png`/`jpeg`), `prompt_extend`, `negative_prompt` |
| Qwen Image 2.0 / 2.0 Pro | `prompt`*, `images_list`* (edit only; up to 9 on 2.0, up to 6 on 2.0 Pro), `aspect_ratio` (`16:9`, `9:16`, `1:1`, `4:3`, `3:4`, `21:9`, `9:21`) |
| Wan 2.7 Image | `prompt`*, `images_list`* (edit only, up to 9), `aspect_ratio` (adds `9:21`, `3:2`, `2:3`), `thinking_mode` (text-to-image only) |
| Grok Imagine text-to-image / Image 2 | `prompt`*, `aspect_ratio` (`1:1`, `2:3`, `3:2`, `16:9`, `9:16`) |
| Grok Imagine Image 2 edit | `prompt`*, `request_id`* (a prior Grok Imagine result), `mask_indexs` (up to 20) |
| Z-Image Turbo | `prompt`*, `width`, `height` (default 1024 × 1024) |

Notes:

- Image-to-image endpoints take an `images_list` array of public image URLs, with a different maximum per family. Do not copy payloads between families unchanged.
- The Grok Imagine Image 2 edit endpoint works on a previous generation via its `request_id` instead of an uploaded image.
- Resolution values are capitalised (`1K`/`2K`) on Seedream 5.0 Pro and lowercase (`1k`/`2k`) on Qwen Image 3.0.
- Z-Image Turbo is sized with `width` and `height` rather than an aspect-ratio enum.

## Choosing an endpoint

1. **Input you have:** a prompt only (text-to-image) or one or more source images to edit or restyle (image-to-image).
2. **Resolution needs:** Seedream 5.0 Pro, Qwen Image 3.0 and Wan 2.7 Image reach 2K.
3. **Cost and speed:** Z-Image Turbo is the low-cost, fast option; Grok Imagine is fast and flat-priced per call; Qwen Image 2.0 Pro is the most expensive per request in this list.
4. **Editing control:** Seedream edit accepts up to 10 reference images; Qwen Image 3.0 up to 3.
5. **Evaluate on your own prompts.** This repo makes no quality, benchmark or moderation-permissiveness claims; compare results and content-policy behavior on representative prompts before committing to a model.
6. **Failure handling:** submissions are asynchronous. Poll and handle both completed and failed statuses explicitly.

## Quick start with cURL

```bash
export MUAPI_API_KEY="your-api-key"
```

Text-to-image on Seedream 5.0 Pro:

```bash
curl -X POST "https://api.muapi.ai/api/v1/bytedance-seedream-5.0-pro" \
  -H "x-api-key: ${MUAPI_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{"prompt":"A cinematic editorial portrait with dramatic red lighting and intricate styling","aspect_ratio":"2:3","resolution":"2K"}'
```

Image-to-image on Seedream 4.5:

```bash
curl -X POST "https://api.muapi.ai/api/v1/bytedance-seedream-v4.5-edit" \
  -H "x-api-key: ${MUAPI_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{"prompt":"Change the jacket to a glossy black leather jacket while preserving the pose and lighting","images_list":["https://example.com/source.jpg"],"quality":"high"}'
```

Each call returns `{"request_id":"REQUEST_ID"}`. Poll it:

```bash
curl "https://api.muapi.ai/api/v1/predictions/REQUEST_ID/result" \
  -H "x-api-key: ${MUAPI_API_KEY}"
```

## Python example

Requires Python 3.9+ and `requests`:

```bash
python -m pip install -r requirements.txt
export MUAPI_API_KEY="your-api-key"
python examples/submit.py seedream5-t2i
```

`examples/submit.py` submits one of several preconfigured jobs, polls until a terminal status, and prints the result. Replace the placeholder image URL before running an image-to-image job.

## Links

- Landing page: <https://muapi.ai/ai-spicy-image-generator>
- API reference: <https://muapi.ai/docs/api-reference>
- API keys: <https://muapi.ai/access-keys>

## License

MIT
