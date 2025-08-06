import os
import torch
from openvoice import se_extractor
from openvoice.api import ToneColorConverter
from pydub import AudioSegment

ckpt_path = 'checkpoints/converter'
device = "cuda" if torch.cuda.is_available() else "cpu"
output_dir = "outputs"
os.makedirs(output_dir, exist_ok=True)

converter = ToneColorConverter(f'{ckpt_path}/config.json', device=device)
converter.load_ckpt(f'{ckpt_path}/converter.pth')

def clone_voice(ref_audio_path, text):
    reference_path_wav = os.path.splitext(ref_audio_path)[0] + ".wav"
    audio = AudioSegment.from_file(ref_audio_path)
    audio.export(reference_path_wav, format="wav")

    tone_color = se_extractor.get_se(reference_path_wav, converter)
    src_path = "reference.wav"  # A neutral reference file in your project
    output_file = os.path.join(output_dir, "cloned_output.wav")

    converter.infer(
        src_path=src_path,
        text=text,
        output_path=output_file,
        tone_color=tone_color,
        sdp_ratio=0.2
    )
    return output_file
