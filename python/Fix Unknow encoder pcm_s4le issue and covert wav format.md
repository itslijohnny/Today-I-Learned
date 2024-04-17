When cutting wav file into small piece using the following code.  
```python  
from pydub import AudioSegment  
newAudio = AudioSegment.from_wav("./content/REC0001.WAV")  
newAudio = newAudio[t1:t2]  
newAudio.export('newSong.wav', format="wav") #Exports to a wav file in the current path.  
```  
I got an error saying `Unknown encoder 'pcm_s4le'`  
  
```python  
import soundfile as sf  
f = sf.SoundFile('./content/REC0001.WAV')  
f.format, f.subtype, f.endian  
# output: ('WAV', 'IMA_ADPCM', 'FILE')  
```  
  
So I save it in PCM_16 format  
```python  
sig, samplerate = sf.read('./content/REC0001.WAV')  
sf.write('./content/processed_rec001.wav', sig, samplerate)  
```  
  
