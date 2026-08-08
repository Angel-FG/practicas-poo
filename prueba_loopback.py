import soundcard as sc
import soundfile as sf
import numpy as np
import os

FRECUENCIA = 48000
DURACION = 10

print("Dispositivo de salida predeterminado:")
altavoces = sc.default_speaker()
print(altavoces)

print("\nDispositivos loopback encontrados:")

loopbacks = [
    dispositivo
    for dispositivo in sc.all_microphones(include_loopback=True)
    if dispositivo.isloopback
]

for indice, dispositivo in enumerate(loopbacks):
    print(f"{indice}: {dispositivo}")

if not loopbacks:
    print("No se encontró ningún dispositivo loopback.")
    raise SystemExit

# Busca el loopback correspondiente a los altavoces predeterminados
try:
    dispositivo_loopback = sc.get_microphone(
        id=altavoces.name,
        include_loopback=True
    )
except Exception:
    # Si no encuentra coincidencia por nombre, usa el primero
    dispositivo_loopback = loopbacks[0]

print("\nLoopback seleccionado:")
print(dispositivo_loopback)

print("\nReproduce el video o live.")
print(f"Grabando {DURACION} segundos...")

with dispositivo_loopback.recorder(
    samplerate=FRECUENCIA
) as grabador:

    audio = grabador.record(
        numframes=FRECUENCIA * DURACION
    )

nivel_maximo = float(np.max(np.abs(audio)))
nivel_promedio = float(np.mean(np.abs(audio)))

print(f"\nNivel máximo: {nivel_maximo:.6f}")
print(f"Nivel promedio: {nivel_promedio:.6f}")

archivo_salida = os.path.abspath("prueba_loopback.wav")

sf.write(
    archivo_salida,
    audio,
    FRECUENCIA
)

print(f"\nArchivo guardado en:\n{archivo_salida}")

if nivel_maximo < 0.0001:
    print("\nADVERTENCIA: se capturó silencio.")
    print("Revisa que el navegador salga por los altavoces predeterminados.")
else:
    print("\nSí se detectó audio.")

os.startfile(archivo_salida)