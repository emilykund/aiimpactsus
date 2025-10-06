# AI Impacts US – Site

This repo contains a simple static site mirroring the structure and content at the public reference page.

## Structure

- `site/index.html`: main page
- `site/assets/css/styles.css`: styles
- `site/assets/js/main.js`: small JS helpers
- `site/assets/images/`: favicon and images

## Local preview

You can serve the `site` directory with any static server. Examples:

```bash
python3 -m http.server --directory site 8080
# or
npx serve site -l 8080
```

Then open `http://localhost:8080`.

## Deploying

- Any static host works (GitHub Pages, Netlify, Vercel, S3/CloudFront).
- Set the publish directory to `site/`.

## Editing

- Update content in `site/index.html`.
- Tweak styles in `site/assets/css/styles.css`.