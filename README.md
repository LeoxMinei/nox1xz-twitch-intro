# Nox1Xz Twitch intro

A free, original, reproducible **15-second, 1280×720, 24 fps H.264 MP4** animated intro with AAC synthesizer audio for OBS. No Higgsfield API, subscriptions or paid assets.

## Scenes

- **0–3 s** animated RGB mouse close-up
- **3–7 s** futuristic gaming room with three monitors, microphone, and hoodie character
- **7–10 s** stylized animated thumbs-up
- **10–12 s** electric particles assemble `Nox1Xz`
- **12–15 s** hold `Nox1Xz` and `STREAM STARTING SOON`

This is programmatic 2.5D, not photorealistic AAA character animation. The video and audio are generated procedurally; the font is freely licensed DejaVu Sans Bold.

## Download on Android or iPhone

1. Open the repository on GitHub in your phone browser, sign in if needed.
2. After the PR is merged into `main`, tap **Actions → Render Nox1Xz intro → Run workflow** (or open the successful automatically triggered run).
3. Open the green completed workflow run and scroll to **Artifacts**.
4. Tap **Nox1Xz-intro** to download the ZIP.
5. Open the ZIP using your phone's built-in Files manager; extract `Nox1Xz-intro.mp4`. No phone app installation or credit card is required.

Artifacts are kept for 30 days by this workflow (subject to repository retention policies).

## Optional local render (Ubuntu)

```bash
sudo apt-get install -y ffmpeg fonts-dejavu-core
python -m pip install -r requirements.txt
python render.py --output dist/Nox1Xz-intro.mp4
python validate.py dist/Nox1Xz-intro.mp4
```

## OBS

Add a **Media Source** and select the extracted MP4. Enable **Restart playback when source becomes active**. Turn off Loop for a one-time intro.

## Source license

MIT; Pillow, NumPy, FFmpeg, libx264 and the installed font have their respective open licenses.
