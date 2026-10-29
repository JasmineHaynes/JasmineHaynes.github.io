# Jasmine Haynes — AI × I-O Psychology Portfolio

A responsive, dark-tech personal portfolio connecting AI/ML, I-O Psychology, and people analytics.

## Included
- `index.html`: portfolio homepage
- `assets/styles.css`: responsive visual design
- `assets/main.js`: mobile navigation and footer year
- `projects/*/index.html`: individual project briefs/case-study pages
- `demos/people-analytics-lab/index.html`: interactive browser-based demo (no backend)
- `demos/people-analytics-lab/app.py`: optional Streamlit version
- `PROJECT_CASE_STUDY_TEMPLATE.md`: repeatable case-study outline

## Important before publishing
1. Replace `REPLACE_WITH_YOUR_EMAIL`, LinkedIn URL, and GitHub URL in `index.html`.
2. Add a résumé PDF at `assets/Jasmine-Haynes-Resume.pdf`, or remove the résumé button until ready.
3. Review every skill and education statement; update official degree/certificate titles and dates.
4. The pages for FoodHub and AllLife Bank are placeholders until original files and results are reviewed. Do not invent metrics.
5. All projects marked planned or needing verification should remain labeled that way until the work is completed.
6. Never upload private employer/student data, secrets, API keys, or personal information.

## Preview locally
Open `index.html` in a browser. For local navigation to work reliably with absolute paths (`/projects/...`), use a local server from this folder:
```bash
python -m http.server 8000
```
Then visit `http://localhost:8000`. Stop with Ctrl+C.

## Publish free with GitHub Pages
1. Create/sign in to GitHub.
2. Create a public repository named `YOURUSERNAME.github.io`.
3. Upload the *contents* of this folder to the repository root (not the parent folder itself).
4. Open **Settings → Pages** and select the `main` branch and root folder as the publishing source.
5. Wait for GitHub to show the published site URL.
6. Test every navigation and project link on desktop and mobile.

Official guide: https://docs.github.com/en/pages

## Custom domain
Optional. After the free site works, buy a domain from a registrar and connect it in GitHub Pages settings. No paid site builder is required for this version.

## Interactive demo
The homepage links to a browser-only interactive demo at `/demos/people-analytics-lab/`. It uses sliders to change visualized inputs. It is explicitly not a predictive model and collects no data.

### Optional Streamlit version
The `app.py` can be deployed as a separate app using Streamlit Community Cloud:
1. Create a separate GitHub repo containing `app.py` and `requirements.txt`.
2. Sign in at https://share.streamlit.io/
3. Create app, choose repository and `app.py`, then deploy.
4. Add the live app URL to the portfolio when it is ready.

## Suggested next project workflow
1. Upload the original FoodHub and AllLife Bank files privately to your working session.
2. Verify dataset sources, results, code, and assignment constraints.
3. Refactor each project into a clean repository with a reproducible notebook and concise executive summary.
4. Replace each placeholder with verified results, visualizations, and links.
