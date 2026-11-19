# Mohamed Hisham Ibrahim — Data Analyst Portfolio

Live site: https://portfolio-sigma-navy-21.vercel.app

Static site (HTML / CSS / JavaScript). No build step and no dependencies, so it loads instantly on Vercel.

## Structure

```
index.html            main portfolio page
dashboard.html        interactive Sales Dashboard (synthetic data)
css/style.css         all styles and colors (see :root)
js/site.js            menu, photo and screenshot loading
js/dashboard.js       dashboard data + charts
assets/               put your images here (see below)
```

## Images (all optional)

Upload these into the `assets/` folder:

| File                                | Where it appears                          |
|-------------------------------------|-------------------------------------------|
| `profile.jpg` (or .png / .webp)     | round photo in the top banner             |
| `dashboard1.png` (or .jpg / .webp)  | first card in the "Dashboards" section    |
| `dashboard2.png` (or .jpg / .webp)  | second card in the "Dashboards" section   |

If an image is missing, its card is hidden. If both screenshots are missing the whole section disappears.
Edit the titles, tools and descriptions in `index.html` (search for `id="dashboards"`).

## Deploy on Vercel

1. Push this folder to a GitHub repository (files at the root of the repo, not inside a sub-folder).
2. Go to https://vercel.com/new and import the repository.
3. Framework Preset: **Other**. Leave Build Command and Output Directory empty. Click **Deploy**.
4. Every later `git push` redeploys automatically.

## Run locally

```bash
python -m http.server 8000
# open http://localhost:8000
```
