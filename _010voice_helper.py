import asyncio
import time
from pathlib import Path
import edge_tts
from manim_voiceover.services.base import SpeechService


class EdgeTTSService(SpeechService):
    def __init__(self, voice="en-US-AndrewNeural", **kwargs):
        self.voice = voice
        super().__init__(**kwargs)

    def generate_from_text(self, text, cache_dir=None, path=None, **kwargs):
        if cache_dir is None:
            cache_dir = self.cache_dir
        input_data = {"input_text": text, "service": "edge_tts", "voice": self.voice}
        cached = self.get_cached_result(input_data, cache_dir)
        if cached is not None:
            return cached

        audio_path = (self.get_audio_basename(input_data) + ".mp3") if path is None else path
        full_path = str(Path(cache_dir) / audio_path)

        async def _save():
            communicate = edge_tts.Communicate(text, self.voice)
            await communicate.save(full_path)

        # Retry up to 4 times if Edge TTS temporarily drops or rate-limits a request
        for attempt in range(4):
            try:
                time.sleep(0.6)  # Small pause to avoid rapid-fire rate limiting
                asyncio.run(_save())
                break
            except Exception:
                if attempt == 3:
                    raise
                time.sleep(1.5 * (attempt + 1))

        return {
            "input_text": text,
            "input_data": input_data,
            "original_audio": audio_path,
        }
    