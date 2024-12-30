from moviepy import vfx
from moviepy.audio.io.AudioFileClip import AudioFileClip
import gradio as gr

def reverse_audio(input_audio):
  sr, data = input_audio
  audio=AudioFileClip(data)

  reversed_audio=audio.fx(vfx.time_mirror)
  output_path="reversed_audio.mp3"
  reversed_audio.write_audiofile(output_path)
  return output_path
demo=gr.Interface(
    fn=reverse_audio,
    inputs=gr.Audio(label="Upload Audio"),
    outputs=gr.Audio(label="Reversed Audio"),
    title="Reverse Audio Generator",
    description="Upload an audio file, and this app will reverse the audio.",
)
demo.launch(debug=True,share=True)
