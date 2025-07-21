import subprocess

def extract_adpcm(input_wav, output_ima):
    command = [
        'ffmpeg',
        '-i', input_wav,
        '-f', 'adpcm_ima_wav',  # Формат для ADPCM IMA
        output_ima
    ]
    
    subprocess.run(command)

# Пример использования
input_wav = 'input.wav'
output_ima = 'output.ima'

extract_adpcm(input_wav, output_ima)
