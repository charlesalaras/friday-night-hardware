from mido import MidiFile
from queue import Queue
# A5 to A6

freqdict = {
   69: 880, #A5
   70: 932.32,
   71: 987.76,
   72: 1046.50,
   73: 1108.73,
   74: 1174.65,
   75: 1244.50,
   76: 1318.51,
   77: 1386.91,
   78: 1489.97,
   79: 1567.98,
   80: 1661.21,
   81: 1760
}

f = open("c-array.txt","w")
f.write("char melody[] = {")
mid = MidiFile('song.mid')

q = Queue(1500)

notes = 0;
rhythms = 0;

for i, track in enumerate(mid.tracks):
    print('Track {}: {}'.format(i, track.name))
    for msg in track:
        print(msg)
        if msg.type == 'note_on':
            f.write(str(msg.note) + ', ')
            q.put(msg.time)
            notes = notes + 1
        elif msg.type == 'note_off':
            f.write("0, ")
            q.put(msg.time)
            notes = notes + 1
        else:
            # Do nothing
            continue

f.write("};\n")
f.write("int rhythm[] = {")
while q.empty() == False:
    f.write(str(q.get()) + ", ")
    rhythms = rhythms + 1
f.write("};\n")
f.close()

print("Number of Notes: " + str(notes))
print("Number of Rhythm: " + str(rhythms))
