from config.features import *
from config.channels import CHANNELS
from modules import notifier, health_check
from modules import script_generator, voice_generator
from modules import video_generator, youtube_uploader

def main():
    notifier.send("▶️ Manual run started")

    ok, msg = health_check.run()
    if not ok:
        notifier.send(f"❌ Health check failed: {msg}")
        return

    for channel_name, channel in CHANNELS.items():
        if not ENABLE_LONG_VIDEOS:
            continue

        notifier.send(f"🎬 Generating video for {channel_name}")

        script = script_generator.generate(channel)
        voice = voice_generator.generate(script)
        video = video_generator.generate(script, voice)

        if PREVIEW_MODE:
            notifier.send("👀 Preview mode ON – upload skipped")
            continue

        youtube_uploader.upload(video, channel)
        notifier.send("✅ Video uploaded successfully")

        if STOP_AFTER_UPLOAD:
            notifier.send("⏹ System stopped after upload")
            return

    notifier.send("🏁 Manual run finished")

if __name__ == "__main__":
    main()
