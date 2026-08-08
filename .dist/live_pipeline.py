import speech_recognition as sr
import os

INDICE = 13

r = sr.Recognizer()

try:
    with sr.Microphone(
        device_index=INDICE,
        sample_rate=48000
    ) as source:

        print("Reproduce el video o live.")
        print("Grabando 10 segundos...")

        # record() no espera a detectar voz
        audio = r.record(source, duration=10)

    nombre_archivo = "prueba_mezcla_estereo.wav"

    with open(nombre_archivo, "wb") as archivo:
        archivo.write(
            audio.get_wav_data(
                convert_rate=16000,
                convert_width=2
            )
        )

    print("Audio guardado.")
    os.startfile(nombre_archivo)

except Exception as error:
    print("Error:", error)